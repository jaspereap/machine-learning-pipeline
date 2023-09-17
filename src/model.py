from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X, y, n_estimators, random_state):
    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    model.fit(X, y)
    return model

def train_logistic_regression(X, y, C, penalty, max_iter):
    # Train a Logistic Regression Classifier
    model = LogisticRegression(C=C, penalty=penalty, max_iter=max_iter)
    model.fit(X, y)
    return model

def train_gradient_boosting(X, y, n_estimators, learning_rate):
    # Train a Gradient Boosting Classifier
    model = GradientBoostingClassifier(n_estimators=n_estimators, learning_rate=learning_rate)
    model.fit(X, y)
    return model
