// src/main.rs

use actix_web::{web, App, HttpServer, HttpRequest, HttpResponse, Responder};
use chrono::Duration;
use jsonwebtoken;
use log::info;

mod auth; // Import the auth module

use auth::{Claims, validate_jwt};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    env_logger::init();

    HttpServer::new(|| {
        App::new()
            .route("/login", web::post().to(login))
            .route("/protected", web::get().to(protected))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}

async fn login() -> impl Responder {
    let claims = Claims {
        sub: "user_id".to_owned(),
        company: "example".to_owned(),
        exp: (chrono::Utc::now() + Duration::days(1)).timestamp() as usize,
    };

    let token = jsonwebtoken::encode(
        &jsonwebtoken::Header::default(),
        &claims,
        &jsonwebtoken::EncodingKey::from_secret("secret".as_ref()),
    )
    .unwrap();

    HttpResponse::Ok().body(token)
}

async fn protected(req: HttpRequest) -> impl Responder {
    let auth_header = req
        .headers()
        .get("Authorization")
        .and_then(|header| header.to_str().ok());

    if let Some(token) = auth_header {
        if let Some(token) = token.strip_prefix("Bearer ") {
            match validate_jwt(token) {
                Ok(claims) => {
                    info!("Claims: {:?}", claims);
                    return HttpResponse::Ok().body("Access granted to protected resource");
                }
                Err(_) => return HttpResponse::Unauthorized().body("Invalid token"),
            }
        }
    }

    HttpResponse::Unauthorized().body("Authorization header missing or invalid")
}
