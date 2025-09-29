import requests
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        # "model": "deepseek-r1",
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })

    response = r.json()
    print(response)
    return response

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={"model": "bge-m3", "input": text_list})
    return r.json()['embeddings'][0]

# Load dataframe
df = joblib.load("Embeddings.joblib")

# Query embedding
query = input("Enter Your Query: ")
question_embedding = np.array(create_embeddings([query]), dtype=np.float32).reshape(1, -1)

# --- Process in streaming mode ---
batch_size = 200  # adjust if RAM is very low
scores = []
indices = []

for start in range(0, len(df), batch_size):
    end = start + batch_size
    batch_embeddings = df['embeddings'].iloc[start:end]

    # convert only this batch
    batch_arr = np.vstack([np.array(x, dtype=np.float32) for x in batch_embeddings if isinstance(x, (list, np.ndarray))])
    
    # compute similarity
    sims = cosine_similarity(batch_arr, question_embedding).ravel()

    # store with indices
    for i, s in zip(range(start, end), sims):
        scores.append(s)
        indices.append(i)

# Convert to numpy
scores = np.array(scores)
indices = np.array(indices)

# Get top 3
top_idx = scores.argsort()[::-1][:3]
final_rows = df.iloc[indices[top_idx]]

#print(final_rows[["title", "number", "text", "start", "end"]])

for index, item in final_rows.iterrows():
    print(index, item['title'], item['number'], item['text'], item['start'], item['end'])

prompt = f'''I am teaching web development in my Sigma web development course. Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{final_rows[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
"{query}"
User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course
'''
with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt", "w") as f:
    f.write(response)