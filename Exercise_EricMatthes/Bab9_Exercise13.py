from random import randint

class Dice:
    """Class untuk memodelkan sebuah dadu."""

    def __init__(self, sides=6):
        """Inisialisasi jumlah sisi dadu (default: 6 sisi)."""
        self.sides = sides

    def roll_die(self):
        """Mengembalikan nilai acak antara 1 dan jumlah sisi dadu."""
        return randint(1, self.sides)


# 1. Dadu 6 sisi (diulang 10 kali)
dice_6 = Dice(6)
results_6 = []
for _ in range(10):
    results_6.append(dice_6.roll_die())
print(f"Hasil lemparan dadu 6 sisi (10x): {results_6}")


# 2. Dadu 10 sisi (diulang 10 kali)
dice_10 = Dice(10)
results_10 = []
for _ in range(10):
    results_10.append(dice_10.roll_die())
print(f"Hasil lemparan dadu 10 sisi (10x): {results_10}")


# 3. Dadu 20 sisi (diulang 10 kali)
dice_20 = Dice(20)
results_20 = []
for _ in range(10):
    results_20.append(dice_20.roll_die())
print(f"Hasil lemparan dadu 20 sisi (10x): {results_20}")