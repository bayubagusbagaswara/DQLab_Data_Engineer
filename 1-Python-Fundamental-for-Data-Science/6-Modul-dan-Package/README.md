# Pendahuluan
Modul merupakan objek python yang telah tersedia dari pengembangnya atau dapat kamu kembangkan sendiri. Dalam bahasa yang cukup sederhana, modul adalah kumpulan kode Python yang distruktur ke dalam beberapa fungsi, kelas, dan variabel. Python sendiri telahmemiliki banyak library dan module yang bisa diakses oleh pengguna secara free.

Umumnya modul dikembangkan untuk tujuan umum yang luas penerapannya seperti:

- untuk pengolah data numerik seperti array 1D, 2D, 3D atau hingga nD dengan contohnya adalah numpy
- untuk komputasi saintifik yang berbasis metode numerik dan statistik dengan contohnya adalah scipy dan statsmodel
- untuk pengolah dan analisis data seperti Microsoft Excel atau Google Spreadsheets dengan contohnya adalah pandas, pypolar, dan modin
- untuk visualisasi data dengan contohnya yaitu matplotlib, seaborn, plotnine, altair, mayavi, bokeh, plotly, dll.  
- untuk pembelajaran mesin dengan contohnya yaitu scikit-learn, xgboost, lightgbm, catboost, pycaret, dll
- untuk deep learning dengan contohnya adalah keras, tensorflow, pytorch, cafe, dll

Tentunya masih banyak lagi jika disebutkan. Library atau modul-modul yang telah disebutkan merupakan library yang umum digunakan oleh data scientist.

# Import Package dan Menggunakan modul
Pada sesi praktik ini, kita akan menggunakan modul math yang merupakan module standar untuk berbagai fungsi matematika. Panggil terlebih dahulu modul ini seperti yang ditunjukkan berikut ini:

```bash
import math
```
Terlihat bahwa cara menggunakan modul cukup sederhana.

Secara umum, module memiliki banyak fungsi. Cara pemrogram untuk mengakses fungsi-fungsi yang tersedia pada suatu modul juga berbeda-beda. Untuk saat ini, perhatikan kode berikut dan kemudian ketikkan kode di bawah ini di Code Editor:

```bash
import math
print("Nilai pi adalah:", math.pi)  # math.pi merupakan sintak untuk memanggil fungsi pi
```

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python-Fundamental-for-Data-Science/6-Modul-dan-Package/ImportPackage.py) | Import Package |

# Import dengan Module Rename atau Alias
Kita bisa mengimpor modul dengan mengganti namanya. Hal ini biasa dilakukan untuk menyingkat nama modul yang panjang.

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python-Fundamental-for-Data-Science/6-Modul-dan-Package/ImportAlias.py) | Import Alias |

# Import Sebagian Fungsi
Sebuah module dapat memiliki puluhan atau ratusan fungsi. Terkadang kasus tertentu ketika memprogram, kita hanya membutuhkan satu, dua, atau beberapa buah fungsi saja. Untuk meminimalisir ketidakefisienan suatu program dalam me-load suatu module seperti yang telah dilakukan dalam format import module_name. Selanjutnya, kita dapat mengimport beberapa modul yang dibutuhkan saja menggunakan format from module_name import function_name

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python-Fundamental-for-Data-Science/6-Modul-dan-Package/ImportSebagianFungsi.py) | Import Sebagian Fungsi |

# Import Semua isi Moduls
Namun, jika memang yang dibutuhkan banyak, semisal lebih dari 10 atau bahkan ratusan fungsi, bisa dilakukan import semuanya dengan menggunakan format from module_name import *. Tanda * disini menunjukan semua fungsi diimport ke dalam code

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/1-Python-Fundamental-for-Data-Science/6-Modul-dan-Package/ImportSemuaIsiModuls.py) | Import Semua Isi Moduls |