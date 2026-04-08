# Install dependencies using: pip install datasets fsspec==2023.1.0
import json
import datasets
import requests

urls = [
    "https://people.cs.kuleuven.be/~thomas.bauwens/irse_documents_2026_recipes.parquet",
    "https://people.cs.kuleuven.be/~thomas.bauwens/irse_queries_2026_recipes.json",
]
filenames = []

# Download the files
for url in urls:
    response = requests.get(url)
    filename = url.split("/")[-1]
    filenames.append(filename)

# Save it to your computer
for filename in filenames:
    with open(filename, "wb") as f:
        f.write(response.content)

dataset = datasets.load_dataset("parquet", data_files=filenames[0])["train"]
# queries = json.load(open("./irse_queries_2026_recipes.json", "r"))
