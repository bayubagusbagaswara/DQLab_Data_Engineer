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