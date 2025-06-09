🔬 What I Did in This Project
Data Collection & Exploration:
Collected and explored a structured dataset loan_approval_dataset.csv containing features like number of dependents, education, employment status, income, loan amount, loan term, CIBIL credit score, and various asset values.

Data Preprocessing:

Handled missing values where necessary

Encoded categorical features (e.g., education, self_employed)

Scaled numerical features to normalize input for the model

Dimensionality Reduction with PCA:

Applied Principal Component Analysis (PCA) to reduce feature dimensionality

Retained the most important components while minimizing information loss

Helped improve training speed, reduce overfitting, and increase model generalization

Feature Engineering & Selection:

Selected key financial indicators

Transformed features using PCA before model training

Model Training:

Trained an optimized XGBoost Classifier with the following tuned parameters:
max_depth=4, n_estimators=50, learning_rate=0.2, reg_alpha=2, reg_lambda=1

Trained on PCA-transformed features using X_train and y_train

Model Evaluation:

Evaluated performance using accuracy_score and classification_report

Plotted confusion matrix for both training and testing predictions

Displayed metrics for both correct and incorrect classifications

Model Saving:

Serialized the trained model using joblib and saved it as best_model.pkl for later use

Streamlit Web App Deployment:

Created a modern interactive interface using Streamlit in loan_approval_streamlit.py

Users can enter loan application details and receive a prediction instantly

Displayed probability of approval and rejection with visual feedback (✅ or ❌)

