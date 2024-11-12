import pandas as pd
import matplotlib.pyplot as plt

def create_visualization():
    # Load preprocessed data
    data = pd.read_csv("/home/doc-bd-a1/res_dpre.csv")
    
    # Example visualization: Passenger class distribution
    plt.figure(figsize=(8, 6))
    data['Pclass'].value_counts().plot(kind='bar', color='skyblue')
    plt.title("Passenger Class Distribution")
    plt.xlabel("Passenger Class")
    plt.ylabel("Count")
    
    # Save the plot as vis.png
    plt.savefig("/home/doc-bd-a1/vis.png")
    print("Visualization saved as vis.png.")

if __name__ == "__main__":
    create_visualization()
