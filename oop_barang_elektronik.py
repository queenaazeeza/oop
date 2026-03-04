from abc import ABC, abstractmethod

# 1. ABSTRACTION: Menggunakan ABC agar class induk tidak bisa di-instansiasi langsung
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        # 2. ENCAPSULATION: Menggunakan __ (private) agar tidak bisa diakses sembarangan
        self.__harga_dasar = harga_dasar
        self.__stok = 0

    # Getter untuk mendapatkan nilai atribut private
    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    # Method dengan validasi (Sesuai rubrik penilaian: stok tidak boleh negatif)
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")
            return True

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

# 3. INHERITANCE: Laptop mewarisi BarangElektronik
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    # 4. POLYMORPHISM: Implementasi berbeda untuk Laptop (Pajak 10%)
    def tampilkan_detail(self):
        return f"[LAPTOP] {self.nama} | Proc: {self.processor}"

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.10
        total = (self.get_harga_dasar() + pajak) * jumlah
        return total, pajak

# 3. INHERITANCE: Smartphone mewarisi BarangElektronik
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    # 4. POLYMORPHISM: Implementasi berbeda untuk Smartphone (Pajak 5%)
    def tampilkan_detail(self):
        return f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}"

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.05
        total = (self.get_harga_dasar() + pajak) * jumlah
        return total, pajak

# Fungsi untuk mencetak struk sesuai format output modul
def cetak_struk(keranjang):
    print("\n--- STRUK TRANSAKSI ---")
    total_akhir = 0
    
    for i, pesanan in enumerate(keranjang, 1):
        produk = pesanan['produk']
        qty = pesanan['qty']
        
        subtotal, pajak_satuan = produk.hitung_harga_total(qty)
        total_akhir += subtotal
        
        print(f"{i}. {produk.tampilkan_detail()}")
        print(f"   Harga Dasar: Rp {produk.get_harga_dasar():,.0f} | Pajak: Rp {pajak_satuan:,.0f}")
        print(f"   Beli: {qty} unit | Subtotal: Rp {subtotal:,.0f}\n")

    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {total_akhir:,.0f}")
    print("-" * 40)

# --- RUNNING PROGRAM ---
if __name__ == "__main__":
    print("--- SETUP DATA ---")
    
    # Inisialisasi Produk
    laptop1 = Laptop("MJ's Swarovski", 55000000000, "Intel Xeon W-Series")
    hp1 = Smartphone("Falcon Supernova iPhone 6 Pink Diamond", 49000000000, "8MP with Pink Diamond Inlay ")

    # Simulasi Pengelolaan Stok
    laptop1.tambah_stok(10)
    hp1.tambah_stok(-5)  # Ini akan memicu pesan gagal sesuai modul
    hp1.tambah_stok(20)

    # Simulasi Transaksi
    daftar_belanja = [
        {"produk": laptop1, "qty": 2},
        {"produk": hp1, "qty": 1}
    ]

    cetak_struk(daftar_belanja)