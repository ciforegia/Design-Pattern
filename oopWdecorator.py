from datetime import datetime

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

# Decorator Base Class
class VehicleDecorator(Vehicle):
    def __init__(self, decorated_vehicle):
        self._decorated_vehicle = decorated_vehicle
    
    def display_info(self):
        return self._decorated_vehicle.display_info()

# Concrete Decorators
class CarDecorator(VehicleDecorator):
    def __init__(self, decorated_vehicle, num_seats):
        super().__init__(decorated_vehicle)
        self.num_seats = num_seats
    
    def display_info(self):
        return super().display_info() + f"Jumlah Kursi: {self.num_seats}\n"

class MotorcycleDecorator(VehicleDecorator):
    def __init__(self, decorated_vehicle, engine_capacity):
        super().__init__(decorated_vehicle)
        self.engine_capacity = engine_capacity
    
    def display_info(self):
        return super().display_info() + f"Kapasitas Mesin: {self.engine_capacity} cc\n"

class TruckDecorator(VehicleDecorator):
    def __init__(self, decorated_vehicle, cargo_capacity):
        super().__init__(decorated_vehicle)
        self.cargo_capacity = cargo_capacity
    
    def display_info(self):
        return super().display_info() + f"Kapasitas Muatan: {self.cargo_capacity} kg\n"

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
            
            vehicle = Vehicle(brand, manufacture_date, price, mileage, features)
            
            if choice == "1":
                num_seats = int(input("Masukkan jumlah kursi: "))
                vehicle = CarDecorator(vehicle, num_seats)
            elif choice == "2":
                engine_capacity = float(input("Masukkan kapasitas mesin (cc): "))
                vehicle = MotorcycleDecorator(vehicle, engine_capacity)
            elif choice == "3":
                cargo_capacity = int(input("Masukkan kapasitas muatan (kg): "))
                vehicle = TruckDecorator(vehicle, cargo_capacity)
            else:
                print("Pilihan tidak valid.")
                continue
            
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
