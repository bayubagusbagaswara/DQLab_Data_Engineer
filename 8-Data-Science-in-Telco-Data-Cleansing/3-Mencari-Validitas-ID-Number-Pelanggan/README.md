# Memfilter ID Number Pelanggan Format Tertentu
Mencari format ID Number (Phone Number) Pelanggan `customerID` yang benar, dengan kriteria:

- Panjang karakter adalah 11-12.
- Terdiri dari angka Saja, tidak diperbolehkan ada karakter selain angka
- Diawali dengan angka 45 2 digit pertama.
 
Gunakan fungsi `count()` untuk menghitung banyaknya rows Customer ID, anda juga bisa menggunakan `str.match()` & regex untuk mencocokan dengan kriteria diatas. Jangan lupa gunakan `astype()` untuk merubah tipe datanya yang semula numeric

Notes : Buat kolom bantuan baru dengan nama `valid_id`

Hasil yang diharapkan adalah sebagai berikut:

```bash
Hasil jumlah ID Customer yang terfilter adalah 7006
```

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/8-Data-Science-in-Telco-Data-Cleansing/3-Mencari-Validitasi-ID-Number-Pelanggan/MemfilterIDNumberPelangganFormatTertentu.py) | Memfilter ID Number Pelanggan Format Tertentu |

# Memfilter Duplikasi ID Number Pelanggan
Memastikan bahwa tidak ada Id Number pelanggan yang duplikat. Biasanya duplikasi ID number ini tipenya:

- Duplikasi dikarenakan inserting melebihi satu kali dengan nilai yang sama tiap kolomnya
- Duplikasi dikarenakan inserting beda periode pengambilan data

Gunakan hasil dari pengolahan di tahap sebelumnya `df_load` untuk diolah di tahap ini. Gunakan fungsi `drop_duplicates()` untuk menghapus duplikasi rows, dan gunakan `sort_values()` untuk mengecek pengambilan data terakhir.

Berikut adalah hasil jumlah Customer ID:

```bash
Hasil jumlah ID Customer yang sudah dihilangkan duplikasinya (distinct) adalah 6993
```

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/8-Data-Science-in-Telco-Data-Cleansing/3-Mencari-Validitasi-ID-Number-Pelanggan/MemfilterDuplikasiIDNumberPelanggan.py) | Memfilter Duplikasi ID Number Pelanggan |

Kesimpulan
Validitas dari ID Number pelanggan sangat diperlukan untuk memastikan bahwa data yang kita ambil sudah benar. Berdasarkan hasil tersebut, terdapat perbedaan jumlah nomor ID dari data pertama kali di load sampai dengan hasil akhir. Jumlah row data ketika pertama kali di load ada sebanyak 7113 rows dan 22 columns dengan 7017 jumlah ID yang unique. Kemudian setelah di cek validitas dari ID pelanggan, maka tersisa 6993 rows data