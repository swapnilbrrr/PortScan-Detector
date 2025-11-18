from scanner.port_scan import PortScanner
from scanner.utils import setup_logger
import os
import logging

logging.basicConfig(
    filename='logs/scan.log',  # log file path
    level=logging.INFO,        # log everything info or higher
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", "scan.log")
    logger = setup_logger(log_path)

    target = input("Enter IP or hostname to scan: ").strip()

    scanner = PortScanner(target)
    open_ports = scanner.run_scan()

    if open_ports:
        logger.info(f"Open ports on {target}: {open_ports}")
    else:
        logger.info(f"No open ports found on {target}")

    print("\nDone. Results saved to logs/scan.log")

if __name__ == "__main__":
    main()
