#include "../include/FoodReceiver.h"

// Constructor
FoodReceiver::FoodReceiver(int id, string name, string contact, string zone, ReceiverType type, int urgency)
    : User(id, name, contact, zone) {
    this->receiverType = type;
    this->urgencyLevel = urgency;
}

// Destructor
FoodReceiver::~FoodReceiver() {
    // No dynamic memory used
}

// Getters
ReceiverType FoodReceiver::getReceiverType() const {
    return receiverType;
}

int FoodReceiver::getUrgencyLevel() const {
    return urgencyLevel;
}

// Setters
void FoodReceiver::setReceiverType(ReceiverType type) {
    this->receiverType = type;
}

void FoodReceiver::setUrgencyLevel(int urgency) {
    this->urgencyLevel = urgency;
}

// Convert enum to string
string FoodReceiver::getReceiverTypeString() const {
    switch (receiverType) {
        case NGO: return "NGO";
        case ORPHANAGE: return "Orphanage";
        default: return "Unknown";
    }
}

// Convert urgency to string
string FoodReceiver::getUrgencyString() const {
    switch (urgencyLevel) {
        case 1: return "Low";
        case 2: return "Medium";
        case 3: return "High";
        default: return "Unknown";
    }
}

// Functional Method
void FoodReceiver::requestFood() {
    cout << "Receiver " << name << " is requesting food with urgency: "
         << getUrgencyString() << endl;
}

// Overridden Method
void FoodReceiver::displayProfile() const {
    cout << "\n--- Food Receiver Profile ---" << endl;
    cout << "ID: " << userId << endl;
    cout << "Name: " << name << endl;
    cout << "Contact: " << contact << endl;
    cout << "Zone: " << zone << endl;
    cout << "Receiver Type: " << getReceiverTypeString() << endl;
    cout << "Urgency Level: " << getUrgencyString() << endl;
}

// Overridden Method
string FoodReceiver::getUserType() const {
    return "Food Receiver";
}