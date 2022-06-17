# Secara default setelah suatu dataframe dibaca dari file dengan format tertentu, index-nya merupakan single index.

# Pada sub bab ini akan mencetak index dan kolom yang dimiliki oleh file "https://storage.googleapis.com/dqlab-dataset/sample_csv.csv". Untuk menentukan index dan kolom yang dimiliki oleh dataset yang telah dinyatakan sebagai sebuah dataframe pandas dapat dilakukan dengan menggunakan atribut .index dan .columns.

import pandas as pd
# Baca file TSV sample_tsv.tsv
df = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/sample_csv.csv", sep="\t")
# Index dari df
print("Index:", df.index)
# Column dari df
print("Columns:", df.columns)
