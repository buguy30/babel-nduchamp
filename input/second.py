# Second traitement

# INPUT
# VALIDATION
# AFFICHAGE

import re


def manage_input():
    in_fullname = input("Entrez votre nom et votre prénom\n")
    names = validate(in_fullname)
    if "error" in names:
        print(names["error"])
    else:
        print(names)


F_FIRST = "firstname"
F_LAST = "lastname"
F_MIDDLE = "middlename"
F_FULL = "fullname"
F_ERROR = "error"


def validate_string(input):
    """ si la string input contient juste des caratères A-Z,
        renvoie True, sinon False
    """
    # si vide
    # enlève les espaces
    # regarde si AZ ou az
    print(input)
    if not len(input):
        return False
    r = re.match("^[A-Za-z]+$", input)
    print(r)
    return True if r else False


def validate(fullname):
    """ validation et affichage d'une string 
        selon format Prénom <Milieu> Nom 
    """
    names = fullname.split()
    len_listnames = len(names)
    # vérifier que chaque string de names ne comporte que des lettres de l'alphabet
    type(names)
    for n in names:
        n = n.strip()  # enlève les espaces devant, derrière
        if not validate_string(n):
            return {F_ERROR: "Erreur de validation sur " + n}

    d = {}
    if len_listnames == 2:
        d[F_FIRST] = names[0]
        d[F_LAST] = names[1]
    elif len_listnames == 3:
        d[F_FIRST] = names[0]
        d[F_MIDDLE] = names[1]
        d[F_LAST] = names[2]
    elif len_listnames == 1:
        d[F_LAST] = names[0]
    else:
        error = "Format : Prénom <Milieu> Nom\n"
        if len_listnames == 0:
            error += "valeur manquante"
        else:
            error += "Que faire de : " + " ".join(names[3:])
        d[F_ERROR] = error
    return d


def validate_display(fullname):
    """
    Validation et affichage d'une string dans le format Prénom Particule Nom
    """
    l = len(fullname)
    names = fullname.split(" ")
    if l == 2:
        print("Prénom : {}, Nom : {}".format(names[0], names[1]))
    elif l == 3:
        print(
            "Prénom : {}, Particule : {}, Nom : {}".format(names[0], names[1], names[2])
        )
    elif l == 1:
        print("Nom seul : {}".format(names[0]))
    else:
        print("Format : Prénom, particule, nom")
        print("Que faire de : " + " ".join(names[3:]))


if __name__ == "__main__":
    manage_input()
