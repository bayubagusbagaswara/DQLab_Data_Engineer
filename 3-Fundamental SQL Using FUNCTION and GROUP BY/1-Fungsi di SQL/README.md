# Fungsi Scalar vs Fungsi Aggregate
“Bagian fungsi nih, Nja. Boleh kasih tahu perannya apa dalam pengolahan data?” Aku mulai bertanya.

“Oke, begini Aksara. Fungsi adalah metode yang digunakan untuk melakukan operasi data di database. Operasi ini bisa berupa kalkulasi numerik seperti sum, count, avg, etc; atau operasi non-numerik seperti string concatenations dan sub-strings. SQL Function dapat dibagi ke dalam 2 kategori, yaitufungsi scalar dan fungsi aggregate.”

Penjelasan Senja mengundang pertanyaan baru di benakku.

“Hm, apa aja sih bedanya fungsi skalar dan fungsi aggregate?”

“Fungsi skalar dalam SQL digunakan untuk mengembalikan nilai tunggal (single value) dari suatu nilai input yang diberikan, sedangkan fungsi agregat dalam SQL digunakan untuk melakukan perhitungan pada sekelompok nilai dan kemudian mengembalikan nilai tunggal. Nah, biar lebih mudah dipahami mari kita bahas dan praktekkan fungsi-fungsi dari kedua kategori ini.”

# Fungsi Skalar Matematika

“Memangnya fungsi-fungsi apa saja yang bisa dilakukan di SQL?”

“Untuk mengecek fungsi-fungsi apa saja yang bisa dilakukan di SQL, kita bisa membuka dokumentasi fungsi SQL di sini: https://www.postgresql.org/docs/9.5/functions-math.html, untuk postgresql database dan di sini: https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html, untuk mysql database.

![Fungsi_Skalar](img/skalar-matematika.png)


Untuk memudahkan pemahaman, aku diberikan Senja tabel dummy berisi nilai siswa semester 1 dan 2 di suatu sekolah. Berikut contoh penggunaan fungsi skalar dengan menggunakan tabel dummy: 

Tabel: students

![Table_Student](img/table-student.png)

# Fungsi Skalar Matematika - ABS()
Fungsi ABS( )

Syntax: 
```bash
SELECT ABS(ColumnName)  
FROM TableName; 
```

|Code 	|               Title              	|
|:----:	|:--------------------------------:	|
| [📜](https://github.com/bayubagusbagaswara/dqlab-data-engineer/blob/master/3-Fundamental%20SQL%20Using%20FUNCTION%20and%20GROUP%20BY/1-Fungsi%20di%20SQL/1-Fungsi-ABS().sql) | Operand And |