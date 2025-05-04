import pandas as pd
import sqlite3

# Carica i dati da Excel
df = pd.read_excel("utenti.xlsx")

# Connessione al database SQLite
conn = sqlite3.connect('database_utenti.db')
cursor = conn.cursor()

# Crea la tabella
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        ID TEXT PRIMARY KEY,
        CodiceFiscale TEXT,
        Nome TEXT,
        Cognome TEXT,
        Email TEXT UNIQUE,
        Telefono TEXT UNIQUE,
        LuogoNascita TEXT,
        DataNascita TEXT,
        PEC TEXT,
        Indirizzo TEXT,
        Civico TEXT,
        Città TEXT,
        Provincia TEXT,
        CAP TEXT,
        Nazione TEXT,
        Mansione TEXT
    )
''')

# Inserisce i dati nel database
for _, row in df.iterrows():
    cursor.execute('''
        INSERT OR IGNORE INTO utenti (
            ID, CodiceFiscale, Nome, Cognome, Email, Telefono, LuogoNascita, DataNascita, PEC, Indirizzo, Civico, Città, Provincia, CAP, Nazione, Mansione
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        row['ID'],
        row['Codice Fiscale'],
        row['Nome'],
        row['Cognome'],
        row['Email'],
        row['Numero di telefono'],
        row['Luogo di nascita'],
        row['Data di nascita'],
        row.get('PEC', ''),
        row['Indirizzo'],
        row['Civico'],
        row['Città'],
        row['Provincia'],
        row['CAP'],
        row['Nazione'],
        row['Mansione']
    ))

# Salva e chiude la connessione
conn.commit()
conn.close()
