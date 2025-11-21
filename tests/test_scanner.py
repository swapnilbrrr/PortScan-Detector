# tests/test_scanner.py
import logging
from scanner.port_scan import PortScanner

# Optional: suppress logging during test to keep output clean
logging.getLogger("PortScanner").disabled = True

def test_scanner_runs():
    """
    Basic functionality test:
    - Runs a scan on 127.0.0.1 for ports 1-10.
    - Confirms the result is a list of open ports.
    """
    scanner = PortScanner("127.0.0.1", start_port=1, end_port=10)
    result = scanner.run_scan()

    # Validate type
    assert isinstance(result, list)

    # Optional: validate contents
    for port in result:
        assert isinstance(port, int)
        assert 1 <= port <= 10
