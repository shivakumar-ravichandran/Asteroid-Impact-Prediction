import sys
from src.custom_exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class DataIngestionPipeline:
    def __init__(self):
        pass

    def get_data(self):
        try:
            config_manager_obj = ConfigurationManager()
            config = config_manager_obj.get_data_ingestion_config()

            data_ingestion_obj = DataIngestion(config=config)
            data_ingestion_obj.download_data_file()
            data_ingestion_obj.extract_zip_file()

        except Exception as exp:
            raise CustomException(exp, sys)

    def transform_data(self):
        try:
            config_manager_obj = ConfigurationManager()
            config = config_manager_obj.get_model_transformer_config()

            data_transformer_obj = DataTransformation()
            train, test = data_transformer_obj.initiate_data_transformation(config)

            return train, test
        except Exception as exp:
            raise CustomException(exp, sys)

    def model_trainer(self, train, test):
        try:
            config_manager_obj = ConfigurationManager()
            config = config_manager_obj.get_save_model_config()

            model_train_obj = ModelTrainer(train, test)
            model_train_obj.initiate_model_training(config)
        except Exception as exp:
            raise CustomException(exp, sys)


if __name__ == "__main__":
    obj = DataIngestionPipeline()
    obj.get_data()
    train, test = obj.transform_data()
    obj.model_trainer(train, test)
