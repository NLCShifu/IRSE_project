# Install dependencies using: pip install datasets fsspec==2023.1.0
import json
import datasets
import requests

url = "https://people.cs.kuleuven.be/~thomas.bauwens/irse_documents_2026_recipes.parquet"
filename = "irse_documents_2026_recipes.parquet"

# Download the file
response = requests.get(url)

# Save it to your computer
with open(filename, "wb") as f:
    f.write(response.content)

dataset = datasets.load_dataset("parquet", data_files=filename)['train']
queries = json.load(open("./irse_queries_2026_recipes.json", "r"))
