try_again = 'y'
while try_again == 'y' or try_again == '':
    dotaznik = input("Dokázalo lidstvo už prolomit aerodynamický třesk ?")
    if (dotaznik == 'ano'):
        print("Správně dostáváte bezvýznamné plus")
    elif (dotaznik == "ne"):
        print("Špatná odpověď")
    else:
        print("Zadej ano nebo ne !!!\n")
        continue
    dotaznik2 = input("Je země kulatá ?")
    if (dotaznik == 'ano'):
        print("Správně dostáváte bezvýznamné plus")
    elif (dotaznik == "ne"):
        print("Špatná odpověď")
    else:
        print("Zadej ano nebo ne !!!\n")
        continue
    dotaznik3 = input("Je slunce hvězda?")
    if (dotaznik == "ano"):
        print("Správně dostáváte bezvýznamné plus")
    elif (dotaznik == "ne"):
        print("Špatná odpověď")
    else:
        print("Zadej ano nebo ne !!!\n")
    dotaznik4 = input("Je pravda, že většina oceánů je dosud neprozkoumaná?")
    if (dotaznik == "ano"):
        print("Správně dostáváte bezvýznamné plus")
    elif (dotaznik == "ne"):
        print("Špatná odpověď")
    else:
        print("Zadej ano nebo ne !!!\n")
    try_again = input("Chcete odpovídat znova? [Y/n]")
