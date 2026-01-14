from pymongo import MongoClient
import json

# 1. Buka file JSON
with open("ai_datajobs_1.json", "r") as file:
    data = json.load(file)

# 2. Koneksi ke MongoDB
# Pastikan MongoDB sudah berjalan (default port 27017)
client = MongoClient("mongodb://localhost:27017/")

# 3. Pilih database dan collection
db = client["bigdata_ai"]        # Nama database
collection = db["ai_jobs"]       # Nama collection

# 4. Insert data ke MongoDB
if isinstance(data, list):
    collection.insert_many(data)     # Jika data berupa list
else:
    collection.insert_one(data)      # Jika data hanya satu object

print("✅ Data berhasil dimasukkan ke MongoDB!")
