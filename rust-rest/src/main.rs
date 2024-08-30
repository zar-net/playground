use actix_web::{web, App, HttpServer, HttpRequest, HttpResponse, Responder};
use actix_web::http::StatusCode;
use serde::Deserialize;
use std::sync::Arc;
use log::info;

mod auth;
mod model;

use auth::{create_jwt, validate_jwt, extract_jwt};
use model::{AppState, Item, CreateItemRequest};

#[derive(Deserialize)]
struct LoginRequest {
    username: String,
    password: String,
}

async fn login(data: web::Json<LoginRequest>) -> impl Responder {
    if data.username == "user" && data.password == "password" {
        let token = create_jwt("user_id");
        HttpResponse::Ok().body(token)
    } else {
        HttpResponse::Unauthorized().body("Invalid credentials")
    }
}

async fn create_item(
    req: HttpRequest,
    data: web::Json<CreateItemRequest>,
    state: web::Data<Arc<AppState>>,
) -> impl Responder {
    if let Some(token) = extract_jwt(&req) {
        if validate_jwt(&token).is_ok() {
            let item = state.add_item(data.name.clone(), data.description.clone());
            return HttpResponse::Ok().json(item);
        }
    }

    HttpResponse::Unauthorized().body("Unauthorized")
}

async fn get_item(
    req: HttpRequest,
    path: web::Path<String>,
    state: web::Data<Arc<AppState>>,
) -> impl Responder {
    if let Some(token) = extract_jwt(&req) {
        if validate_jwt(&token).is_ok() {
            if let Some(item) = state.get_item(&path.into_inner()) {
                return HttpResponse::Ok().json(item);
            } else {
                return HttpResponse::NotFound().body("Item not found");
            }
        }
    }

    HttpResponse::Unauthorized().body("Unauthorized")
}

async fn update_item(
    req: HttpRequest,
    path: web::Path<String>,
    data: web::Json<CreateItemRequest>,
    state: web::Data<Arc<AppState>>,
) -> impl Responder {
    if let Some(token) = extract_jwt(&req) {
        if validate_jwt(&token).is_ok() {
            if let Some(item) = state.update_item(&path.into_inner(), data.name.clone(), data.description.clone()) {
                return HttpResponse::Ok().json(item);
            } else {
                return HttpResponse::NotFound().body("Item not found");
            }
        }
    }

    HttpResponse::Unauthorized().body("Unauthorized")
}

async fn delete_item(
    req: HttpRequest,
    path: web::Path<String>,
    state: web::Data<Arc<AppState>>,
) -> impl Responder {
    if let Some(token) = extract_jwt(&req) {
        if validate_jwt(&token).is_ok() {
            if state.delete_item(&path.into_inner()) {
                return HttpResponse::Ok().body("Item deleted");
            } else {
                return HttpResponse::NotFound().body("Item not found");
            }
        }
    }

    HttpResponse::Unauthorized().body("Unauthorized")
}

async fn list_items(req: HttpRequest, state: web::Data<Arc<AppState>>) -> impl Responder {
    if let Some(token) = extract_jwt(&req) {
        if validate_jwt(&token).is_ok() {
            let items = state.list_items();
            return HttpResponse::Ok().json(items);
        }
    }

    HttpResponse::Unauthorized().body("Unauthorized")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    env_logger::init();

    let state = web::Data::new(Arc::new(AppState::new()));

    HttpServer::new(move || {
        App::new()
            .app_data(state.clone())
            .route("/login", web::post().to(login))
            .route("/items", web::post().to(create_item))
            .route("/items/{id}", web::get().to(get_item))
            .route("/items/{id}", web::put().to(update_item))
            .route("/items/{id}", web::delete().to(delete_item))
            .route("/items", web::get().to(list_items))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
