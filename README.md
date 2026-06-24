# *** Desktop Tracking Application ***

## Project Overview ::>>
This is a Python-based Desktop Tracking Application built using **PySide6** and **MySQL**.  
It tracks user activity, captures screenshots, and syncs data in the background like a real-time monitoring system.

----------------------------------------------------------------------------------------------

##  Features ::>>

-  Login System (Mock Authentication)
-  Dashboard UI (Start / Stop Tracking)
-  Automatic Screenshot Capture (every 60 seconds)
-  Keyboard &  Mouse Activity Tracking
-  MySQL Database Storage
-  Background Sync Service (uploads data automatically)
-  Session Management (start / stop sessions)
-  System Tray Support (runs in background)
-  Error Handling for API/DB failures

----------------------------------------------------------------------------------------------

##  Architecture Overview ::>>
UI Layer (PySide6)
↓
Tracker Controller
↓
Activity Tracker + Screenshot Module
↓
Local Storage (MySQL)
↓
Sync Service (Background Thread)
↓
Mock API Server

----------------------------------------------------------------------------------------------




##  Modules Explanation ::>>

### 1. UI Module
Handles:
- Login Screen
- Dashboard
- System Tray

---

### 2. Tracker Module
Responsible for:
- Starting & stopping tracking sessions
- Managing threads
- Coordinating all services

---

### 3. Activity Tracker
Tracks:
- Keyboard events
- Mouse events

---

### 4. Screenshot Module
- Captures screen every interval
- Saves with timestamp filename

---

### 5. Database Layer (MySQL)
Stores:
- Users
- Sessions
- Activity Logs
- Screenshots Metadata

---

### 6. Sync Service
- Runs in background thread
- Syncs data every 30 seconds
- Handles network failures gracefully

---

##  Assumptions Made ::>>

- Authentication is mock-based (no real backend login API)
- API endpoints are simulated
- System is designed for Windows OS
- MySQL is running locally
- Screenshots stored in local folder before sync
- Single user session at a time

---

##  Database Tables ::>>

- users
- tracking_sessions
- activity_logs
- screenshots

---

## 🚀 Setup Instructions

### 1. Install Dependencies
```bash
    pip install -r requirements.txt

2. Setup MySQL Database
    Create database: desktop_tracker
        Import file:
            desktop_tracker.sql

3. Run Application
    python main.py


Requirements ::>>
Python 3.11+
PySide6
PyMySQL
Requests
PyAutoGUI

----------------------------------------------------------------------------------------------