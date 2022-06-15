# Pendahuluan
Perulangan atau looping merupakan salah satu elemen atau fungsi yang bisa dikatakan sangat menunjang untuk kebutuhan programming dan data science.

Ambil contoh, seandainya kita harus memproses 1000x eksekusi code. Tentu akan menghabiskan waktu bila kita harus menulis ulang kode tersebut sebanyak 1000x juga.

Selain tidak bersifat scalable, efisiensi akan mempengaruhi performa dari program yang kita buat. Seperti pada umumnya pada python juga memiliki fungsi for dan while untuk melakukan looping. Logikanya hampir sama, namun hanya berbeda dalam penulisannya jika kamu sudah terbiasa dengan C ataupun Java.

# while
Struktur while pada python tidak berbeda jauh dengan bahasa pemrograman lainnya. Lebih sederhananya, struktur penulisan python membuat dia mudah untuk dibaca.

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python%20Fundamental%20for%20Data%20Science/4-Perulangan/1-while/While.py) | While |

# For
Struktur looping for pada python berbeda dengan struktur for pada umumnya. Pastikan untuk memperhatikan hal ini dengan baik.

Maksud dari fungsi for i in range (1,6) adalah, jika kita konversi pada JAVA atau C sama dengan for(i=1;i<6i++). Jika dikonversi menjadi kalimat maka akan menjadi “perulangan dimulai dari nilai i = 1 hingga nilai i kurang dari 6 dimana setiap kali perulangan nilai i akan selalu ditambah 1”. Jika nilai i sudah mencapai 6 perulangan akan dihentikan.

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python%20Fundamental%20for%20Data%20Science/4-Perulangan/2-for/For.py) | For |

# for (2) with access element
Keunikan lain dari looping dengan python adalah selain bahasa yang mudah dimengerti, kita juga bisa mengakses elemen yang terdapat pada sebuah list.

# Tugas Praktek

- Buatlah sebuah program yang bisa mengeluarkan angka 1 sampai 10.
- Tampilan akan menunjukan "Angka ganjil 1" untuk angka ganjil dan "Angka genap 2" untuk angka genap. (Menggunakan looping for)

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python%20Fundamental%20for%20Data%20Science/4-Perulangan/3-for-with-access-element/TugasPraktek.py) | Tugas Praktik |