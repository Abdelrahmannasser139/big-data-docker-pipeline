# Big Data Docker Pipeline
- Project Overview:
  
  This project sets up a data processing pipeline within a Docker container using Python. It processes a dataset through loading, preprocessing, exploratory data    analysis (EDA), visualization, and K-means clustering. Results are saved to a specified directory on the local machine.

# Docker Hub Image
The Docker image for this project is available on Docker Hub. This image includes Python and the following libraries: Pandas, Numpy, Seaborn, Matplotlib, Scikit-learn, and Scipy, along with all necessary project files.

Docker Hub Repository: abdelrahmannasser13/bd-a1-image

# Project Structure :

bd-a1/

├── titanic.csv              # Dataset to be processed

├── Dockerfile               # Docker setup and environment specifications

├── final.sh                 # Script to copy outputs from container to host and stop container

├── service-result/          # Directory to store output files after processing

└── README.md                # Project documentation

# Instructions
1. Set Up Project
- Clone the Repository
   git clone https://github.com/abdelrahman139/bd-a1.git
   cd bd-a1
  
Adding Dataset
titanic.csv in the bd-a1/ directory.

2. Docker Setup
The Dockerfile contains instructions for creating an Ubuntu-based Docker image with the following libraries installed:
Python3, Pandas, Numpy, Seaborn, Matplotlib, Scikit-learn, Scipy
It also copies the dataset to /home/doc-bd-a1/ in the container .

3. Build and Run the Docker Container
- Build the Docker Image
   docker build -t bd-a1-image .
- Start the Docker Container
   docker run -it --name bd-a1-container bd-a1-image
4. Execute the Pipeline Inside the Container
- python3 load.py titanic.csv
This will process the dataset through the following steps:

  Data Loading (load.py): Loads the dataset as a DataFrame and passes it to the next step.
  Data Preprocessing (dpre.py): Cleans, transforms, reduces, and discretizes the data, saving it to res_dpre.csv.
  Exploratory Data Analysis (eda.py): Saves 3 text files (eda-in-1.txt, eda-in-2.txt, eda-in-3.txt) with insights.
  Visualization (vis.py): Saves a bar chart as vis.png.
  Modeling (model.py): Runs K-means clustering and saves cluster counts in k.txt.
  
5. Copy Results from the Container to Local Machine
Run final.sh on your local machine to copy the output files from the container and then stop the container:

./final.sh
Output files will be in the bd-a1/service-result/ directory in local machine.

# Output Files
After the pipeline completes the following files will be generated in service-result/:
eda-in-1.txt, eda-in-2.txt, eda-in-3.txt: Text files with EDA insights.
vis.png: A bar chart visualization.
k.txt: Text file with the cluster counts from K-means clustering.

# Docker Commands Summary
- Build the Docker Image
docker build -t bd-a1-image .

- Run the Docker Container
docker run -it --name bd-a1-container bd-a1-image

- Execute the Pipeline Inside the Container
python3 load.py train.csv
- Copy Results and Stop the Container Run on your local machine:
./final.sh

# Project Structure Recap
bd-a1/

├── titanic.csv               # Original dataset

├── Dockerfile                # Docker configuration

├── final.sh                  # Script to copy outputs and stop container

├── README.md                 # Documentation

└── service-result/           # Directory with output files

    ├── eda-in-1.txt          # EDA insight 1
    
    ├── eda-in-2.txt          # EDA insight 2
    
    ├── eda-in-3.txt          # EDA insight 3
    
    ├── vis.png               # Visualization image
    
    └── k.txt                 # Cluster counts
