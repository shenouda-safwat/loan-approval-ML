
#💰 Loan Approval Prediction Using PCA and XGBoost
🏦 Project Overview
This project predicts whether a loan application will be approved or rejected based on applicant information using machine learning.
It involves data preprocessing, feature engineering, dimensionality reduction using Principal Component Analysis (PCA), and classification using XGBoost Classifier.
A Streamlit web app is also built to interactively use the trained model.

##🗂️ Dataset
The dataset contains several applicant-related features:

Personal & Financial Details:

Number of Dependents

Education Level

Employment Status

Applicant Income

Coapplicant Income

Loan Amount

Loan Term

CIBIL Credit Score

Property Area

Asset Values

Target Variable:

Loan_Status: 1 = Approved, 0 = Rejected

##🔍 Data Preprocessing
Handled missing values

Encoded categorical features using Label Encoding

Scaled numerical features using StandardScaler

Split the dataset into:

Training set (70%)

Validation set (15%)

Test set (15%)

##📊 Feature Engineering & Dimensionality Reduction
Applied Principal Component Analysis (PCA) to reduce dimensionality

#Retained essential components to capture most of the variance

##PCA helped improve model performance, training time, and reduced overfitting

##🤖 Model Training
#Used XGBoost Classifier with tuned hyperparameters:
#max_depth=4, n_estimators=50, learning_rate=0.2, reg_alpha=2, reg_lambda=1

#Trained on the PCA-transformed training data

#Validated on the validation set

##📈 Performance Metrics
Metric	Value
Accuracy	92%
Precision	0.91
Recall	0.90
F1-score	0.91
ROC AUC Score	0.93

##📊 Classification Report
#The model showed high performance in predicting both approved and rejected loans with balanced precision and recall.

##🚀 How to Run
#Clone the repository and install dependencies:


#git clone https://github.com/shenouda-safwat/loan-approval-ML.git
#cd loan-approval-ML
#pip install -r requirements.txt
#To run the Streamlit web app:


#streamlit run loan_approval_streamlit.py
