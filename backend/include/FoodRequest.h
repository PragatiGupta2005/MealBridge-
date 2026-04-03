#ifndef FOODREQUEST_H
#define FOODREQUEST_H

#include <iostream>
#include <string>
#include "FoodReceiver.h"
using namespace std;

class FoodRequest {
private:
    int requestId;
    FoodReceiver* receiver;
    int quantityNeeded;
    int urgencyLevel; // 1 = Low, 2 = Medium, 3 = High
    string zone;

public:
    // Constructor
    FoodRequest(int id, FoodReceiver* receiver, int quantity, int urgency, string zone);

    // Getters
    int getRequestId() const;
    FoodReceiver* getReceiver() const;
    int getQuantityNeeded() const;
    int getUrgencyLevel() const;
    string getZone() const;

    // Display
    void display() const;
};

// Comparator (HIGH urgency first)
struct RequestCompare {
    bool operator()(const FoodRequest& r1, const FoodRequest& r2) {
        return r1.getUrgencyLevel() < r2.getUrgencyLevel();
    }
};

#endif