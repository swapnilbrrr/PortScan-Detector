# **Network Security Auditor (Port‑Scan‑Detector)**

**Author:** Swapnil Katuwal
**Role:** SOC Analyst / Cybersecurity Researcher
**Status:** Active Development

---

## 🛡️ **Project Overview**

Port‑Scan‑Detector is a modular network enumeration tool that replicates key stages of the **Reconnaissance** and **Vulnerability Assessment** phases of the Cyber Kill Chain.

Unlike basic port checkers, this tool focuses on security‑centric techniques:

* **Service Identification** via banner grabbing
* **Forensic Logging** with timestamped trails
* **Socket‑Level Behavior Analysis** (open / closed / filtered detection)

Designed for **SOC analysts**, **blue‑team labs**, and **defensive security research**.

---

## 🚀 **Key Features**

### **🔎 Service Version Detection**

Banner grabbing for common services (HTTP, SSH, FTP, RPC) to detect exposed or outdated versions.

### **📁 Forensic Logging**

Generates timestamped logs in `logs/scan.log`, structured for SIEM-style ingestion.

### **⚡ Concurrent Scanning**

Uses `Fast multi-threaded scanning` for high‑speed enumeration of TCP ports.

### **🧩 Modular Architecture**

Clear separation between scanning engine, helper utilities, and logging components — designed for future scalability.

---

## 📌 **Usage**

### 1️⃣ Run the Auditor

```bash
python main.py
```

### 2️⃣ Enter Target

Example:

```
192.168.1.1
scanme.nmap.org
```

### 3️⃣ Review Logs

Logs generated under:

```
logs/scan.log
```

Each record includes:

* Timestamp
* Port number & state
* Normalized service banner

---

## 📁 **Project Structure**

```
Port-Scan-Detector/
│
├── main.py                 # Entry point
├── README.md               # Documentation
├── .gitignore
│
├── scanner/                # Core scanning engine
│   ├── __init__.py
│   ├── port_scan.py        # Socket connections & banner grabbing
│   └── utils.py            # Helper functions (timestamp, log writer)
│
├── logs/
│   └── scan.log            # Generated scan logs
│
└── tests/
    └── test_scanner.py     # Pytest unit tests
```

---

## 🧪 **Running Tests**

```bash
pytest
```

---

## ✨ **Roadmap & Future Improvements**

* **CVE Mapping**
  Correlate service banners with known vulnerabilities.

* **JSON Output Mode**
  Export structured results for ELK, Splunk, or custom SOC dashboards.

* **SYN Stealth Scan**
  Raw-socket based half‑open scanning.

---

## 📜 **Disclaimer**

This tool is intended for **educational** and **authorized security auditing** only.
Unauthorized network scanning may be illegal in your jurisdiction.

