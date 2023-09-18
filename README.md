# AIAP Batch 15 Technical Assessment
## Personal Details
| Full Name            | Email address       |
| ---------------------| ------------------- |
| Eap Wei Hang, Jasper | jaspereap@gmail.com |

## Overview of submitted folder
```
base/
├── .github/
│   └── workflows/
│       └── github-actions.yml
├── src/
│   ├── data.py
│   ├── model.py
│   ├── evaluate.py
│   ├── main.py
│   ├── feature_engineering.py
│   └── config.yml
├── eda.ipynb
├── requirements.txt
├── README.md
└── run.sh
```

## Instructions for executing pipeline and modifying any parameters
### To adjust parameters,
- Modify `config.yml`, under `hyperparameters` in `/src/`

Current Parameters:
  - RandomForestClassifier
    1. n_estimators: 200
    2. random_state: 42
    3. max_depth: 7
  - LogisticRegression:
    1. C: 0.8
    2. penalty: l2
    3. max_iter: 700
    4. solver: 'sag'
  - GradientBoostingClassifier:
    1. n_estimators: 200
    2. learning_rate: 0.2
    3. random_state: 42

### To run MLP
- Run `run.sh` via `./run.sh`

## Description of logical steps of pipeline
**Outline:**
1. **Data Loading**
    - Load raw data from the data source, into a format that is suitable for further processing.
2. **Basic Data Exploration**
    - Initial EDA to understand the characteristics of the dataset.
    - Includes checking for missing values, basic statistics and visualizing distributions of variables.
3. **Data Preprocessing**
    - Cleaning and preparing the data for modeling.
    - Includes handling missing values, encoding categorical variables, scaling numerical features, and other necessary data transformations.
4. **Feature Engineering**
    - Create additional features to improve performance of the machine learning model.
    - Includes creating transformation and interactions of existing features.
5. **In-Depth Data Exploration**
    - After preprocessing and feature engineering, a more detailed EDA can be performed to understand how the new features interact with the target variable.
    - Includes using bivariate plots and feature importance classifiers to identify relevant features
6. **Model Selection**
    - Choose a set of models suitable for the prediction problem.
    - In this case, for multi-class classification problem, Gradient Boosting, Logistic Regression and Random Forest models were shortlisted for evaluation.
7. **Model Training and Evaluation**
    - Train selected models on processed and engineered dataset.
    - Evaluate performance of each models using metrics such as accuracy, precision, recall and F1-score and choose the best performing one.
8. **Hyperparameter Tuning**
    - Fine-tune the hyperparameters of the chosen models to further improve performance.

## Exploratory Data Analysis (EDA)
### Overview of key findings
**Target Variable Distribution:**
- The distribution of 'Ticket Type' revealed a balanced representation of Standard, Deluxe, and Luxury ticket types.

**Correlation Analysis:**
- Strong correlations were observed between specific features (e.g., 'Online Check-in', 'Port Check-in Service') and the target variable 'Ticket Type'.

**Feature Importance:**
- 'Age' was identified as the most influential feature for prediction, followed by 'Online Check-in' and 'Onboard Wifi Service'.

### Choices made in pipeline based on findings
**Missing Data Handling:**
- Missing values were imputed using suitable methods for each feature.

**Feature Engineering:**
- New features `Onboard Experience` and `Check-in Experience` were created to capture aggregated service ratings, providing a more comprehensive view.

**Feature Selection:**
- `Age` was identified as the most influential feature, followed by `Onboard Experience` and `Check-in Experience`

## Summary of how features in the dataset are processed
| Feature                                    | Actions                                                                                        |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| Date of Birth                              | Used with `Logging` to calculate `Age`, then impute missing values with `mode`                 |
| Source of Traffic                          | Encode-> Direct-Company Website=0, Email Marketing=1, Indirect-Search Engine=2, Social Media=3 |
| Onboard Wifi Service                       | Encode-> Numeric ratings, impute missing value with `mode`                                     |
| Onboard Dining Service                     | Encode-> Numeric ratings, impute missing value with `mode`                                     |
| Cabin Comfort                              | Impute missing value with `mode`                                                               |
| Onboard Entertainment                      | Encode-> Numeric ratings, impute missing value with `mode`                                     |
| Cabin Service                              | Impute missing value with `mode`                                                               |
| Onboard Service                            | Impute missing value with `mode`                                                               |
| Cleanliness                                | Impute missing value with `mode`                                                               |
| Embarkation/Disembarkation time Convenient | Impute missing value with `mode`                                                               |
| Ease of Online booking                     | Impute missing value with `mode`                                                               |
| Gate location                              | Impute missing value with `mode`                                                               |
| Onboard Dining Service                     | Impute missing value with `mode`                                                               |
| Online Check-in                            | Impute missing value with `mode`                                                               |
| Baggage handling                           | Impute missing value with `mode`                                                               |
| Port Check-in Service                      | Impute missing value with `mode`                                                               |
| Logging                                    | Used with `Age` to calculate `Age`                                                             |
| Cruise Name                                | Corrected spelling to either `Blastoise` or `Lapras`, impute missing value with `mode`         |
| Cruise Distance                            | Correct invalid distances, convert all to kilometre, impute missing value with `mean`                                                                                               |

## Explanation of choice of models for each ML task
**Models Used:**
- Gradient Boosting Classifier
- Logistic Regression
- Random Forest Classifier

## Evaluation of models developed
**Metrics Considered for Evaluation:**
1. Accuracy
    - ..
2. Precision
    - ..
3. Recall
    - ..
4. F1-Score
    - ..

**Gradient Boosting Classifier:**
- ..

**Logistic Regression:**
- ..

**Random Forest Classifier:**
- ..

## Other considerations for deploying the models developed
Placeholder
