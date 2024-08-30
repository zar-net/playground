# Rust JWT CRUD Web Service

This project is a basic RESTful web service built with Rust using the `actix-web` framework. The service demonstrates user authentication with JSON Web Tokens (JWT) and supports CRUD operations on an in-memory data store.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Best Practices](#best-practices)

## Features

- **JWT Authentication**: Secure API endpoints using JSON Web Tokens (JWT).
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on an in-memory data store.
- **In-Memory Storage**: Store data in-memory, which can be easily extended to use a flat file or database.
- **Actix-Web Framework**: Built using the high-performance Actix-Web framework.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Rust](https://www.rust-lang.org/) (latest stable version)
- [Cargo](https://doc.rust-lang.org/cargo/) (comes with Rust)
- [Git](https://git-scm.com/)

## Getting Started

Follow these steps to set up and run the project locally.

### Clone the Repository

```bash
git clone https://github.com/yourusername/rust_jwt_crud.git
cd rust_jwt_crud
```

### Install Dependencies
Install the necessary dependencies using Cargo:

```bash
cargo build
```

###Run the Server
Start the server with:

```bash
cargo run
```

The server will run at http://127.0.0.1:8080.

## Usage

```
curl -X POST -H "Content-Type: application/json" -d '{"username":"user", "password":"password"}' http://127.0.0.1:8080/login

curl -X POST -H "Authorization: Bearer <your_jwt_token>" -H "Content-Type: application/json" -d '{"name":"Item 1", "description":"Description 1"}' http://127.0.0.1:8080/items

curl -H "Authorization: Bearer <your_jwt_token>" http://127.0.0.1:8080/items/<item_id>

curl -X PUT -H "Authorization: Bearer <your_jwt_token>" -H "Content-Type: application/json" -d '{"name":"Updated Item", "description":"Updated Description"}' http://127.0.0.1:8080/items/<item_id>


curl -X DELETE -H "Authorization: Bearer <your_jwt_token>" http://127.0.0.1:8080/items/<item_id>

curl -H "Authorization: Bearer <your_jwt_token>" http://127.0.0.1:8080/items

```

## Best Practices

- **Secret Management.** Store JWT secret keys securely, such as in environment variables, instead of hardcoding them in the source code.
- **Token Expiry.** Always set an expiration (exp) for JWT tokens to minimize risks if a token is compromised.
- **Authorization.** Checks: Ensure that all CRUD operations validate the JWT before performing any actions.
- **Error Handling.** Provide meaningful but secure error messages to avoid revealing sensitive information.


