# 📚 Elibrary

An online bookstore where users can **browse, purchase, and pay for books securely**.  
Built with Python’s Django framework, this app provides a smooth shopping experience with integrated Stripe payments and user authentication.

## ✨ Features
- **Book Listings & Detail Pages:** Browse all available books and view detailed descriptions.  
- **Order & Checkout:** Add books to a cart, place orders, and track purchases.  
- **Stripe Payment Integration:** Secure online payments with Stripe.  
- **User Authentication:** Sign up, login, and manage personal orders.

## 🛠 Tech Stack
- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (default, easy to switch to PostgreSQL/MySQL)  

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Kkiprop/Elibrary.git
cd Elibrary
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py migrate
```

### 5️⃣ Run the Development Server
```bash
python manage.py runserver
```
Visit the site at `http://127.0.0.1:8000/`.

## 📂 Project Structure (key folders)
```
Elibrary/
│
├─ elibrary/       # Core Django app
├─ templates/      # HTML templates
├─ static/         # CSS/JS assets
└─ manage.py
```

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss proposed improvements.

## 📜 License
This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this project.

## 🔗 Live Repo
[GitHub Repository](https://github.com/Kkiprop/Elibrary)

## 📜 Screenshots
https://github.com/Kkiprop/Elibrary/issues/1#issue-3448356044
