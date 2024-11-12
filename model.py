import pandas as pd
from sklearn.cluster import KMeans

def kmeans_clustering():
    # Load the preprocessed data
    data = pd.read_csv("/home/doc-bd-a1/res_dpre.csv")
    
    # Use 'Survived' and 'Pclass' columns for K-Means clustering
    selected_columns = ['Survived', 'Pclass']
    
    # Ensure the selected columns are in the data
    if not all(col in data.columns for col in selected_columns):
        print("Error: One or more of the selected columns are missing from the dataset.")
        return
    
    # Extract data for clustering
    clustering_data = data[selected_columns].dropna()  # Drop any rows with NaN in selected columns

    # Check if clustering_data is empty
    if clustering_data.empty:
        print("No valid data available for clustering after filtering. Check the dataset or selected columns.")
        return
    
    # Apply K-Means with k=3
    kmeans = KMeans(n_clusters=3, random_state=42)
    data.loc[clustering_data.index, 'Cluster'] = kmeans.fit_predict(clustering_data)
    
    # Count records in each cluster
    cluster_counts = data['Cluster'].value_counts()
    
    # Save the counts to k.txt
    with open("/home/doc-bd-a1/k.txt", "w") as file:
        file.write("Number of records in each cluster:\n")
        file.write(str(cluster_counts))
    
    print("Cluster record counts saved as k.txt.")

if __name__ == "__main__":
    kmeans_clustering()
