import pandas as pd

def data_preprocessing():
    
    data = pd.read_csv("/home/doc-bd-a1/titanic.csv")
    
    data.dropna(inplace=True)  
    data.drop_duplicates(inplace=True)  
    
    data['Fare'] = data['Fare'].apply(lambda x: x * 1.05)  #transformation on Age

    columns_to_keep = ['Survived', 'Pclass', 'Age', 'Fare', 'Sex']
    data = data[columns_to_keep]  

    data['Fare'] = pd.cut(data['Fare'], bins=4, labels=['Low', 'Medium', 'High', 'Very High'])  # Discretize Fare
    data['Age'] = pd.cut(data['Age'], bins=3, labels=['Young', 'Adult', 'Senior'])  

    data.to_csv("/home/doc-bd-a1/res_dpre.csv", index=False)
    print("Data preprocessing completed and saved to res_dpre.csv.")

if __name__ == "__main__":
    data_preprocessing()
