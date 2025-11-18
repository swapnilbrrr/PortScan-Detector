from scanner.port_scan import PortScanner

def test_scanner_runs():
    scanner = PortScanner("127.0.0.1", 1, 10)
    result = scanner.run_scan()
    assert isinstance(result, list)
