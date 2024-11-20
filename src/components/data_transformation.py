import sys
from src.custom_exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import numpy as np
from src.entity.config_entity import DataTransformConfig
from src.utils.common import CommonUtils

class DataTransformation:
    def __init__(self):
        pass

    def get_preprocessing_obj(self, num_cols, cat_cols):
        try:
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("stand_scalar", StandardScaler()),
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot_encoder", OneHotEncoder()),
                ]
            )

            col_transformer = ColumnTransformer(
                [
                    ("num_cols", num_pipeline, num_cols),
                    ("cat_cols", cat_pipeline, cat_cols),
                ]
            )

            return col_transformer
        except Exception as exp:
            raise CustomException(exp, sys)

    def initiate_data_transformation(self, config: DataTransformConfig):
        try:
            columns_to_delete = [
                "Name",
                "Relative Velocity km per hr",
                "Miss Dist.(lunar)",
                "Miss Dist.(kilometers)",
                "Miss Dist.(miles)",
                "approach_year",
                "approach_month",
                "Orbit Uncertainity",
                "Jupiter Tisserand Invariant",
                "Perihelion Time",
                "Epoch Osculation",
                "Mean Motion",
            ]
            columns_to_rename = {
                "Relative Velocity km per sec": "Relative Velocity",
                "Miss Dist.(Astronomical)": "Miss Dist",
            }

            df = pd.read_csv("artifacts/data_ingestion/asteriod_dataset.csv")

            df.drop(columns=columns_to_delete, inplace=True)
            df.rename(columns=columns_to_rename, inplace=True)

            cat_cols = df.select_dtypes(include="object").columns
            num_cols = df.select_dtypes(exclude="object").columns
            num_cols = [
                col for col in num_cols if col != "Hazardous"
            ]  # removing target column

            X = df.drop(columns=["Hazardous"], axis=1)
            y = df["Hazardous"]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.3, random_state=42
            )

            preprocessing_obj = self.get_preprocessing_obj(num_cols, cat_cols)

            X_train_arr = preprocessing_obj.fit_transform(X_train)
            X_test_arr = preprocessing_obj.fit_transform(X_test)

            train = np.c_[X_train_arr, y_train]
            test = np.c_[X_test_arr, y_test]

            CommonUtils.save_object(
                file_path=config.root_dir,
                file_name=config.file_name,
                obj=preprocessing_obj,
            )

            # print(train)
            return train, test

        except Exception as exp:
            raise CustomException(exp, sys)
