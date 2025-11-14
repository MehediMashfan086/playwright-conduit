import logging


def get_logger():
    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        fh = logging.FileHandler("test_run.log", mode="w")
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
