import logging


def setup_logging(log_file="application.log"):
    logging.basicConfig(
        level=logging.INFO,  # Mude para DEBUG, WARNING, ERROR conforme necessário
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),  # Log em arquivo
            logging.StreamHandler(),  # Log no console
        ],
    )
