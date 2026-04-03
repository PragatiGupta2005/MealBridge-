#include "../include/SystemManager.h"

// Initialize static instance
SystemManager* SystemManager::instance = nullptr;

// Private constructor
SystemManager::SystemManager() {
    totalMealsSaved = 0;
    totalMatches = 0;
}

// Get instance
SystemManager* SystemManager::getInstance() {
    if (instance == nullptr) {
        instance = new SystemManager();
    }
    return instance;
}

// Add donor
void SystemManager::addDonor(FoodDonor* donor) {
    donors.push_back(donor);
}

// Add receiver
void SystemManager::addReceiver(FoodReceiver* receiver) {
    receivers.push_back(receiver);
}

// Add donation
void SystemManager::addDonation(const FoodDonation& donation) {
    donations.push(donation);
}

// Add request
void SystemManager::addRequest(const FoodRequest& request) {
    requests.push(request);
}

// Matching logic
void SystemManager::runMatching() {
    while (!donations.empty() && !requests.empty()) {

        FoodDonation donation = donations.top();
        FoodRequest request = requests.top();

        donations.pop();
        requests.pop();

        if (donation.getZone() == request.getZone()) {

            cout << "\n✅ MATCH FOUND!" << endl;
            cout << "Donor: " << donation.getDonor()->getName() << endl;
            cout << "Receiver: " << request.getReceiver()->getName() << endl;

            int allocated = request.getQuantityNeeded();
            totalMealsSaved += allocated;
            totalMatches++;

        } else {
            cout << "\n❌ No match (zone mismatch)" << endl;
        }
    }
}

// Display stats
void SystemManager::displayStats() const {
    cout << "\n===== SYSTEM STATS =====" << endl;
    cout << "Total Matches: " << totalMatches << endl;
    cout << "Meals Saved: " << totalMealsSaved << endl;
}