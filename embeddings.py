import json
import os
import requests
import pandas as pd
import joblib

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={"model":"bge-m3", "input":text_list})
    return r.json()['embeddings']

jsons = os.listdir("jsons")

chunk_id = 0
all_embeddings = []

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)
        print(f"Creating Embeddings for {json_file}")
        embeddings = create_embeddings([c['text'] for c in content['chunks']])

    for i, chunk in enumerate(content['chunks']):
        chunk["chunk_id"] = chunk_id
        chunk['embeddings'] = embeddings
        chunk_id += 1
        all_embeddings.append(chunk)

df = pd.DataFrame.from_records(all_embeddings)

joblib.dump(df, "Embeddings.joblib")