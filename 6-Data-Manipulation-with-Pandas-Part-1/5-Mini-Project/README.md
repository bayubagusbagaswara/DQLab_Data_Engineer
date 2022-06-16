# Pendahuluan
“Ndra, aku sudah cukup paham dengan teorinya,” sahutku seakan memberi kode jika aku sudah siap mengerjakan proyek yang tadi dijanjikan.

“Saya suka kepercayaan dirimu, Aksara. Kalau begitu, sudah siap kalau diberi proyek?” pancing Andra.

Aku mengangguk mantap.

“Oke, untuk proyek pertama, kamu akan melakukan ETL sebelum analisis data. Karena data yang dibutuhkan masih belum bersih, sehingga tidak bisa dilakukan analisis lebih lanjut.”

Aku menyimak pemaparan dari Andra sembari memikirkan solusi untuk ETL. Tentunya bisa aku eksekusi dengan Pandas. “Baik, Ndra. Data yang dibutuhkan apa saja nantinya?”

“Data untuk cabang perusahaan ritel kita, Aksara. Berarti kumpulan data bulan Januari 2019 untuk setiap kota dan provinsi, tanggal order-nya, customer, order-nya apa aja terkait brand, product, quantity dan item price-nya juga. Dan, yang terakhir adalah GMV/Gross Merchandise Volume (total price)-nya.”

“Banyak banget!” gumamku dalam hati.

“Saya tahu kamu pasti sudah memikirkan detlennya karena data yang dibutuhkan banyak. Jangan khawatir, saya beri tenggat waktu sampai akhir minggu ini, bukan besok. Cukup?”

Aku mengangkat ibu jari, “Langsung aku cicil dari sekarang deh, Ndra.”

“Baik, selamat bekerja Aksara!”


# Project dari Andra
Berikut adalah isi email yang ditugaskan oleh Andra:

Diberikan dataset ‘retail_raw_test.csv’

1. Baca dataset
2. Tipe data diubah menjadi tipe yang seharusnya
    - customer_id dari string ke int64,
    - quantity dari string ke int64,
    - item_price dari string ke int64
3. transform product_value supaya bentuknya seragam dengan format PXXXX, assign ke kolom baru "product_id", dan drop kolom "product_value", jika terdapat nan gantilah dengan "unknown".
4. transform order_date menjadi value dengan format YYYY-mm-dd
5. cek data hilang dari tiap kolom dan kemudian isi missing value
    - di brand dengan "no_brand", dan
    - cek dulu bagaimana missing value di city & province - isi missing value di city dan province dengan "unknown"
6. create column city/province dari gabungan city & province
7. membuat index berdasarkan city_provice, order_date, customer_id, order_id, product_id (cek index)
8. membuat kolom "total_price" sebagai hasil perkalian quantity dengan item_price
9. slice data hanya untuk Jan 2019

Notes :

Dataset :  https://storage.googleapis.com/dqlab-dataset/retail_raw_test.csv

Preview akhir data:

![Preview](img/preview-tugas-praktek.png)

Jawaban :

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/6-Data-Manipulation-with-Pandas-Part-1/5-Mini-Project/Project.py) | Project |

# Evaluasi Andra untuk Project yang Telah Disubmit

Aku baru saja mengumpulkan hasil kerja dari proyek pertamaku pada Andra. Lebih cepat satu hari dari tenggat waktu yang diberikan, semoga hasilnya juga memuaskan! Doaku dalam hati.

“Aksara, saya baru saja meninjau pekerjaanmu. Saya ada pertanyaan,” ujar Andra yang lagi-lagi sudah ada di sebelahku. Sepertinya Andra punya kemampuan teleportasi yang bisa muncul tiba-tiba.

“Ada yang salah, Ndra?”

“Saya ingin tahu alasanmu mengapa di langkah ketiga, kamu cari tahu terlebih dulu nilai null. Mengapa tidak kamu convert to string secara langsung?”

“Soalnya, kalau aku cek di df.info()nya masih ada yang kosong di kolom ‘product_value’, Ndra.  Kalau aku langsung convert to string, nantinya value NaN akan berubah menjadi string ‘nan’, kemudian ketika aku pad 0 di depan dan concat dengan char ‘P’, hasilnya akan menjadi ‘P0nan’ yang aneh sekali, Ndra,” jelasku.

“Oke. Satu lagi pertanyaanku, Aksara. Kenapa kamu memakai langkah ke-4? Mengapa tidak langsung menggunakan kolom date yang sudah ada. Bukankah format waktunya sudah ideal?”

Aku merasa tanya jawab ini tampak seperti ujian apakah aku benar-benar memahami cara kerja Pandas. Aku memantapkan diri untuk memberi jawaban, “Tidak semua format datetime yang ideal pada umumnya akan ideal di dalam pandas environment. Seenggaknya harus translate dulu menjadi format yang ideal di dalam pandas sehingga pandas bisa mengenali.”

“Great! Untuk materi dan proyek ini, kamu dinyatakan lulus, Aksara.”

Mendengar apresiasi ini langsung dari Andra membuat hatiku hangat. Senang sekali rasanya!

# Hasil Belajarku :)

Walau harus bekerja keras, aku cukup puas dengan hasil kerjaku hari ini. Aku memandangi kode final yang sudah selesai kukerjakan. Diam-diam ada perasaan bangga menyelip di benakku! YES!

Akhirnya, aku telah menyelesaikan modul Data Manipulation with Pandas - Part 1. Materi-materi yang telah kupelajari dan praktikkan dalam modul ini aku telah mendapatkan pengetahuan (knowledge) dan praktek (skill) untuk:
    - Memahami library Pandas dan interaksinya dengan numpy
    - Memahami dan mempraktekkkan bagaimana membuat series dan dataframe pada pandas dari berbagai tipe data seperti list, list of list, dict, ataupun numpy array
    - Memahami dan mempraktekkkan bagaimana membaca dataset dari berbagai format standar seperti csv, tsc, excel, json, sql sehingga dapat dijadikan pandas dataframe/series serta bagaimana cara menyimpannya ke format standar dataset.
    - Mampu memahami dan mempraktikkan proses indexing, transformasi, dan slicing pada dataframe
    - Mampu memahami dan mempraktikkan bagaimana cara melakukan handle missing value pada suatu dataframe
    - Latihan dalam mengerjakan project bisnis sederhana menggunakan pandas

Semangat!