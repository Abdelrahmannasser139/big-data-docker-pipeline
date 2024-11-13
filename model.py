import pandas as pd
from sklearn.cluster import KMeans

def kmeans_clustering():
    data = pd.read_csv("/home/doc-bd-a1/res_dpre.csv")

    selected_columns = ['Survived', 'Pclass']
    
    clustering_data = data[selected_columns].dropna()  

    if clustering_data.empty:
        print("No valid data available for clustering. ")
        return
    
    kmeans = KMeans(n_clusters=3, random_state=42)
    data.loc[clustering_data.index, 'Cluster'] = kmeans.fit_predict(clustering_data)
    
    cluster_counts = data['Cluster'].value_counts()
    
    with open("/home/doc-bd-a1/k.txt", "w") as file:
        file.write("Number of records in each cluster:\n")
        file.write(str(cluster_counts))
    
    print("Cluster record counts saved as k.txt.")

if __name__ == "__main__":
    kmeans_clustering()
