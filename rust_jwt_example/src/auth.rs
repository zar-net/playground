
use serde::{Deserialize, Serialize};
use jsonwebtoken::{decode, DecodingKey, Validation, Algorithm};
use actix_web::{Error, HttpRequest};

#[derive(Debug, Serialize, Deserialize)]
pub struct Claims {
    pub sub: String,
    pub company: String,
    pub exp: usize,
}

pub fn validate_jwt(token: &str) -> Result<Claims, Error> {
    let validation = Validation::new(Algorithm::HS256);
    let decoding_key = DecodingKey::from_secret("secret".as_ref());

    match decode::<Claims>(&token, &decoding_key, &validation) {
        Ok(token_data) => Ok(token_data.claims),
        Err(_) => Err(actix_web::error::ErrorUnauthorized("Invalid token")),
    }
}
