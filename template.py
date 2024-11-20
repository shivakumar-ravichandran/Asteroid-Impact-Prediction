import os
from pathlib import Path

project_name = "Asteriod Impact Prediction"

# list of files and folders need to be created as a project template.
list_of_files = [
    ".guthub/workflow/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/predict_pipeline.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/utils/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

# function to create the above list of files and folders.
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w"):
            pass
