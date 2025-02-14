from datetime import datetime  # Mengimpor modul datetime untuk mengelola tanggal
from collections.abc import Iterator, Iterable  # Mengimpor Iterator dan Iterable untuk membuat pola iterator

# Parent class
class Vehicle:
    def __init__(self, brand: str, manufacture_date: str, price: float, mileage: int, features: dict):
        # Inisialisasi atribut kendaraan
        self.brand = brand  # Merek kendaraan
        self.manufacture_date = datetime.strptime(manufacture_date, "%Y-%m-%d")  # Konversi string tanggal ke objek datetime
        self.price = price  # Harga kendaraan
        self.mileage = mileage  # Jarak tempuh kendaraan dalam kilometer
        self.features = features  # Fitur tambahan kendaraan dalam bentuk dictionary

    def display_info(self):
        # Menampilkan informasi kendaraan
        vehicle_info = (
            f"Merek: {self.brand}\n"
            f"Tanggal Produksi: {self.manufacture_date.strftime('%d-%m-%Y')}\n"  # Format ulang tanggal ke format dd-mm-yyyy
            f"Harga: Rp{self.price:,.2f}\n"  # Format harga dengan pemisah ribuan dan dua desimal
            f"Kilometer: {self.mileage} km\n"
            "Fitur:\n"
        )
        # Loop untuk menampilkan fitur kendaraan
        for key, value in self.features.items():
            vehicle_info += f"  - {key}: {value}\n"
        return vehicle_info

# Subclasses
class Car(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, num_seats):
        # Memanggil konstruktor parent class
        super().__init__(brand, manufacture_date, price, mileage, features)
        self.num_seats = num_seats  # Menambahkan atribut jumlah kursi

    def display_info(self):
        # Menampilkan informasi kendaraan termasuk jumlah kursi
        return super().display_info() + f"Jumlah Kursi: {self.num_seats}\n"

class Motorcycle(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, engine_capacity):
        # Memanggil konstruktor parent class
        super().__init__(brand, manufacture_date, price, mileage, features)
        self.engine_capacity = engine_capacity  # Menambahkan atribut kapasitas mesin

    def display_info(self):
        # Menampilkan informasi kendaraan termasuk kapasitas mesin
        return super().display_info() + f"Kapasitas Mesin: {self.engine_capacity} cc\n"

class Truck(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, cargo_capacity):
        # Memanggil konstruktor parent class
        super().__init__(brand, manufacture_date, price, mileage, features)
        self.cargo_capacity = cargo_capacity  # Menambahkan atribut kapasitas muatan

    def display_info(self):
        # Menampilkan informasi kendaraan termasuk kapasitas muatan
        return super().display_info() + f"Kapasitas Muatan: {self.cargo_capacity} kg\n"

# Iterator Pattern
class VehicleIterator(Iterator):
    def __init__(self, vehicles):
        # Inisialisasi iterator untuk daftar kendaraan
        self._vehicles = vehicles
        self._index = 0  # Menyimpan posisi iterasi saat ini

    def __next__(self):
        # Mengembalikan kendaraan berikutnya dalam daftar
        if self._index < len(self._vehicles):
            vehicle = self._vehicles[self._index]
            self._index += 1
            return vehicle
        raise StopIteration  # Menghentikan iterasi jika semua kendaraan telah diakses

class VehicleCollection(Iterable):
    def __init__(self):
        # Inisialisasi daftar kendaraan kosong
        self._vehicles = []

    def add_vehicle(self, vehicle):
        # Menambahkan kendaraan ke daftar
        self._vehicles.append(vehicle)
        print(f"{vehicle.brand} berhasil ditambahkan.")

    def remove_vehicle(self, brand):
        # Menghapus kendaraan berdasarkan mereknya
        self._vehicles = [v for v in self._vehicles if v.brand != brand]
        print(f"{brand} berhasil dihapus dari daftar.")

    def get_vehicle_list(self):
        # Mengembalikan daftar informasi kendaraan
        if not self._vehicles:
            return ["Tidak ada kendaraan dalam daftar."]
        return [v.display_info() for v in self._vehicles]

    def __iter__(self):
        # Mengembalikan iterator untuk kendaraan
        return VehicleIterator(self._vehicles)

# Main Program
if __name__ == "__main__":
    vehicle_collection = VehicleCollection()  # Membuat instance koleksi kendaraan
    
    while True:
        # Menampilkan menu utama
        print("--- Pilih Aksi ---")
        print("1. Tambah Kendaraan")
        print("2. Hapus Kendaraan")
        print("3. Tampilkan Kendaraan")
        print("4. Keluar")
        action = input("Masukkan pilihan (1/2/3/4): ")  # Input pilihan pengguna
        
        if action == "1":
            # Menu untuk memilih jenis kendaraan
            print("--- Pilih Jenis Kendaraan ---")
            print("1. Mobil")
            print("2. Sepeda Motor")
            print("3. Truk")
            choice = input("Masukkan pilihan (1/2/3): ")  # Input jenis kendaraan
            
            # Meminta informasi kendaraan dari pengguna
            brand = input("Masukkan merek kendaraan: ")
            manufacture_date = input("Masukkan tanggal produksi (YYYY-MM-DD): ")
            price = float(input("Masukkan harga kendaraan: "))
            mileage = int(input("Masukkan kilometer kendaraan: "))
            
            # Mengisi fitur kendaraan dalam bentuk dictionary
            features = {}
            while True:
                key = input("Masukkan nama fitur (atau 'selesai' untuk mengakhiri): ")
                if key.lower() == "selesai":
                    break
                value = input(f"Masukkan nilai fitur untuk {key}: ")
                features[key] = value
            
            # Membuat objek kendaraan berdasarkan pilihan pengguna
            if choice == "1":
                num_seats = int(input("Masukkan jumlah kursi: "))
                vehicle = Car(brand, manufacture_date, price, mileage, features, num_seats)
            elif choice == "2":
                engine_capacity = float(input("Masukkan kapasitas mesin (cc): "))
                vehicle = Motorcycle(brand, manufacture_date, price, mileage, features, engine_capacity)
            elif choice == "3":
                cargo_capacity = int(input("Masukkan kapasitas muatan (kg): "))
                vehicle = Truck(brand, manufacture_date, price, mileage, features, cargo_capacity)
            else:
                print("Pilihan tidak valid.")  # Jika input salah, kembali ke awal
                continue
            
            vehicle_collection.add_vehicle(vehicle)  # Menambahkan kendaraan ke koleksi
        
        elif action == "2":
            # Menghapus kendaraan berdasarkan merek
            brand = input("Masukkan merek kendaraan yang ingin dihapus: ")
            vehicle_collection.remove_vehicle(brand)
        
        elif action == "3":
            # Menampilkan daftar kendaraan
            print("\n--- Daftar Kendaraan ---")
            for info in vehicle_collection.get_vehicle_list():
                print(info)
                print("-")
        
        elif action == "4":
            # Keluar dari program
            print("Terima kasih telah menggunakan program ini.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")  # Pesan jika input tidak valid
