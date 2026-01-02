# 🔐 PyPass Manager (Lite)

> **Minimalist. Local. Efficient.**
> A lightweight, desktop-based password manager built to keep your credentials organized and your workflow uninterrupted.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge)
![Data](https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas)

## ⚡ About The Project

Stop forgetting your passwords. This application provides a clean Graphical User Interface (GUI) to store, manage, and generate secure credentials locally. No cloud subscriptions, no internet required—just you and your data.

The project utilizes **Pandas** for robust data handling and **NumPy** for high-entropy randomization, wrapped in a native **Tkinter** interface.

## 🚀 Features

* **🖥️ Intuitive Dashboard:** Clean input fields for Website, Username, and Password management.
* **🎲 Smart Generator:** Instantly generate strong, 12-character alphanumeric passwords (A-Z, 0-9, symbols) using NumPy's random choice algorithms.
* **💾 Persistent Storage:** Automatically saves and loads your credentials from a local `passwords.csv` file using Pandas DataFrames.
* **⚡ Instant Validation:** Built-in error handling ensures no empty fields are saved.

## 🛠️ Built With

* **Python 3**
* **Tkinter** (Standard GUI Library)
* **Pandas** (Data Manipulation & CSV I/O)
* **NumPy** (Randomization Engine)

## 📦 Installation & Setup

1.  **Clone the Repo** (or download the file):
    ```bash
    git clone [https://github.com/yourusername/pypass-manager.git](https://github.com/yourusername/pypass-manager.git)
    ```

2.  **Install Dependencies:**
    You need `pandas` and `numpy` to run the magic.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App:**
    ```bash
    python project.py
    ```

## 🎮 How to Use

1.  **Launch:** Run the script to open the Password Manager window.
2.  **Add:** Type in your Website and Username.
3.  **Generate:** Click **Suggest Password** to let the algorithm create a secure key for you.
4.  **Save:** Click **Add Entry** to commit the data to your local storage.

## ⚠️ Disclaimer

*This project is for educational and personal portfolio purposes. It stores passwords in a local CSV file. For enterprise-grade security, consider implementing encryption (hashing/salting) before deployment.*
