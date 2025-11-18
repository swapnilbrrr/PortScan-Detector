import datetime
import logging

def setup_logger(log_file_path: str):
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("PortScanner")

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
