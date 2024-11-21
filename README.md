# Asteroid Impact Prediction
## 🚀 Problem Statement
Asteroids are small, rocky objects orbiting the Sun, primarily found in the asteroid belt between Mars and Jupiter. They are remnants from the early solar system, formed over 4.6 billion years ago, and are considered planetesimals—the building blocks of planets.

Asteroid impacts have been a shaping force throughout Earth's history, ranging from minor events to catastrophic collisions that caused mass extinctions. Understanding the asteroid impact threat is critical for mitigating potential risks to Earth.

This project leverages machine learning techniques to classify whether an asteroid will make an impact on Earth or not, using key features derived from asteroid characteristics.

## 🛠️ Models Used
The following machine learning models were tested for classification:

- Logistic Regression
- Support Vector Classifier (SVC)
- DecisionTreeClassifier
- RandomForestClassifier
- KNeighborsClassifier

Among these, RandomForestClassifier outperformed others with an impressive accuracy of 95%.

## 📊 Dataset
The dataset for this project was sourced from Kaggle:<br/>
Kaggle Dataset: Asteroids Data

## 💻 How to Run the Project Locally
To run this project locally, follow these steps:

1. **Clone the Repository**

```bash
git clone https://github.com/shivakumar-ravichandran/Asteroid-Impact-Prediction/tree/main  
cd Asteroid-Impact-Prediction
```
2. **Install Required Dependencies**<br/>
Ensure you have Python installed. Install the necessary libraries using:

```bash
pip install -r requirements.txt
```
3. **Run the Application**<br/>
Execute the main pipeline for data ingestion and prediction.

```bash
python src/pipeline/data_ingestion.py  
```
4. **Explore the Output**<br/>
The application processes the dataset and generates predictions on whether an asteroid will impact Earth or not.

## 🛠️ Project Features<br/>
Data preprocessing and feature engineering.<br/>
Evaluation of multiple classification models.<br/>
Identification of the most effective model (RandomForestClassifier).<br/>
## 📂 Repository Structure<br/>
src/: Contains all source files.<br/>
pipeline/: Code for data ingestion and processing.<br/>
data/: Includes the dataset used for training and testing (download from Kaggle).<br/>
notebooks/: Jupyter notebooks for experimentation and visualization.<br/>
requirements.txt: List of dependencies for the project.<br/>
## 📧 Contact<br/>
Developed by Shivakumar Ravichandran<br/>
📧 Email: shivakumar.mcet@gmail.com<br/>

## 🌟 Acknowledgments<br/>
Special thanks to Kaggle for providing the dataset and to the amazing open-source ML libraries used in this project.
