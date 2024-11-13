import pandas as pd

def eda():
    data = pd.read_csv("/home/doc-bd-a1/res_dpre.csv")

    age_distribution = data['Age'].value_counts()
    pclass_distribution = data['Pclass'].value_counts()
    gender_distribution = data['Sex'].value_counts()

    insights = [
        f"Age distribution (non-numeric values):\n{age_distribution}", 
        f"Total number of passengers in each class:\n{pclass_distribution}",  
        f"Gender distribution:\n{gender_distribution}"  
    ]

    for i, insight in enumerate(insights, 1):
        with open(f"/home/doc-bd-a1/eda-in-{i}.txt", "w") as file:
            file.write(insight)

    print("EDA insights saved as text files.")

if __name__ == "__main__":
    eda()
