# Port-Scan-Detector

A lightweight, modular TCP port scanner for Windows, implemented in Python. Designed for learning, testing, and easy extension.

---

## 🚀 Features
- Scans TCP ports (1–1024)
- Fully modular structure (PortScanner class, helper utils)
- Works on Windows with no extra libraries
- Logs results to `logs/scan.log`
- Beginner-friendly and easy to extend

---

## 📌 Usage

Run the scanner:

```bash
python main.py
```

When prompted, enter an IP address or hostname to scan.

---

## 📁 Project Structure

```plaintext
Port-Scan-Detector/
│
├── main.py
├── README.md
├── .gitignore
│
├── scanner/
│   ├── __init__.py
│   ├── port_scan.py
│   └── utils.py
│
├── logs/
│   └── sample.log
│
└── tests/
    └── test_scanner.py
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## ✨ Future Improvements

* Add async scanning for speed
* Add TCP SYN scanning
* Add UI (CLI or GUI)
* Auto-export scan results to JSON/CSV

---

## Author

Swapnil Katuwal