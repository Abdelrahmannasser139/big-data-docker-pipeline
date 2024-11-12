import pandas as pd

def eda():
    # Load the preprocessed data
    data = pd.read_csv("/home/doc-bd-a1/res_dpre.csv")
    
    insights = []
    
    # Check if the 'Survived' column is present and add an insight
    if 'Survived' in data.columns:
        # Check if the 'Age' column contains numeric values
        if pd.api.types.is_numeric_dtype(data['Age']):
            avg_age_survivors = data[data['Survived'] == 1]['Age'].mean()
            insights.append(f"Average age of survivors: {avg_age_survivors}")
        else:
            age_counts = data['Age'].value_counts()
            insights.append(f"Age distribution (non-numeric values):\n{age_counts}")

    # Check for 'Pclass' and add insight on passenger count per class
    if 'Pclass' in data.columns:
        insights.append(f"Total number of passengers in each class:\n{data['Pclass'].value_counts()}")

    # Check for 'Sex' and add gender distribution insight
    if 'Sex' in data.columns:
        insights.append(f"Gender distribution:\n{data['Sex'].value_counts()}")

    # Write insights to files
    for i, insight in enumerate(insights, 1):
        with open(f"/home/doc-bd-a1/eda-in-{i}.txt", "w") as file:
            file.write(insight)

    print("EDA insights saved as text files.")

if __name__ == "__main__":
    eda()
