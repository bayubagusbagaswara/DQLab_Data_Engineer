# Pendahuluan
Teknik agregasi diperlukan ketika mau melihat dataset dengan view yang berbeda, bisa set data tersebut akan dikelompokkan seperti apa, yang kemudian juga bisa menerapkan beberapa fungsi atau metode statistik ke hasil group dataset itu untuk mengetahui behavior dari data tersebut secara summary/overview.

Basic Concept of Groupby & Aggregation

![Basic_Concept](img/basic-concept-groupby-aggregation.png)

Groupby memiliki konsep untuk:

1. `Split`: melakukan indexing/multi-indexing dengan apa yang di specify as groupby menjadi kelompok
2. `Apply`: menerapkan fungsi pada masing-masing kelompok tersebut
3. `Combine`: mengumpulkan semua hasil fungsi dari tiap kelompok kembali menjadi dataframe

# Review Inspeksi Data
Mari review kembali terkait dengan inspeksi data yang pernah dilakukan pada modul sebelumnya. Akan menggunakan dataset https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv

`[1]` Load data dari csv

![Load_Data](img/load-data-csv.png)

dengan output:

![Output_Load_Data](img/output-load-data-csv.png)

`[2]` Melakukan pengecekan terhadap data

![Cek_Data](img/cek-data.png)

dengan output:

![Output_cek_data](img/output-cek-data.png)

`[3]` Melakukan count tanpa groupby

![Count_Data](img/count-tanpa-groupby.png)

dengan output:

![Output_count_data](img/output-count-tanpa-groupby.png)

`[4]` Melakukan count dengan groupby

![Count_with_groupby](img/count-dengan-groupby.png)

dengan output:

![Output_Count_with_groupby](img/output-count-dengan-groupby.png)

Terdapat perbedaan antara melakukan count dengan groupby dan tanpa groupby:

1. Terdapat index apa yang di specify as groupby
2. Perhitungan jadi berdasarkan apa yang di specify as groupby
3. Overall, lebih mudah untuk membaca data summary yang telah di groupby

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/3-Aggregation-dan-GroupBy/ReviewInpeksiData.py) | Stack dan Unstack |

# Groupby dan Aggregasi dengan Fungsi Statistik Dasar - Part 1
Pada subbab ini akan menerapkan groupby dan fungsi aggregasi mean dan std untuk menentukan nilai rata-rata dan standar deviasi dari masing-masing kelompok data dari dataset https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv dan di assign sebagai variabel gaq.

Akan buat variabel pollutant.

![Dataframe_create_var_pollutant](img/dataframe-create-var-pollutant.png)

dengan output dataframenya di console:

![Output_dataframe_pollutant](img/output-dataframe-pollutant.png)

`[1]` Group berdasarkan country dan terapkan aggregasi mean, method .mean() setelah penerapan method .groupby() digunakan untuk mencari rata-rata dari tiap kelompok.

![Groupby_country_mean](img/groupby-country-mean.png)

dengan output:

![Output_groupby_country_mean](img/output-groupby-country-mean.png)

`[2]` Group berdasarkan country dan terapkan aggregasi std, method .std() setelah penerapan method .groupby() digunakan untuk mencari standard deviasi (penyimpangan) dari tiap kelompok.

![Groupby_country_aggregasi](img/groupby-country-aggregasi.png)

dengan ouput di console:

![Output_Groupby_Country_Aggregasi](img/output-groupby-country-aggregasi.png)

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/3-Aggregation-dan-GroupBy/GroupbyDanAggregasiDenganFungsiStatistikDasarPart1.py) | Groupby dan Aggregasi dengan Fungsi Statistik Dasar |

# Groupby dan Aggregasi dengan Fungsi Statistik Dasar - Part 2
Akan melanjutkan untuk fungsi statistik lainnya yaitu .sum() dan .nunique() untuk mengaggregasi dataset pollutant setelah di groupby.

`[3]` Group berdasarkan country dan terapkan aggregasi sum, method .sum() setelah penerapan method .groupby() digunakan untuk mencari total nilai dari tiap kelompok.

![Groupby_country_sum](img/groupby-country-sum.png)

dengan output:

![Output_groupby_country_sum](img/output-groupby-country-sum.png)

`[4]` Group berdasarkan country dan terapkan aggregasi nunique, method .nunique() setelah penerapan method .groupby() digunakan untuk mencari berapakah jumlah unique value dari tiap kelompok.

![Groupby_country_nunique](img/groupby-country-nunique.png)

dengan output:

![Output_groupby-country_nunique](img/output-groupby-country-nunique.png)

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/3-Aggregation-dan-GroupBy/GroupbyDanAggregasiDenganFungsiStatistikDasarPart2.py) | Groupby dan Aggregasi dengan Fungsi Statistik Dasar |

# Groupby dan Aggregasi dengan Fungsi Statistik Dasar - Part 3
Akan melanjutkan untuk fungsi statistik .min() dan .max() untuk mengaggregasi dataset pollutant setelah di groupby.

`[5]` Group berdasarkan country dan terapkan aggregasi min, method .min() setelah penerapan method .groupby() digunakan untuk memunculkan nilai terkecil dari tiap kelompok.

![Groupby_min](img/groupby-min.png)

dengan output:

![Output_groupby_min](img/output-groupby-min.png)

`[6]` Group berdasarkan country dan terapkan aggregasi max, method .max() setelah penerapan method .groupby() digunakan untuk memunculkan nilai terbesar dari tiap kelompok.

![Groupby_max](img/groupby-max.png)

dengan output:

![Output_groupby_max](img/output-groupby-max.png)

Tugas Praktik:

Gunakanlah method .first() dan .last() untuk aggregasi setelah penerapan .groupby() yang masing-masingnya bertujuan untuk memunculkan item pertama dan item terakhir dari tiap kelompok.

![Tugas_Praktek](img/tugas-praktek-1.png)

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/3-Aggregation-dan-GroupBy/GroupbyDanAggregasiDenganFungsiStatistikDasarPart3.py) | Groupby dan Aggregasi dengan Fungsi Statistik Dasar |

# Groupby dengan Multiple Aggregations
Kali ini akan menggunakan grouby dengan multiple aggregations yang berupa kombinasi antara beberapa fungsi. Mari perhatikan contoh berikut ini!

![Multiple_Aggregations](img/code-multiple-aggregations.png)

output yang diberikan oleh baris ke-9 adalah:

![Output_Multiple_Aggregations](img/output-multiple-aggregations.png)

Tugas Praktik: 

Terapkanlah multiple aggregations pada dataframe pollutant dengan fungsi aggregasinya adalah 'min', 'median', 'mean', 'max'.

![Tugas_Praktek_2](img/tugas-praktek-2.png)

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/3-Aggregation-dan-GroupBy/GroupbyDenganMultipleAggregations.py) | Groupby dengan Multiple Aggregations |

# Groupby dengan Custom Aggregations
Dengan membuat sebuah Python function (user defined) dapat menggunakan sebagai custom aggregation pada dataframe yang telah di groupby.

Perhatikan contoh yang diberikan berikut ini!

![Custom_Aggregations](img/code-custom-aggregations.png)

di sini dibuat sebuah fungsi untuk menentukan range pada setiap kelompok. Diperoleh output:

![Output_custom_aggreagations](img/output-custom-aggregations.png)

Tugas Praktek:

Tentukanlah inter quartile range (IQR) pada setiap kelompok data, dan kemudian tampilkanlah 5 data teratas saja.

![Tugas_Praktek_3](img/tugas-praktek-3.png)

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/3-Aggregation-dan-GroupBy/GroupbyDenganCustomAggregations.py) | Groupby dengan Custom Aggregations |


# Groupby dengan Custom Aggregations by dict
Penggunaan custom aggregation lainnya pada dataframe yang telah di groupby dapat dilakukan dengan mempasskan sebuah dict yang berisi 'key' dict sebagai nama kolomnya dan 'value' dict adalah fungsi untuk aggregasi, baik user defined function atau yang telah tersedia.

Berdasarkan kode berikut ini:

![Dataframe_Aggregations](img/dataframe-aggregations.png)

Telah dimiliki dataset yang akan di apply teknik custom aggregation dengan menggunakan dict ini yaitu:

![Output_before_apply_dic](img/output-before-apply-dic.png)

Akan apply teknik custom aggregation pada kolom 'o3' dan 'so' dengan fungsi aggregasi masing-masingnya adalah 'max' dan 'data_range'. Fungsi 'data_range' ini merupakan fungsi yang didefinisikan sendiri (user-defined) untuk menentukan jangkauan (range) data.

![Apply_dic](img/code-apply-dic.png)

dengan output berupa:

![Output_Apply_Dic](img/output-apply-dic.png)

Tugas Praktik:

Dengan dataset yang masih sama seperti tersedia di code editor, tentukanlah median untuk kolom 'pm10' serta iqr untuk kolom 'pm25' dan 'so2'. Tampilkan pula 5 data teratas saja.

![Tugas_Praktek_4](img/tugas-praktek-4.png)

| Code  |               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/7-Data-Manipulation-with-Pandas-Part-2/3-Aggregation-dan-GroupBy/GroupbyDenganCustomAggregationsByDict.py) | Groupby dengan Custom Aggregations By Dict |

# Quiz

![Quiz_1a](img/quiz-1a.PNG)

![Quiz_1b](img/quiz-1b.PNG)

![Quiz_1c](img/quiz-1c.PNG)