# Ada permintaan datang dari tim logistik bahwa mereka membutuhkan kode pos dari peserta agar pengiriman piala lebih mudah dan cepat sampai. Maka dari itu buatlah kolom baru bernama postal_code yang memuat informasi mengenai kode pos yang diambil dari alamat peserta (kolom address).

# Diketahui bahwa kode pos berada di paling akhir dari alamat tersebut.

# Note:
# Jika regex yang dimasukkan tidak bisa menangkap pattern dari value kolom address maka akan menghasilkan NaN.

import pandas as pd
df_participant = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/dqthon-participants.csv')

df_participant['postal_code'] = df_participant['address'].str.extract(
    r'(\d+)$')  # Masukkan regex Anda didalam fungsi extract
