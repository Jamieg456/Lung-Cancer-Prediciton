import pandas as pd

def preprocess_data(df):
    # Clean whitespace from column names
    df.columns = df.columns.str.strip()

    # Replace underscores with spaces in column names
    df.columns = df.columns.str.replace('_', ' ', regex=False)

    # Check for duplicates and remove them
    df.drop_duplicates(inplace=True)

    # Replace values (convert 2 to 1 and 1 to 0)
    df.replace({2: 1, 1: 0}, inplace=True)

    # Encode binary categorical columns
    df['LUNG CANCER'] = df['LUNG CANCER'].map({'YES': 1, 'NO': 0})
    df['GENDER'] = df['GENDER'].map({'M': 1, 'F': 0})

    return df

def load_and_preprocess_data(file_path):
    # Load data from a CSV file
    df = pd.read_csv(file_path)
    # Preprocess data
    df = preprocess_data(df)
    return df
