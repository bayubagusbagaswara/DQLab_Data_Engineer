# Pendahuluan
CSV atau comma separated value adalah salah satu tipe file yang digunakan secara luas di dunia programming. Tidak hanya itu CSV pun sering digunakan dalam pengolahan informasi yang dihasilkan spreadsheet untuk diproses lebih lanjut melalui mesin analitik. CSV pun dianggap sebagai file yang agnostik karena dapat digunakan oleh berbagai database untuk proses backup data. CSV dianggap sebagai salah satu tipe data yang sering dipakai untuk mengelola data pada proses lanjutan.

# Membaca Teks File (CSV)

Sekarang kita akan mencoba membaca sebuah file CSV yang telah dihasilkan aplikasi atau program lain. Di Python, hasil pembacaan setiap baris pada file CSV akan dikonversi menjadi list Python.

Jika kamu ingin membaca file csv yang tersimpan di direktori yang sama dengan direktori program python kamu, maka kode berikut dapat kamu gunakan (misalnya di local computer kamu): 

```bash
import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv', 'r')
reader = csv.reader(f)

# membaca baris per baris
for row in reader:
     print (row)

# menutup file csv
f.close()
```

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python%20Fundamental%20for%20Data%20Science/7-Membaca-dari-File/1-membaca-text-file-csv/ReadCsv.py) | Membaca file CSV |

# Membaca file CSV dengan menggunakan PANDAS

Bagi yang belum familiar, PANDAS merupakan salah satu library yang sangat sering digunakan untuk aplikasi dan implementasi data science baik untuk data manipulation, data pre-processing, atau data wrangling. Pada sesi kali ini, kita akan menggunakan PANDAS untuk membaca file dari csv.

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python%20Fundamental%20for%20Data%20Science/7-Membaca-dari-File/2-membaca-csv-with-pandas/ReadCsvWithPandas.py) | Membaca file dengan PANDAS |
