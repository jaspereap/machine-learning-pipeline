# This modules hold functions for training models

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier

def train_RandomForestClassifier(X, y, n_estimators, random_state, max_depth):
    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state, max_depth=max_depth)
    model.fit(X, y)
    return model

def train_LogisticRegression(X, y, C, penalty, max_iter, solver):
    # Train a Logistic Regression Classifier
    model = LogisticRegression(C=C, penalty=penalty, max_iter=max_iter, solver=solver)
    model.fit(X, y)
    return model

def train_GradientBoostingClassifier(X, y, n_estimators, learning_rate, random_state):
    # Train a Gradient Boosting Classifier
    model = GradientBoostingClassifier(n_estimators=n_estimators, learning_rate=learning_rate, random_state=random_state)
    model.fit(X, y)
    return model
