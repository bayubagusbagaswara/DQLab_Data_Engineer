# Pendahuluan

Kalau mau pakai perintah SELECT untuk akses data, lebih baik belajarnya langsung praktik.

# Tabel yang digunakan

Table `ms_pelanggan`

```bash
+---------+----------------+---------------------+------------------------------------------+
| no_urut | kode_pelanggan | nama_customer       | alamat                                   |
+---------+----------------+---------------------+------------------------------------------+
|       1 | dqlabcust01    | Eva Novianti, S.H.  | Vila Sempilan, No. 67 - Kota B           |
|       2 | dqlabcust02    | Heidi Goh           | Vila Sempilan, No. 11 - Kota B           |
|       3 | dqlabcust03    | Unang Handoko       | Vila Sempilan, No. 1 - Kota B            |
|       4 | dqlabcust04    | Jokolono Sukarman   | Vila Permata Intan Berkilau, Blok C5-7   |
|       5 | dqlabcust05    | Tommy Sinaga        | Vila Permata Intan Berkilau, Blok A1/2   |
|       6 | dqlabcust06    | Irwan Setianto      | Vila Gunung Seribu, Blok O1 - No. 1      |
|       7 | dqlabcust07    | Agus Cahyono        | Vila Gunung Seribu, Blok F4 - No. 8      |
|       8 | dqlabcust08    | Maria Sirait        | Vila Bukit Sagitarius, Gang. Sawit No. 3 |
|       9 | dqlabcust09    | Ir. Ita Nugraha     | Vila Bukit Sagitarius, Gang Kelapa No. 6 |
|      10 | dqlabcust10    | Djoko Wardoyo, Drs. | Vila Bukit Sagitarius, Blok A1 No. 1     |
|      11 | dqlabcust11    | Unang Handoko       | Vila Sempilan, No. 1 - Kota B            |
|      12 | dqlabcust12    | Tommy Sinaga        | Vila Permata Intan Berkilau, Blok A1/2   |
+---------+----------------+---------------------+------------------------------------------+ 
```

Table `ms_produk`

```bash
| no_urut | kode_produk | nama_produk                        | harga  |
+---------+-------------+------------------------------------+--------+
|       1 | prod-01     | Kotak Pensil DQLab                 |  62500 |
|       2 | prod-02     | Flashdisk DQLab 64 GB              |  55000 |
|       3 | prod-03     | Gift Voucher DQLab 100rb           | 100000 |
|       4 | prod-04     | Flashdisk DQLab 32 GB              |  40000 |
|       5 | prod-05     | Gift Voucher DQLab 250rb           | 250000 |
|       6 | prod-06     | Pulpen Multifunction + Laser DQLab |  92500 |
|       7 | prod-07     | Tas Travel Organizer DQLab         |  48000 |
|       8 | prod-08     | Gantungan Kunci DQLab              |  15800 |
|       9 | prod-09     | Buku Planner Agenda DQLab          |  92000 |
|      10 | prod-10     | Sticky Notes DQLab 500 sheets      |  55000 |
+---------+-------------+------------------------------------+--------+ 
```

# Mengambil Seluruh Kolom dalam suatu Tabel

“Untuk mengakses data di database, kita dapat menggunakan SELECT statement. Pada SELECT statement kita menyatakan kolom - kolom mana saja yang ingin kita tampilkan dari suatu tabel di database. SELECT statement tidak berdiri sendiri. Setelah menyatakan kolom - kolom yang ingin ditampilkan, kita melanjutkan dengan FROM. Di FROM inilah kita menyatakan dari tabel mana data yang ingin kita tampilkan berada. SELECT… FROM… adalah statement paling sederhana di SQL, dan merupakan bagian utama dari query. Kita tidak bisa meng-query data tanpa menggunakan statement ini,” jelas Senja.

Senja juga menunjukkan padaku Query dasar dan sederhana perintah SELECT yang berfungsi untuk menampilkan seluruh kolom, sebagai berikut:

![Select_From](img/select-from.png)

- Kata awal, yaitu `SELECT` digunakan untuk menginformasikan kepada sistem bahwa kita ingin mengambil data. 
- Tanda `* (bintang)` artinya seluruh kolom perlu diambil dari tabel yang dirujuk. Tanda ini sering juga disebut sebagai wildcard.
- `FROM [NAMA_TABLE]`, artinya table yang akan diambil datanya.
- Tanda `; (titik koma)` adalah tanda yang menyatakan akhir dari perintah SELECT atau SQL lain.

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/2-Fundamental-SQL-using-SELECT-Statement/3-Penggunaan-Perintah-SELECT-FROM/MengambilSeluruhKolom.sql) | Mengambil Seluruh Kolom |

# Mengambil Satu Kolom dari Tabel
Aku sudah cukup paham dengan penjelasan Senja tadi. Tapi, masih ada satu yang mengganjal. “Bagaimana kalau aku hanya ingin menampilkan satu kolom saja dari suatu tabel/data, Nja?”

![Ambil_Satu_Kolom](img/ambil-satu-kolom.png)

“Secara umum penggunaan perintah SELECT untuk mengambil satu kolom dinyatakan oleh sintaks berikut ini,” ujar Senja sambil menggeser layar laptopnya agar bisa kuperhatikan:

“Kita coba ya dengan menampilkan data pelanggan yang ada di database. Kita sudah menggunakan perintah SELECT sebelumnya untuk mengambil seluruh kolom. Nah, berikut adalah contoh query untuk mengambil satu kolom saja yaitu nama_produk,” tambah Senja.

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/2-Fundamental-SQL-using-SELECT-Statement/3-Penggunaan-Perintah-SELECT-FROM/MengambilSatuKolom.sql) | Mengambil Satu Kolom |

# Quiz

![Quiz](img/quiz-1.PNG)

# Mengambil Lebih dari Satu Kolom dari Tabel

Tabel ms_produk memiliki lebih dari satu kolom data. Kalau aku ingin mengambil kolom lainnya, aku hanya perlu menuliskan tiap kolom yang ingin ditampilkan dipisahkan dengan tanda koma, seperti contoh berikut untuk dua kolom.

![Ambil_Lebih_Dari_Satu_Kolom](img/ambil-lebih-dari-satu-kolom.png)

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/2-Fundamental-SQL-using-SELECT-Statement/3-Penggunaan-Perintah-SELECT-FROM/MengambilLebihDariSatuKolom.sql) | Mengambil Lebih dari Satu Kolom |

![Quiz](img/quiz-2.PNG)

# Membatasi Pengambilan Jumlah Row Data

Selain pembatasan kolom, aku bisa membatasi jumlah baris data yang diambil. Seperti yang aku pelajari di materi RDMS sebelumnya, bahwa untuk tiap produk RDBMS, caranya agak berbeda-beda. Untuk MySQL dan PostgreSQL, aku dapat menggunakan LIMIT. Secara umum syntaxnya dinyatakan sebagai berikut

![Batasi_pengambilan_data](img/batasi-pengambilan-jumlah-row-data.png)

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/2-Fundamental-SQL-using-SELECT-Statement/3-Penggunaan-Perintah-SELECT-FROM/MembatasiPengambilanJumlahRowData.sql) | Membatasi Pengambilan Jumlah Row Data |

# Quiz

![Quiz](img/quiz-3.PNG)

# Penggunaan SELECT DISTINCT statement

Untuk menghilangkan data duplikasi, aku bisa menggunakan SELECT DISTINCT statement. Dengan SELECT DISTINCT, data yang sama atau duplikat akan dieliminasi dan akan ditampilkan data yang unik saja.

![Distinct](img/distinct.png)

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/2-Fundamental-SQL-using-SELECT-Statement/3-Penggunaan-Perintah-SELECT-FROM/SelectDistinct.sql) | Select Distinct |

# Kesimpulan
Aku mengambil catatanku, dan mulai menulis apa yang aku pelajari, sebelum aku melanjutkan belajarku:

- Perintah SELECT dapat digunakan untuk menentukan apa saja kolom yang akan diambil dengan menuliskan nama-nama kolom yang diinginkan menggunakan pemisah tanda koma.
- Perintah SELECT juga dapat digunakan untuk membatasi jumlah data yang dikeluarkan. Namun untuk berbagai produk bisa berbeda penulisannya. MySQL menggunakan LIMIT untuk tujuan tersebut.
- Perintah SELECT DISTINCT dapat digunakan untuk menghilangkan duplikasi baris dalam tabel dan hanya menampilkan baris data yang unik tanpa duplikasi.