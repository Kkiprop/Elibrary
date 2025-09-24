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

![App Screenshot](https://private-user-images.githubusercontent.com/131892136/493245021-c5db2c85-dafa-4062-9253-266838b3a9fc.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTg3MDQ1MDgsIm5iZiI6MTc1ODcwNDIwOCwicGF0aCI6Ii8xMzE4OTIxMzYvNDkzMjQ1MDIxLWM1ZGIyYzg1LWRhZmEtNDA2Mi05MjUzLTI2NjgzOGIzYTlmYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwOTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDkyNFQwODU2NDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03YmRjZjg0NDI2YzUxNDgwZGEwMWNjZGYwM2UwMDU0MjQ4YWFkMTdkY2IwMWI1MGZmYjJkNWQ0ZTNmNmU3M2IwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.qXY3kKtgjZrszpg39BMLKW_z7e001bE7H3_sTUdHmOs)

![App Screenshot](https://private-user-images.githubusercontent.com/131892136/493245022-f3c746e2-071c-4772-bdc6-8336a5c7302a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTg3MDQ3MzYsIm5iZiI6MTc1ODcwNDQzNiwicGF0aCI6Ii8xMzE4OTIxMzYvNDkzMjQ1MDIyLWYzYzc0NmUyLTA3MWMtNDc3Mi1iZGM2LTgzMzZhNWM3MzAyYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwOTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDkyNFQwOTAwMzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hN2U0OTNmODA5ZDk3NmE5M2IyZTRiYjk2MjRlMTRmMmZjZGMyMGMyZjlmM2I4M2I4ODJhYmY3NTA0ZTNhOTk5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.uE8EtEKfoKD4FW4KQBtQhHteyiMcakc1ZShzcpgwfZ8)
