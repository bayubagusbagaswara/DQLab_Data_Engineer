Di masa pandemi seperti ini, kompetisi coding seperti Competitive Programming maupun Hackathon banyak diselenggarakan karena sangat memungkinkan untuk dilakukan secara online.

Hackathon merupakan kompetisi membuat perangkat lunak (software) yang dilaksanakan secara marathon yang biasanya diikuti secara tim. Umumnya, peserta hackathon diminta untuk mengembangkan platform (mobile, web, desktop, dll.) dalam kurun waktu tertentu untuk menyelesaikan permasalahan yang sudah ditetapkan/didefinisikan oleh penyelenggara ataupun berdasarkan tema yang dipilih oleh tim tersebut.

Untuk bisa mengikuti hackathon dari suatu instansi, calon peserta diwajibkan untuk mendaftarkan diri mereka pada situs/form tertentu dengan memasukkan beberapa informasi yang diminta oleh penyelenggara tersebut.
 

Extract, Transform dan Load (ETL) merupakan kumpulan proses untuk "memindahkan" data dari satu tempat ke tempat lain.
Tempat yang dimaksud adalah dari sumber data (bisa berupa database aplikasi, file, logs, database dari 3rd party, dan lainnya) ke data warehouse.

Apa itu data warehouse?

Singkatnya, data warehouse merupakan database yang berisi data-data (tabel-tabel) yang sudah siap untuk dilakukan analisis oleh Data Analyst maupun Data Scientist.

Lebih lengkapnya bisa dilihat di:
https://en.wikipedia.org/wiki/Data_warehouse.

Pada modul ini kita akan mempelajari masing-masing dari proses tersebut.

# Project yang Akan Dikerjakan
Pada proyek kali ini, Anda diminta untuk mengolah data pendaftar hackathon yang diselenggarakan oleh DQLab bernama DQThon.

Dataset ini terdiri dari 5000 baris data (5000 pendaftar) dengan format CSV (Comma-separated values) dan memiliki beberapa kolom diantaranya:

- participant_id: ID dari peserta/partisipan hackathon. Kolom ini bersifat unique sehingga antar peserta pasti memiliki ID yang berbeda
- first_name: nama depan peserta
- last_name: nama belakang peserta
- birth_date: tanggal lahir peserta
- address: alamat tempat tinggal peserta
- phone_number: nomor hp/telepon peserta
- country: negara asal peserta
- institute: institusi peserta saat ini, bisa berupa nama perusahaan maupun nama universitas
- occupation: pekerjaan peserta saat ini
- register_time: waktu peserta melakukan pendaftaran hackathon dalam second

Namun pada proyek ini nantinya Anda diminta untuk menghasilkan beberapa kolom dengan memanfaatkan kolom-kolom yang ada, sehingga akhir dari proyek ini berupa hasil transformasi data dengan beberapa kolom baru selain dari 10 kolom diatas.

Sebagai pemanasan dalam proyek ini, Anda dipersilakan untuk membuka isi datasetnya dan melihat values-nya. Jika sudah siap dengan perjalanan di proyek ini, silakan klik Next.

# Transform
Transform merupakan proses melakukan transformasi data, atau perubahan terhadap data. Umumnya seperti:

1. Merubah nilai dari suatu kolom ke nilai baru,
2. Menciptakan kolom baru dengan memanfaatkan kolom lain,
3. Transpose baris menjadi kolom (atau sebaliknya),
4. Mengubah format data ke bentuk yang lebih standard (contohnya, kolom date, maupun datetime yang biasanya memiliki nilai yang tidak standard maupun nomor HP yang biasanya memiliki nilai yang tidak sesuai format standardnya), dan lainnya. 



# Kesimpulan
Dengan begitu, tibalah kita di penghujung dari chapter bagian transform ini.

Jika dilihat kembali, dataset Anda saat ini sudah berbeda dengan saat proses extract sebelumnya. Ada beberapa kolom tambahan yang memanfaatkan nilai kolom lain.

Dataset Anda saat ini memuat kolom:

1. participant_id: ID dari peserta/partisipan hackathon. Kolom ini bersifat unique sehingga antar peserta pasti memiliki ID yang berbeda
2. first_name: nama depan peserta
3. last_name: nama belakang peserta
4. birth_date: tanggal lahir peserta (sudah diformat ke YYYY-MM-DD)
5. address: alamat tempat tinggal peserta
6. phone_number: nomor hp/telepon peserta
7. country: negara asal peserta
8. institute: institusi peserta saat ini, bisa berupa nama perusahaan maupun nama universitas
9. occupation: pekerjaan peserta saat ini
10. register_time: waktu peserta melakukan pendaftaran hackathon dalam second
11. team_name: nama tim peserta (gabungan dari nama depan, nama belakang, negara dan institusi)
12. postal_code: kode pos alamat peserta (diambil dari kolom alamat)
13. city: kota peserta (diambil dari kolom alamat)
14. github_profile: link profil github peserta (gabungan dari nama depan, dan nama belakang)
15. email: alamat email peserta (gabungan dari nama depan, nama belakang, institusi dan negara)
16. cleaned_phone_number: nomor hp/telepon peserta (sudah lebih sesuai dengan format nomor telepon)
17. register_at: tanggal dan waktu peserta melakukan pendaftaran (sudah dalam format DATETIME)


# Load
Pada bagian load ini, data yang sudah ditransformasi sedemikian rupa sehingga sesuai dengan kebutuhan tim analyst dimasukkan kembali ke database yaitu Data Warehouse (DWH). Biasanya, dilakukan pendefinisian skema database terlebih dahulu seperti:

1. Nama kolom
2. Tipe kolom
3. Apakah primary key, unique key, index atau bukan
4. Panjang kolomnya

Karena umumnya Data Warehouse merupakan database yang terstruktur sehingga mereka memerlukan skema sebelum datanya dimasukkan.

Pandas sudah menyediakan fungsi untuk memasukkan data ke database yaitu to_sql().

Detail dari fungsi tersebut bisa dilihat pada dokumentasi Pandas: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html