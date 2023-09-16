# This Python module handles data retrieval and preprocessing

import sqlite3
import pandas as pd
import yaml

def load_config(config_path):
    with open(config_path, 'r') as stream:
        config = yaml.safe_load(stream)
    return config

def load_data_set(db_name, config):
    db_path = config['data'][db_name]
    data = []
    # Load data from the database and preprocess as needed

    # Define a function that returns database connection object
    def get_db_connection(db_path):
        conn = sqlite3.connect(db_path)        # points database connection object to conn
        conn.row_factory = sqlite3.Row     # set return rows as dictionaries instead of tuples
        return conn
    # Define variable to store name of the tables
    table_name = db_name.rstrip('.db')

    # Create connection to database using defined function
    conn = get_db_connection('data/'+ table_name + '.db')

    # Execute query to fetch all rows and columns
    db_query_output = conn.execute('SELECT * FROM {}'.format(table_name)).fetchall()

    # Append row to data store
    for row in db_query_output:
        data.append(dict(row))

    # close database connection after completion of task
    conn.close()

    # Read list of dictionaries into Pandas Dataframe
    # Set 'index' column as index
    data = pd.DataFrame(data=data).set_index('index')

    return data

# def load_post_trip_data(config):
#     post_trip_db_path = config['data']['post_trip_db_path']
#     # Load data from the database and preprocess as needed
#     return post_trip_data
