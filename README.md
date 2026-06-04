# 🚀 Python Project Generator

A simple but powerful Python script that **automatically creates a production-ready project folder structure** with a single command. No dependencies, no installations — just Python.

---

## 📌 Overview

Instead of manually creating folders and files every time you start a new Python project, this script does it all for you in seconds.

**Just run the script → enter a project name → everything is created automatically.**

---

## 📂 Generated Project Structure

When you run the script, it creates the following structure:
your_project_name/
├── app.py              # Main application entry point
├── README.md           # Project documentation
├── .env                # Environment variables (secret keys, config)
├── .gitignore          # Files to exclude from Git
└── requirements.txt    # Project dependencies list

---
## 🖥️ Demo
<img width="1433" height="751" alt="image" src="https://github.com/user-attachments/assets/507bb7aa-8352-47b0-ac43-2db011110b9c" />
<img width="1878" height="653" alt="image" src="https://github.com/user-attachments/assets/aa6dd69c-c777-4132-9347-cdb3b2cec80e" />


## ⚙️ Requirements

- Python 3.6 or higher
- No external libraries needed (uses only built-in `os` and `sys`)

---

## ▶️ How to Run

### Step 1 — Clone or download the script
```bash
git clone https://github.com/YushBytes/python-project-generator.git
cd python-project-generator
```

### Step 2 — Run the script
```bash
python generate_project.py
```

### Step 3 — Enter your project name when prompted

🚀 Python Project Generator
Enter your project name: greenflag

### Step 4 — Your project is ready!
📁 Created project folder: my_app/
📝 Generating files...
✅ Created: app.py
✅ Created: README.md
✅ Created: .env
✅ Created: .gitignore
✅ Created: requirements.txt

---

## 🛡️ Features

- ✅ Asks for project name at runtime — fully dynamic
- ✅ Validates input — won't allow empty names
- ✅ Checks if folder already exists — prevents accidental overwrite
- ✅ All files created with real starter content — not empty files
- ✅ Works on Windows, Mac, and Linux
- ✅ Zero external dependencies

---

## 📄 What Each Generated File Does

| File | Purpose |
|---|---|
| `app.py` | Main entry point of your project |
| `README.md` | Documentation for your project |
| `.env` | Stores secret keys and config variables |
| `.gitignore` | Tells Git which files to ignore |
| `requirements.txt` | Lists all libraries your project needs |

---

## 💡 After Your Project is Created

```bash
cd your_project_name
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## 👨‍💻 Author

**Ayush Bidwai**  
GitHub: [@YushBytes](https://github.com/YushBytes)

---

## 📄 License

MIT License — free to use and modify.
