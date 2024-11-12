import pandas as pd
import sys

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")

if __name__ == "__main__":
    file_path = sys.argv[1]
    load_data(file_path)
