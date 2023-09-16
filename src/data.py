# This Python module handles data retrieval and preprocessing

import sqlite3
import pandas as pd
import yaml

def load_config(config_path):
    with open(config_path, 'r') as stream:
        config = yaml.safe_load(stream)
    return config

# def load_pre_purchase_data(config):
#     pre_purchase_db_path = config['data']['pre_purchase_db_path']
#     # Load data from the database and preprocess as needed
#     return pre_purchase_data

# def load_post_trip_data(config):
#     post_trip_db_path = config['data']['post_trip_db_path']
#     # Load data from the database and preprocess as needed
#     return post_trip_data
