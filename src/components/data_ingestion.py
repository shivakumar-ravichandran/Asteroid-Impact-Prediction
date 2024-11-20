import os
import sys
from src.custom_exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataIngestionConfig
import urllib.request as request
import zipfile
from src.utils.common import CommonUtils


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data_file(self):
        """Function to download the data file from URL to local folder

        Raises:
            CustomException: raise exception if any.
        """
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, header = request.urlretrieve(
                    url=self.config.source_URL, filename=self.config.local_data_file
                )
                logging.info("Data file download successfully!")
            else:
                logging.info("File Already exist in local folder.")
        except Exception as exp:
            raise CustomException(exp, sys)

    def extract_zip_file(self):
        try:
            CommonUtils.create_directories([self.config.unzip_dir])
            with zipfile.ZipFile(self.config.local_data_file, "r") as unzip:
                unzip.extractall(self.config.unzip_dir)
        except Exception as exp:
            raise CustomException(exp, sys)
