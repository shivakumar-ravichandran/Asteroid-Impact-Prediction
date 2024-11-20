from pathlib import Path
from src.constants import *
from src.utils.common import CommonUtils
from src.entity.config_entity import DataIngestionConfig


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
