import socket
import logging
from typing import List, Optional
from .utils import timestamp

class PortScanner:
    def __init__(self, target: str, start_port: int = 1, end_port: int = 1024, timeout: float = 1.0):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.timeout = timeout

    def scan_port(self, port: int) -> Optional[str]:
        """
        Checks if port is open. If open, grabs the banner.
        Returns: Banner string if open, None if closed.
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                # BANNER GRABBING LOGIC
                try:
                    # Send 'garbage' to provoke a response
                    sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                    # Receive response (limit to 1024 bytes)
                    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                    if not banner:
                        banner = "Unknown Service (Open)"
                except:
                    banner = "Unknown Service (Open)"
                
                sock.close()
                return banner
            
            sock.close()
            return None
        except:
            return None

    def run_scan(self) -> List[int]:
        """Scans ports and logs detailed findings."""
        print(f"[{timestamp()}] Starting SECURITY AUDIT on {self.target}...\n")
        logging.info(f"Starting SECURITY AUDIT on {self.target}...")

        open_ports = []

        for port in range(self.start_port, self.end_port + 1):
            banner = self.scan_port(port)
            if banner:
                # This looks like a real SOC log now
                log_msg = f"[ALERT] Port {port} OPEN | Service: {banner}"
                print(log_msg)
                logging.info(log_msg)
                open_ports.append(port)

        print(f"\n[{timestamp()}] Audit completed.")
        logging.info(f"Audit completed on {self.target}")
        return open_ports