'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

# Konstanty
EARTH_GRAVITY = 9.81  # m/s^2, normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62   # m/s^2, měsíční gravitace
SPEED_OF_LIGHT = 299_792_458  # m/s, rychlost světla ve vakuu
SPEED_OF_SOUND = 343          # m/s, rychlost zvuku při 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

# Výpočtové funkce
def free_fall_time(distance, gravity=EARTH_GRAVITY):
    """
    Vypočítá čas volného pádu pro danou vzdálenost a gravitaci.
    :param distance: Vzdálenost volného pádu (v metrech).
    :param gravity: Hodnota gravitačního zrychlení (výchozí je pozemská gravitace).
    :return: Čas volného pádu (v sekundách).
    """
    if distance < 0:
        raise ValueError("Vzdálenost musí být nezáporná.")
    return (2 * distance / gravity) ** 0.5

def energy_of_light_mass(mass):
    """
    Vypočítá energii tělesa podle jeho hmotnosti za využití vztahu E=mc^2.
    :param mass: Hmotnost tělesa (v kilogramech).
    :return: Energie (v joulech).
    """
    return mass * SPEED_OF_LIGHT ** 2

def sound_travel_time(distance):
    """
    Vypočítá čas potřebný pro zvuk na urazení určité vzdálenosti při teplotě 20 °C ve vzduchu.
    :param distance: Vzdálenost (v metrech).
    :return: Čas (v sekundách).
    """
    return distance / SPEED_OF_SOUND

def moon_weight(mass):
    """
    Vypočítá váhu tělesa na Měsíci.
    :param mass: Hmotnost tělesa (v kilogramech).
    :return: Váha na Měsíci (v newtonech).
    """
    return mass * MOON_GRAVITY


