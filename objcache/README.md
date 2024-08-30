# Async Object Cache in Rust

Since IBM, I have used Object Cache's as one way of learning libraries and playing around with programming languages. 
This project is an example implementation of an asynchronous object cache in Rust. The cache is generic over key-value 
pairs and is designed to work in an asynchronous environment using the `tokio` runtime and `async-std` for synchronization.

## Features

- **Asynchronous Operations**. The cache supports async `get`, `put`, and `remove` operations.
- **Thread-Safe**. The cache is protected by an `async_std::sync::Mutex` to ensure thread safety.
- **Simple API**. The cache provides a straightforward API for inserting, retrieving, and removing items.
- **Generic Implementation**. The cache is implemented using generics, making it flexible for use with different types.

## Requirements

- Rust 1.53 or later
- `tokio` for async runtime
- `async-std` for async synchronization

## Getting Started

### Prerequisites

Ensure you have Rust installed. You can install Rust using `rustup`:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

You also need to add tokio and async-std as dependencies in your Cargo.toml file:

```
[dependencies]
tokio = { version = "1", features = ["full"] }
async-std = "1.10"
```

## Installation
Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

## Usage
The example code provided in main.rs demonstrates how to:

1. Create a new cache.
2. Insert key-value pairs into the cache.
3. Retrieve a value from the cache.
4. Remove a value from the cache.
5. Display the contents of the cache.

You can run the example using cargo run:

```
cargo run
```

### Example Output

```
Retrieved from cache: key2 = value2
Removed key2 from cache
Key not found in cache: key2
Key: key1, Value: value1
Key: key3, Value: value3
```


