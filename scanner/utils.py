import logging
from logging import FileHandler, Formatter

# Common port → service mapping
PORT_NAME_MAP = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP-Server",
    68: "DHCP-Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    111: "RPCBind",
    123: "NTP",
    135: "MSRPC",
    137: "NetBIOS-NS",
    138: "NetBIOS-DGM",
    139: "NetBIOS-SSN",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    631: "CUPS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Proxy"
}


def get_port_name(port: int) -> str:
    return PORT_NAME_MAP.get(port, "Unknown Service")

def setup_logger(log_file: str):
    logger = logging.getLogger("scanner")
    logger.setLevel(logging.INFO)

    fh = FileHandler(log_file)
    fh.setFormatter(Formatter("[%(asctime)s] %(message)s"))

    logger.addHandler(fh)

    return logger
