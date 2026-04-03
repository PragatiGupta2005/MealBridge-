#include "../include/FoodDonation.h"
#include "../include/FoodDonor.h"   // ✅ include here instead
#include <climits>
#include <iostream>
using namespace std;
// Constructor
FoodDonation::FoodDonation(int id, FoodDonor* donor, string zone) {
    this->donationId = id;
    this->donor = donor;
    this->zone = zone;
}

// Add food item
void FoodDonation::addFoodItem(const FoodItem& item) {
    foodItems.push_back(item);
}

// Getters
int FoodDonation::getDonationId() const {
    return donationId;
}

string FoodDonation::getZone() const {
    return zone;
}

FoodDonor* FoodDonation::getDonor() const {
    return donor;
}

vector<FoodItem> FoodDonation::getFoodItems() const {
    return foodItems;
}

// Find earliest expiry among items
int FoodDonation::getEarliestExpiry() const {
    if (foodItems.empty()) return INT_MAX;

    int minExpiry = foodItems[0].getExpiryTime();

    for (const auto& item : foodItems) {
        if (item.getExpiryTime() < minExpiry) {
            minExpiry = item.getExpiryTime();
        }
    }

    return minExpiry;
}

// Display
void FoodDonation::display() const {
    cout << "\n--- Donation ID: " << donationId << " ---" << endl;
    cout << "Donor: " << donor->getName() << endl;
    cout << "Zone: " << zone << endl;

    cout << "Food Items:" << endl;
    for (const auto& item : foodItems) {
        item.display();
    }

    cout << "Earliest Expiry: " << getEarliestExpiry() << " hrs" << endl;
}