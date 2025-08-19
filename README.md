# Personal-firewall-python
A simple personal firewall built using python
# Personal Firewall Using Python  

## 📌 Introduction  
This project is a simple **personal firewall** built in Python for Windows 10.  
It monitors network connections, applies allow/deny rules using Windows `netsh`, and provides basic control over which apps can access the internet.  

---

## ⚡ Features  
- Monitors active network connections  
- Allows or blocks applications via Windows Firewall  
- Lightweight and beginner-friendly  

---

## 🛠️ Tools & Libraries  
- Python 3.x  
- Windows 10 (tested)  
- Libraries: `socket`, `psutil`, `subprocess`  
- Command-line utility: `netsh`  

---

## 🚀 Setup & Usage  
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/personal-firewall-python.git
   cd personal-firewall-python
   pip install psutil
   python firewall.py
