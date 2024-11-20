import sys
from src.custom_exception import CustomException
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from src.utils.common import CommonUtils
from src.entity.config_entity import SaveModelConfig


class ModelTrainer:
    def __init__(self, train, test):
        self.train = train
        self.test = test

    def initiate_model_training(self, config: SaveModelConfig):
        try:

            X_train = self.train[:, :-1]
            y_train = self.train[:, -1]
            X_test = self.test[:, :-1]
            y_test = self.test[:, -1]

            models = {
                "Logistic Regression": LogisticRegression(),
                "Random Forest Classifier": RandomForestClassifier(),
                "SVC": SVC(),
                "K-Neighbors": KNeighborsClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
            }

            scores = []
            for i in range(len(list(models))):
                model = list(models.values())[i]
                # print(f"model name: {list(models.keys())[i]}")

                model.fit(X_train, y_train)

                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)
                # print(y_test_pred)
                scores.append(accuracy_score(y_test, y_test_pred))

            best_model_name = (
                pd.DataFrame(data={"Models": list(models.keys()), "Scores": scores})
                .sort_values(by="Scores", ascending=False)
                .iloc[0]["Models"]
            )

            best_model = models[best_model_name]

            CommonUtils.save_object(
                file_path=config.root_dir,
                file_name=config.file_name,
                obj=best_model,
            )

        except Exception as exp:
            raise CustomException(exp, sys)
