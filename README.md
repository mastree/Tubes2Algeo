# Tugas Besar 2 Aljabar Linier dan Geometri
## Penerapan Metrik Berbasiskan Vektor di Sistem Pengenalan Wajah (<i>Face Recognition</i>)

<p>Tugas besar ini dikerjakan oleh 3 orang yaitu:</p>
<ul>
    <li>Ricky Fernando - 1358062</li>
    <li>Fritz Gerald Tjie - 13518065</li>
    <li>MUhammad Kamal Shafi - 13518113</li>
</ul>
<p>Tugas besar ini dibuat dengan menggunakan bahasa pemrograman <i>Python</i></p>

# Menjalankan program
## Menginstall library yang akan digunakan
<p>Program ini memerlukan beberapa library untuk dapat digunakan, yaitu:</p>
<ul>
    <li>tkinter</li>
    <li>pillow</li>
    <li>cv2</li>
    <li>numpy</li>
    <li>scipy</li>
    <li>matplotlib</li>
    <li>_pickle</li>
    <li>random</li>
    <li>os</li>
    <li>sys</li>
    <li>math</li>
    <li>shutil</li>
</ul>
Beberapa library di atas dapat diinstall dengan menggunakan <i>command</i>

`pip install <package>`
Beberapa library di atas merupakan library bawaan <i>Python</i>

## First time setup
Jika anda akan menjalankan program ini untuk pertama kali, maka anda harus menjalankan fungsi `run_DataSet_extractor()` dan `run_Reference_extractor()` yang berada di file `fecesrecognition.py` untuk mengekstrak vektor-vektor yang ada di gambar ke file `Data_features.pck` dan `Ref_features.pck`

## Cara menjalankan program
1. Dengan menjalankan file `faceRecognition.exe`
2. Dengan menggunakan cmd dan menjalankan perintah `python faceRecognition.py`

## Langkah penggunaan
1. Tekan tombol "Browse" untuk memasukkan gambar yang akan dijadikan referensi
2. Pilih metode yang akan digunakan (<i>Euclidean</i> atau <i>Cosine</i>)
3. Tentukan hasil pencocokan yang diinginkan, maksimal berupa 20 gambar
4. Tekan tombol "Send" untuk memulai program
5. Tunggu sampai "Progress Bar" penuh
6. Akan muncul 2 gambar, gambar di kiri merupakan gambar referensi dan gambar di kanan merupakan gambar hasil pencocokan
7. Tombol "Prev" untuk memunculkan gambar sebelumnya dengan tingkat kemiripan lebih besar dari gambar sekarang atau jika gambar sekarang merupakan gambar pertama maka akan memunculkan gambar terakhir
8. Tombol "Next" untuk memunculkan gambar setelahnya dengan tingkat kemiripan lebih kecil dari gambar sekarang atau jika gambar sekarang merupakan gambar terakhir maka akan memunculkan gambar pertama
9. Tombol "Exit" untuk keluar dari pencocokan gambar dan kembali ke tampilan awal program
10. Tekan tombol "X" di pojok kanan atas window untuk keluar dari program