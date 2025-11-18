import socket
from typing import List
from .utils import timestamp

class PortScanner:
    def __init__(self, target: str, start_port: int = 1, end_port: int = 1024, timeout: float = 0.5):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.timeout = timeout

    def scan_port(self, port: int) -> bool:
        """Returns True if port is open."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            sock.close()
            return result == 0
        except:
            return False

    def run_scan(self) -> List[int]:
        """Scans ports in the configured range."""
        print(f"[{timestamp()}] Starting scan on {self.target}...\n")
        open_ports = []

        for port in range(self.start_port, self.end_port + 1):
            if self.scan_port(port):
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)

        print(f"\n[{timestamp()}] Scan completed.")
        return open_ports
