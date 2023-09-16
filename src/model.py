from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier

def train_random_forest(X, y, n_estimators, max_depth):
    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X, y)
    return model

def train_logistic_regression(X, y, C, penalty):
    # Train a Logistic Regression Classifier
    model = LogisticRegression(C=C, penalty=penalty)
    model.fit(X, y)
    return model

def train_gradient_boosting(X, y, n_estimators, learning_rate):
    # Train a Gradient Boosting Classifier
    model = GradientBoostingClassifier(n_estimators=n_estimators, learning_rate=learning_rate)
    model.fit(X, y)
    return model