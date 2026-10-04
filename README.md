# Railway Management System

A beginner-level Railway Management and Ticket Booking System built using **Python and MySQL**.

This project simulates a railway reservation system where users can register, log in, search trains, book tickets, check PNR status, generate tickets, and receive ticket details through email.

## Features

* User registration and login
* Passenger management
* Train information and train selection
* Railway ticket booking
* Automatic PNR generation
* Seat and berth allocation
* PNR status checking
* PDF ticket generation
* QR code generation for tickets
* Email delivery of generated tickets
* MySQL database integration
* Admin/train data insertion through a separate Python script

## Technologies Used

* **Python**
* **MySQL**
* **MySQL Connector/Python**
* **ReportLab** – PDF ticket generation
* **Tkinter** – GUI
* **QR Code**
* **SMTP/Email** – Ticket email delivery

## Project Structure

```text
Railway-Management-System/
│
├── railway.py
├── add_trains.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

Make sure the following are installed:

* Python 3.x
* MySQL Server
* MySQL Workbench (recommended)
* Required Python packages listed in `requirements.txt`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shashwatm140-mishra/Railway-Management-System.git
cd Railway-Management-System
```

### 2. Install required Python packages

```bash
pip install -r requirements.txt
```

### 3. Set up MySQL

Create the required MySQL database and tables before running the application.

Update the database connection details in the Python files according to your local MySQL setup.

**Do not upload your MySQL password or email credentials to GitHub.**

### 4. Add train data

Run:

```bash
python add_trains.py
```

This script can be used to insert train records into the database.

### 5. Run the application

```bash
python railway.py
```

## Main Modules

### Passenger Registration & Login

Users can create an account and log in to access the railway booking system.

### Train Selection

Users can select a train and provide journey details such as travel date, class, passenger information, and email address.

### Ticket Booking

The system processes the booking and generates a unique PNR along with seat/berth information.

### PNR Status

Users can use their PNR to retrieve their booking information.

### PDF Ticket

After a successful booking, the system generates a PDF ticket containing the booking details.

### QR Code

A QR code is generated as part of the ticket for storing booking information.

### Email Ticket

The generated ticket can be sent to the passenger's email address.

## Project Flow

```text
User Registration/Login
        ↓
Passenger Menu
        ↓
Train Selection
        ↓
Enter Journey & Passenger Details
        ↓
Ticket Booking
        ↓
PNR + Seat/Berth Allocation
        ↓
PDF Ticket + QR Code
        ↓
Email Ticket
```

## Database

The application uses **MySQL** for storing railway-related data such as:

* Passenger information
* User accounts
* Train information
* Booking information
* PNR details
* Seat/berth information

A database setup file will be added to the repository in a future update.

## Limitations

This is an **educational project** developed to demonstrate Python programming and MySQL database integration.

It is **not an official Indian Railways or IRCTC booking system** and does not connect to their real-time reservation systems.

Train information and booking operations are handled within the project's own database.

## Future Improvements

* Web-based frontend using HTML, CSS and JavaScript
* Flask backend
* Password hashing and improved authentication
* Parameterized SQL queries
* Environment variables for sensitive credentials
* Improved database architecture
* Online payment integration
* Real-time train availability
* Improved user interface
* Admin dashboard
* Deployment as a web application

## Learning Outcomes

Through this project, I worked with:

* Python programming
* Object-oriented and procedural programming concepts
* MySQL database connectivity
* SQL queries
* CRUD operations
* User authentication
* Ticket booking logic
* PDF generation
* QR code generation
* Email automation
* Git and GitHub

## Disclaimer

This project is created for **educational and demonstration purposes only**.

It is not affiliated with, operated by, or connected to **Indian Railways or IRCTC**.
