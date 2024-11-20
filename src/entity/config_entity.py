from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataTransformConfig:
    root_dir: Path
    file_name: str


@dataclass
class SaveModelConfig:
    root_dir: Path
    file_name: str
