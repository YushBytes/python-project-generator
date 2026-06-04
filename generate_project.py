import os
import sys

# ─────────────────────────────────────────────
# STEP 1: Ask the user for a project name
# ─────────────────────────────────────────────
def get_project_name():
    print("\n🚀 Python Project Generator")
    print("=" * 35)
    project_name = input("Enter your project name: ").strip()

    # Validate: must not be empty
    if not project_name:
        print("❌ Error: Project name cannot be empty.")
        sys.exit(1)

    # Validate: replace spaces with underscores (safe folder name)
    project_name = project_name.replace(" ", "_")
    return project_name


# ─────────────────────────────────────────────
# STEP 2: Create the project folder
# ─────────────────────────────────────────────
def create_project_folder(project_name):
    if os.path.exists(project_name):
        print(f"❌ Error: Folder '{project_name}' already exists. Choose a different name.")
        sys.exit(1)

    os.makedirs(project_name)
    print(f"\n📁 Created project folder: {project_name}/")


# ─────────────────────────────────────────────
# STEP 3: Define file contents
# ─────────────────────────────────────────────
def get_file_contents(project_name):
    files = {

        "app.py": f'''\
# {project_name} - Main Application Entry Point

def main():
    print("Welcome to {project_name}!")

if __name__ == "__main__":
    main()
''',

        "README.md": f'''\
# {project_name}

## 📌 Overview
A brief description of what this project does.

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/{project_name}.git
cd {project_name}
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Copy `.env` and fill in your values:
```bash
cp .env .env.local
```

### 5. Run the app
```bash
python app.py
```

## 📄 License
MIT
''',

        ".env": '''\
# Environment Variables
# DO NOT commit this file to version control

APP_NAME=MyApp
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
''',

        ".gitignore": '''\
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.egg
*.egg-info/
dist/
build/
.eggs/

# Virtual Environment
venv/
env/
.venv/

# Environment Variables
.env
.env.local
.env.*.local

# IDE / Editor
.vscode/
.idea/
*.swp
*.swo

# OS Files
.DS_Store
Thumbs.db

# Logs
*.log
logs/
''',

        "requirements.txt": '''\
# Add your project dependencies here
# Example:
# flask==3.0.0
# requests==2.31.0
# python-dotenv==1.0.0
''',
    }

    return files


# ─────────────────────────────────────────────
# STEP 4: Write all files to the project folder
# ─────────────────────────────────────────────
def create_files(project_name, files):
    for filename, content in files.items():
        filepath = os.path.join(project_name, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"   ✅ Created: {filename}")


# ─────────────────────────────────────────────
# STEP 5: Print final success summary
# ─────────────────────────────────────────────
def print_summary(project_name):
    print(f"""
{'=' * 35}
🎉 Project '{project_name}' is ready!

📂 Structure:
   {project_name}/
   ├── app.py
   ├── README.md
   ├── .env
   ├── .gitignore
   └── requirements.txt

▶  Next Steps:
   1. cd {project_name}
   2. python -m venv venv
   3. source venv/bin/activate
   4. pip install -r requirements.txt
   5. python app.py
{'=' * 35}
""")


# ─────────────────────────────────────────────
# MAIN: Run all steps
# ─────────────────────────────────────────────
if __name__ == "__main__":
    project_name = get_project_name()
    create_project_folder(project_name)
    print("\n📝 Generating files...")
    files = get_file_contents(project_name)
    create_files(project_name, files)
    print_summary(project_name)