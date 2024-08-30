use serde::{Deserialize, Serialize};
use std::sync::Mutex;
use uuid::Uuid;

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Item {
    pub id: String,
    pub name: String,
    pub description: String,
}

#[derive(Debug, Deserialize)]
pub struct CreateItemRequest {
    pub name: String,
    pub description: String,
}

pub struct AppState {
    pub items: Mutex<Vec<Item>>,
}

impl AppState {
    pub fn new() -> Self {
        AppState {
            items: Mutex::new(vec![]),
        }
    }

    pub fn add_item(&self, name: String, description: String) -> Item {
        let item = Item {
            id: Uuid::new_v4().to_string(),
            name,
            description,
        };

        self.items.lock().unwrap().push(item.clone());
        item
    }

    pub fn get_item(&self, id: &str) -> Option<Item> {
        self.items.lock().unwrap().iter().cloned().find(|item| item.id == id)
    }

    pub fn update_item(&self, id: &str, name: String, description: String) -> Option<Item> {
        let mut items = self.items.lock().unwrap();
        if let Some(item) = items.iter_mut().find(|item| item.id == id) {
            item.name = name;
            item.description = description;
            return Some(item.clone());
        }
        None
    }

    pub fn delete_item(&self, id: &str) -> bool {
        let mut items = self.items.lock().unwrap();
        if let Some(index) = items.iter().position(|item| item.id == id) {
            items.remove(index);
            return true;
        }
        false
    }

    pub fn list_items(&self) -> Vec<Item> {
        self.items.lock().unwrap().clone()
    }
}
