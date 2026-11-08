# 1. Class Car (Parent Class)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


# 2. Class Battery (Komposisi)
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini memiliki kapasitas baterai {self.battery_size}-kWh.")

    def get_range(self):
        if self.battery_size == 75:
            range_miles = 260
        elif self.battery_size == 100:
            range_miles = 315

        print(f"Mobil ini dapat menempuh jarak sekitar {range_miles} mil saat baterai penuh.")

    # Method baru untuk Latihan 9-9
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print("Baterai berhasil di-upgrade ke 100 kWh!")
        else:
            print("Baterai sudah mencapai kapasitas maksimum (100 kWh).")


# 3. Class ElectricCar (Child Class)
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# Uji Coba Kode

# Buat mobil listrik baru
my_tesla = ElectricCar ("Tesla", "Model X", 2025)
print(my_tesla.get_descriptive_name())

# Cek jarak tempuh sebelum upgrade baterai
print("\n[Sebelum Upgrade]")
my_tesla.battery.get_range()

# Upgrade baterai
print("\n[Proses Upgrade]")
my_tesla.battery.upgrade_battery()

# Cek jarak tempuh setelah upgrade baterai
print("\n[Setelah Upgrade]")
my_tesla.battery.get_range()