# Rust JWT Web Service

This project is a simple example of a RESTful web service built with Rust using the `actix-web` framework. The service demonstrates how to implement JWT token authentication to secure API endpoints.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Best Practices](#best-practices)
- [License](#license)

## Features

- **JWT Authentication**. Secure your API endpoints using JSON Web Tokens (JWT).
- **REST API**. Basic RESTful routes for login and accessing protected resources.
- **Actix-Web Framework**. High-performance and easy-to-use web framework for Rust.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- [Rust](https://www.rust-lang.org/) (latest stable version)
- [Cargo](https://doc.rust-lang.org/cargo/) (comes with Rust)
- [Git](https://git-scm.com/)

## Getting Started

Follow these steps to set up and run the project locally.

### Clone the Repository

```bash
git clone https://github.com/yourusername/rust_jwt_api.git
cd rust_jwt_api
```

### Install Dependencies
All dependencies are managed with Cargo. To install them, run:

```bash
cargo build
```

This will download and compile all the necessary dependencies.

### Run the Server
Start the server with:

```bash
cargo run
```

The server will be running at http://127.0.0.1:8080.

## Usage
1. Login and Get a JWT Token
To login and receive a JWT token, send a POST request to /login:

```bash
curl -X POST http://127.0.0.1:8080/login
```

This will return a JWT token that you can use to access protected routes.

2. Access a Protected Resource
To access a protected resource, send a GET request to /protected with the JWT token in the Authorization header:

```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://127.0.0.1:8080/protected
```

Replace <your_jwt_token> with the token you received from the login endpoint.

## Best Practices
- Secret Management. Store the JWT secret key securely, such as in environment variables or a secrets management service. Do not hardcode secrets in your codebase.
- Token Expiry. Always set an expiration (exp) for JWT tokens to limit the risk of misuse if a token is compromised.
- Error Handling. Ensure that API responses do not leak sensitive information, especially during authentication and authorization failures.
- Logging. Implement logging to monitor access patterns and detect potential misuse or attacks.
