# Pendahuluan
“Sudah bisa menjawab kuis-kuisnya, Aksara?”

Aku mengangguk. Syukurlah materi baru hari ini berjalan lancar dan aku belum menemukan persoalan berarti. “Ini juga berkat kamu,” pujiku tulus.

“Baiklah, kamu tentu tahu kenapa saya cukup ‘ngebut’ mengajarimu banyak hal minggu ini. Soalnya dari atasan sudah menyiapkan mini proyek untuk kamu. Untuk mengerjakan proyek ini kamu perlu menguasai kompetensi dari materi yang diajarkan sepanjang minggu.”

Ini bukan kali pertama aku diberi proyek setelah pembelajaran berakhir. Tapi, tetap saja tiap kali mendengarnya berhasil bikin aku tegang. Seperti biasa, aku tetap menyanggupi.

“Sekarang istirahat saja dulu, Aksara. Sebentar lagi jam makan siang. Aku akan mengirim detail proyeknya melalui email. Nanti bisa langsung dikerjakan ya, tenggat waktunya besok siang,” tambah Senja sembari mengedipkan satu matanya padaku saat mengatakan tenggat waktu.

Dan, email berisi mini proyek itu pun mampir ke kotak masuk kurang dari setengah jam sesudahnya:

- Project INNER JOIN, dan
- Project UNION.

Akupun membuka project pertama (INNER JOIN).

# Project INNER JOIN
Dalam database, terdapat tabel ms_pelanggan yang berisi data - data pelanggan yang membeli produk dan tabel tr_penjualan yang berisi data transaksi pembelian di suatu store.

Suatu hari, departemen marketing & promotion meminta bantuan untuk meng-query data-data pelanggan yang membeli produk Kotak Pensil DQLab, Flashdisk DQLab 32 GB, dan Sticky Notes DQLab 500 sheets.

Buatlah query menggunakan tabel ms_pelanggan dan tr_penjualan untuk mendapatkan data - data yang diminta oleh marketing yaitu kode_pelanggan, nama_customer, alamat.

NB: Gunakan SELECT DISTINCT untuk menghilangkan duplikasi, jika diperlukan.

`Tabel ms_pelanggan`

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

`Tabel tr_penjualan`

```bash
+----------------+----------------+---------+-------------+-------------------------------+------+--------+
| kode_transaksi | kode_pelanggan | no_urut | kode_produk | nama_produk                   | qty  | harga  |
+----------------+----------------+---------+-------------+-------------------------------+------+--------+
| tr-001         | dqlabcust07    |       1 | prod-01     | Kotak Pensil DQLab            |    5 |  62500 |
| tr-001         | dqlabcust07    |       2 | prod-03     | Flash disk DQLab 32 GB        |    1 | 100000 |
| tr-001         | dqlabcust07    |       3 | prod-09     | Buku Planner Agenda DQLab     |    3 |  92000 |
| tr-001         | dqlabcust07    |       4 | prod-04     | Flashdisk DQLab 32 GB         |    3 |  40000 |
| tr-002         | dqlabcust01    |       1 | prod-03     | Gift Voucher DQLab 100rb      |    2 | 100000 |
| tr-002         | dqlabcust01    |       2 | prod-10     | Sticky Notes DQLab 500 sheets |    4 |  55000 |
| tr-002         | dqlabcust01    |       3 | prod-07     | Tas Travel Organizer DQLab    |    1 |  48000 |
| tr-003         | dqlabcust03    |       1 | prod-02     | Flashdisk DQLab 64 GB         |    2 |  55000 |
| tr-004         | dqlabcust03    |       1 | prod-10     | Sticky Notes DQLab 500 sheets |    5 |  55000 |
| tr-004         | dqlabcust03    |       2 | prod-04     | Flashdisk DQLab 32 GB         |    4 |  40000 |
| tr-005         | dqlabcust05    |       1 | prod-09     | Buku Planner Agenda DQLab     |    3 |  92000 |
| tr-005         | dqlabcust05    |       2 | prod-01     | Kotak Pensil DQLab            |    1 |  62500 |
| tr-005         | dqlabcust05    |       3 | prod-04     | Flashdisk DQLab 32 GB         |    2 |  40000 |
| tr-006         | dqlabcust02    |       1 | prod-05     | Gift Voucher DQLab 250rb      |    4 | 250000 |
| tr-006         | dqlabcust02    |       2 | prod-08     | Gantungan Kunci DQLab         |    2 |  15800 |
+----------------+----------------+---------+-------------+-------------------------------+------+--------+
```

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/4-Fundamental-SQL-using-INNER-JOIN-and-UNION/4-Mini-Project/ProjectInnerJoin.sql) | Project Inner Join |

# Project UNION
Persiapkanlah data katalog mengenai mengenai nama - nama produk yang akan dijual di suatu store. Data tersebut akan digunakan dalam meeting untuk mereview produk mana saja yang akan dilanjutkan penjualannya dan mana yang tidak akan dilanjutkan.

Siapkan hanya data produk dengan harga di bawah 100K untuk kode produk prod-1 sampai prod-5; dan dibawah 50K untuk kode produk prod-6 sampai prod-10, tanpa mencantumkan kolom no_urut.

Saat mengecek data produk di database, terdapat 2 tabel yang sama - sama berisi data katalog, yaitu:

`Tabel ms_produk_1`

```bash
+---------+-------------+--------------------------+--------+
| no_urut | kode_produk | nama_produk              | harga  |
+---------+-------------+--------------------------+--------+
|       1 | prod-01     | Kotak Pensil DQLab       |  62500 |
|       2 | prod-02     | Flashdisk DQLab 64 GB    |  55000 |
|       3 | prod-03     | Gift Voucher DQLab 100rb | 100000 |
|       4 | prod-04     | Flashdisk DQLab 32 GB    |  40000 |
|       5 | prod-05     | Gift Voucher DQLab 250rb | 250000 |
+---------+-------------+--------------------------+--------+
```

`Tabel ms_produk_2`

```bash
+---------+-------------+------------------------------------+-------+
| no_urut | kode_produk | nama_produk                        | harga |
+---------+-------------+------------------------------------+-------+
|       6 | prod-06     | Pulpen Multifunction + Laser DQLab | 92500 |
|       7 | prod-07     | Tas Travel Organizer DQLab         | 48000 |
|       8 | prod-08     | Gantungan Kunci DQLab              | 15800 |
|       9 | prod-09     | Buku Planner Agenda DQLab          | 92000 |
|      10 | prod-10     | Sticky Notes DQLab 500 sheets      | 55000 |
+---------+-------------+------------------------------------+-------+
```

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/4-Fundamental-SQL-using-INNER-JOIN-and-UNION/4-Mini-Project/ProjectUnion.sql) | Project Union |


# Hasil Belajarku
Wah, tidak terasa aku telah menyelesaikan modul Fundamental SQL Using INNER JOIN and UNION. Selama belajar dengan modul ini, aku sudah dapat memahami dan mampu mempraktikkan:

- Penggabungan dua tabel dengan menggunakan WHERE clause dan teknik cross join.
- Penggabungan dua tabel relasi dengan menggunakan INNER JOIN.
- Penggabungan dua tabel secara vertikal dengan menggunakan UNION.
- Mengerjakan mini project yang merupakan integrasi keseluruhan materi dan tentunya materi-materi pada modul-modul sebelumnya untuk menyelesaikan persoalan bisnis.

Dengan kemampuan ini, aku lebih pede untuk mengolah data dengan SQL. Keterampilan ini sendiri adalah 60% aktivitas awal yang akan dilakukan seorang analis. Keep Fighting!