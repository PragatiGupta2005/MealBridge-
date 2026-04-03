#include <iostream>
#include "SystemManager.h"

using namespace std;

int main() {

    // Get Singleton instance
    SystemManager* system = SystemManager::getInstance();

    // ==============================
    // 1. Create Donors
    // ==============================
    FoodDonor* d1 = new FoodDonor(1, "ABC Hotel", "9876543210", "Zone A", HOTEL);
    FoodDonor* d2 = new FoodDonor(2, "City Hostel", "9123456789", "Zone B", HOSTEL);

    // Add donors to system
    system->addDonor(d1);
    system->addDonor(d2);

    // ==============================
    // 2. Create Receivers
    // ==============================
    FoodReceiver* r1 = new FoodReceiver(101, "Helping NGO", "9988776655", "Zone A", NGO, 3);
    FoodReceiver* r2 = new FoodReceiver(102, "Hope Orphanage", "8877665544", "Zone B", ORPHANAGE, 2);

    // Add receivers
    system->addReceiver(r1);
    system->addReceiver(r2);

    // ==============================
    // 3. Create Donations
    // ==============================
    FoodDonation donation1(201, d1, "Zone A");
    donation1.addFoodItem(FoodItem("Rice", 50, 5));
    donation1.addFoodItem(FoodItem("Bread", 30, 2));

    FoodDonation donation2(202, d2, "Zone B");
    donation2.addFoodItem(FoodItem("Dal", 40, 6));
    donation2.addFoodItem(FoodItem("Chapati", 60, 3));

    // Add donations
    system->addDonation(donation1);
    system->addDonation(donation2);

    // ==============================
    // 4. Create Requests
    // ==============================
    FoodRequest request1(301, r1, 40, 3, "Zone A");  // High urgency
    FoodRequest request2(302, r2, 50, 2, "Zone B");  // Medium urgency

    // Add requests
    system->addRequest(request1);
    system->addRequest(request2);

    // ==============================
    // 5. Display Initial Data
    // ==============================
    cout << "\n===== INITIAL DATA =====" << endl;

    d1->displayProfile();
    d2->displayProfile();

    r1->displayProfile();
    r2->displayProfile();

    cout << "\nDonations:" << endl;
    donation1.display();
    donation2.display();

    cout << "\nRequests:" << endl;
    request1.display();
    request2.display();

    // ==============================
    // 6. Run Matching Algorithm
    // ==============================
    cout << "\n===== RUNNING MATCHING =====" << endl;
    system->runMatching();

    // ==============================
    // 7. Display Statistics
    // ==============================
    system->displayStats();

    // ==============================
    // 8. Cleanup Memory
    // ==============================
    delete d1;
    delete d2;
    delete r1;
    delete r2;

    return 0;
}