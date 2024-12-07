# Tugas-Rekayasa-Perangkat-Lunak-

## 🌳Tentang Project CarbonWISE🌳

Jejak karbon global tahunan kini telah melampaui angka yang mengkhawatirkan, yaitu 40 miliar ton, menyoroti kebutuhan mendesak akan tindakan kolektif untuk mengurangi perubahan iklim. Terdapat hubungan langsung dan tak terbantahkan antara kebiasaan harian individu dengan meningkatnya emisi CO2. Praktik sehari-hari, mulai dari konsumsi energi dan transportasi hingga sistem pemanas-pendingin di rumah serta produksi-konsumsi makanan, secara signifikan berkontribusi terhadap tantangan lingkungan yang terus meningkat ini. Dengan menyadari peran penting individu dalam situasi ini, menjadi sangat penting untuk meningkatkan kesadaran mengenai dampak mereka terhadap peningkatan level CO2 global.
Tujuan utama dari proyek ini adalah memberdayakan individu dengan membantu mereka menghitung jejak karbon sehari-hari mereka. Dengan mempertimbangkan kebiasaan dan pilihan gaya hidup harian, inisiatif ini bertujuan untuk memberikan wawasan yang dipersonalisasi. Selain itu, proyek ini tidak hanya berfokus pada peningkatan kesadaran, tetapi juga memberikan rekomendasi praktis agar individu dapat secara aktif mengurangi jejak karbon mereka. Melalui upaya ini, tujuan yang ingin dicapai adalah mendorong praktik hidup berkelanjutan yang berkontribusi pada komunitas global yang lebih sadar lingkungan dan bertanggung jawab.

## 🛠️Langkah-Langkah Proyek
#### 🧩Pengembangan Backend:
1. **Pengolahan Data dengan SQLite:**
   - Menggunakan SQLite untuk menyimpan dan mengambil data jejak karbon yang dihitung oleh pengguna.

2. **Operasi I/O:**
   - Memanfaatkan library sqlite3 untuk operasi input/output dalam menyimpan dan mengakses data dari database.

3. **Pemrograman Basis Data:**
   - Membuat dan mengelola tabel di database SQLite untuk menyimpan data jejak karbon yang dimasukkan oleh pengguna.

4. **Pengolahan Data dengan Pandas:**
   - Menggunakan Pandas untuk mengelola dan memanipulasi data yang terkait dengan jejak karbon dalam format CSV. 

5. **Penggunaan StringIO**
   - Mengonversi data ke dalam format yang dapat diunduh dan kemudian disediakan untuk diunduh oleh pengguna.

#### 🖥️Pengembangan Frontend :

1. **Setup Streamlit**
   - Menggunakan Streamlit untuk membuat aplikasi web interaktif yang memungkinkan pengguna memasukkan data jejak karbon dan melihat hasil perhitungan..

2. **Desain Antarmuka Pengguna (UI):**
   - Merancang antarmuka pengguna yang intuitif dengan komponen-komponen dari Streamlit, serta menambahkan elemen desain CSS untuk meningkatkan pengalaman pengguna..

3. **Encoding/Decoding Base64:**
   - Menggunakan base64 untuk meng-encode dan mendecode data gambar biner yang digunakan untuk latar belakang atau elemen visual dalam aplikasi web.

4. **Pengujian:**
   - Menguji aplikasi secara menyeluruh untuk memastikan bahwa semua komponen backend dan frontend berfungsi dengan baik dan sesuai harapan.
