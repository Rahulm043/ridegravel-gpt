"""Load html from files, clean up, split, ingest into Weaviate."""
import glob
from pathlib import Path
from langchain.document_loaders import DirectoryLoader

print(glob.glob("./granfondo-cycling.com/the-best-gravel-bike-review/**/*.md"))

if __name__ == "__main__":
    loader = DirectoryLoader("./granfondo-cycling.com/the-best-gravel-bike-review/", glob="**/*.md")
    raw_documents = loader.load()
    print(len(raw_documents))
    dir_path = Path("ingested_data")
    dir_path.mkdir(parents=True, exist_ok=True)
    for i, doc in enumerate(raw_documents):
        path = dir_path / f"{i}.json"
        with open(path, "w") as f:
            f.write(doc.json())
