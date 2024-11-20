from setuptools import find_packages, setup
from typing import List


HYPEN_DOT = "-e ."


def get_install_required(file_name: str) -> List[str]:
    requirements = []
    with open(file_name) as file_object:
        requirements = file_object.readlines()
        requirements = [
            req.replace("\n", "") for req in requirements if req != HYPEN_DOT
        ]

    return requirements


setup(
    name="Asteroid Impact Prediction",
    version="0.0.1",
    description="Model to predict the actual impact of asteroid to the Earth.",
    author="Shivakumar Ravichandran",
    author_email="shivakumar.mcet@gmail.com",
    packages=find_packages(),
    install_requires=get_install_required("requirements.txt"),
)
