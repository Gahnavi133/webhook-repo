GitHub Webhook Receiver & UI

This project is part of a developer assessment task.  
It captures GitHub repository events using "GitHub Webhooks", stores minimal required data in "MongoDB", and displays repository activity on a clean UI that refreshes every 15 seconds.

---
## Features

- Receives GitHub webhook events:
  - Push
  - Pull Request
  - Merge (PR merged)
- Stores event data in MongoDB Atlas
- Displays activity in a clean UI
- Auto-refreshes UI every 15 seconds
- Built using Flask (Python)

---

 ## Tech Stack

- Backend: Flask (Python)
- Database: MongoDB Atlas
- Frontend: HTML, CSS, JavaScript
- Integration: GitHub Webhooks
- Tunneling: ngrok

---

## 📂 Project Structure
webhook-repo/
│
├── app.py
├── requirements.txt
├── .gitignore
├── templates/
│ └── index.html
└── static/
└── style.css


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/webhook-repo.git
cd webhook-repo

## Create virtual environment
python -m venv venv

## Windows
venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Environment Variables
Create a .env file in the root directory:
MONGO_URI=your_mongodb_atlas_connection_string

## Run the application

## Application Flow

GitHub action occurs (Push / PR / Merge)

GitHub sends webhook to Flask endpoint

Flask processes and stores data in MongoDB

UI polls backend every 15 seconds

Latest activity is displayed

## Sample Output

Travis pushed to staging on 1st April 2021 - 9:30 PM UTC

Travis submitted a pull request from dev to master on 1st April 2021

Travis merged branch dev to master on 2nd April 2021
