# ☕ Coffee Marketplace

The **Coffee Marketplace** is the official product listing and catalog application for House of Beans — a specialty coffee roaster delivering high-quality beans to customers around the world. This app powers the product browsing experience and is designed as a modern, modular 3-tier web application.

---

## 📦 Overview

This service enables customers to:

- View available coffee products
- Check prices and product descriptions
- Interface with our future e-commerce and inventory systems

---

## 🏗 Architecture

This application is built with simplicity and modularity in mind, following a standard 3-tier web architecture:
- **Frontend**: Renders product listings via browser using API calls.
- **Backend**: Python Flask application exposing RESTful endpoints.
- **Database**: Lightweight SQLite used for development and testing (can be swapped with PostgreSQL/MySQL in production).

---

## ⚙️ Technology Stack

| Component | Technology         |
|----------:|--------------------|
| Frontend  | HTML, Vanilla JS   |
| Backend   | Python 3, Flask    |
| Database  | SQLite (default)   |
| Infra     | GitHub, Docker     |

> This service is cloud-native compatible and designed to be containerized or deployed as a serverless function if needed.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Setup Instructions

```bash
# Navigate to backend
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

Then open frontend/index.html in a browser.

API Endpoint
	•	GET /products – Returns a list of current coffee products in JSON format.

🧪 Sample Products

On startup, the backend seeds the database with two core offerings:
	•	Espresso – Bold and rich, $2.50
	•	Latte – Smooth and creamy, $3.00

You can expand this list via the models.py file.

👥 Contributors

Maintained by the House of Beans engineering team.