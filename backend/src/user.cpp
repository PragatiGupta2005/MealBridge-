#include "../include/User.h"

// Constructor
User::User(int id, string name, string contact, string zone) {
    this->userId = id;
    this->name = name;
    this->contact = contact;
    this->zone = zone;
}

// Destructor
User::~User() {
    // Virtual destructor ensures proper cleanup
}

// Getters
int User::getUserId() const {
    return userId;
}

string User::getName() const {
    return name;
}

string User::getContact() const {
    return contact;
}

string User::getZone() const {
    return zone;
}

// Setters
void User::setName(string name) {
    this->name = name;
}

void User::setContact(string contact) {
    this->contact = contact;
}

void User::setZone(string zone) {
    this->zone = zone;
}