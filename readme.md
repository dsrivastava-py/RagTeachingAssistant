# RAG based AI Teaching Assistant

## Stack Used-
- Python
- Liabs : [pandas, numpy, sklearn, joblib, whisper, json, requests, os, subprocess, ffmpeg]
- AI Models : [OpenAI-Whisper, Ollama-llama3.2, Ollama-bge-m3]

## Videos Used-
### This entire Project is made for the first 18 videos of [Sigma Web Development Course]("https://youtube.com/playlist?list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w&si=Op51LtvUIdK3CZP2") launched by the YouTube Creator - [Code With Harry]("https://www.youtube.com/@codewithharry")
- All the videos are not processed due to limited resources
- The same code can be used for any set of videos

## What does this Repo Contains?
- This Repo has the audio files of the 18 videos which have been used to build this RAG based AI Teaching Assistant
- The Video files are not included in this Repo, you can access them through [YouTube]("https://youtube.com/playlist?list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w&si=Op51LtvUIdK3CZP2")
- This Repo also contains the JSON files with the Transcription of all the 18 videos

## What does this Repo DO NOT Contains?
- You Do Not Get the Video Files
- You Do Not Get the OpenAI's Whisper
- You Do Not Get the Ollama's llama3.2
- You Do Not Get the Ollama's bge-m3
### You may install all these Liabraries, AI Models and other dependencies through internet in order to use this code

## What does this AI based Teaching Assistant actually do?
- Firstly, the _process.py_ converts all the video files into audio (.mp3) files and saves them in _/audios_ folder with proper naming.
- Then, the _audiototext.py_ uses _OpenAI's Whisper (large-v3)_ to transcribe and translate the entire Hindi audios into English JSONs and saves them into _/jsons_ folder.
- The _embeddings,py_ then reads all the JSON files, chunks them and embeds them into numeric values using _Ollama bge-m3_. It then saves the generated DataFrame in a joblib format using joblib to _Embeddings.joblib_
- Lastly, the _similarities.py_ loads the _embeddings.joblib_ file, inputs the Query of the user, embeds the User Query using _Ollama bge-m3_ and then calculates the _Cosine Similarities_ using _SciKit Learn_. It then, combines the User Query along with the prompt to be used in RAG Agent into _prompt.txt_ which is then used to find the desired result for the user query using _Ollama llama3.2_ and saves the final results into _response.txt_

## Thank-You
- This is working of this RAG based AI Teaching Assistant, it was fun making it. The only issue is that you must have High End GPUs for processing large chunk of files, or you can use OpenAI API or use platforms like Google Colab in order to run such programs with efficiency.

### With Efforts - [Devansh Srivastava](https://linkedin.com/in/connectwithdevansh)
