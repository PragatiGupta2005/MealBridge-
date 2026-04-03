#ifndef SYSTEMMANAGER_H
#define SYSTEMMANAGER_H

#include <iostream>
#include <vector>
#include <queue>

#include "FoodDonor.h"
#include "FoodReceiver.h"
#include "FoodDonation.h"
#include "FoodRequest.h"

using namespace std;

class SystemManager {
private:
    // Singleton instance
    static SystemManager* instance;

    // Data storage
    vector<FoodDonor*> donors;
    vector<FoodReceiver*> receivers;

    priority_queue<FoodDonation, vector<FoodDonation>, DonationCompare> donations;
    priority_queue<FoodRequest, vector<FoodRequest>, RequestCompare> requests;

    // Statistics
    int totalMealsSaved;
    int totalMatches;

    // Private constructor
    SystemManager();

public:
    // Get instance
    static SystemManager* getInstance();

    // User management
    void addDonor(FoodDonor* donor);
    void addReceiver(FoodReceiver* receiver);

    // Data entry
    void addDonation(const FoodDonation& donation);
    void addRequest(const FoodRequest& request);

    // Core logic
    void runMatching();

    // Statistics
    void displayStats() const;
};

#endif