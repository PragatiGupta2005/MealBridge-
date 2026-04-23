#ifndef FOODDONATION_H
#define FOODDONATION_H

#include <iostream>
#include <vector>
#include "FoodItem.h"
using namespace std;
class FoodDonor;

class FoodDonation {
private:
    int donationId;
    FoodDonor* donor;
    vector<FoodItem> foodItems;
    string zone;

public:
    // Constructor
    FoodDonation(int id, FoodDonor* donor, string zone);

    // Add food item
    void addFoodItem(const FoodItem& item);

    // Getters
    int getDonationId() const;
    string getZone() const;
    FoodDonor* getDonor() const;
    vector<FoodItem> getFoodItems() const;

    // Utility
    int getEarliestExpiry() const;

    // Display
    void display() const;
};

// Comparator do type of sorting
struct DonationCompare {
    bool operator()(const FoodDonation& d1, const FoodDonation& d2) {
        return d1.getEarliestExpiry() > d2.getEarliestExpiry();
    }
};

#endif