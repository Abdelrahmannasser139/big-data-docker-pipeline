import pandas as pd

def data_preprocessing():
    # Load data
    data = pd.read_csv("/home/doc-bd-a1/titanic.csv")
    
    # Data Cleaning
    data.dropna(inplace=True)  # Remove rows with missing values
    data.drop_duplicates(inplace=True)  # Remove duplicate rows

    # Data Transformation
    if 'Age' in data.columns:
        data['Age'] = data['Age'].apply(lambda x: x + 1)  # Example transformation on Age
    if 'Fare' in data.columns:
        data['Fare'] = data['Fare'].apply(lambda x: x * 1.05)  # Example transformation on Fare

    # Data Reduction
    columns_to_keep = ['Survived', 'Pclass', 'Age', 'Fare', 'Sex']
    data = data[columns_to_keep]  # Select relevant columns, including 'Survived'

    # Data Discretization
    if 'Fare' in data.columns:
        data['Fare'] = pd.cut(data['Fare'], bins=4, labels=['Low', 'Medium', 'High', 'Very High'])  # Discretize Fare
    if 'Age' in data.columns:
        data['Age'] = pd.cut(data['Age'], bins=3, labels=['Young', 'Adult', 'Senior'])  # Discretize Age

    # Save the preprocessed data
    data.to_csv("/home/doc-bd-a1/res_dpre.csv", index=False)
    print("Data preprocessing completed and saved to res_dpre.csv.")

if __name__ == "__main__":
    data_preprocessing()
