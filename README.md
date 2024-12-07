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

## 👩‍🏫Cara Menggunakan
1. Buka Aplikasi
 - Unduh file ZIP aplikasi CarbonWISE dengan nama "simple carbon calculator".
 - Ekstrak file yang sudah diunduh ke perangkat Anda. Pastikan Anda sudah menginstal Python dan mengunduh semua pustaka yang dibutuhkan.
 - Jalankan aplikasi dengan perintah streamlit run simple_carbon_calculator.py melalui terminal di dalam folder aplikasi.
 - Setelah itu, aplikasi akan membuka halaman utama yang menampilkan logo dan penjelasan mengenai alasan pengembangan aplikasi ini.

2. Isi Formulir
 - Setelah membuka aplikasi, Anda akan melihat beberapa kolom yang perlu diisi. Masukkan informasi Anda, seperti nama, tanggal, dan data lainnya yang dibutuhkan untuk menghitung jejak karbon.

3. Masukkan Data Jejak Karbon
 - Setelah mengisi formulir, masukkan data yang relevan untuk menghitung konsumsi energi dan emisi karbon Anda.
 - Anda tidak perlu menekan tombol apapun, karena output akan muncul secara otomatis

4. Lihat Hasil Jejak Karbon
 - Setelah selesai mengisi semua data, aplikasi akan menghitung dan menampilkan hasil jejak karbon Anda dalam bentuk tulisan.
 - Hasil ini menunjukkan total jejak karbon yang telah Anda hasilkan.

5. Unduh Data CSV
 - Setelah perhitungan selesai, Anda dapat mengunduh file CSV yang berisi data jejak karbon Anda untuk disimpan atau dianalisis lebih lanjut. Dengan cara Anda harus menyimpan jejak karbon Anda terlebih dahulu, jika tidak maka fitur unduh data CSV tidak akan tersedia.
 - Klik tombol "Download CSV" untuk mengunduh file tersebut.



