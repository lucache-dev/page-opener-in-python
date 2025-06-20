# Python Page Opener
A simple Python automation script that opens the Chrome web browser at a specified URL every X seconds.

![image](https://github.com/user-attachments/assets/45784dac-c83a-4afe-ad2b-4338c6726e2d)



## Project Setup Guide
This guide helps you set up and run the project in your local environment.

### 📦 Prerequisites

##### Install Python 3

Make sure Python 3 is installed on your system.

- [Download for Windows](https://www.python.org/downloads/windows/)
- [Download for Linux](https://www.python.org/downloads/source/)

To check if it's already installed, run:

```bash
python3 --version
```

##### Install tkinter
Tkinter is required for GUI functionality.

On Windows, Tkinter usually comes pre-installed with Python.

On Ubuntu/Debian-based systems, you can install it using:

```bash
sudo apt-get install python3-tk
```

### ⚙️ Setup

##### In the project folder, create a Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate # On Linux/macOS:
.\venv\Scripts\activate # On
```

##### Install Project Dependencies

 ```bash
pip install -r requirements.txt
```

##### Running the Project

```bash
python openPage.py
```
