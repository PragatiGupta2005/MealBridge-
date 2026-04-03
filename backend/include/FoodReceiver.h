#ifndef FOODRECEIVER_H
#define FOODRECEIVER_H

#include "User.h"
#include <iostream>
using namespace std;

// Enum for receiver type
enum ReceiverType {
    NGO,
    ORPHANAGE
};

class FoodReceiver : public User {
private:
    ReceiverType receiverType;
    int urgencyLevel; // 1 = Low, 2 = Medium, 3 = High

public:
    // Constructor
    FoodReceiver(int id, string name, string contact, string zone, ReceiverType type, int urgency);

    // Destructor
    ~FoodReceiver();

    // Getters
    ReceiverType getReceiverType() const;
    int getUrgencyLevel() const;

    // Setters
    void setReceiverType(ReceiverType type);
    void setUrgencyLevel(int urgency);

    // Functional Method
    void requestFood();

    // Overridden Methods
    void displayProfile() const override;
    string getUserType() const override;

    // Helper Methods
    string getReceiverTypeString() const;
    string getUrgencyString() const;
};

#endif