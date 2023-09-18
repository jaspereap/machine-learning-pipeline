import data
import feature_engineering
import model
import evaluate
from sklearn.model_selection import train_test_split
import numpy as np

def main():
    config = data.load_config('src/config.yaml')
    models_to_train = config['models']
    hyperparameters = config['hyperparameters']

    cruise_pre_data = data.load_data_set('cruise_pre.db', config)
    cruise_post_data = data.load_data_set('cruise_post.db', config)
    merged_data = data.merge_data(cruise_pre_data, cruise_post_data, on='Ext_Intcode')

    # Preprocess data
    preprocessor = data.DataPreprocessor(merged_data)
    merged_data = preprocessor.preprocess_data()

    # Handle missing data
    missinghandler = data.MissingDataHandler(merged_data)
    merged_data = missinghandler.handle_missing_data()

    merged_data = merged_data.copy()
    # Add new feature: Age
    merged_data = feature_engineering.add_age(merged_data)
    # Add new feature: Onboard Experience
    merged_data = feature_engineering.add_onboard_experience(merged_data)
    # Add new feature: Check-in Experience
    merged_data = feature_engineering.add_check_in_experience(merged_data)

    feature_columns = ['Onboard Wifi Service',
                    'Onboard Dining Service',
                    'Cabin Comfort',
                    'Onboard Entertainment',
                    'Cabin service',
                    'Onboard Service',
                    'Cleanliness',
                    'Onboard Experience',
                    'Age',
                    'Ease of Online booking',
                    'Check-in Experience',
                    'Gate location',
                    'Onboard Dining Service',
                    'Online Check-in']
    
    target_column = ['Ticket Type']
    print(f'Feature Columns: {feature_columns}')
    print(f'Target Column: {target_column}')

    # Setting up feature columns X and target column y
    X = merged_data[feature_columns]
    y = np.ravel(merged_data[target_column])

    # Splitting exisiting dataset into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Iterate model training and model evaluation for each model of interest
    for model_name in models_to_train:
        hyperparams = hyperparameters[model_name]
        train_function = getattr(model, f'train_{model_name}')
        trained_model = train_function(X_train, y_train, **hyperparams)
        metrics = evaluate.evaluate_model(trained_model, X_test, y_test)
        print(f'{model_name} - Metrics:')
        print(f"Accuracy = {round(metrics['Accuracy'], 2)}")
        print(f"Precision = {round(metrics['Precision'], 2)}")
        print(f"Recall = {round(metrics['Recall'], 2)}")
        print(f"F1 Score = {round(metrics['F1 Score'], 2)}\n")

if __name__ == '__main__':
    main()
