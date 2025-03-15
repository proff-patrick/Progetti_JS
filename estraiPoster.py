import pandas as pd
import urllib.request
import re
import json, requests

def estrai_codice(url):
    # Estrai la parte numerica dopo "tt"
    match = re.search(r'tt(\d+)', url)
    
    if match:
        # Ottieni il numero trovato
        numero = match.group(1)
        # Riempi con zeri fino a 7 cifre
        numero_formattato = numero.zfill(7)
        # Ritorna "tt" seguito dal numero formattato
        return f"tt{numero_formattato}"
    else:
        return None  # Se non c'è un match, restituisci None

dataFrame = pd.read_csv('MovieGenre.csv', encoding='ISO-8859-1')
arr = []
with open('lista-film.txt', 'a') as f:
    for index, row in dataFrame.iterrows():
        if index >= 39198:
            print(index)
            imdbIndex = estrai_codice(row['Imdb Link'])
            veroImdbLink = "https://www.imdb.com/it/title/" + imdbIndex
            titolo = row['Title'][:-7]
            annoTemp = row['Title'][-5:-1]
            if annoTemp.isdigit() and len(annoTemp) == 4:
                generiTemp = str(row['Genre'])
                if len(generiTemp) > 0:
                    if "Animation" in generiTemp or int(annoTemp) >= 1980:
                        generi = str(row['Genre']).split('|')
                        anno = int(row['Title'][-5:-1])
                        richiesta = 'https://www.omdbapi.com/?i=' + imdbIndex + '&apikey=936a1781'
                        resp = requests.get(url=richiesta)
                        dataImdb = json.loads(resp.text)    
                        numVoti = dataImdb['imdbVotes'].replace(",", "")
                        if numVoti.isdigit():
                            numVoti = int(numVoti)
                            if numVoti >= 100000:
                                url = dataImdb['Poster']
                                url = re.sub(r'(_SX\d+)', '_SX1000', url)
                                response = urllib.request.urlopen(url)
                                data = response.read()
                                file = open('images/'+ str(imdbIndex)+ '.jpg', 'wb')
                                file.write(bytearray(data))
                                file.close()
                                attori = dataImdb["Actors"].split(", ")
                                regista = dataImdb["Director"].split(",")
                                paese = dataImdb["Country"]
                                boxOffice = dataImdb["BoxOffice"].replace(",", "")
                                boxOffice = boxOffice.replace("$", "")
                                if boxOffice == "N/A":
                                    boxOffice = 0;
                                boxOffice = int(boxOffice)
                                arr = [titolo, anno, imdbIndex, generi, regista, attori, numVoti, paese, boxOffice, veroImdbLink]
                                f.write(repr(arr) + ",\n")