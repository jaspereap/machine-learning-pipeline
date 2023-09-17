# AIAP Batch 15 Technical Assessment
### Personal Details
| Full Name            | Email address       |
| ---------------------| ------------------- |
| Eap Wei Hang, Jasper | jaspereap@gmail.com |

### Overview of submitted folder
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

### Instructions for executing pipeline and modifying any parameters
#### To adjust parameters,
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

#### To run MLP
- Run `run.sh` via `./run.sh`

### Description of logical steps of pipeline
**Outline:**
1. Data Loading
2. Basic Data Exploration

    2a. Findings

    2ai. Pre-purchase Survey

    2aii. Post-trip Data
        
3. Data Preprocessing

    3a. Merging Dataset

    3b. Standardising Indicator Value

    3c. Standardising Cruise Name

    3d. Standising Cruise Distance

    3e. Correct Indicators with Invalid Ratings

    3f. Correct `Dining` column data type

    3g. Encode `Ticket Type`, `Gender` and `Source of Traffic`

    3h. Handling Missing Data

      3hi. Drop NaN Rows in `Ticket Type` Column

      3hii. Imput NaN Rows in `Cruise Name` with Column Mode

      3hiii. Impute NaN Rows in `Gender` with Column Mode

      3hiv. Impute NaN Rows in `Onboard Dining Service` to `Cleanliness` with Column Mode

      3hvi. Impute NaN Rows in `Cruise Distance` with Column Mean
4. Feature Engineering

    4a. Create `Age` Column from `Date of Birth` and `Logging`

    4b. Create `Onboard Experience` Rating

    4c. Create `Check-in Experience` Rating
    
5. In-Depth Data Exploration

### Exploratory Data Analysis (EDA)
##### Overview of key findings
Placeholder
##### Choices made in pipeline based on findings
Placeholder

### Summary of how features in the dataset are processed
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

### Explanation of choice of models for each ML task
Placeholder

### Evaluation of models developed
Placeholder
Include explanation for any metrics used in evaluation

### Other considerations for deploying the models developed
Placeholder