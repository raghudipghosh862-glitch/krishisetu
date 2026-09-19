

# 🌾 KrishiSetu

### Agricultural Supply Chain & Logistics Platform

**Bridging Farmers, Transporters, and Buyers — Securely and Transparently**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![Django](https://img.shields.io/badge/Django-REST%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#)
[![Status](https://img.shields.io/badge/Status-Active%20Development-yellow?style=for-the-badge)](#)



---

## 📖 About The Project

**KrishiSetu** (कृषि + सेतु — "Bridge of Agriculture") is an integrated logistics and escrow platform designed to eliminate middlemen in agricultural trade. It connects **farmer groups**, **transport companies**, and **buyers** on a single trusted platform — with secure payments, verified deliveries, and real-time freight tracking baked in from day one.


---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧑‍🌾 **Role-Based Portals** | Dedicated dashboards for Group Leaders (Farmers), Transport Companies, Drivers, and Buyers |
| 🔒 **Secure Escrow Payments** | Buyers lock in lots via an advance payment gateway; funds stay in escrow until delivery is verified |
| 🔑 **OTP-Based Delivery Verification** | Cryptographic OTP validation at drop-off confirms crops arrive in good condition before funds release |
| 📦 **Dynamic Logistics Board** | Transport companies browse open delivery requests, accept trips, and assign drivers in real time |
| 📍 **Live Freight Tracking** | End-to-end visibility of shipments from farm to buyer |

---

## 🛠️ Tech Stack



![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white)
![Razorpay](https://img.shields.io/badge/Razorpay-Test%20Mode-0C2451?style=flat-square&logo=razorpay&logoColor=white)


| Layer | Technology |
|---|---|
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Backend** | Python, Django, Django REST Framework |
| **Database** | PostgreSQL / SQLite |
| **Payments** | Custom UPI Simulation / Razorpay (Test Mode) |

---

## 🚀 Installation & Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/raghudipghosh862-glitch/krishisetu.git
cd krishisetu
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the development server

```bash
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser. 🎉

---

## 👥 User Roles



| 🧑‍🌾 Farmer / Group Leader | 🚛 Transport Company | 🚗 Driver | 🛒 Buyer |
|:---:|:---:|:---:|:---:|
| Lists crop lots for sale | Views & accepts delivery requests | Executes assigned trips | Secures lots with escrow payment |
| Tracks payment status | Assigns drivers to trips | Updates delivery status | Verifies delivery via OTP |

---

## 🗺️ Roadmap

- [x] Role-based authentication & dashboards
- [x] Escrow payment flow
- [x] OTP delivery verification
- [ ] Live GPS tracking integration
- [ ] Multi-language support (Hindi, regional languages)
- [ ] Mobile app (Android/iOS)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.
---

⭐ **Star this repo if you find it useful!** ⭐

