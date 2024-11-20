from pathlib import Path
from src.constants import *
from src.utils.common import CommonUtils
from src.entity.config_entity import (
    DataIngestionConfig,
    SaveModelConfig,
    DataTransformConfig,
)


class ConfigurationManager:
    def __init__(
        self,
        config_path: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
    ):
        self.config = CommonUtils.read_yaml(config_path)
        self.params = CommonUtils.read_yaml(params_filepath)

        # create artifacts root directory
        CommonUtils.create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Function to get the configuration related to data ingestion from config.yaml file

        Returns:
            DataIngestionConfig: data ingestion configurations
        """
        config = self.config.data_ingestion

        # Create root directory for data ingestion as specified in config.yaml
        CommonUtils.create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_model_transformer_config(self) -> DataTransformConfig:
        config = self.config.data_transform

        # Create root directory to save preprocessor as specified in config.yaml
        CommonUtils.create_directories([config.root_dir])

        data_transformer_config = DataTransformConfig(
            root_dir=config.root_dir,
            file_name=config.file_name,
        )

        return data_transformer_config

    def get_save_model_config(self) -> SaveModelConfig:
        config = self.config.save_model

        # Create root directory to save model as specified in config.yaml
        CommonUtils.create_directories([config.root_dir])

        save_model_config = SaveModelConfig(
            root_dir=config.root_dir,
            file_name=config.file_name,
        )

        return save_model_config
