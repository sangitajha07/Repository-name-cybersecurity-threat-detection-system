# 🛡️ Cybersecurity Threat Detection System

An AI/ML-based web application designed to detect suspicious activities and potential cybersecurity threats using Python, Flask, and Machine Learning.

## 📌 Project Overview

The Cybersecurity Threat Detection System analyzes security-related activities such as failed login attempts and network traffic to identify potentially suspicious behavior.

The system provides a web-based interface for threat detection, login monitoring, security log analysis, and dashboard-based monitoring.

## 🚀 Features

- 🔐 Login activity monitoring
- 🚨 Suspicious activity detection
- 🤖 Machine Learning-based threat classification
- 📊 Security dashboard
- 🌐 Network traffic analysis
- 📝 Security log monitoring
- 🚫 IP blocking after multiple failed login attempts
- 📈 Threat statistics and monitoring

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- JavaScript
- Machine Learning
- Git & GitHub

## 🧠 Machine Learning

The project uses a Machine Learning model to analyze security-related parameters and classify activity as:

- Safe Activity
- Threat Detected

The model is integrated with the Flask web application for real-time prediction through the web interface.

## 📂 Project Structure

```text
Cybersecurity-Threat-Detection-System/
│
├── app.py
├── model.py
├── dataset.csv
├── log.json
├── log.txt
│
├── templates/
│   ├── admin.html
│   ├── base.html
│   ├── dashboard.html
│   ├── home.html
│   └── index.html
│
└── static/
    ├── script.js
    └── style.css
