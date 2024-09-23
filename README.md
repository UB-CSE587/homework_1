# Homework 1
This homework consists of two tasks. The first task requires students to implement a Linear Regression model for anomaly detection. The second task involves applying the K-Nearest Neighbors (KNN) algorithm and K-means clustering for image editing.

## 1. Tasks
### 1.1 Linear Regression:
Please use the provided dataset linear_regression.csv for training. The dataset contains 2000 data points with 100 features, and the last column represents the target variable y. Your task is to:

- Train a linear regression model using the 100 features to predict the target value y.
- Additionally, there are a few samples in the dataset that are mislabeled, meaning their y values have large errors compared to the rest of the data. Your objective is to identify all mislabeled samples using your approach.

Make sure to explain the method you use to detect these mislabeled samples in your report.

### 1.2. Image Editing using k-means and kNN:
1.2. Image Editing using K-means and kNN:

In this task, you are required to load images as tensors and treat all pixel colors as 3-dimensional features (RGB) and edit the image using K-means and KNN algorithms. To complete this task, you must:

- **Determine the optimal number of clusters ($k$)**: You are expected to choose a method to determine the value of $k$, such as the Elbow Method, Silhouette Score, or any other appropriate technique. While there is no single “correct” answer for the optimal $k$, you must describe the rationale behind your chosen approach, ensuring it is based on numerical reasoning, not personal preference.
- **Apply K-means**: Once the optimal $k$ is identified, apply the K-means algorithm to compress `image1.png`. This process clusters the pixel colors and replaces each pixel with the color of its corresponding cluster centroid, resulting in a compressed version of `image1.png` with a reduced set of distinct colors.
- **Use K-Nearest Neighbors (KNN) for color assignment to `image2.png`**: After compressing `image1.png`, use the same color palette (the centroids obtained from K-means) to assign colors to `image2.png`. This will be done using the K-Nearest Neighbors (KNN) algorithm, ensuring that `image2.png` adopts the same color scheme as `image1.png` after compression.

A demo: 
<p align="center">
  <img src="https://raw.githubusercontent.com/UB-CSE587/homework_1/main/demo.png" alt="demo" width="800"/>
</p>

## 2. Submission Format:
You are expected to submit a zip file in UBLearn consists all your code and your report in pdf and organized as following:
```
<UBIT_Name>
--<UBIT_Name>.pdf
--linear_regression.py
--image_edit.py
--requirement.txt (optional)
--additional script (optional)
...
```
### 2.1 Report
Please write a report describing the implementation details, such as package and parameter settings, how you propose to detect mislabeled data and why you choose the number of colors $k$ in k-means. Please write in English not coding language. (Do NOT include any code in your report).

### 2.2 Code
We will run your code using the following commands:
```
unzip <UBIT_Name>
cd <UBIT_Name>
pip install -r requirement.txt
python linear_regression.py
python image_edit.py
```
- Task 1: Your code `linear_regression.py` should save the results in a new CSV file named `linear_regression_done.csv` in the same folder. The file should include a column named "Outlier", containing binary values for each row, where: 1 indicates mislabeled data. 0 indicates correctly labeled data.

- Task 2: Your code `image_edit.py` should save two images, `image1_done.png` and `image2_done.png` in the same folder. These should be the compressed versions of `image1.png` and `image2.png`, respectively, using the same set of colors. The saved images should be identical to the ones included in your report. 

We will set up a Python environment with common packages like Torch, scikit-learn, pandas, matplotlib, Pillow, etc. If you plan to use an uncommon package that we may not have installed, please ask on Piazza, and we’ll try to set it up in our test environment. Alternatively, you can provide a requirements.txt file, and we will install the necessary packages during testing. However, we recommend simplifying your code dependencies to minimize the risk of losing points due to code execution errors.

## 3. Score
The score will be assigned as:
### Task 1
- Successful code execution: 15,
- Mislabeled data detection: 15, 
- report writing quality: 20

### Task 2
- Successful code execution: 25
- Report writing quality: 25
