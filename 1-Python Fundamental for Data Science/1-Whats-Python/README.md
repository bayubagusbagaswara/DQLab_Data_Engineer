# Pendahuluan Tentang Python

Python merupakan bahasa pemrograman yang diciptakan pada tahun 1991 oleh Guido van Russom, seorang matematikawan.

Saat ini python merupakan bahasa pemrograman populer. Kondisi ini dibuktikan dengan hasil beberapa survey terkait bahasa pemrograman yang sering dicari melalui mesin pencari google. Python berhasil naik dengan melonjak tajam semenjak kelahirannya bahkan saat ini telah mengungguli Java. Menurut insight developer survey dari stackoverflow pada tahun 2018 atau melalui TIOBE Index, Python berhasil naik pada TOP 10 programming language yang paling dicari menggungguli seniornya, C, PHP, dan C#.

Python dapat dikatakan sebagai programming language dengan perkembangan tercepat. Perkembangan ini didukung oleh library atau pustaka python yang cukup melimpah. Libraries (pustaka-pustaka) python ini dikontribusikan oleh akademisi dari berbagai universitas di seluruh dunia serta developer dari perusahaan IT ternama seperti Google, Facebook, Microsoft, Apache Software Foundation, dan perusahaan lainnya. Dengan demikian, hal inilah yang menjadikan python sebagai salah satu programming language yang solid dan berkembang pesat.

Python sendiri berguna dalam berbagai aspek :

- Web Development (Server – Side)
- Software Development
- Mathematics
- Scripting
- Data Science
- Bisa mengelola Big Data dan Rumus matematika yang complex
- Cocok untuk riset dan rapid prototype suatu product dan launch hingga produksi
- CRUD sebuah file dan database

Kepopuleran python sendiri sekarang ada pada track data science. Banyaknya library dan framework seperti scikit-learn, tensorflow/keras, pytorch membuat para pecinta data mining, AI, dan Machine learning lebih menyukai python untuk pengembangan riset dan penelitian mereka. Berkembangnya dunia data science didunia ini juga salah satu alasan kenapa python menjadi begitu populer sekarang.

![Manfaat_Python](img/1-manfaat-python.PNG)

# Mengapa Python Populer
Meningkatnya minat masyarakat dunia terhadap data science menyebabkan penggunaan Python menjadi sangat populer. Python merupakan salah satu programming language yang cocok untuk scripting dan bisa berjalan dalam berbagai platform OS dan IoT. Meskipun tergolong sebagai high level programming language, python sangat mudah dimengerti karena syntax-nya yang sederhana. Jika diperhatikan, python sangat mirip penulisannya dengan bahasa Inggris.

Python dapat digunakan dalam paradigma pemrograman fungsional dan berorientasi object (OOP - object oriented programming). Berbeda dengan C, C++, dan Java yang berjenis kompilasi, Python merupakan bahasa pemrograman berjenis interpretasi yang artinya code yang sudah ditulis bisa dijalankan sesegera mungkin.

Beberapa hal yang menjadi kelebihan dari python:

- Python dirancang untuk mudah ditulis dan dibaca, serta memiliki beberapa kesamaan dengan bahasa Inggris dengan pengaruh dari matematika.
- Python menggunakan baris baru untuk mengakhiri perintah, dibandingkan dengan bahasa pemrograman lain yang sering menggunakan titik koma atau tanda kurung.
- Python bergantung pada indentasi, menggunakan spasi, untuk mendefinisikan ruang lingkup; seperti lingkup loop, fungsi, dan kelas. Bahasa pemrograman lainnya sering menggunakan kurung kurawal untuk tujuan ini
- Jika kalian mencari di internet tentang programming python, biasanya akan ada 2 jenis python, python 2 dan python 3. Versi utama Python yang paling baru adalah Python 3 dan digunakan dalam platform academy ini. Saat ini, python 2 sudah memasuki end-of-life pada Januari 2020.

![Python_Populer](img/2-python-populer.PNG)

# Code Hello World
Struktur code pada Python relatif sangat sederhana, tidak serumit seperti pada Java ataupun C. Selain karena memang mudah dibaca, python juga termasuk pada high level programming language seperti yang telah dibahas sebelumnya

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python%20Fundamental%20for%20Data%20Science/1-Whats-Python/1-code-hello-world/HelloWorld.py) | Code Hello World |

# Comment Pada Python
Ketika menuliskan suatu kode program diperlukan sebuah dokumentasi. Mengapa dokumentasi ini sangat penting? Sederhananya, jika kode yang telah dituliskan memiliki ribuan baris dan ada beberapa bagian yang perlu diperbaiki karena suatu alasan, para penulis kode cukup melihat dokumentasinya saja. Penulis kode tidak perlu membaca dan memahami seluruh isi code dari awal. Nah, salah satu metode yang biasa digunakan adalah menggunakan comment. Sama dengan Bahasa R, python juga menggunakan tanda “#” untuk membuat comment pada script.

Perlu diketahui, comment tidak akan pernah tampil pada hasil melalui console atau GUI. Fungsi comment dapat dikatakan sebagai sebuah penanda. Kenapa bab ini diberikan diawal? Harapannya yaitu agar kamu memiliki pengetahuan dan langsung mempraktikkannya ketika kamu menuliskan baris kode program berikut dengan dokumentasinya. 

Dokumentasi kode juga berlaku untuk variable karena diperlukan suatu keterangan bahwa variable berfungsi sebagai apa dan isinya apa. Maka dari itu jangan lupa untuk membuat dan memberi comment untuk setiap kode program yang telah kamu tuliskan!

| Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python%20Fundamental%20for%20Data%20Science/1-Whats-Python/2-comment-pada-python/Comment.py) | Comment Pada Python |

# Variable, Basic Data Type and Print
Penggunaan variabel atau suatu objek yang bisa merepresentasikan sebuah nilai atau value sangat penting dalam bahasa pemrograman. Selain itu mempermudah dalam membaca source code, pemberian variable yang efisien juga akan membuat code berjalan optimal dan dinamis. Pada sesi kali ini kita akan belajar bagaimana cara inisialisasi variable dalam beberapa data type dan menampilkannya (print).

| Tipe Data | Contoh | Penjelasan |
|:---------:|:------:|:----------:|
| Boolean | True atau False | Menyatakan benar True yang bernilai 1, atau salah False yang bernilai 0 |
| String | "Ayo belajar Python" | Menyatakan karakter/kalimat bisa berupa huruf angka, dll (diapit tanda " atau ') |
| Integer | 25 atau 1209 | Menyatakan bilangan bulat |
| Float | 3.14 atau 0.99| Menyatakan bilangan yang mempunyai koma |
| List | ['xyz', 786, 2.23] | Data untaian yang menyimpan berbagai tipe data dan isinya bisa diubah-ubah |
| Tuple | ('xyz', 768, 2.23) | Data untaian yang menyimpan berbagai tipe data tapi isinya tidak bisa diubah |
| Dictionary | {'nama': 'adi','id':2} | Data untaian yang menyimpan berbagai tipe data berupa pasangan penunjuk dan nilai |