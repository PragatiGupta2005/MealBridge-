🍽️ Meal Bridge  
A Smart Food Redistribution System for Reducing Food Waste and Hunger

📌 Project Description

Meal Bridge is a smart food redistribution platform designed to bridge the gap between food surplus and food demand.  
The system connects **food donors** such as Hotels, Hostels, and Catering Services with **food receivers** like NGOs and Orphanages, ensuring that excess food is efficiently redistributed instead of being wasted.
This project simulates a real-world food logistics system using **Object-Oriented Programming (OOPS)** in C++ and a **Python-based GUI**, without relying on external databases or APIs.

🎯 Objectives

- Reduce food wastage  
- Provide food to needy communities  
- Optimize allocation using smart algorithms  
- Demonstrate real-world application of OOPS concepts  
- Build a scalable and modular system  

🧠 System Architecture

The system follows a **layered architecture** with clear separation of concerns:
[ Python GUI (Frontend) ]
↓
[ File-based Communication Layer ]
↓
[ C++ Backend (OOPS + Algorithms) ]
↓
[ In-Memory Data Structures (STL) ]

🔹 Frontend (Python - Tkinter)
- Provides interactive UI  
- Handles user input and visualization  
- Sends data to backend via files  

🔹 Backend (C++)
- Implements business logic using OOPS  
- Handles food matching and allocation  
- Uses STL for efficient data management  

🔹 Communication Layer
- Uses `input.txt` and `output.txt`  
- Simulates real-world API interaction  

🧱 Object-Oriented Design

The project is built using core OOPS principles:

🔹 Class Hierarchy

- User (Abstract Class)
- FoodDonor (Hotel, Hostel, Catering Service)  
- FoodReceiver(NGO, Orphanage)  
- FoodItem
- FoodDonation  
- FoodRequest
- SystemManager (Singleton)  

⚙️ Core Workflow

1. User opens GUI  
2. Registers as donor or receiver  
3. Donor enters food donation details  
4. Receiver submits food request  
5. Data is passed to C++ backend  
6. Matching algorithm processes data  
7. Best matches are selected  
8. Results are displayed in GUI  
9. Statistics are updated  

🧠 Smart Matching Algorithm

The system prioritizes allocation based on:

1. Expiry Time → earliest expiry first  
2. Urgency Level → high urgency first  
3. Zone Matching → same zone preferred  

🔹 Data Structures Used

- `priority_queue`  
- `vector`  
- `map`  

🗺️ Zone-Based Routing

Users are grouped into zones:

- Zone A  
- Zone B  
- Zone C  

Advantages:
- Simplifies routing  
- Faster matching  
- Efficient simulation  

 🖥️ GUI Features

- 📊 Dashboard (stats & alerts)  
- 🍱 Donation Panel  
- 🙏 Request Panel  
- 🔄 Matching Interface  
- 📈 Statistics Dashboard  
- 🗺️ Zone Map  
- 🔔 Priority Alerts  
- 📜 History Log  
- 🏆 Leaderboard  
- 📈 Trend Charts  

📊 Output Metrics

- Total meals saved  
- Successful matches  
- Food wastage reduced  
- System efficiency  

📁 Folder Structure
MealBridge/
│
├── backend/
│ ├── include/
│ ├── src/
│ └── build/
│
├── frontend/
│ ├── app.py
│ ├── ui/
│ ├── utils/
│ └── assets/
│
├── data/
│ ├── input.txt
│ └── output.txt
│
├── docs/
│ └── UML/
│
├── tests/
│
├── README.md
└── .gitignore

 🚀 Future Enhancements

- Database integration  
- GPS-based tracking  
- Mobile application  
- AI-based demand prediction  


⭐ Conclusion
Meal Bridge is a scalable and efficient system that leverages **OOPS, algorithms, and UI design** to solve real-world food waste and hunger problems.
