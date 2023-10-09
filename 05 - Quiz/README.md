# Diskusi dan Perbandingan

Pertama kita melihat keseimbangan jumlah dataset yang terdapat di MNIST Dataset. Dalam analisis ini, jumlah data terbukti seimbang, yang dibuktikan dengan perhitungan menggunakan rumus berikut:

$CV = \frac{\text{Standard Deviation}}{\text{Mean}} \times 100$

Perhitungan Koefisien Varians dilakukan untuk melihat varians data, dan ditemukan bahwa CV mencapai hanya 5%. Selanjutnya, hasil ini juga diperkuat dengan visualisasi distribusi data menggunakan bar chart.

![Distribusi Data](docs/bar-chart-cv.png)

## Support Vector Machine (SVM)

1. **SVC Kernel RBF dengan C = 1 dan Gamma = 0.01**
   - Model menggunakan SVC kernel rbf dengan parameter C = 1 dan Gamma = 0.01.
   - Proses preprocessing melibatkan PCA dengan 60 komponen yang dibagi menjadi data latih sebesar 70% dan data uji sebesar 30%.
   - Hasil prediksi mencapai akurasi 93%.
2. **SVC dengan Hyperparameter Tuning**
   - Model SVC diuji dengan hyperparameter tuning menggunakan GridSearchCV dengan variasi nilai C dan gamma.
   - Parameter terbaik yang ditemukan adalah `{'svc__C': 10, 'svc__gamma': 0.01}`, dengan akurasi mencapai 97%.
   - Confusion matrix dan hasil prediksi gambar juga ditampilkan.
3. 
Setelah itu, dilakukan ekstraksi fitur, dan beberapa pengujian model dilakukan dengan ekstraksi PCA (Principal Component Analysis) dengan reduksi dimensi hingga ke-n. Sebagai contoh, reduksi sebesar 49 komponen digunakan.

![Reduksi Dimensi PCA](docs/reduksi-dimensi-pca.png)

Kemudian, Kelompok 4 melakukan perbandingan antara model SVM (Support Vector Machine) dan Naive Bayes. Berikut adalah hasil perbandingan tersebut:

1. **SVC Kernel RBF dengan C = 1 dan Gamma = 0.01**

   - Model menggunakan SVC kernel rbf dengan parameter C = 1 dan Gamma = 0.01.
   - Proses preprocessing melibatkan PCA dengan 60 komponen yang dibagi menjadi data latih sebesar 70% dan data uji sebesar 30%.
   - Hasil prediksi mencapai akurasi 93%.

   ![Hasil Prediksi](docs/hasil-1-svc.png) [1]

2. **Naive Bayes dengan 5 Parameter**

   - Model Naive Bayes menggunakan 5 parameter yang berbeda dengan var_smoothing sebagai salah satu parameter.
   - Ditemukan bahwa model mendapatkan akurasi sebesar 87.25%, dengan parameter terbaik adalah `1e-05`.

   ![Hasil Prediksi](docs/hasil-2-naive.png) [2]

3. **Naive Bayes MultinomialNB**

   - Model ini menggunakan jenis model Multinomial Naive Bayes dengan Alpha (n_features) di-set menjadi 1.0.
   - Hasil akurasi data latih mencapai 82.6% dan data uji mencapai 82.9%.
   - Confusion matrix dan hasil prediksi gambar juga ditampilkan.

   ![Confusion Matrix](docs/hasil-3-multinomial.png)
   ![Prediksi Gambar](docs/hasil-3-multinomial-label.png)

4. **SVC dengan Hyperparameter Tuning**

   - Model SVC diuji dengan hyperparameter tuning menggunakan GridSearchCV dengan variasi nilai C dan gamma.
   - Parameter terbaik yang ditemukan adalah `{'svc__C': 10, 'svc__gamma': 0.01}`, dengan akurasi mencapai 97%.
   - Confusion matrix dan hasil prediksi gambar juga ditampilkan.

   ![Confusion Matrix](docs/hasil-4-svm-cm.png)
   ![Prediksi Gambar](docs/hasil-4-svm-label.png)  [4,5]

Referensi Model:
[1] [SVC RBF Model MNIST - Ali Zulfikar](https://github.com/alizul01/machine-learning-course/blob/main/05%20-%20Quiz/Quiz_Challenge.ipynb)
[2] [Naive Bayes for MNIST - Izamul Fikri](https://github.com/zenosance/machine-learning/blob/main/Pembelajaran_Mesin_Kuis_1_Naive_Bayes.ipynb)
[3] [MultinomialNB Naive Bayes for MNIST - Ulfi Izza](https://github.com/ulfiizza27/2141720052-Machine-Learning-2023/blob/main/Week%205/NaiveBayes_Multinominal.ipynb)
[4] [SVM Hyperparameter Tuning - Ulfi Izza](https://github.com/ulfiizza27/2141720052-Machine-Learning-2023/blob/main/Week%205/SVM.ipynb)
[5] [SVM Hyperparameter Tuning - Ilham Yudantyo](https://github.com/ilhamydn17/2141720091-MachLearn-2023/blob/week-05-kuis1/kuis_1_result.ipynb)
[6] [SVM]()
