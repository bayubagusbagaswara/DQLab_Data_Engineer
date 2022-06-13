# Value yang hilang/tidak lengkap dari dataframe akan membuat analisis atau model prediksi yang dibuat menjadi tidak akurat dan mengakibatkan keputusan salah yang diambil. Terdapat beberapa cara untuk mengatasi data yang hilang/tidak lengkap tersebut.

# Data COVID-19 yang akan digunakan ini diambil dari google big query, tetapi sudah disediakan datasetnya dalam format csv dengan nama https://storage.googleapis.com/dqlab-dataset/datacovid19.csv. Ini adalah studi kasus untuk meng-handle missing value. Bagaimanakah langkah-langkahnya?

# Di pandas data yang hilang umumnya direpresentasikan dengan NaN.

# Langkah pertama, harus tahu kolom mana yang terdapat data hilang dan berapa banyak dengan cara:

# Cara 1: menerapkan method .info() pada dataframe yang dapat diikuti dari kode berikut ini:

# Cara 2: mengetahui berapa banyak nilai hilang dari tiap kolom di dataset tersebut dengan menerapkan chaining method pada dataframe yaitu .isna().sum(). Method .isna() digunakan untuk mengecek berapa data yang bernilai NaN dan .sum() menjumlahkannya secara default untuk masing-masing kolom dataframe.

# Tugas Praktek:
# Ketikkanlah kembali statement seperti yang ditunjukkan dalam kedua cara untuk mendeteksi missing value pada dataframe dengan mengisi tanda _ _ _ di code editor.

import pandas as pd
# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
# Cetak info dari df
print(df.info())
# Cetak jumlah missing value di setiap kolom
mv = df.isna().sum()
print("\nJumlah missing value per kolom:\n", mv)
