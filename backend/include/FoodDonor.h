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
    // Constructor
    FoodDonor(int id, string name, string contact, string zone, DonorType type);

    // Destructor
    ~FoodDonor();

    // Getter
    DonorType getDonorType() const;

    // Setter
    void setDonorType(DonorType type);

    // Functional Methods
    void donateFood();  // will connect with FoodDonation later

    // Overridden Methods (Polymorphism)
    void displayProfile() const override;
    string getUserType() const override;

    // Helper
    string getDonorTypeString() const;
};

#endif