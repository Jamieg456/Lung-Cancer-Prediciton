[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TnJIQ-Y6)
# Data Mining and Machine Learning Group Coursework


## Group Members

1. Jamie Garrity - @jamieg456 - H00243621
2. Tasnim Ramnarine - @tasnimzah - H00448137
3. Prakash Kabra - @prakashkabra7 - H00484825
4. Antonin Moreno @[github_username] - H00478052
5. Numan Arif [Rf-numan] - H00457584

## Initial Project Proposal
Our project aims to look at cancer prediction, specifically lung cancer. This was prompted by the desire to work with an imaging dataset as well as a CSV.

### [MSc Students Only] Research objectives
Our Research objective is to investigate how accurately machine learning models could predict the presence of cancer using symptoms, lifestyle data, or imaging scans (symptoms and images independent of each other). And further to investigate how effectively imagaging scans can be diffrentiated.


Our hypothese are as following:

Hypothesis 1: The neural network model will effectively distinguish between healthy lungs and those affected by cancer using imaging datasets.

Hypothesis 2: The neural network model will also effectively differentiate between various types of lung cancer using imaging datasets.

Hypothesis 3: Models trained on symptoms and lifestyle information will accurately predict lung cancer presence.


### Source of Datasets

1. A Lung Cancer Dataset – Can be accessed on Kaggle at https://www.kaggle.com/datasets/samuelotiattakorah/lung-cancer-data/data . Available under a CC0: Public domain licence.
<img width="452" alt="image" src="https://github.com/user-attachments/assets/c5531550-3a08-45d0-ab57-5049ec9c399c">

An example of pre-processed data


2. A CT scan dataset - Can be accessed on Kaggle at https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images. Available under an Open Database Licence.

![000002](https://github.com/user-attachments/assets/71186872-b059-47f8-a0ff-c366535d7b87)

An example of a CT scan from out image dataset


### Milestones
Our Group Milestones are as follows:

1.Topic and dataset selection.

2.Dataset processing and analysis.

3.Minimum 3 clustering algorithms
  
  -3.1 Any additional clustering algorithms will also be considered milestones

4.Minimum 2 Predictive models
  
  -4.1 Any additional predictive models will also be considered milestones

5.CNN development
  
  -5.1 CNN refinement


## Installing the project

This project consists of mainly jupyternookebook files. To run this project both python3 and jupyter notebook will need to be installed on the system.

The repository should be downloaded and then dependdencies installed.

pip install numpy pandas opencv-python sklearn scikit-learn seaborn tensorflow matplotlib

The project folder can then be accessed by launching jupyter notebook with the following command

jupyter notebook

and then navigating to the corresponding folder.

## Data Preparation Pipeline

Our lung cancer CSV dataset is stored in the data folder of our repo, and there is a python script data_preprocessing.py in our scripts folder that is called in the necessary notebooks to ensure the data is correclty cleaned and formatted.

Our Image dataset was too large to upload to the git repository, thus there is a pyhton script download_image_dataset.py that will retrieve our dataset and store it in a corresponding root directory and reformat it within the necessary image notebooks.


## Coursework Requirements

### R2. Data Analysis and Exploration
  Found in the notebook folder with the heading R2 is the inital analysis of out dataset.

### R3. Clustering
  Found in the notebook folder with the heading R3, these are multiple files with different clustering of our datasets to help us decide on feature for our predictive models in R4.

### R4.	Baseline Training and Evaluation Experiments
  Found in the notebook folder with the heading R4, this is the code for our predictive models (for the csv dataset) and the evaluation of their effetiveness.

### R5. Neural Networks
  Found in the notebook folder with the heading R5, this is the code for our CNN that categorises our image data.

## Documentation

Weekly updates are kept in the `documentation/` directory.
