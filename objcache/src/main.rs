use async_std::sync::Mutex;
use std::collections::HashMap;
use std::hash::Hash;
use std::sync::Arc;
use std::fmt::Display; // Import Display trait
use tokio::time::{sleep, Duration};

// Cache struct with a generic key-value pair
struct Cache<K, V> {
    store: Arc<Mutex<HashMap<K, V>>>,
}

impl<K, V> Cache<K, V>
where
    K: Eq + Hash + Clone + Display, // Ensure K implements Display
    V: Clone + Display,              // Ensure V implements Display
{
    // Creates a new Cache
    fn new() -> Self {
        Cache {
            store: Arc::new(Mutex::new(HashMap::new())),
        }
    }

    // Gets a value from the cache asynchronously
    async fn get(&self, key: &K) -> Option<V> {
        let store = self.store.lock().await;
        store.get(key).cloned()
    }

    // Puts a value into the cache asynchronously
    async fn put(&self, key: K, value: V) {
        let mut store = self.store.lock().await;
        store.insert(key, value);
    }

    // Removes a value from the cache asynchronously
    async fn remove(&self, key: &K) {
        let mut store = self.store.lock().await;
        store.remove(key);
    }

    // Display the contents of the cache
    async fn display(&self) {
        let store = self.store.lock().await;
        for (key, value) in store.iter() {
            println!("Key: {}, Value: {}", key, value);
        }
    }
}

// Example of using the Cache in an async function
#[tokio::main]
async fn main() {
    let cache = Cache::new();

    // Insert values into cache
    cache.put("key1", "value1").await;
    cache.put("key2", "value2").await;
    cache.put("key3", "value3").await;

    // Simulate some async work
    sleep(Duration::from_secs(1)).await;

    // Retrieve a value from the cache
    if let Some(value) = cache.get(&"key2").await {
        println!("Retrieved from cache: key2 = {}", value);
    } else {
        println!("Key not found in cache: key2");
    }

    // Remove a value from the cache
    cache.remove(&"key2").await;
    println!("Removed key2 from cache");

    // Try to retrieve the removed value
    if let Some(value) = cache.get(&"key2").await {
        println!("Retrieved from cache: key2 = {}", value);
    } else {
        println!("Key not found in cache: key2");
    }

    // Display remaining cache contents
    cache.display().await;

    // Wait for user input before exiting
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
}
