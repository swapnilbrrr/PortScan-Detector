from scanner.port_scan import PortScanner
from scanner.utils import setup_logger
import os

def main():
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    logger = setup_logger("logs/scan.log")

    target = input("Enter IP or hostname to scan: ").strip()

    scanner = PortScanner(target)
    open_ports = scanner.run_scan()

    # Log final summary
    if open_ports:
        logger.info(f"Open ports on {target}: {open_ports}")
    else:
        logger.info(f"No open ports found on {target}")

    print("\nOpen ports:", open_ports)
    print("Done. Results saved to logs/scan.log")

if __name__ == "__main__":
    main()
