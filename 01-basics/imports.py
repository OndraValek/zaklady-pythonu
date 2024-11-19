'''
Importování modulů v Pythonu

Větší programy je žádoucí členit do samostatných modulů.
Modul je soubor obsahující definice a příkazy v Pythonu.
Moduly v Pythonu jsou uloženy v samostatných souborech s příponou .py.
Definice uvnitř modulů mohou být importovány do jiných modulů nebo do interaktivní pythonovské konzoly.
Připojení modulů provádíme klíčovým slovem import.
'''

'''
Příklad importu modulu math. V tomto případě můžeme pomocí tečkového operátoru využít všechny atributy a funkce,
které nám modul math nabízí.
'''
import math
print(math.pi)
print('Goniometrické funkce: sin 45° = {}, cos 45° = {}'.format(math.sin(45), math.cos(45)))

'''
Příklad importu modulu sys a jedné jeho funkce path. Použijeme k tomu konstrukci:
from jméno_modulu import jméno_funkce
'''

from sys import path
print(path) # Zobrazuje seznam (list) cest k adresářům, které aplikace využívá

'''
Moduly math a sys patří k interním modulům, jež jsou součástí standardní instalace Pythonu.
Externí moduly jsou distribuovány systémem balíčků (packages) a musí být instalovány pomocí nástroje pip.

pip install <jméno_balíčku>

Balíček můžeme odinstalovat příkazem:

pip uninstall <jméno_balíčku>

Používáme-li virtuální prostředí (virtual environment), jsou nainstalované balíčky ukládány v adresáři tohoto prostředí
(v našem případě venv) v podsložkách Lib a site-packages.

Přehled všech instalovaných balíčků získáme příkazem:

pip list

Můžeme také vytvořit soubor requirements.txt, který obsahuje záznam všech tzv. závislostí naší aplikace - čili 
informace o všech balíčcích, které je nutné do virtuálního prostředí nainstalovat, aby aplikace mohla fungovat.
Vytvoření souboru requirements.txt provedeme příkazem:

pip freeze > requirements.txt

Zobrazení podrobnějších informací o některém z nainstalovaných balíčků získáme příkazem:

pip show <jméno_balíčku>

Automatickou instalaci všech závislostí zaznamenaných v souboru requirements.txt provedeme příkazem:

pip install -r requirements.txt     
'''

# V konzoli virtuálního prostředí proveďte instalaci externího balíčku camelcase
# (venv) E:\python\projekt\venv>pip install camelcase
# Poté tento balíček importujte
import camelcase
c = camelcase.CamelCase() # Konstruktor třídy CamelCase() vytvoří objekt v proměnné c
txt = 'ahoj světáku'
print(c.hump(txt)) # Metoda hump() přeformátuje předaný řetězec podle zásad camel syntaxe (velká první písmena slov)

"""
Cvičení 4:

Použijte vhodné moduly v Pythonu (včetně jejich případné instalace) k tomu, abyste: 
1) vypsali aktuální datum a čas
2) vypsali datum velikonoční neděle (easter) v následujících 5 letech
3) vypsali nejbližší rok, v němž bude Štědrý den v neděli

K řešení prvního úkolu je možné doporučit importovat interní modul datetime
Řešení dalších dvou úkolů můžete odvodit z příkladů v dokumentaci k externímu modulu dateutil - viz https://pypi.org/project/python-dateutil/
"""


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

