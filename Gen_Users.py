import random
from faker import Faker
import pandas as pd

# Utilizzo due faker di cui uno localizzato per il territorio italiano
fake = Faker('it_IT')

# Definisco delle mansioni da far scegliere al codice
mansioni = ['Impiegato', 'Manager', 'Tecnico', 'Consulente', 'Operaio', 'Direttore', 'Analista']

# Definisco le provincie da far scegliere al codice
province = ["Milano", "Roma", "Torino", "Napoli", "Firenze", "Bologna", "Palermo", "Genova"]


data = {
    "Codice Fiscale": [fake.ssn() for _ in range(10)],
    "Nome": [fake.first_name() for _ in range(10)],
    "Cognome": [fake.last_name() for _ in range(10)],
    "Email": [fake.email() for _ in range(10)],
    "Numero di telefono": [fake.phone_number() for _ in range(10)],
    "Luogo di nascita": [fake.city() for _ in range(10)],
    "Data di nascita": [fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%d/%m/%Y") for _ in range(10)],
    "PEC": ["" for _ in range(10)],  # Lascio la possibilità di lasciare il campo vuoto
    "Indirizzo": [fake.street_name() for _ in range(10)],
    "Civico": [str(fake.building_number()) for _ in range(10)],
    "Città": [fake.city() for _ in range(10)],
    "Provincia": [random.choice(province) for _ in range(10)],
    "CAP": [fake.postcode() for _ in range(10)],
    "Nazione": ["Italia" for _ in range(10)],  # Supponendo siano tutti nati in Italia
    "Mansione": [random.choice(mansioni) for _ in range(10)]
}

df = pd.DataFrame(data)

df.to_excel("utenti.xlsx", index=False)