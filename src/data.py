# This Python module handles data retrieval and preprocessing

import sqlite3
import pandas as pd
import yaml
import re

def load_config(config_path):
    with open(config_path, 'r') as stream:
        config = yaml.safe_load(stream)
    return config

# Load data from the database and preprocess as needed
def load_data_set(db_name, config):
    db_path = config['data'][db_name]
    data = []

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

class DataPreprocessor:
    def __init__(self, df):
        self.df = df

    def standardise_indicator(self):
        # Define a string-to-value map to help encode these columns
        indicator_map = {'Not at all important':1.0,
                        'A little important':2.0,
                        'Somewhat important':3.0,
                        'Very important': 4.0,
                        'Extremely important':5.0}

        # Store columns to encode
        encode_columns = ['Onboard Wifi Service', 'Onboard Entertainment', 'Onboard Dining Service']

        # Iterate encoding for each column
        for column in encode_columns:
            self.df[column] = self.df[column].map(indicator_map)
        return self.df

    def standardise_cruise_name(self):
        # Define function to replace misspellings with correct spelling
        def correct_spelling(cruise_name):
            misspellings = {
                'blast': 'Blastoise',
                'blast0ise': 'Blastoise',
                'blastoise': 'Blastoise',
                'IAPRAS': 'Lapras',
                'lap': 'Lapras',
                'lapras': 'Lapras'
            }
            return misspellings.get(cruise_name, cruise_name)

        # Apply function to 'Cruise Name' column
        self.df['Cruise Name'] = self.df['Cruise Name'].apply(correct_spelling)
        return self.df

    def standardise_cruise_distance(self):
        def convert_to_km(distance):
            numbers = re.findall(r'\d+', distance)
            if numbers:
                if 'Miles' in distance:
                    return int(numbers[0]) * 1.60934  # Convert miles to kilometers
                else:
                    return int(numbers[0])

        # Apply the conversion function to each element in the Series
        self.df['Cruise Distance'] = self.df['Cruise Distance'].apply(lambda x: convert_to_km(x) if x else None)
        # Convert the Series back to numeric type
        self.df['Cruise Distance'] = pd.to_numeric(self.df['Cruise Distance'])
        return self.df

    def correct_dining_datatype(self):
        # Convert 'Dining' data type to float
        self.df['Dining'] = self.df['Dining'].astype(float)
        return self.df

    def encode_column(self):
        # Encodes Ticket Type, Gender and Source of Traffic
        # Ticket Type
        # Standard = 0
        # Deluxe = 1
        # Luxury = 2
        # Gender
        # Male = 0
        # Female = 1
        # Source of Traffic
        # Direct - Company Website = 0
        # Direct - Email Marketing = 1
        # Indirect - Search Engine = 2
        # Indirect - Social Media = 3
        # Encode Ticket Type
        ticket_type_mapping = {'Standard': 0, 'Deluxe': 1, 'Luxury': 2}
        self.df['Ticket Type'] = self.df['Ticket Type'].replace(ticket_type_mapping)

        # Encode Gender
        gender_mapping = {'Male': 0, 'Female': 1}
        self.df['Gender'] = self.df['Gender'].replace(gender_mapping)

        # Encode Source of Traffic
        source_of_traffic_mapping = {
            'Direct - Company Website': 0,
            'Direct - Email Marketing': 1,
            'Indirect - Search Engine': 2,
            'Indirect - Social Media': 3
        }
        self.df['Source of Traffic'] = self.df['Source of Traffic'].replace(source_of_traffic_mapping)
        return self.df

    def preprocess_data(self):
        self.df = self.standardise_indicator()
        self.df = self.standardise_cruise_name()
        self.df = self.standardise_cruise_distance()
        self.df = self.correct_dining_datatype()
        self.df = self.encode_column()
        return self.df