import sys
from src.custom_exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManager


class DataIngestionPipeline:
    def __init__(self):
        pass

    def get_data(self):
        try:
            data_ingestion_config_obj = ConfigurationManager()
            config = data_ingestion_config_obj.get_data_ingestion_config()

            data_ingestion_obj = DataIngestion(config=config)
            data_ingestion_obj.download_data_file()
            data_ingestion_obj.extract_zip_file()

        except Exception as exp:
            raise CustomException(exp, sys)


if __name__ == "__main__":
    obj = DataIngestionPipeline()
    obj.get_data()
