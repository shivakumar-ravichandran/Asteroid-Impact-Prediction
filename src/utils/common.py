import sys
from src.custom_exception import CustomException
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
import yaml
import os
import pickle


class CommonUtils:
    def __init__(self):
        pass

    @staticmethod
    @ensure_annotations
    def read_yaml(filepath: Path) -> ConfigBox:
        """Read the YAML file from specified filepath

        Args:
            filepath (Path): path of the YAML file

        Raises:
            CustomException: raise exception anything raised or empty YAML file

        Returns:
            ConfigBox: returns YAML context in ConfigBox format
        """
        try:
            with open(filepath) as yaml_file:
                content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
        except Exception as exp:
            raise CustomException(exp, sys)

    @staticmethod
    @ensure_annotations
    def create_directories(path_to_directories: list):
        """create list of directories
        Args:
            path_to_directories (list): list of path of directories
            ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
        """
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)

    @staticmethod
    def save_object(file_path, file_name, obj):
        try:
            os.makedirs(file_path, exist_ok=True)

            file = os.path.join(file_path, file_name)

            with open(file, "wb") as file_obj:
                pickle.dump(obj, file_obj)

        except Exception as exp:
            raise CustomException(exp, sys)
