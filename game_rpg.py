from abc import ABC, abstractmethod

# 1. INTERFACE / ABSTRACT CLASS (ABSTRAKSI)
# Ini adalah kontrak utama. Semua unit wajib punya method ini.
class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

# 2. PARENT CLASS (HERO) & ENKAPSULASI
class Hero(GameUnit):
    def __init__(self, nama, hp_awal=100, attack_power=10):
        self.nama = nama
        self.attack_power = attack_power
        # ENKAPSULASI: HP bersifat Private agar aman
        self.__hp = hp_awal

    # GETTER: Cara resmi melihat HP
    def get_hp(self):
        return self.__hp

    # SETTER: Cara resmi mengubah HP dengan validasi
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0  # HP tidak boleh negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    # Implementasi method info (Abstraksi)
    def info(self):
        print(f"Hero: {self.nama} | HP: {self.get_hp()} | Power: {self.attack_power}")

    # Implementasi method serang (Abstraksi)
    def serang(self, lawan):
        print(f"{self.nama} menyerang {lawan.nama}!")
        lawan.diserang(self.attack_power)

    # Method diserang: Menerima damage
    def diserang(self, damage):
        # Pakai setter/getter bahkan di dalam class sendiri agar aman
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")

# 3. CHILD CLASSES (INHERITANCE & POLIMORFISME)
class Mage(Hero):
    def __init__(self, nama, hp_awal, attack_power, mana):
        # Memanggil constructor milik Parent (Hero)
        super().__init__(nama, hp_awal, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.nama} [Mage] | HP: {self.get_hp()} | Mana: {self.mana}")

    # Polimorfisme: Respon serangan yang berbeda
    def serang(self, target=None):
        if target:
            super().serang(target)
        else:
            print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")

    # Skill khusus Mage
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.nama} menggunakan Fireball ke {lawan.nama}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2) # Damage 2x lipat
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")

class Archer(Hero):
    def serang(self, target=None):
        if target:
            super().serang(target)
        else:
            print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")

class Fighter(Hero):
    def serang(self, target=None):
        if target:
            super().serang(target)
        else:
            print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")

# 4. IMPLEMENTASI MONSTER (Abstraksi)
class Monster(GameUnit):
    def __init__(self, jenis, hp=100):
        self.nama = jenis # Properti nama agar konsisten saat diserang
        self.jenis = jenis
        self.hp = hp

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target.nama}!")

    def diserang(self, damage):
        self.hp -= damage
        print(f"Monster {self.jenis} terluka! Sisa HP: {self.hp}")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")

# --- MAIN PROGRAM ---
print("--- Pertarungan Dimulai ---")
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()
hero1.serang(hero2)
hero2.serang(hero1)

print("\n--- Uji Coba Enkapsulasi ---")
hero1.set_hp(-50)       # Coba set negatif
print(f"HP {hero1.nama} setelah set negatif: {hero1.get_hp()}") # Output: 0

print("\n--- Update Class Mage & Monster ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)
eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)

print("\n--- Penerapan Polymorphism (Pasukan) ---")
pasukan = [
    Mage("Eudora", 80, 30, 100),
    Archer("Miya", 90, 25),
    Fighter("Zilong", 120, 35),
    Mage("Gord", 70, 40, 80)
]

for pahlawan in pasukan:
    pahlawan.serang() # Merespon berbeda-beda sesuai jenis class-nya