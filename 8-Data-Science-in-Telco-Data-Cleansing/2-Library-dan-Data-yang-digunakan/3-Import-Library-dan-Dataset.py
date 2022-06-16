# Berdasarkan penjelasan mengenai library dan dataset yang akan digunakan, sekarang hal pertama yang akan kita lakukan adalah melakukan import library dan dataset ke dalam workspace kita.

# Setelah dataset di-import ke dalam workspace, tampilkan jumlah kolom dan baris dari data set dengan menggunakan .shape dan print 5 baris teratas dengan menggunakan head() dan carilah ada

# Notes:

# 1. pd.options.display.max_columns = 50 digunakan untuk mempermudah penampilan row data
# 2. Simpan dataset ke dalam variabel df_load

#import library
import pandas as pd
pd.options.display.max_columns = 50

#import dataset
df_load = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')

# Tampilkan jumlah baris dan kolom
print(df_load.shape)

# Tampilkan 5 data teratas
print(df_load.head(5))

# Jumlah ID yang unik
print(df_load.customerID.unique())
