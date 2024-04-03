import csv
import random

# Functie om willekeurige data te genereren met een extreem laag valrisico
def generate_data(num_samples):
    data = []
    for _ in range(num_samples):
        # Simuleer een extreem laag valrisico door het genereren van zeer beperkte waarden voor yaw, pitch en roll
        yaw = random.uniform(-10, 10)   # Yaw kan variëren van -10 tot 10 graden
        pitch = random.uniform(-5, 5)   # Pitch kan variëren van -5 tot 5 graden
        roll = random.uniform(-5, 5)    # Roll kan variëren van -5 tot 5 graden
        data.append([yaw, pitch, roll])
    return data

# Het genereren van 100 samples van data
data = generate_data(100)

# Het schrijven van de data naar een CSV-bestand
with open('extreem_laag_valrisico_data3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Schrijf de kolomkoppen
    writer.writerow(['Yaw', 'Pitch', 'Roll'])
    # Schrijf de data
    writer.writerows(data)

print("CSV-bestand met data met extreem laag valrisico is gegenereerd.")
