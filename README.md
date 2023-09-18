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
    - Includes using uni/bivariate plots, feature importance classifiers and correlation analysis to identify relevant features
6. **Model Selection**
    - Choose a set of models suitable for the prediction problem.
    - In this case, for multi-class classification problem, Gradient Boosting, Logistic Regression and Random Forest models were shortlisted for evaluation.
7. **Model Training and Evaluation**
    - Train selected models on processed and engineered dataset.
    - Evaluate performance of each models using metrics such as accuracy, precision, recall and F1-score and choose the best performing one.
    - In the script, scores for each model is printed, together with the features considered.
8. **Hyperparameter Tuning**
    - Fine-tune the hyperparameters of the chosen models to further improve performance.

## Exploratory Data Analysis (EDA)
### Overview of key findings
**Target Variable Distribution:**
- The distribution of 'Ticket Type' revealed a skewed representation towards `Standard` and `Luxury` ticket types.
- `Deluxe` ticket are minority of the dataset.
- `Age` is the most influential feature for `Ticket Type`.
    - Older passengers tend to go for `Luxury` tickets
    - Younger passengers tend to go for `Standard` and `Deluxe`

**`Age` Distribution:**
- Older passengers highly prefers `Cabin Comfort`, `Cleanliness` and `Cabin Service`
- Younger passengers has low preference for `Cleanliness`

**Correlation Analysis:**
- Strong correlations were observed between features like `Cruise Distance`, `Online Check-in` and `Onboard Experience` and the target variable `Ticket Type`.

**Feature Importance:**
- `Age` was identified as the most influential feature for prediction, followed by `Onboard Experience` and 'Check-in Experience'.

### Choices made in pipeline based on findings

**Feature Engineering:**
- New features `Onboard Experience` and `Check-in Experience` were created to capture aggregated service ratings
- `Age` was also created to make `Date of Birth` usable in our analysis

**Feature Selection:**
- `Age` was identified as the most influential feature, followed by `Online Check-in`, `Onboard Experience` and `Check-in Experience`

## Summary of how features in the dataset are processed
Feature                                    | Actions                                                                                        |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| Ticket Type                                | Drop all rows with missing value                                                               |
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
| Cruise Name                                | Correct spelling to either `Blastoise` or `Lapras`, impute missing value with `mode`         |
| Cruise Distance                            | Correct invalid distances, convert all to kilometre, impute missing value with `mean`                |

## Explanation of choice of models for each ML task
- This is a multi-class classification problem, the model needs to be able to handle multi-class target variable.
**Models Used:**
- Gradient Boosting Classifier
    - Gradient Boosting Classifiers are powerful techniques for multi-class classification tasks.

- Logistic Regression
    - Logistic Regression is a widely used linear model for binary and multi-class classification.
    - Not only is it computationally efficient, it serves as a good baseline model

- Random Forest Classifier
    - Random Forest Classifiers builds multiple decision trees and combines their output to make predictions.
    - Works well with categorical features, well-suited for multi-class classification tasks
    - Also capable of providing feature importance scores, which can be useful for understanding the influence of variables in the classification process.

## Evaluation of models developed
**Metrics Considered for Evaluation:**
1. Accuracy
    - Accuracy measures the overall correctness of a classification model
    - (True Positives + True Negatives) / (True Positives + True Negatives + False Positives + False Negatives)
2. Precision
    - Precision focuses on the accuracy of positive predictions.
    - True Positives / (True Positives + False Positives)
3. Recall
    - Recall measures the proportion of actual positives that were correctly predicted by the model
    - True Positives / (True Positives + False Negatives)
4. F1-Score
    - F1-Score is the harmonic mean of precision and recall
    - Provides a balanced measure between precision and recall, considering both false positives and false negatives.
    - 2 * (Precision * Recall) / (Precision + Recall)

### Summary of Results
- Overall, this analysis provides insights into the effectiveness of different machine learning models for predicting ticket types based on pre-cruise survey features.
- Among the three models, the Gradient Boosting Classifier demonstrated the highest accuracy (73%), followed by the Random Forest Classifier (70%) and Logistic Regression (62%).
- The Gradient Boosting Classifier showed balanced performance with precision and recall both around 70%. This suggests that it effectively identified true positives while minimizing false positives.
- The Gradient Boosting Classifier had the highest F1-Score at 71%, followed by the Random Forest Classifier at 67%, and the Logistic Regression model at 60%.
- Based on the evalutaion metrics, the Gradient Boosting Classifier stands out as the top-performing model.

**Conclusion:**
- Gradient Boosting Classifier is recommended for predicting ticket types.
- Further iterative fine-tuning and feature engineering is required to improve the performance further.

| Metric    | <div style="text-align:center;">Gradient Boosting Classifier</div> | <div style="text-align:center;">Logistic Regression</div> | <div style="text-align:center;">Random Forest Classifier</div> |
|-----------|------------------------------------------------------------------|--------------------------------------------------------|------------------------------------------------------------|
| Accuracy  | <div style="text-align:center;">0.73</div>                         | <div style="text-align:center;">0.62</div>               | <div style="text-align:center;">0.7</div>                    |
| Precision | <div style="text-align:center;">0.7</div>                          | <div style="text-align:center;">0.65</div>               | <div style="text-align:center;">0.73</div>                   |
| Recall    | <div style="text-align:center;">0.73</div>                         | <div style="text-align:center;">0.62</div>               | <div style="text-align:center;">0.7</div>                    |
| F1-Score  | <div style="text-align:center;">0.71</div>                         | <div style="text-align:center;">0.6</div>                | <div style="text-align:center;">0.67</div>                   |

## Other considerations for deploying the models developed
**Model Serving Medium**
- Consider suitable platform to serve the models, which can be cloud-based platforms like AWS SageMaker or Google AI Platform, or open-source solution like FastAPI.

**API Integration**
- Develop user-friendly interface for end-users to interact with the deployed models. Ensure that it aligns with their needs and can integrate well into their exisiting systems.