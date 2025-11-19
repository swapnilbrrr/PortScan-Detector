# **Network Security Auditor (Port-Scan-Detector)**

**Author:** Swapnil Katuwal
**Role:** SOC Analyst / Cybersecurity Researcher
**Status:** Active Development

---

## 🛡️ **Project Overview**

A modular network enumeration tool designed to emulate the **Reconnaissance** and **Vulnerability Assessment** phases of the Cyber Kill Chain.

Unlike simple connectivity checkers, this tool emphasizes:

* **Service Identification** (via banner grabbing)
* **Forensic Logging** (timestamped audit trails)
* **Socket-Level Behavior Analysis** (open/closed/filtered detection)

This makes the auditor suitable for **SOC analysis**, **security labs**, and **blue-team simulations**.

---

## 🚀 **Key Features**

* **Service Version Detection**
  Performs banner grabbing for HTTP, SSH, RPC and more to identify exposed or outdated services.

* **Forensic Logging**
  Automatically generates timestamped logs in `logs/scan.log`, imitating SIEM-style ingestion.

* **Custom TCP State Analysis**
  Uses socket-level low-level connection attempts to distinguish:
  **Open**, **Closed**, **Filtered** (firewall-dropped).

* **Modular Architecture**
  Clean separation between scanning logic, utilities, and logging for maintainability and scalability.

---

## 📌 **Usage**

### **1. Run the Auditor**

```bash
python main.py
```

### **2. Input Target**

Enter a valid IP or hostname (e.g., `192.168.1.1` or `scanme.nmap.org`).

### **3. Review Logs**

Scan results are saved in:

```
logs/scan.log
```

Each entry includes:

* Timestamp
* Port state
* Service banner (if captured)

---

## 📁 **Project Structure**

```
Port-Scan-Detector/
│
├── main.py                 # Entry point for the auditor
├── README.md               # Documentation
├── .gitignore
│
├── scanner/                # Core Logic Module
│   ├── __init__.py
│   ├── port_scan.py        # Socket connection & banner grabbing logic
│   └── utils.py            # Logging & timestamp helpers
│
├── logs/                   
│   └── sample.log          # Example scan output
│
└── tests/
    └── test_scanner.py     # Unit tests for scanner reliability
```

---

## 🧪 **Running Tests**

Ensure scanning reliability and proper error-handling:

```bash
pytest
```

---

## ✨ **Roadmap & Future Improvements**

* **Multithreading Support**
  For high-speed scanning similar to Nmap’s "Insane" timing.

* **CVE Mapping**
  Auto-correlate banners with known vulnerabilities using CVE databases.

* **JSON Export Mode**
  For direct ingestion into ELK, Splunk, or custom SOC dashboards.

* **SYN Scan Mode**
  Implement raw socket-based stealth scanning.

---

## 📜 **Disclaimer**

This tool is developed strictly for **educational** and **authorized security auditing** purposes.
Unauthorized scanning of networks is a violation of cybersecurity laws.
