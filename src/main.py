# Possible models for this project
# Logistic Regression
# Random Forest Classifier
# Gradient Boosting Classifier

# General to-do
# Data preprocessing - decide how to handle missing values etc.
# Split data into training and testing sets - do random selection
# Evaluation metrics: accuracy, precision, recall, F1-score

import data
# import feature_engineering
# import model
# import evaluate

def main():
    config = data.load_config('src/config.yaml')

    cruise_pre_data = data.load_data_set('cruise_pre.db', config)
    cruise_post_data = data.load_data_set('cruise_post.db', config)

    
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
