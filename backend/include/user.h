#ifndef USER_H
#define USER_H

#include <iostream>
#include <string>
using namespace std;

// Abstract Base Class
class User {
protected:
    int userId;
    string name;
    string contact;
    string zone;

public:
    // Constructor
    User(int id, string name, string contact, string zone);

    // Virtual Destructor
    virtual ~User();

    // Getters (Encapsulation)
    int getUserId() const;
    string getName() const;
    string getContact() const;
    string getZone() const;

    // Setters
    void setName(string name);
    void setContact(string contact);
    void setZone(string zone);

    // Pure Virtual Functions (Abstraction + Polymorphism)
    virtual void displayProfile() const = 0;
    virtual string getUserType() const = 0;
};

#endif