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
#### To adjust parameters
- Modify `config.yml` in `/src/`
#### To run MLP
- Run `run.sh`

### Description of logical steps of pipeline
Placeholder

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