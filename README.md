# 🎯 Project Title: Phishing Detector

---

## 👥 Team Members
- **Shahbaz Ali** (Team Leader)
- **Harshit** (Team Member)
- **Himanshu** (Team Member)
- **Kartik Yadav** (Team Member)

---

## 📝 Project Overview
Phishing Detector is a web-based tool that helps users analyze URLs and determine whether they are safe or potentially malicious. It offers a simple and user-friendly interface to input suspicious links and receive a visual safety result.

---

## 🚀 Features
- 🔍 URL Analysis
- ✅ Safe / ⚠️ Suspicious Result Display
- 📋 Safety Tips Display
- 🎨 Clean & Responsive UI

---

## 🧰 Tech Stack
- **Frontend:** HTML5, CSS3
- **Backend:** Python (Flask)
- **Deployment:** Localhost (can be deployed on Render/Heroku)

---

## 🖼 Screenshots/Diagrams
_Add screenshots here_
+-----------------------+
|  User (Browser)      |
|  - Enters URL        |
|  - Submits Form      |
+----------+------------+
           |
           v
+-----------------------+
|  Flask App (index()) |
|  - POST Request       |
|  - Extract URL        |
|  - Parse Domain       |
|  - Check Trust List   |
|  - Generate Result    |
+----------+------------+
           |
           v
+------------------------+
|  HTML Template         |
|  - Renders Result      |
|  - Shows ✓ or ⚠️       |
|  - Highlights Safe/Danger |
+----------+------------+
           |
           v
+------------------------+
|  User Sees Result      |
|  - ✅ Legitimate URL   |
|  - ⚠️ Suspicious URL   |
|  - Safety Tips Shown   |
+------------------------+
