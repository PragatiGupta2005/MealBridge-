#include "../include/FoodRequest.h"

// Constructor
FoodRequest::FoodRequest(int id, FoodReceiver* receiver, int quantity, int urgency, string zone) {
    this->requestId = id;
    this->receiver = receiver;
    this->quantityNeeded = quantity;
    this->urgencyLevel = urgency;
    this->zone = zone;
}

// Getters
int FoodRequest::getRequestId() const {
    return requestId;
}

FoodReceiver* FoodRequest::getReceiver() const {
    return receiver;
}

int FoodRequest::getQuantityNeeded() const {
    return quantityNeeded;
}

int FoodRequest::getUrgencyLevel() const {
    return urgencyLevel;
}

string FoodRequest::getZone() const {
    return zone;
}

// Display
void FoodRequest::display() const {
    cout << "\n--- Food Request ---" << endl;
    cout << "Receiver: " << receiver->getName() << endl;
    cout << "Zone: " << zone << endl;
    cout << "Quantity Needed: " << quantityNeeded << endl;
    cout << "Urgency: " << urgencyLevel << endl;
}