<div align="center">
 <h1> 📚 Book Management </h1>
</div>

![screenshot](https://raw.githubusercontent.com/angelof-exe/flask-library/main/screenshot/screenshot.png)


## Indice
- [Riguardo al progetto](#riguardo-al-progetto)
    - [Creato con](###Built-with)
- [Installazione e Setup](##installazione-e-Setup)
    - [Prerequisiti](###prerequisiti)
    - [Installazione](###installazione)
- [Utilizzo](##utilizzo)

## Riguardo al progetto

WebApp realizzata in **Flask**, permette di aggiungere dei libri all'interno di una libreria o anche di rimuoverli tramite interfaccia Web. I libri vengono immagazzinati in un DataBase gestito con **MySQL**.

### Creato con
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [MySQL](https://www.mysql.com/it/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)

## Installazione e Setup

### Prerequisiti

- Python
- Avviare un server MySQL

**❗ Importante**: Per poter utilizzare la libreria `flask_mysqldb` sarà necessario installare delle dipendenze:
```
sudo apt-get install python-dev default-libmysqlclient-dev libssl-dev
```


Per ulteriori informazioni consultare la documentazione di [flask_mysqldb](https://pypi.org/project/Flask-MySQLdb/) e [questa domanda su StackOverflow](https://stackoverflow.com/questions/58957474/how-to-install-flask-mysqldb-for-python)

### Installazione
1. Clona la repo
`git clone https://github.com/angelof-exe/flask-library.git`

2. Crea un ambiente virtuale e attivarlo _(Opzionale)_ 
```
python3 -m venv venv

. venv/bin/activate
```
Per altre informazioni consulare la [documentazione di Python sul come creare ambienti virtuali.](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

3. Installare i moduli necessari:

```
    pip3 install -r requirements.txt
```
4. Fai partire lo script `library_book.sql` sul tuo server MySQL

## Utilizzo
Avvia il file app.py tramite `python3 app.py`. 

Il server verra avviato all'indirizzo ` http://127.0.0.1:8000`
 
