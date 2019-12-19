import requests
import json
import os
from bs4 import BeautifulSoup

dataset = []


def get(url):
    user_agent_text = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
    headerdict = {"User-Agent": user_agent_text}
    r = requests.get(url, headers=headerdict)
    r.raise_for_status()
    return r


def get_urls(arglist, is_verbose=False):
    for url_en_arg in arglist:
        try:
            r = get(url_en_arg)
        except Exception as e:
            print(f"Erreur de requests vers {url_en_arg}")
            print(str(e))
            r = None
        if r:
            displayurl(r, is_verbose)
            writetodict(r, is_verbose)


F_URL = "url"
F_STATUS = "status_code"
F_HTML = "content"
F_TITLE = "title"


def writetodict(r, is_verbose=False):
    dict = {F_URL: r.url, F_STATUS: r.status_code, F_HTML: r.text[:1000]}
    title = search_title(r.text)
    if title:
        dict[F_TITLE] = title

    # ATTENTION : Dataset est défini en global comme une liste
    global dataset
    dataset.append(dict)


def search_title_by_bs4(text):
    soup = BeautifulSoup(text, "lxml")
    print(soup.title.string)
    
    # ATTENTION CODE DE FIN DE JOURNEE
    d = soup.find_all("h1")
    if d:
        for h1 in d:
            print(f"--> h1 : {h1}")
    d = soup.find_all("h2")
    if d:
        for h2 in d:
            print(f"--> h2 : {h2}")
    # FIN DE CODE DE FIN DE JOURNEE


def search_title(text):
    return search_title_by_bs4(text)
    # DEPRECIATED USE BEAUTIFULL SOUP INSTEAD
    retbuffer = begin = 0
    end = None
    begin = text.find("<title>")
    if begin != -1:
        begin += len("<title>")
        end = text[begin:].find("</title>")
        if end != -1:
            end += begin
            retbuffer = text[begin:end]
    print(f"Test search_title : {begin}, {end}, {retbuffer}")
    return retbuffer
            

def displayurl(r, is_verbose=False):
    print(f"->> Il y a {len(r.text)} octets and {r.url}")
    if is_verbose:
        print(r.status_code)
        # pprint.pprint(r.headers, indent=4)
        # print(json.dumps(r.headers))
        for key, value in r.headers.items():
            print(f"{key} : {value}")
        print("-" * 30)
        print(r.text[:1000])
        print("-" * 30)


if __name__ == "__main__":
    ltqp = ["matin", "midi", "soir", "minuit", "aube"]
    for item in ltqp:
        print(item)

    listedesurls = [
        "https://www.midilibre.fr/",
        "https://www.objectifgard.com/",
        "https://www.20minutes.fr/",
    ]

    get_urls(listedesurls, False)

    # ATTENTION : dataset est défini en global comme une liste
    print(len(dataset))

    # affiche le nom du fichier .py
    print(__file__)
    # affiche le répertoire absolue pour le système d'exploitation
    print(os.path.abspath(__file__))
    # affiche le répertoire contenant le fichier .py
    print(os.path.dirname(__file__))
    # récupère le répertoire dans la configuration du système d'exploitation
    basedir = os.path.abspath(__file__)
    print(basedir)
    # création du fichier checkurl.json dans le répetoire scrap
    filename = basedir + "/" + "checkurl.json" 
    with open("test.json", "w", encoding="utf8") as f:
        json.dump(dataset, f)
        print(f"file {filename} created !")

# CES TROIS LIGNES EQUIVALENT AUX DEUX LIGNES DU with
# f = open ("test.json", "w+", encoding="utf8")
# json.dump(dataset, f)
# f.close()
