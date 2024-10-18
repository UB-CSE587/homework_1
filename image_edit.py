import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import os

def compress_image(image, n_colors):
    """
    Compress the image using K-means clustering to reduce the number of colors.
    
    Parameters:
    - image: Input image as a 3D NumPy array (height, width, 3).
    - n_colors: The number of colors for K-means clustering (number of clusters).
    
    Returns:
    - compressed_image: The compressed image.
    - centroids: The color centroids obtained from K-means clustering.
    """
    # Step 1: Reshape the image to be a 2D array of pixels
    pixels = image.reshape(-1, 3)
    
    # Step 2: Apply K-means to the pixel colors
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(pixels)
    
    # Step 3: Replace each pixel color with its nearest cluster centroid
    compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]
    
    # Step 4: Reshape the 2D array back to the original image shape
    compressed_image = compressed_pixels.reshape(image.shape)
    
    # Convert pixel values to integers
    compressed_image = np.clip(compressed_image, 0, 255).astype('uint8')
    
    return compressed_image, kmeans.cluster_centers_

def assign_colors(image, centroids):
    """
    Assign each pixel in the image to the nearest centroid using KNN.
    
    Parameters:
    - image: Input image as a 3D NumPy array (height, width, 3).
    - centroids: The color centroids obtained from K-means clustering.
    
    Returns:
    - recolored_image: The image with colors assigned based on the centroids.
    """
    # Reshape the image to a 2D array of pixels
    pixels = image.reshape(-1, 3)
    
    # Create and fit the KNN model
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(centroids, np.arange(len(centroids)))
    
    # Predict the nearest centroid for each pixel
    nearest_centroids = knn.predict(pixels)
    
    # Recolor the image by replacing each pixel with its nearest centroid's color
    recolored_pixels = centroids[nearest_centroids]
    
    # Reshape the recolored pixels back to the original image shape
    recolored_image = recolored_pixels.reshape(image.shape)
    
    # Convert pixel values to integers
    recolored_image = np.clip(recolored_image, 0, 255).astype('uint8')
    
    return recolored_image

# Main code block
if __name__ == "__main__":
    # Paths to the images
    image1_path = './data/image1.png'
    image2_path = './data/image2.png'
    
    # Ensure the image files exist
    if not os.path.exists(image1_path):
        raise FileNotFoundError(f"Image file '{image1_path}' not found.")
    if not os.path.exists(image2_path):
        raise FileNotFoundError(f"Image file '{image2_path}' not found.")
    
    # Load the images using PIL
    image1 = Image.open(image1_path).convert("RGB")
    image2 = Image.open(image2_path).convert("RGB")
    
    # Convert the PIL images to NumPy arrays
    image1 = np.array(image1)
    image2 = np.array(image2)
    
    # Compress image1 using K-means
    n_colors = 15  # Number of colors for compression
    compressed_image1, centroids = compress_image(image1, n_colors)
    
    # Save and display the compressed image1
    compressed_image1_pil = Image.fromarray(compressed_image1)
    compressed_image1_pil.save('./image1_done.png')
    # compressed_image1_pil.show()
    
    # Use KNN to recolor image2 with the centroids from image1
    recolored_image2 = assign_colors(image2, centroids)
    
    # Save and display the recolored image2
    recolored_image2_pil = Image.fromarray(recolored_image2)
    recolored_image2_pil.save('./image2_done.png')
    # recolored_image2_pil.show()