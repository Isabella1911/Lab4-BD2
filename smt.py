import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
cliente = MongoClient(os.getenv('MONGO_URI'))
db = cliente["lab4_analytics"]
collection = db["dinero"]

# Leer CSV
df = pd.read_csv("money.csv")

# Limpiar nombres
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Reemplazar NaN por None (esencial para MongoDB)
df = df.where(pd.notnull(df), None)

# Insertar
collection.insert_many(df.to_dict("records"))
print(f"✅ {len(df)} documentos insertados")