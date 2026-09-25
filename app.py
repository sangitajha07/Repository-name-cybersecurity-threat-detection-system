from flask import Flask, render_template, request
import datetime
import random

app = Flask(__name__)

attempts = {}
blocked_ips = set()

def log_event(ip, status):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {ip} - {status}\n")

def get_stats():
    try:
        with open("log.txt", "r") as f:
            logs = f.readlines()
    except:
        logs = []

    total = len(logs)
    failed = sum(1 for l in logs if "FAILED" in l)
    blocked = sum(1 for l in logs if "BLOCKED" in l)

    return {
        "total": total,
        "failed": failed,
        "blocked": blocked,
        "top_ip": "8.8.8.8"
    }

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    ip = request.remote_addr
    user = request.form.get("username")
    pwd = request.form.get("password")

    if ip in blocked_ips:
        return "🚫 IP BLOCKED"

    if user == "admin" and pwd == "1234":
        log_event(ip, "SUCCESS")
        return "✅ Login Success"

    else:
        attempts[ip] = attempts.get(ip, 0) + 1
        log_event(ip, "FAILED")

        if attempts[ip] >= 3:
            blocked_ips.add(ip)
            log_event(ip, "BLOCKED")
            return "🚨 IP BLOCKED!"

        return f"❌ Wrong! Attempt {attempts[ip]}"

@app.route("/dashboard")
def dashboard():
    stats = get_stats()
    return render_template("dashboard.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
