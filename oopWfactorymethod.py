from datetime import datetime
from abc import ABC, abstractmethod

# Parent class
class Vehicle:
    def __init__(self, brand: str, manufacture_date: str, price: float, mileage: int, features: dict):
        self.brand = brand
        self.manufacture_date = datetime.strptime(manufacture_date, "%Y-%m-%d")
        self.price = price
        self.mileage = mileage
        self.features = features

    def display_info(self):
        vehicle_info = (
            f"Merek: {self.brand}\n"
            f"Tanggal Produksi: {self.manufacture_date.strftime('%d-%m-%Y')}\n"
            f"Harga: Rp{self.price:,.2f}\n"
            f"Kilometer: {self.mileage} km\n"
            "Fitur:\n"
        )
        for key, value in self.features.items():
            vehicle_info += f"  - {key}: {value}\n"
        return vehicle_info

# Concrete Products
class Car(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, num_seats):
        super().__init__(brand, manufacture_date, price, mileage, features)
        self.num_seats = num_seats

    def display_info(self):
        return super().display_info() + f"Jumlah Kursi: {self.num_seats}\n"

class Motorcycle(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, engine_capacity):
        super().__init__(brand, manufacture_date, price, mileage, features)
        self.engine_capacity = engine_capacity

    def display_info(self):
        return super().display_info() + f"Kapasitas Mesin: {self.engine_capacity} cc\n"

class Truck(Vehicle):
    def __init__(self, brand, manufacture_date, price, mileage, features, cargo_capacity):
        super().__init__(brand, manufacture_date, price, mileage, features)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return super().display_info() + f"Kapasitas Muatan: {self.cargo_capacity} kg\n"

# Factory Method
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, *args):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self, brand, manufacture_date, price, mileage, features, num_seats):
        return Car(brand, manufacture_date, price, mileage, features, num_seats)

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self, brand, manufacture_date, price, mileage, features, engine_capacity):
        return Motorcycle(brand, manufacture_date, price, mileage, features, engine_capacity)

class TruckFactory(VehicleFactory):
    def create_vehicle(self, brand, manufacture_date, price, mileage, features, cargo_capacity):
        return Truck(brand, manufacture_date, price, mileage, features, cargo_capacity)

# Vehicle List
vehicle_list = []

def add_vehicle(vehicle):
    vehicle_list.append(vehicle)
    print(f"{vehicle.brand} berhasil ditambahkan.")

def remove_vehicle(brand):
    global vehicle_list
    vehicle_list = [v for v in vehicle_list if v.brand != brand]
    print(f"{brand} berhasil dihapus dari daftar.")

def get_vehicle_list():
    if not vehicle_list:
        return ["Tidak ada kendaraan dalam daftar."]
    return [v.display_info() for v in vehicle_list]

# Program utama
if __name__ == "__main__":
    factories = {
        "1": CarFactory(),
        "2": MotorcycleFactory(),
        "3": TruckFactory()
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
