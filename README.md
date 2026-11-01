SECUREX | Advanced Password Generator

A Modern, Secure & Customizable Password Generation Application

SECUREX is a Python-based desktop application designed to generate strong, random, and customizable passwords through a clean and intuitive graphical user interface. It focuses on password complexity, ease of use, and secure password generation.

Overview

SECUREX provides users with flexible password generation options, allowing them to customize password length and character combinations according to their requirements.

Key Features

- Secure Password Generation: Uses Python's "secrets" module for cryptographically strong random password generation.
- Custom Password Length: Supports password lengths from 4 to 64 characters.
- Character Customization: Includes uppercase letters, lowercase letters, numbers, and special characters.
- Password Visibility: Show or hide generated passwords.
- Clipboard Integration: Copy generated passwords instantly.
- Password Strength Indicator: Displays a password complexity assessment.
- Regenerate Option: Generate a new password instantly.
- Generation History: View recent generation timestamps without storing actual passwords.
- Modern User Interface: Built with CustomTkinter for a modern desktop experience.

Technology Stack

Technology| Purpose
Python| Core programming language
CustomTkinter| Graphical user interface
Tkinter| Message boxes and clipboard integration
Secrets| Secure random generation
String| Character set management

Installation & Execution

1. Clone the repository

git clone YOUR_REPOSITORY_URL

2. Navigate to the project directory

cd SECUREX-Advanced-Password-Generator

3. Install dependencies

pip install customtkinter

4. Launch the application

python main.py

Project Structure

SECUREX/
│
├── main.py
├── README.md
└── main_backup.py

Security Considerations

SECUREX uses Python's "secrets" module instead of the standard pseudo-random generator for password generation. Generated passwords are not retained in the history feature.

Project Information

Project Name: SECUREX – Advanced Password Generator
Domain: Python Programming
Internship Organization: Oasis Infobyte
Developer: Aditi Khobragade

Learning Outcomes

- Python application development
- GUI development using CustomTkinter
- Secure random password generation
- Event handling and clipboard integration
- User interface design and functionality

---

Developed as part of the Oasis Infobyte Python Programming Internship.

Building practical applications through Python and continuous learning.
