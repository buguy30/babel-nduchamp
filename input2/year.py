import datetime


def controller_input():
 
    while True:
        year = input("Année > ")
        if not year:
            print("Au revoir")
            break
        valyear = validate_year(year)
        if valyear:
            display_line_year(valyear)
        else:
            print(f"Error in the format of {year}")


def validate_year(valyear):
    """
    validate_year - validation d'une string en int
    """
    dt = datetime.datetime.now()
    todyear = dt.year
    if isinstance(valyear,str):
        try:
            valyear = int(valyear)
        except ValueError:
            # print(str(e))
            return None

    # logique de siècle 1900 / 2000
    if valyear < 100:
        todyear -= 2000
        if valyear <= todyear:
            valyear += 2000
        else:
            valyear += 1900

    return valyear


def display_line_year(valyear):
    """
    display_line_year - affichage de l'année
    """
    dt = datetime.date.today()
    diffyear = dt.year - valyear
    diffdt = dt - datetime.date(valyear, 1, 1)
    print(f"Année de naissance {valyear}, il y a {diffyear} ans ou {diffdt.days} jours")


if __name__ == "__main__":
    controller_input()
