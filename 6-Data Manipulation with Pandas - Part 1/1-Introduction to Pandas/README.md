# Pendahuluan
“Apa kegunaan mempelajari Pandas? Aku tahunya Pandas nama hewan,” kelakarku pada Andra. Benar kan! Lagi-lagi aku menemukan istilah umum tapi punya makna berbeda di dunia data.

“Itu Panda, Aksara. Kalau Pandas berguna untuk melakukan analisis dan pengolahan data dari menengah sampai besar. Coba dibaca saja dulu modulnya biar lebih jelas. Nanti akan ada praktik yang memperjelas,” tukas Andra.

Seperti yang bisa kutebak, aku harus memahami modul dan pembelajaran baru ini sendiri. Karena kulihat Andra sudah melengang pergi setelah memberi intruksi sederhana seperti itu. Tak apa, perlahan aku terbiasa juga belajar mandiri. Walau memang lebih nyaman kalau dibimbing, hehehe.

# Memanggil Library Pandas
Pandas adalah library python open source yang biasanya digunakan untuk kebutuhan data analisis. Pandas membuat Python supaya dapat bekerja dengan data yang berbentuk tabular seperti spreadsheet dengan cara pemuatan data yang cepat, manipulasi data, menggabungkan data, serta ada berbagai fungsi yang lain.

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/6-Data%20Manipulation%20with%20Pandas%20-%20Part%201/1-Introduction%20to%20Pandas/1-memanggil-library-pandas.py) | Memanggil Library Pandas |

# DataFrame & Series
Di Pandas terdapat 2 kelas data baru yang digunakan sebagai struktur dari spreadsheet:

1. `Series`: satu kolom bagian dari tabel dataframe yang merupakan 1 dimensional numpy array sebagai basis datanya, terdiri dari 1 tipe data (integer, string, float, dll).
2. `DataFrame`: gabungan dari Series, berbentuk rectangular data yang merupakan tabel spreadsheet itu sendiri (karena dibentuk dari banyak Series, tiap Series biasanya punya 1 tipe data, yang artinya 1 dataframe bisa memiliki banyak tipe data).

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/6-Data%20Manipulation%20with%20Pandas%20-%20Part%201/1-Introduction%20to%20Pandas/2-dataframe-dan-series.py) | Dataframe dan Series |


# Atribut DataFrame & Series - Part 1

Dataframe dan Series memiliki sangat banyak atribut yang digunakan untuk transformasi data, tetapi ada beberapa attribute yang sering dipakai. Di sini series `number_list` dan dataframe `matrix_list` pada subbab sebelumnya digunakan kembali.

1. `Method .info()`

Method .info() digunakan untuk mengecek kolom apa yang membentuk dataframe itu, data types, berapa yang non null, dll. Method ini tidak dapat digunakan pada series, hanya pada dataframe saja.

![Method_Info](img/method-info.png)

Output di console untuk penggunaan method .info() ini adalah:

![Hasil_method_info](img/hasil-method-info.png)

2. `Attribute .shape`

Attribute .shape digunakan untuk mengetahui berapa baris dan kolom, hasilnya dalam format tuple (baris, kolom).

![Shape](img/shape.png)

Output di console untuk penggunaan attribute .shape ini adalah:

![Hasil_Shape](img/hasil-shape.png)

3. `Attribute .dtypes`

Attribute .dtypes digunakan untuk mengetahui tipe data di tiap kolom. Tipe data object: kombinasi untuk berbagai tipe data (number & text, etc).

![Dtypes](img/dtypes.png)

Output di console untuk penggunaan attribute .dtypes ini adalah:

![Hasil_dtypes](img/hasil-dtypes.png)

4. `Method .astype(nama_tipe_data)`

Method .astype(nama_tipe_data) untuk convert tipe data berdasarkan tipe data seperti: float, int, str, numpy.float, numpy.int ataupun numpy.datetime.

![Astype](img/astype.png)

Output di console untuk penggunaan method .astype() ini adalah:

![Hasil_astype](img/hasil-astype.png)

Tugas Praktek

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/6-Data%20Manipulation%20with%20Pandas%20-%20Part%201/1-Introduction%20to%20Pandas/3-Atribut-DataFrame-%26-Series-Part1.py) | Atribut Dataframe dan Series |

# Atribut DataFrame & Series - Part 2
Dataframe dan Series memiliki sangat banyak atribut yang digunakan untuk transformasi data, tetapi ada beberapa attribute yang sering dipakai. Di sini series number_list dan data frame matrix_list digunakan kembali.

5. `Attribute .copy()`

Attribute .copy() digunakan melakukan duplikat, untuk disimpan di variable yang berbeda mungkin supaya tidak loading data lagi.

![Copy](img/copy.png)

Output di console untuk penggunaan attribute .copy() ini adalah:

![Hasil_copy](img/hasil-copy.png)

6. `Attribute .to_list()`

Attribute .to_list() digunakan untuk mengubah series menjadi list dan tidak dapat digunakan untuk dataframe.

![To_list](img/to-list.png)

Output di console untuk penggunaan attribute .to_list() ini adalah:

![Hasil_to_list](img/hasil-to-list.png)

7. `Attribute .unique()`

Attribute .unique() digunakan menghasilkan nilai unik dari suatu kolom, hasilnya dalam bentuk numpy array. Attribute ini hanya digunakan pada series saja.

![Unique](img/unique.png)

Output di console untuk penggunaan attribute .unique() ini adalah:

![Hasil_unique](img/hasil-unique.png)

Tugas Praktek

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/6-Data%20Manipulation%20with%20Pandas%20-%20Part%201/1-Introduction%20to%20Pandas/4-Atribut-DataFrame-%26-Series-Part2.py) | Atribut Dataframe dan Series |