import requests
import json
import os
from bs4 import BeautifulSoup

dataset = []

"""

soup.find("meta", property="og:title")
soup.find("meta", property="og:description")
soup.find("meta", property="og:image")
soup.find("meta", property="og:url")










"""


def get(url):
    user_agent_text = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"   # variable
    headerdict = {"User-Agent": user_agent_text}  # variable
    r = requests.get(url, headers=headerdict)
    r.raise_for_status()
    return r


def get_urls(arglist, is_verbose=False):
    for url_en_arg in arglist:
        try:
            r = get(url_en_arg)   # variable
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
F_DESCRIPTION = "description"
F_IMAGE = "image"
F_H1 = "items_h1"
F_H2 = "items_h2"


def writetodict(r, is_verbose=False):
    dict_html = {F_URL: r.url, F_STATUS: r.status_code}  # variable
    dict_meta = search_meta_by_bs4(r.text)
    if dict_meta:
        dict_html.update(dict_meta)

    # ATTENTION : Dataset est défini en global comme une liste
    global dataset
    dataset.append(dict_html)


def search_meta_by_bs4(text):
    """search _meta_by_bs4 :
        cette fonction sert à ...
        elle récupère ...
    """
    soup = BeautifulSoup(text, "lxml")  # variable
    dict_meta = dict()

    meta_title = soup.find("meta", property="og:title")
    if not meta_title:
        meta_title = soup.title.string
    else:
        dict_meta[F_TITLE] = meta_title["content"]

    meta_description = soup.find("meta", property="og:description")
    dict_meta[F_DESCRIPTION] = meta_description["content"] if meta_description else ""

    meta_image = soup.find("meta", property="og:image")
    dict_meta[F_IMAGE] = meta_image["content"] if meta_image else ""

    # ATTENTION CODE DE FIN DE MATINEE
    d = soup.find_all("h1")
    if d:
        dict_meta[F_H1] = []
        for h1 in d:
            dict_meta[F_H1].append(h1.text)
            print(f"--> h1 : {h1.text}")
    d = soup.find_all("h2")
    if d:
        dict_meta[F_H2] = []
        for h2 in d:
            dict_meta[F_H2].append(h2.text)
            print(f"--> h2 : {h2}")
    # FIN DE CODE DE FIN DE MATINEE

    print("-" * 100)
    print(type(meta_title))
    print(meta_title["content"])
    return dict_meta
    """
    s = (
        str(meta_title)
        .replace('<meta content="', "") 
        .replace('"property="og:title"/>', "")
    )
    s = str(meta_title)
    begin = s.find('content="')
    if begin != -1:
        end = s.find('"', begin)
        if end != -1
            s = s[begin:end]

    print(s)
    print("-" * 100)
    return s

    meta_description = soup.find("meta", property = "og:description")
    meta_image = soup.find("meta", property = "og:image")
    meta_url = soup.find("meta", property = "og:url")
    return meta_title
    """
    
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


"""
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
"""
            

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
        "https://www.20minutes.fr/",
        "https://www.mediapart.fr/",
        "https://www.marianne.net/",
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
    basedir = os.path.dirname(os.path.abspath(__file__))
    print(basedir)
    # création du fichier checkurl.json dans le répetoire scrap

    dataset_api = {"count": len(dataset), "dataset": dataset}

    filename = basedir + "/" + "checkurl.json" 
    with open(filename, "w", encoding="utf8") as f:
        json.dump(dataset_api, f)
        print(f"file {filename} created !")

# CES TROIS LIGNES EQUIVALENT AUX DEUX LIGNES DU with
# f = open ("test.json", "w+", encoding="utf8")
# json.dump(dataset, f)
# f.close()
