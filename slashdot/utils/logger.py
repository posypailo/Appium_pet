import logging
import os


class SingletonLogger:
    _instance = None

    def __new__(cls, log_file='app.log'):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance._init_logger(log_file)
        return cls._instance

    def _init_logger(self, log_file):
        self.logger = logging.getLogger('app_logger')

        # Define the project root directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        log_file_path = os.path.join(project_root, log_file)
        print(log_file_path)

        if not self.logger.hasHandlers():
            self.logger.setLevel(logging.DEBUG)

            fh = logging.FileHandler(log_file_path, mode='w')
            fh.setLevel(logging.DEBUG)

            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger


def configure_logging():
    logger_instance = SingletonLogger()
    return logger_instance.get_logger()
