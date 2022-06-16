# Pendahuluan
“Revisianmu sudah saya pelajari kembali. Hasilnya cukup memuaskan. Kamu berhasil menganalisisnya dengan tepat dan mendalam. Saya jadi tertarik untuk memberikanmu sebuah proyek,” ujar Kroma setelah mengecek satu per satu hasil revisi pekerjaanku.

Aku tidak tahu harus senang atau gugup saat ini. Proyek yang dipercayakan langsung dari Kroma? Jujur saja, aku cukup gelisah. Beragam kemungkinan menggantung di dadaku, apakah aku mampu? Aku hanya anak baru yang selama ini banyak dibimbing Senja dan dibantu Andra. 

Tanpa sadar aku terdiam lama. “Jangan khawatir. Saya yakin proyek ini sesuai dengan program belajarmu selama ini bersama Senja dan Andra. Jika ada penyesuaian dan pengembangan, hanya beberapa. Saya yakin kamu bisa melakukan improvisasi dengan baik,” lanjut Kroma.

Aku curiga atasanku ini memang bisa mendengar suara hati! Tapi mengetahui Kroma menaruh harapan dan kepercayaan padaku, aku seharusnya bangga. Dengan mengumpulkan kepercayaan diriku, aku mengiyakan proyek tersebut. 

“Baik. Lima menit lagi saya akan mengirimkan data dari cabang kita di daerah G. Tolong bersihkan saja dulu datanya, detailnya yang harus kamu lakukan akan saya arahkan juga di email.”

“Baik.”

Aku pun keluar dari ruangan. Setelah mengatur napas sejenak, aku bergegas kembali ke meja. Apalagi setelah aku mendengar notifikasi email masuk di ponselku. Dan tahu kalau itu pasti dari Kroma.

# Case Studi: Data Profiling
Dear Aksara, 

Tolong proses dataset terlampir yang  disimpan dalam bentuk csv bernama 'https://storage.googleapis.com/dqlab-dataset/uncleaned_raw.csv'.

Kamu bisa memprosesnya dengan cara berikut:

1. Import dataset csv ke variable bernama uncleaned_raw
2. Inspeksi dataframe uncleaned_raw
3. Check kolom yang mengandung missing value. Jika ada, kolom apakah itu dan berapa persen missing value pada kolom tersebut?
4. Mengisi missing value tersebut dengan mean dari kolom tersebut!

Setelah membaca email tersebut, aku pun memulai kode programnya di code editor.

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/5-Data%20Quality%20with%20Python%20for%20Beginner/3-Mini%20Project/1-case-data-profiling.py) | Case Data Profiling |

# Case Study: Data Cleansing - Part 1

Untuk memprosesnya bisa dilakukan dengan cara berikut:

5. Mengetahui kolom yang memiliki outliers! Gunakan visualisasi dengan boxplot pada dataframe uncleaned_raw.

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/5-Data%20Quality%20with%20Python%20for%20Beginner/3-Mini%20Project/2-Data-Cleansing-Part1.py) | Case Data Cleansing |

# Case Study: Data Cleansing - Part 2
Langkah selanjutnya bisa dilakukan dengan cara berikut:

6. Melakukan proses removing outliers pada kolom UnitPrice.
7. Checking duplikasi dan melakukan deduplikasi dataset tersebut!

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/5-Data%20Quality%20with%20Python%20for%20Beginner/3-Mini%20Project/3-Data-Cleansing-Part-2.py) | Case Data Cleansing |

# Penutup/Kesimpulan
Congratulations! Aku telah menyelesaikan modul Data Quality with Python for Beginner. Berdasarkan materi-materi yang diberikan Kroma yang telah kupelajari dan praktekkan dalam modul ini, aku telah mendapatkan pengetahuan (knowledge) dan praktek (skill) yang diantaranya :

- Mampu melakukan profiling data baik untuk data angka maupun teks
- Mampu membuat rule untuk data cleansing (standarisasi data, value lookup, dan treatment duplikasi data)

Keep fighting!