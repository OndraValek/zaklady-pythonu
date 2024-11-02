# myapp.py

from physics import free_fall_time, energy_of_light_mass, sound_travel_time, moon_weight

# Příklad volného pádu z výšky 20 metrů na Zemi
print("Čas volného pádu z 20 metrů na Zemi:", free_fall_time(20), "s")

# Výpočet energie tělesa o hmotnosti 1 kg
print("Energie tělesa o hmotnosti 1 kg:", energy_of_light_mass(1), "J")

# Čas potřebný pro zvuk na urazení vzdálenosti 343 metrů
print("Čas, za který zvuk urazí 343 metrů:", sound_travel_time(343), "s")

# Výpočet váhy na Měsíci pro těleso o hmotnosti 70 kg
print("Váha tělesa o hmotnosti 70 kg na Měsíci:", moon_weight(70), "N")