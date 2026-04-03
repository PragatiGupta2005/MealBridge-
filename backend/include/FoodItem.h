#ifndef FOODITEM_H
#define FOODITEM_H

#include <iostream>
#include <string>
using namespace std;

class FoodItem {
private:
    string name;
    int quantity;       // number of meals
    int expiryTime;     // in hours (remaining time)

public:
    // Constructor
    FoodItem(string name, int quantity, int expiryTime);

    // Getters
    string getName() const;
    int getQuantity() const;
    int getExpiryTime() const;

    // Setters
    void setQuantity(int quantity);
    void setExpiryTime(int expiryTime);

    // Display
    void display() const;
};

#endif