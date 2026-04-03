#include "../include/FoodItem.h"

// Constructor
FoodItem::FoodItem(string name, int quantity, int expiryTime) {
    this->name = name;
    this->quantity = quantity;
    this->expiryTime = expiryTime;
}

// Getters
string FoodItem::getName() const {
    return name;
}

int FoodItem::getQuantity() const {
    return quantity;
}

int FoodItem::getExpiryTime() const {
    return expiryTime;
}

// Setters
void FoodItem::setQuantity(int quantity) {
    this->quantity = quantity;
}

void FoodItem::setExpiryTime(int expiryTime) {
    this->expiryTime = expiryTime;
}

// Display
void FoodItem::display() const {
    cout << "Food: " << name
         << " | Quantity: " << quantity
         << " | Expiry (hrs): " << expiryTime << endl;
}