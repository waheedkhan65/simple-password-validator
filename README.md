# 🔐 Password Validator

A simple Python script to validate user-entered passwords based on custom security rules.  
It checks for minimum length, presence of both letters and numbers, and gives user-friendly feedback.

## 🚀 Features

- Ensures password is **at least 8 characters long**
- Requires at least **one letter**
- Requires at least **one digit**
- Provides clear error messages for each missing rule

## 🧠 How It Works

The script uses Python string methods and generator expressions like:
- `char.isdigit()` to check for numeric characters
- `char.isalpha()` to check for alphabetic characters
- `any()` to validate that at least one character meets the criteria

## 📦 Requirements

- Python 3.x  
> No external libraries needed

## 🖥️ Usage

Run the script in your terminal or any Python environment:

```bash
python main.py

Enter your passkey: abc12345
✅ Password is valid


Enter your passkey: abc
❌ Password is invalid
* Must be at least 8 characters long
* Must contain numbers

