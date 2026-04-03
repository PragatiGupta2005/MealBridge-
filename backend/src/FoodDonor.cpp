#include "../include/FoodDonor.h"

// Constructor
FoodDonor::FoodDonor(int id, string name, string contact, string zone, DonorType type)
    : User(id, name, contact, zone) {
    this->donorType = type;
}

// Destructor
FoodDonor::~FoodDonor() {
    // No dynamic memory, so nothing special
}

// Getter
DonorType FoodDonor::getDonorType() const {
    return donorType;
}

// Setter
void FoodDonor::setDonorType(DonorType type) {
    this->donorType = type;
}

// Convert enum to string (for display)
string FoodDonor::getDonorTypeString() const {
    switch (donorType) {
        case HOTEL: return "Hotel";
        case HOSTEL: return "Hostel";
        case CATERING_SERVICE: return "Catering Service";
        default: return "Unknown";
    }
}

// Functional Method
void FoodDonor::donateFood() {
    cout << "Donor " << name << " is donating food." << endl;
    // Later: connect to FoodDonation class
}

// Overridden Method
void FoodDonor::displayProfile() const {
    cout << "\n--- Food Donor Profile ---" << endl;
    cout << "ID: " << userId << endl;
    cout << "Name: " << name << endl;
    cout << "Contact: " << contact << endl;
    cout << "Zone: " << zone << endl;
    cout << "Donor Type: " << getDonorTypeString() << endl;
}

// Overridden Method
string FoodDonor::getUserType() const {
    return "Food Donor";
}