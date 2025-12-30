# Laptop Price Predictor

This is an end-to-end Machine Learning project that predicts laptop prices based on user-selected specifications.
The project includes data preprocessing, model training, model selection, hyperparameter tuning, and deployment using Streamlit.

---

## Project Description

The goal of this project is to predict the price of a laptop using features such as:
- RAM
- Weight
- Brand
- Laptop Type
- Operating System
- CPU Type
- GPU Type
- Touchscreen
- IPS Display

A trained machine learning model is integrated into an interactive web dashboard where users can input laptop specifications and get a predicted price.

---

## Project Structure



LAPTOP_PRICE_PRE/
│
├── App/
│ ├── app.py
│ └── pipeline.pkl
│
├── Model/
│ ├── model building.ipynb
│ ├── laptop_price.csv
│ └── venv/ (ignored)
│
├── .gitignore
└── README.md


---

## Machine Learning Workflow

1. Data cleaning and preprocessing
2. Feature engineering
3. Encoding categorical variables
4. Model selection using cross-validation
5. Hyperparameter tuning with GridSearchCV
6. Creating a full preprocessing + model pipeline
7. Saving the trained pipeline using pickle

---

## Model Details

- Type: Regression
- Best Model: Random Forest Regressor
- Evaluation Method: Cross-validation
- Metric Used: R² score and Mean Absolute Error (MAE)

The entire preprocessing and model are saved together using a scikit-learn Pipeline.

---

## Streamlit Web Application

The trained pipeline is used in a Streamlit application that provides:
- Dropdowns for categorical features
- Numeric inputs for RAM and weight
- Checkboxes for Touchscreen and IPS display
- Real-time price prediction

To run the app locally:



streamlit run App/app.py


---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- VS Code

---

## Notes

- Virtual environment and editor configuration files are ignored using `.gitignore`
- The model pipeline ensures consistent preprocessing during prediction
- This project is suitable for academic and portfolio purposes

---

## Author

Name: Sankadesh  
GitHub: https://github.com/sankadesh