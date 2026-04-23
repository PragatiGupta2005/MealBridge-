#ifndef FOODDONOR_H
#define FOODDONOR_H

#include "User.h"
#include <vector>
using namespace std;

// Enum for donor type
enum DonorType {
    HOTEL,
    HOSTEL,
    CATERING_SERVICE
};

class FoodDonor : public User {
private:
    DonorType donorType;

public:
    // Constructor automatically calls when object is created
    FoodDonor(int id, string name, string contact, string zone, DonorType type);

    // Destructor automatically calls when object is destroyed
    ~FoodDonor();

    // Getter read the value of private class variable
    DonorType getDonorType() const;

    // Setter update the value of private class vaiable
    void setDonorType(DonorType type);

    // Functional Methods
    void donateFood();  // will connect with FoodDonation later

    // Overridden Methods (Polymorphism) 
    void displayProfile() const override;
    string getUserType() const override;

    // Helper make your main code simpler, cleaner, and easier to understand
    string getDonorTypeString() const;
};

#endif