# Possible models for this project
# Logistic Regression
# Random Forest Classifier
# Gradient Boosting Classifier

# General to-do
# Data preprocessing - decide how to handle missing values etc.
# Split data into training and testing sets - do random selection
# Evaluation metrics: accuracy, precision, recall, F1-score

import data
import feature_engineering
# import model
# import evaluate

def main():
    config = data.load_config('src/config.yaml')

    cruise_pre_data = data.load_data_set('cruise_pre.db', config)
    cruise_post_data = data.load_data_set('cruise_post.db', config)
    merged_data = cruise_pre_data.merge(cruise_post_data, left_on='Ext_Intcode', right_on='Ext_Intcode')
    print(merged_data.head())

    # Preprocess data
    preprocessor = data.DataPreprocessor(merged_data)
    merged_data = preprocessor.preprocess_data()

    # Handle missing data
    missingHandler = data.MissingDataHandler(merged_data)
    merged_data = missingHandler.handle_missing_data()

    print(merged_data.head())

    # Add new feature: Age
    merged_data = feature_engineering.add_age(merged_data)

    print(merged_data['Age'].head())

    # models_to_train = config['models']
    
    # hyperparameters = config['hyperparameters']
    
    # for model_name in models_to_train:
    #     hyperparams = hyperparameters[model_name]
    #     train_func = getattr(model, f'train_{model_name}')
    #     trained_model = train_func(engineered_features, y, **hyperparams)
    #     accuracy = evaluate.evaluate_model(trained_model, X_test, y_test)
    #     print(f'{model_name} - Accuracy: {accuracy}')

if __name__ == '__main__':
    main()
