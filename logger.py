import logging.config
import yaml
import os

def setup_logger(name: str = "my_app") -> logging.Logger:
    """
    Setup logger configuration from logging.yaml
    Args:
        name (str): logger name
    Returns:
        logging.Logger: configurated logger
    """
    config_path = os.path.join(os.path.dirname(__file__), "logging.yaml")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    for handler in config.get("handlers", {}).values():
        if handler.get("class") == "logging.FileHandler":
            log_path = handler.get("filename")
            if log_path:
                log_dir = os.path.dirname(log_path)
                os.makedirs(log_dir, exist_ok=True)

    logging.config.dictConfig(config)
    return logging.getLogger(name)
