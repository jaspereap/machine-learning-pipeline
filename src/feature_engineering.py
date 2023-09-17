# This module handles adding new features to the dataset

import pandas as pd

# Adding age column
def add_age(df):
    def convert_to_dmy(date_of_birth):
        if date_of_birth is not None:
            try:
                # Try to parse the date assuming %d/%m/%Y format
                date_obj = pd.to_datetime(date_of_birth, format='%d/%m/%Y')
                return date_obj.strftime('%d/%m/%Y')
            except ValueError:
                try:
                    # If parsing fails, try parsing with %Y/%d/%m format
                    date_obj = pd.to_datetime(date_of_birth, format='%Y/%d/%m')
                    return date_obj.strftime('%d/%m/%Y')
                except ValueError:
                    try:
                        # If parsing fails, try parsing with %Y/%m/%d format
                        date_obj = pd.to_datetime(date_of_birth, format='%Y/%m/%d')
                        return date_obj.strftime('%d/%m/%Y')
                    except ValueError:
                        # If all formats fail, return the original value
                        return date_of_birth
        else:
            return date_of_birth

    # Apply function to every row in cruise_pre_df
    df['Date of Birth'] = df['Date of Birth'].apply(convert_to_dmy)

    # Add a new column 'Age', compute age by subtracting logging date by their date of birth, getting the quotient after dividing by 365
    df['Age'] = (pd.to_datetime(df['Logging'], format='%d/%m/%Y %H:%M') - pd.to_datetime(df['Date of Birth'], format='%d/%m/%Y')).dt.days // 365

    # Keep rows with age <= 120
    df = df[df['Age'] <= 120]

    return df

def add_onboard_experience(df):
    # Define the list of columns to be averaged
    onboard_experience_columns = ['Onboard Wifi Service', 'Onboard Dining Service',
                                'Cabin Comfort', 'Onboard Entertainment',
                                'Cabin service', 'Cleanliness']

    # Calculate the average for the new column
    df['Onboard Experience'] = df[onboard_experience_columns].mean(axis=1).round()
    return df

def add_check_in_experience(df):
    # Define the list of columns to be averaged
    check_in_experience_columns = ['Embarkation/Disembarkation time convenient', 
                                    'Gate location', 
                                    'Online Check-in', 
                                    'Baggage handling', 
                                    'Port Check-in Service']

    # Calculate the average for the new column
    df['Check-in Experience'] = df[check_in_experience_columns].mean(axis=1).round()
    return df