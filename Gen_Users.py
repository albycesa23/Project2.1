import random
from faker import Faker
import pandas as pd
import uuid

# Faker  italiano
fake = Faker('it_IT')

# Mansioni e province predefinite
mansioni = ['Impiegato', 'Manager', 'Tecnico', 'Consulente', 'Operaio', 'Direttore', 'Analista']
province = ["Milano", "Roma", "Torino", "Napoli", "Firenze", "Bologna", "Palermo", "Genova"]

# Costruzione del dizionario dati
data = {
    "ID": [str(uuid.uuid4()) for _ in range(10)],
    "Codice Fiscale": [fake.ssn() for _ in range(10)],
    "Nome": [fake.first_name() for _ in range(10)],
    "Cognome": [fake.last_name() for _ in range(10)],
    "Email": [fake.email() for _ in range(10)],
    "Numero di telefono": [fake.phone_number() for _ in range(10)],
    "Luogo di nascita": [fake.city() for _ in range(10)],
    "Data di nascita": [fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%d/%m/%Y") for _ in range(10)],
    "PEC": ["" for _ in range(10)],
    "Indirizzo": [fake.street_name() for _ in range(10)],
    "Civico": [str(fake.building_number()) for _ in range(10)],
    "Città": [fake.city() for _ in range(10)],
    "Provincia": [random.choice(province) for _ in range(10)],
    "CAP": [fake.postcode() for _ in range(10)],
    "Nazione": ["Italia" for _ in range(10)],
    "Mansione": [random.choice(mansioni) for _ in range(10)]
}

# Creazione del DataFrame e salvataggio su Excel
df = pd.DataFrame(data)
df.to_excel("utenti.xlsx", index=False)
