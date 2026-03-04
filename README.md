Tugas analisis 1: 
Nilai HP hero1 (Layla) yang tadinya 100 akan tertimpa (overwrite) menjadi 500. Di Python, atribut objek secara default bersifat publik, sehingga kamu bisa mengubah isinya kapan saja langsung dari luar class menggunakan operator titik

Tugas analisis 2:
Pada method serang(self, lawan), parameter lawan menerima seluruh objek, bukan cuma sekadar teks (string) nama. Ini sangat penting karena beberapa alasan:

Akses ke Seluruh Data: Dengan menerima objek utuh, method serang bisa mengakses semua atribut lawan sekaligus (nama, HP, defense, dll.). Kalau cuma kirim nama, kita tidak tahu berapa sisa HP lawan tersebut.

Interaksi Antar Objek: Kita bisa memanggil method milik objek lain. Perhatikan baris lawan.diserang(self.attack_power). Di sini, objek hero1 memerintahkan objek hero2 untuk menjalankan fungsinya sendiri.

Sinkronisasi Status: Karena yang dikirim adalah objek aslinya, maka setiap perubahan (seperti pengurangan HP) akan langsung tersimpan pada objek tersebut. Jika kita hanya mengirim string nama, kita tidak bisa mengubah isi darah di objek aslinya.

Tugas analisis 3:
Mengapa error padahal sudah mengirim nama "Eudora"?

Saat kamu membuat objek Mage, Python menjalankan fungsi __init__ milik class Mage.

Jika super().__init__ dihapus, Python hanya menjalankan apa yang ada di dalam __init__ milik Mage saja (yaitu hanya menyimpan mana).

Python tidak akan otomatis menjalankan perintah self.name = name yang ada di class Hero (Induk).

Kesimpulannya: Data "Eudora" memang dikirim ke fungsi, tapi karena perintah penyimpanannya (yang ada di class Induk) tidak dipanggil, maka data tersebut dibuang dan tidak disimpan ke dalam memori objek eudora.

Tugas analisis 4:
Apakah muncul nilai atau Error? Nilai HP akan muncul.

Mengapa Python mengizinkannya? Ini disebut konsep Name Mangling. Python sebenarnya tidak benar-benar mengunci variabel private, melainkan hanya "mengubah namanya" menjadi _NamaClass__NamaVariabel agar tidak sengaja tertimpa.

Mengapa tetap tidak boleh dilakukan? Secara standar pemrograman, mengakses variabel dengan cara ini melanggar prinsip Enkapsulasi. Kita harus selalu menggunakan Getter dan Setter agar integritas data tetap terjaga dan alur program tetap konsisten.

Tugas analisis 5:
Error yang muncul: Can't instantiate abstract class Hero with abstract method serang.

Artinya: Kamu tidak bisa membuat objek dari class tersebut karena belum memenuhi janji/kontrak yang dibuat di Interface (GameUnit).

Konsekuensinya: Jika lupa membuat method yang sudah dijanjikan di Interface, program akan error dan objek tersebut tidak akan pernah bisa dibuat.

Tugas analisis 6:
Apakah program berjalan lancar? Ya, berjalan sangat lancar.
Keuntungan Polimorfisme: Keuntungannya adalah fleksibilitas. Programmer bisa menambah banyak karakter baru (Healer, Tank, Assassin) tanpa perlu mengubah logika Looping utama. Program secara otomatis mengenali cara setiap karakter "beraksi" sesuai dengan class-nya masing-masing.


<img width="957" height="575" alt="image" src="https://github.com/user-attachments/assets/0bcc79c3-0d8f-42a6-a621-4738421627a1" />
<img width="1092" height="430" alt="image" src="https://github.com/user-attachments/assets/5d924f25-134f-42d5-8c2b-2b850fb0d98e" />



