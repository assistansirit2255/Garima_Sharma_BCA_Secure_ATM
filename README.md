# Garima_Sharma_BCA_Secure_ATM
# 🏦 Simple ATM Web Application 💻

## 📝 Description

This project implements a prototype for a web-based ATM (Automated Teller Machine) system. It allows users to securely log in using multiple factors (ATM Number, simulated fingerprint, PIN) and perform basic banking transactions like checking balance, withdrawing funds, and depositing money. The application uses the Flask web framework for the backend logic and SQLite for simple data persistence. It serves as a demonstration of web application development, database interaction, and basic security principles like password hashing.

## ✨ Features

* *Secure Multi-Factor Login:* Requires ATM number, a simulated fingerprint code (12345), and a securely hashed PIN for authentication.
* *Account Balance Inquiry:* Allows logged-in users to view their current account balance.
* *Cash Withdrawal:* Enables users to withdraw funds, validating against the available balance.
* *Cash Deposit:* Allows users to deposit funds into their account.
* *Session Management:* Uses Flask sessions to maintain user login state.
* *Simple Web Interface:* Basic HTML/CSS frontend for user interaction (Login, Dashboard, Transaction pages).

## 💻 Technology Stack

* *Programming Language:* Python 3.x 🐍
* *Web Framework:* Flask
* *Security Library:* Werkzeug (for PIN hashing)
* *Database:* SQLite 💾
* *Frontend:* HTML5, CSS3
* *Package Management:* pip
* *Environment:* Standard Python Virtual Environment (recommended)

## ▶ Running the Application

1.  *Ensure Prerequisites:* Make sure Python 3.x and pip are installed.
2.  *Install Dependencies:* Navigate to the project directory in your terminal and run:
    
    pip install Flask werkzeug
    
3.  *Run the Flask App:* Execute the main application script:
        python app.py
    
4.  *Access the App:* The terminal will show output indicating the Flask server is running (typically on http://127.0.0.1:5000/). Open this URL in your web browser.
5.  *Login:* Use the atm_number and the original PIN (that you hashed) from your schema.sql configuration, along with the simulated fingerprint 12345.

## 🚀 Future Work

Potential enhancements for this project include:

* Replace simulated fingerprint/OTP with actual integration (if hardware/services were available).
* Implement detailed transaction history logging for users.
* Add more robust error handling and user feedback mechanisms.
* Enhance the User Interface (UI) and User Experience (UX).
* Migrate to a more scalable database system (e.g., PostgreSQL) for larger applications.
* Implement user registration and account management features.
* Add administrative functionalities.
* Package for easier deployment (e.g., using Docker 🐳).

## 👥 Team Members

* Garima Sharma

## 🧑‍🏫 Project Co-ordinator

* DR. AMAN JATAIN



