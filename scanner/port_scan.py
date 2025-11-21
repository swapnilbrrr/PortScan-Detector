import socket
import threading
from queue import Queue
from scanner.utils import get_port_name

class PortScanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = []
        self.q = Queue()
        self.max_threads = 100   # FAST

    def scan_port(self):
        while True:
            port = self.q.get()
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)

                if s.connect_ex((self.target, port)) == 0:
                    service = get_port_name(port)
                    print(f"[ALERT] Port {port} OPEN | Service: {service}")
                    self.open_ports.append(port)

                s.close()

            except Exception:
                pass

            self.q.task_done()

    def run_scan(self):
        print(f"\n[+] Scanning {self.target} with {self.max_threads} threads...\n")

        # Start worker threads
        for _ in range(self.max_threads):
            t = threading.Thread(target=self.scan_port)
            t.daemon = True
            t.start()

        # Enqueue all ports
        for port in range(1, 1025):
            self.q.put(port)

        self.q.join()
        return self.open_ports
