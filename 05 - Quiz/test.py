import numpy as np
import pickle
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load model dari file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Unduh data MNIST
X, y = fetch_openml('mnist_784', as_frame=False, return_X_y=True)

# Lakukan PCA untuk mengurangi dimensi data menjadi 2 dimensi
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Lakukan prediksi menggunakan model
y_pred = model.predict(X)

# Plot data dengan warna sesuai label asli
plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', s=10, alpha=0.7, marker='o', edgecolor='k', label='True Labels')

# Plot vektor dukungan
support_vectors = model.support_vectors_
plt.scatter(support_vectors[:, 0], support_vectors[:, 1], s=100, facecolors='none', edgecolors='r', label='Support Vectors')

plt.title('Visualisasi Model SVM pada Data MNIST')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()
