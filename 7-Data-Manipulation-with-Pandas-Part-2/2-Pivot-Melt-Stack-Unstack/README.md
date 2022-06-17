# Pendahuluan

Pendahuluan
Kotak masuk email-ku tak hentinya menerima sejumlah link baru dari Andra untuk bab-bab yang akan kupelajari di modul Pandas part 2 ini. Banyak sekali referensi dari Andra!

“Pivot, Melt, Stack, dan Unstack, apa ini?” gumamku sendiri membaca subject email Andra.

Aku pun bergegas mengaksesnya:

Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html

Melakukan format ulang pada dataset itu sangatlah penting, biasanya hal ini dilakukan untuk mengetahui keseluruhan data secara cepat dengan chart atau visualisasi. Untuk orang yang sudah mahir menggunakan spreadsheet pastilah tau banyak tentang fitur pivot ini.

Di Pandas, ada beberapa teknik untuk melakukan pivot atau unpivot yang biasa disebut as melt di Pandas, terdapat pula konsep stack yang artinya menumpuk data dengan kolom yang lebih sedikit (stack) sama seperti konsep melt dan ada pula yang memperluas data dengan kolom yang lebih banyak (unstack) sama seperti konsep pivot.

# Dataset
Untuk memahami konsep pivot, melt, stack, dan unstack pada Pandas mari persiapkan dataset sederhana terlebih dahulu.

![Contoh_Dataset](img/code-dataset.png)

dengan output:

![Output_Dataset](img/output-dataset.png)

Tugas Praktek:

Carilah unique records/value pada keempat kolom dataframe 'data'.

![Output_Tugas_Praktek](img/output-tugas-praktek.png)

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/2-Pivot-Melt-Stack-Unstack/Dataset.py) | Dataset |

# Pivot
Untuk menerapkan menerapkan method .pivot() pada dataframe dapat dilakukan pada dataframe yang memiliki index tunggal ataupun index-nya adalah multi index. 

Untuk dataset yang masih sama, yaitu `data`.

![Dataset](img/dataset-pivot.png)

`Pivoting` dengan `single column` measurement.

![Pivoting_Single_Column](img/pivoting-dengan-single-column.png)

dengan output:

![Output_Pivoting_Single_Column](img/output-pivoting-single-column.png)

`Pivoting` dengan `multiple column` measurement.

![Pivoting_Multiple_Column](img/pivoting-multiple-column.png)

dengan output:

![Output_Pivoting_Multiple_Column](img/output-pivoting-multiple-column.png)

Penjelasan:

Apa yang berbeda dari kedua code di atas? Pada code pertama di specify values mana yang akan dilakukan pivot sedangkan di kedua tidak specific mana yang akan dilakukan pivot maka Pandas secara default men-treat kolom yang ada selain yang telah di specify as index dan columns as values instead.

Tugas Praktik:

Ketikkanlah kembali kode-kode yang diberikan di atas agar dapat lebih memahami konsep pivoting yang telah diberikan.

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/2-Pivot-Melt-Stack-Unstack/Pivot.py) | Pivot |

# Pivot_table
Apa yang terjadi kalau output pivot tabel memiliki duplicate index? Seperti yang diketahui, index di dataframe adalah unique identifier untuk setiap row, jadi tidak boleh ada duplikat dan setiap membuat pivot tabel, harus specify index as kolom yang mana dan columns-nya memakai kolom yang mana.

Perhatikan contoh yang diilustrasikan berikut ini!

![Dataset](img/contoh-dataset-pivot-table.png)

dengan output:

![Output_pivoting](img/output-pivoting.png)

Hal ini dapat diatasi dengan melakukan method .pivot_table() pada dataframe. Metode ini sama seperti melakukan pivot pada tabel tapi juga melakukan groupby dan aggregation (aggfunc) pada level rows sehingga dipastikan tidak ada duplicate index di rows (secara default aggfunc = 'mean').

Perhatikan cuplikan berikut ini!

![Menggunakan_Pivot_Table](img/menggunakan-pivot-table.png)

dengan output:

![Output_Pivot_Table](img/output-pivot-table.png)

Keyword `aggfunc` yang digunakan pada method `.pivot_table()` dapat menggunakan nilai berikut:

- sum
- 'mean'
- 'median'
 
Tugas Praktek:

Seperti yang dicontohkan untuk meng-create pivot tabel dengan method .pivot_table() tetapi aggfunc yang digunakan adalah 'mean' dan 'median'.

![Output_Tugas_Praktek_Pivot_Table](img/output-tugas-praktek-pivot-table.png)

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/2-Pivot-Melt-Stack-Unstack/PivotTable.py) | Pivot Table |

# Melt - Part 1
Teknik melt melalui `pd.melt()` digunakan untuk mengembalikan kondisi data yang sudah dilakukan pivot menjadi sebelum pivot.

Mari diperhatikan kembali dataframe yang telah digunakan sebelumnya dan dataframenya sudah di pivot.

![Dataframe](img/dataframe-melt-1.png)

dengan bentuk dataframe dari output baris ke-11.

![Output_dataframe](img/output-dataframe-melt-1.png)

Akan melakukan teknik melting pada dataframe output di atas.

`[1] Melting` dataframe

![Melting_dataframe](img/melting-dataframe.png)

yang menghasilkan output:

![Output_Melting_Dataframe](img/output-melting-dataframe.png)

`[2] Dengan menspesifikasi keyword argument id_vars` yang ditujukan untuk membuat fix kolom yang sebagai id tiap barisnya.

![Melting_dataframe_2](img/melting-dataframe-2.png)

dengan output:

![Output_Melting_Dataframe_2](img/output-melting-dataframe-2.png)

Tugas Praktek:

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/2-Pivot-Melt-Stack-Unstack/MeltPart1.py) | Melt |

# Melt - Part 2
Mari melanjutkan ke bagian kedua dari penggunaan teknik melt ini. Mari lihat kembali dataframe yang telah diperoleh melalui pivoting

![Dataframe_melt_2](img/dataframe-melt-2.png)

dengan bentuk dataframe dari output baris ke-11.

![Output_dataframe_melt_2](img/output-dataframe-melt-2.png)

Lanjutkan dengan melakukan teknik melting pada dataframe output di atas untuk keyword argumen lainnya, yaitu

`[3] Dengan menspesifikasikan keyword argument value_vars` yang digunakan untuk menampilkan variasi value apa saja yang perlu dimunculkan di kolom variable. 

![Melting_Value_Vars](img/melting-value-vars.png)

dengan output:

![Output_Melting_Value_Vars](img/output-melting-value-vars.png)

`[4] Dengan spesifikasikan keyword argument var_name dan value_name` yang digunakan untuk menampilkan nama kolom untuk variable dan value.

![Melting_Value_Name](img/melting-value-name.png)

dengan output:

![Output_Melting_Value_Name](img/output-melting-value-name.png)

Tugas Praktik:

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/2-Pivot-Melt-Stack-Unstack/MeltPart2.py) | Melt |

# Stack & Unstack - Part 1
Konsep `stacking` dan `unstacking` sama dengan `melt dan pivot secara berurutan`, hanya saja tidak memasukkan index sebagai parameter di stack/unstack tapi harus set index terlebih dahulu, baru bisa melakukan stacking/unstacking dengan level yang bisa ditentukan sendiri.

Perhatikan kembali dataframe berikut dengan multi index-nya.

![Dataframe_Stack_Unstack](img/dataframe-stack-unstack-1.png)

dengan output:

![Output_Dataframe_Stack_Unstack_1](img/output-dataframe-stack-unstack-1.png)

Mari terapkan bagaimana menggunakan teknik stacking dan unstacking ini pada dataframe multi index 'data':

`[1]` Unstacking dataframe

![Unstacking](img/unstacking-dataframe-1.png)

dengan output:

![Output_Unstacking](img/output-unstacking-dataframe-1.png)

`[2]` Unstacking dengan specify level name

![Unstacking_2](img/unstacking-2.png)

dengan output:

![Output_Unstacking_2](img/output-unstacking-2.png)

`[3]` Unstacking dengan specify level position

![Unstacking_3](img/unstacking-3.png)

dengan output:

![Output_Unstacking_3](img/output-unstacking-3.png)

Tugas Praktek:

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/2-Pivot-Melt-Stack-Unstack/StackAndUnstackPart1.py) | Stack dan Unstack |


# Stack & Unstack - Part 2
Dalam bagian kedua dari Stack & Unstack ini akan membahas stacking dataframe. Untuk itu, mari diperhatikan dataframe berikut ini:

![Dataframe_Unstack_Part_2](img/dataframe-unstack-part-2.png)

dengan dataframe yang dicetak pada langkah ke-11.

![Output_Dataframe_Unstack_Part_2](img/output-dataframe-unstack-part-2.png)

`[1]` Stacking dataframe 

![Stacking_Dataframe](img/stacking-dataframe-1.png)

dengan output:

![Output_Stacking_Dataframe](img/output-stacking-dataframe-1.png)

`[2]` Tukar posisi index setelah stacking dataframe

![Tukar_posisi_index](img/tukar-posisi-index.png)

dengan output:

![Output_tukar_posisi_index](img/output-tukar-posisi-index.png)

`[3]` Melakukan sort_index pada stacking dataframe

![Sort_index](img/sort-index.png)

dengan output:

![Output_sort_index](img/output-sort-index.png)

Tugas Praktik:

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/2-Pivot-Melt-Stack-Unstack/StackAndUnstackPart2.py) | Stack dan Unstack |

# Quiz

![Quiz_1a](img/quiz-1a.PNG)

![Quiz_1b](img/quiz-1b.PNG)

![Quiz_1c](img/quiz-1c.PNG)