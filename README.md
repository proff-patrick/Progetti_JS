# Tracce proposte

## Progetto da 6.5 punti: form di registrazione

### Descrizione generale
Si vuole implementare una pagina web che rappresenti un form di registrazione a un sito a scelta. 
### HTML
La pagina dovrà essere composta da un titolo e da almeno:
- Cinque textbox.
- Una serie di checkbox e una serie di radio-button.
- Un campo relativo a una data e uno relativo a una password.
- Un campo composto da un menu a dropdown.
- Un bottone di reset e uno di conferma.   

Ogni componente dovrà avere un testo di default e/o una label che faccia capire cosa inserire in quel campo.

### CSS
Non vi sono particolari richieste. Il form dovrà comunque apparire gradevole da vedere, sia nel complesso sia considerando i singoli campi. 

### JavaScript
Sono richieste almeno le seguenti funzionalità:
- Controllo campo di conferma: esempio, controllare che mail e conferma mail siano uguali.
- Requisiti password: esempio, controllare che la password sia composta tra 5 e 10 caratteri, che contenga almeno un numero, almeno un simbolo e almeno una maiuscola.
- Password nascosta e visibile: prevedere un bottone che, al click, renda nascosta o visibile il contenuto del campo password.
- Campi obbligatori: esempio, non consentire di registrarsi se non si ha inserito un username.

Le funzionalità possono essere eseguite al click del bottone di conferma, ma almeno una deve essere verificata in fase di compilazione vedendo l’errore accanto al campo. 
In ogni caso, al click del bottone finale si dovranno prevedere due stati: registrazione effettuata con successo, se tutti i controlli sono andati a buon fine, o segnalare l’errore riscontrato in caso contrario.

### Esempio
L’immagine sottostante è totalmente a scopo esemplificativo. **NON DOVETE RIPRODURRE QUESTO**, in quanto mancano anche alcune parti richieste dalla traccia.

![image](https://github.com/user-attachments/assets/84189e31-4f26-4922-ae04-6ba186fbe635)


## Progetto da 8.25 punti: piattaforma quiz

### Descrizione generale
Si vuole implementare una pagina web che somministri piccoli quiz di un argomento generico all’utente.
### HTML
Il sito dovrà comporsi di una home iniziale, nella quale permettere all’utente di scegliere quale quiz svolgere. Successivamente inizierà il quiz, in cui in ogni pagina ci sarà:
- Il titolo del quiz.
- La domanda a cui rispondere attualmente.
- Le quattro opzioni di risposta, di cui una e una sola corretta.
- I pulsanti domanda successiva, domanda precedente e invia.

### CSS
Non vi sono particolari richieste. Il quiz dovrà comunque apparire graficamente gradevole: a tal fine sarebbe opportuno dare, oltre che generalmente alla pagina, uno stile specifico per i pulsanti, la domanda e i bottoni per le risposte.

### JavaScript
Sono richieste almeno le seguenti funzionalità principali (o anche altre che vi vengono in mente e che siano opportune):
- Salvataggio domande: le domande devono essere contenute in opportune strutture dati, in modo da essere facilmente cambiabili e accessibili per la stampa a schermo.
- Stampa domande: le domande devono essere mostrate una dopo l’altra, consentendo di potersi muovere tra le domande tramite i pulsanti domanda successiva e domanda precedente. Sarebbe opportuno anche stampare il numero della domanda (es. 1 di 10).
- Pulsanti mostrati: mostrare i pulsanti solo quando necessario. Per esempio, non mostrare il pulsante domanda precedente se stiamo visualizzando la prima domanda.
- Invio risposte: cliccando sul pulsante invia risposte, deve essere calcolato quali risposte erano corrette e quali no (domande senza risposta sono da considerarsi scorrette). A tal fine si deve:
  - Visualizzare il numero e la percentuale di risposte esatte.
  - Si deve poter nuovamente scorrere tra le domande, visualizzando le risposte corrette in verde, mentre per quelle errate deve venir visualizzato in rosso la risposta data e invece in verde quella che era effettivamente corretta.
 
### Esempio
L’immagine sottostante è totalmente a scopo esemplificativo. **NON DOVETE RIPRODURRE QUESTO**, in quanto mancano anche alcune parti richieste dalla traccia.

 ![image](https://github.com/user-attachments/assets/4ddcbc7e-ac88-4037-a16d-ad1204a1c9db)

 
## Progetto da 8.25 punti: UwUFUFU Film

### Descrizione generale
Si vuole implementare un competitor del sito UwUFUFU. I quiz di UwUFUFU sono un modo divertente per decretare i migliori esponenti su vari temi come anime, giochi o persone. Ogni quiz presenta una serie di confronti tra due elementi e l’utente vota quello che preferisce tra i due in un torneo a eliminazione diretta: gli elementi che vengono votati avanzano al turno successivo, mentre quelli non scelti vengono eliminati. Questo processo continua fino a determinare un vincitore assoluto.
### HTML
Il sito dovrà comporsi di una home iniziale, nella quale permettere all’utente di scegliere tra alcuni parametri per il torneo come:
- Su cosa deve essere il torneo: si potrebbe permettere di scegliere un genere, un regista, un attore, un anno, i migliori film di sempre o un torneo generico.
- Il numero di elementi partecipanti al torneo (un numero comunque congruo a un torneo a eliminazione diretta).
  
Una volta scelto il tipo di torneo, occorrerà presentare di volta in volta i due sfidanti attuali, il numero di round attuale e il numero di sfida attuale interna al round. Si potrebbe anche pensare di mostrare al di sotto, in piccolo, tutti gli sfidanti, differenziando tra quelli ancora in gioco e quelli eliminati.

### CSS
Non vi sono particolari richieste. Il torneo dovrà comunque apparire graficamente gradevole, visivamente coinvolgente e simmetrico.

### JavaScript
Le funzionalità previste sono le principali del UwUFUFU, riassunte di seguito. Potete e siete invitati ad aggiungere altre funzionalità che rendano il vostro gioco unico rispetto allo UwUFUFU originale.
- Gestione del torneo: una volta selezionato il tipo di torneo e il numero di partecipanti, vengono estratti casualmente un numero congruo di film che rispetti il tipo selezionato e, sulla base di essi, viene generato un torneo di duelli casuali.
- Duelli: per ogni sfida, vengono mostrate le due locandine e i titoli dei film, uno accanto all’altro. L’utente deve poter aprire la pagina IMDB del film per approfondimenti, ma soprattutto deve poter scegliere il suo preferito tra i due. Una volta selezionato, esso passa il turno e viene presentato il prossimo duello.
- Progressione: deve essere chiaro, in ogni momento, a che punto del torneo ci troviamo. Potrebbe essere utile anche un resoconto visivo delle sfide fatte e di quelle rimanenti.
- Vittoria: prevedere una schermata finale in cui venga glorificato il vincitore finale e venga scelto di fare una nuova partita.

### Materiale 
Viene fornito, nella cartella "Materiale Film", un vettore contenente circa 1800 film con le loro caratteristiche principali e una cartella con le annesse locandine.

### Esempio
In caso non si conosca il sito, attualmente lo hanno chiuso, quindi cercare qualche video su Youtube che è pieno (uno di esempio: https://www.youtube.com/watch?v=wPtsqFKOy7c&ab_channel=DarioMocciaArchives). **NON DOVETE RIPRODURRE IL SITO ORIGINALE**, dovete anzi cercare di mantenere l’idea di base e possibilmente migliorarla.


## Progetto da 10 punti: Wordle

### Descrizione generale
Si vuole implementare una propria versione del gioco online Wordle: esso consiste nel cercare di indovinare una parola composta da n lettere, ricevendo a ogni tentativo indizi circa la presenza e la posizione delle lettere della parola scritta nella parola da indovinare.
Si vuole chiedere inizialmente la difficoltà del gioco (questa fa variare il numero di tentativi disponibili) e la lunghezza della parola in lettere.
### HTML:
La pagina dovrà essere composta da (linee guida, non è essenziale seguirle purché venga un sito corretto):
- Il titolo del sito.
- X righe (X è il numero di tentativi scelto) di ciascuna Y textbox (Y è la lunghezza della parola scelta) in cui inserire le lettere
- Opzionalmente, la tastiera a schermo al di sotto (evitabile, è consigliato farlo eventualmente alla fine)
### CSS:
Non vi sono particolari richieste. Il gioco dovrà comunque apparire minimale ed elegante, poco affaticante alla vista dal punto di vista grafico.
### JavaScript:
Le funzionalità previste sono le principali del gioco Wordle, riassunte di seguito. Potete e siete invitati ad aggiungere altre funzionalità che rendano il vostro gioco unico rispetto al Wordle originale.
- Inserimento delle lettere: l’inserimento delle lettere per creare le parole deve essere semplice e immediato, così come non deve essere permesso di sovrascrivere celle di parole già confermate (ovvero, si può scrivere solo nell’ultima riga disponibile). L’inserimento potrebbe essere fatto sia da tastiera che usando una tastiera virtuale stampata a schermo.
- Suggerimenti: a ogni parola confermata, vengono dati suggerimenti sulla base di essa e della parola da indovinare. Ogni lettera può essere non presente nella parola, presente ma nel posto sbagliato o presente ma nel posto giusto (evidenziare graficamente in modo chiaro le tre situazioni).
- Parole corrette: devono essere accettate solo parole appartenenti alla lingua italiana.
- Vittoria o termine tentativi: se la parola viene indovinata, comunicare la vittoria dell’utente; se viene inserita anche la sesta parola senza indovinare, viene comunicata la sconfitta dell’utente. In entrambi i casi, stampare la parola che era da indovinare.
### Materiale
Viene fornito, nella cartella "Materiale Wordle", un vettore contenente circa 60.000 parole italiane.
### Esempio generale:
Il sito sottostante è totalmente a scopo esemplificativo. **NON DOVETE RIPRODURRE QUESTO** ma crearne una vostra versione personalizzata.
https://pietroppeter.github.io/wordle-it/

## Progetto da 10 punti: Snake
### Descrizione generale
Si vuole implementare una propria versione del gioco Snake.
### HTML:
La pagina dovrà essere composta da (linee guida, non è essenziale seguirle purché venga un sito corretto):
- Una griglia, il campo da gioco, composta da un numero fisso di celle (ad esempio 20x20).
- All’interno della griglia dovrà figurare il serpente e un cibo alla volta.
- Un pulsante per iniziare la partita.
- Una sezione per visualizzare il punteggio corrente e il miglior punteggio ottenuto.
### CSS:
Non vi sono particolari richieste. Il gioco dovrà comunque apparire piacevole e divertente, permettendo di riconoscere visivamente in modo immediato i diversi elementi del gioco.
### JavaScript:
Le funzionalità previste sono le principali del gioco Snake, riassunte di seguito. Potete e siete invitati ad aggiungere altre funzionalità che rendano il vostro gioco unico rispetto allo Snake originale.
- Inizio partita: cliccando sul pulsante “Nuova partita” il gioco inizia generando un serpente di una sola casella e il primo cibo casuale.
- Movimento del Serpente: gestisci il movimento del serpente tramite i tasti direzionali (su, giù, sinistra, destra). Il serpente deve muoversi in un’unica direzione alla volta e non può invertire la direzione (ad esempio, non puoi muoverti da destra a sinistra senza passare prima per il movimento verso l’alto). Si noti come il serpente dovrà muoversi in automatico, avanzando di una casella dopo un tempo costante nella direzione scelta della freccia.
- Cibo: aggiungi un cibo che appare in una posizione casuale sulla griglia (si noti che non può apparire sul serpente). Ogni volta che il serpente mangia il cibo, il serpente cresce e il punteggio aumenta.
- Oggetti speciali: ogni 5 cibi mangiati, potrebbe apparire un cibo speciale! Inoltre, andando avanti con il gioco, potrebbero apparire degli ostacoli casuali in modo da rendere il gioco ancora più difficile!
- Punteggio: mostra il punteggio in tempo reale mentre il gioco è in corso. Ogni volta che il serpente mangia il cibo, aumenta il punteggio di 1.
- Collisioni: il gioco termina se il serpente colpisce i bordi della griglia o se morde sé stesso. In caso di game over, mostra un messaggio di fine gioco e il punteggio finale, aggiornando eventualmente il miglior punteggio ottenuto.
- Grafica: non ci si aspetta una grafica avanzata, ma potresti sfruttare pixel art e immagini per differenziare il cibo, le diverse parti del serpente, gli ostacoli, il momento in cui il serpente sta per mangiare, ecc...

### Esempio
L’immagine sottostante è totalmente a scopo esemplificativo. **NON DOVETE RIPRODURRE QUESTO**, in quanto mancano anche alcune parti richieste dalla traccia.

![image](https://github.com/user-attachments/assets/62e62ffa-2b5a-4e2b-8732-8517b4cf4658)


 


