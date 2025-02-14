from datetime import datetime  # Mengimpor modul datetime untuk mengelola tanggal
from abc import ABC, abstractmethod  # Mengimpor modul ABC untuk membuat kelas abstrak

# Parent class
class Vehicle:
    def __init__(self, brand: str, manufacture_date: str, price: float, mileage: int, features: dict):
        self.brand = brand  # Menyimpan merek kendaraan
        self.manufacture_date = datetime.strptime(manufacture_date, "%Y-%m-%d")  # Mengonversi string menjadi objek datetime
        self.price = price  # Menyimpan harga kendaraan
        self.mileage = mileage  # Menyimpan jumlah kilometer kendaraan
        self.features = features  # Menyimpan fitur kendaraan dalam bentuk dictionary

    def display_info(self):
        vehicle_info = (
            f"Merek: {self.brand}\n"  # Menampilkan merek kendaraan
            f"Tanggal Produksi: {self.manufacture_date.strftime('%d-%m-%Y')}\n"  # Menampilkan tanggal produksi dengan format berbeda
            f"Harga: Rp{self.price:,.2f}\n"  # Menampilkan harga kendaraan dalam format mata uang
            f"Kilometer: {self.mileage} km\n"  # Menampilkan jarak tempuh kendaraan
            "Fitur:\n"  # Menampilkan fitur kendaraan
        )
        for key, value in self.features.items():  # Iterasi melalui fitur kendaraan
            vehicle_info += f"  - {key}: {value}\n"  # Menambahkan fitur ke dalam informasi kendaraan
        return vehicle_info  # Mengembalikan informasi kendaraan sebagai string

# Concrete Products
class Car(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, num_seats):
        super().__init__(brand, manufacture_date, price, mileage, features)  # Memanggil konstruktor kelas induk
        self.num_seats = num_seats  # Menyimpan jumlah kursi

    def display_info(self):
        return super().display_info() + f"Jumlah Kursi: {self.num_seats}\n"  # Menampilkan informasi kendaraan dan jumlah kursi

class Motorcycle(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, engine_capacity):
        super().__init__(brand, manufacture_date, price, mileage, features)  # Memanggil konstruktor kelas induk
        self.engine_capacity = engine_capacity  # Menyimpan kapasitas mesin

    def display_info(self):
        return super().display_info() + f"Kapasitas Mesin: {self.engine_capacity} cc\n"  # Menampilkan informasi kendaraan dan kapasitas mesin

class Truck(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, cargo_capacity):
        super().__init__(brand, manufacture_date, price, mileage, features)  # Memanggil konstruktor kelas induk
        self.cargo_capacity = cargo_capacity  # Menyimpan kapasitas muatan

    def display_info(self):
        return super().display_info() + f"Kapasitas Muatan: {self.cargo_capacity} kg\n"  # Menampilkan informasi kendaraan dan kapasitas muatan

# Factory Method
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, *args):
        pass  # Metode abstrak yang harus diimplementasikan oleh subclass

class CarFactory(VehicleFactory):
    def create_vehicle(self, brand, manufacture_date, price, mileage, features, num_seats):
        return Car(brand, manufacture_date, price, mileage, features, num_seats)  # Membuat objek Car

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self, brand, manufacture_date, price, mileage, features, engine_capacity):
        return Motorcycle(brand, manufacture_date, price, mileage, features, engine_capacity)  # Membuat objek Motorcycle

class TruckFactory(VehicleFactory):
    def create_vehicle(self, brand, manufacture_date, price, mileage, features, cargo_capacity):
        return Truck(brand, manufacture_date, price, mileage, features, cargo_capacity)  # Membuat objek Truck

# Vehicle List
vehicle_list = []  # List untuk menyimpan kendaraan

def add_vehicle(vehicle):
    vehicle_list.append(vehicle)  # Menambahkan kendaraan ke dalam daftar
    print(f"{vehicle.brand} berhasil ditambahkan.")  # Menampilkan pesan sukses

def remove_vehicle(brand):
    global vehicle_list
    vehicle_list = [v for v in vehicle_list if v.brand != brand]  # Menghapus kendaraan berdasarkan merek
    print(f"{brand} berhasil dihapus dari daftar.")  # Menampilkan pesan sukses

def get_vehicle_list():
    if not vehicle_list:
        return ["Tidak ada kendaraan dalam daftar."]  # Menampilkan pesan jika daftar kosong
    return [v.display_info() for v in vehicle_list]  # Mengembalikan daftar kendaraan sebagai string

# Program utama
if __name__ == "__main__":
    factories = {
        "1": CarFactory(),  # Pilihan untuk membuat mobil
        "2": MotorcycleFactory(),  # Pilihan untuk membuat motor
        "3": TruckFactory()  # Pilihan untuk membuat truk
    }
    
    while True:
        print("--- Pilih Aksi ---")
        print("1. Tambah Kendaraan")
        print("2. Hapus Kendaraan")
        print("3. Tampilkan Kendaraan")
        print("4. Keluar")
        action = input("Masukkan pilihan (1/2/3/4): ")
        
        if action == "1":
            print("--- Pilih Jenis Kendaraan ---")
            print("1. Mobil")
            print("2. Sepeda Motor")
            print("3. Truk")
            choice = input("Masukkan pilihan (1/2/3): ")
            
            if choice not in factories:
                print("Pilihan tidak valid.")
                continue
            
            brand = input("Masukkan merek kendaraan: ")
            manufacture_date = input("Masukkan tanggal produksi (YYYY-MM-DD): ")
            price = float(input("Masukkan harga kendaraan: "))
            mileage = int(input("Masukkan kilometer kendaraan: "))
            features = {}
            while True:
                key = input("Masukkan nama fitur (atau 'selesai' untuk mengakhiri): ")
                if key.lower() == "selesai":
                    break
                value = input(f"Masukkan nilai fitur untuk {key}: ")
                features[key] = value
            
            if choice == "1":
                num_seats = int(input("Masukkan jumlah kursi: "))
                vehicle = factories[choice].create_vehicle(brand, manufacture_date, price, mileage, features, num_seats)
            elif choice == "2":
                engine_capacity = float(input("Masukkan kapasitas mesin (cc): "))
                vehicle = factories[choice].create_vehicle(brand, manufacture_date, price, mileage, features, engine_capacity)
            elif choice == "3":
                cargo_capacity = int(input("Masukkan kapasitas muatan (kg): "))
                vehicle = factories[choice].create_vehicle(brand, manufacture_date, price, mileage, features, cargo_capacity)
            
            add_vehicle(vehicle)
        
        elif action == "2":
            brand = input("Masukkan merek kendaraan yang ingin dihapus: ")
            remove_vehicle(brand)
        
        elif action == "3":
            print("\n--- Daftar Kendaraan ---")
            for info in get_vehicle_list():
                print(info)
                print("-")
        
        elif action == "4":
            print("Terima kasih telah menggunakan program ini.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
