# Import interního modulu datetime pro práci s daty a časy
import datetime

# Import funkce easter z externího modulu dateutil pro výpočet data Velikonoc
from dateutil.easter import easter

# Definice funkce, která provede tři úkoly: výpis aktuálního času, Velikonoc a roku, kdy je Štědrý den v neděli
def holiday_dates():
    # 1. Výpis aktuálního data a času
    # Získání aktuálního data a času pomocí funkce now() z modulu datetime
    current_datetime = datetime.datetime.now()
    # Výpis aktuálního data a času
    print("Aktuální datum a čas:", current_datetime)

    # 2. Výpočet velikonoční neděle v následujících 5 letech
    # Získání aktuálního roku z objektu current_datetime
    current_year = current_datetime.year
    # Výpis textu, který informuje o tom, že budou zobrazeny datumy Velikonoc
    print("\nVelikonoční neděle v následujících 5 letech:")
    # Smyčka, která iteruje přes následujících 5 let (včetně aktuálního)
    for year in range(current_year, current_year + 5):
        # Výpočet data velikonoční neděle pro daný rok pomocí funkce easter()
        easter_date = easter(year)
        # Výpis výsledku (rok a datum Velikonoc pro tento rok)
        print(f"{year}: {easter_date}")

    # 3. Nalezení nejbližšího roku, kdy bude Štědrý den v neděli
    # Inicializace proměnné, která bude obsahovat nejbližší rok, kdy bude 25. prosinec v neděli
    next_christmas_sunday_year = None
    # Smyčka, která prohledává následujících 20 let (od aktuálního roku)
    for year in range(current_year, current_year + 20):
        # Kontrola, zda je 25. prosinec daného roku neděle
        if datetime.date(year, 12, 25).weekday() == 6:  # 6 představuje neděli
            # Uložení roku, kdy je Štědrý den v neděli, a ukončení smyčky
            next_christmas_sunday_year = year
            break

    # Výpis výsledku - rok, kdy bude Štědrý den v neděli
    print(f"\nNejbližší rok, kdy bude Štědrý den v neděli: {next_christmas_sunday_year}")

# Zavolání funkce, aby se provedly všechny výpočty a výpisy
holiday_dates()
