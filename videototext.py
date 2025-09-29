import whisper
import json
import os

model = whisper.load_model("large-v3")

audios = os.listdir("audios")

for audio in audios:
    number = audio.split('_')[0]
    name = audio.split('_')[1][:-4]
    print("Working on", number, name)
    
    result = model.transcribe(audio=f"audios/{audio}", language="hi", task="translate", word_timestamps=False )
    
    chunks = []
    for chunk in result['segments']:
        chunks.append({"number": number, "name": name, "start": chunk['start'], "end": chunk['end'], "text": chunk['text']})
    
    chunks_metadata = {"chunks":chunks, "text":result['text']}

    with open(f"jsons/{audio}.json", "w") as f:
        json.dump(chunks_metadata, f)

    print("JSON File Dumped!")