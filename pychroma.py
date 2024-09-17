#install
#nuitka --onefile --include-package=chromadb --include-package=uvicorn --include-package=fastapi --include-package=starlette --include-package=click --include-package=h11 --include-package=typing_extensions --include-package=bcrypt --include-package=httpx --include-package=mmh3 --include-package=numpy --include-package=onnxruntime --include-package=overrides --include-package=posthog --include-package=pydantic --include-package=tokenizers --include-package=tqdm --include-package=typer --include-package=google --include-module=opentelemetry.context.contextvars_context --include-data-dir=.\chroma_db=chroma_db --follow-imports --show-progress .\pychroma.py --output-dir=.\dist
import os
import sys
import logging
import chromadb
from chromadb.config import Settings
from fastapi import FastAPI
import uvicorn
from chromadb.app import app as chromadb_app

sys.path.insert(0, os.path.join(os.path.dirname(sys.executable), 'chroma_db'))
sys.path.insert(0, os.path.dirname(sys.executable))
from chromadb.utils.embedding_functions.onnx_mini_lm_l6_v2 import ONNXMiniLM_L6_V2

try:
    embedding_function = ONNXMiniLM_L6_V2()
    # Your other code here
except Exception as e:
    print(f"Error initializing embedding function: {e}")
    # Handle the error appropriately

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the actual executable path
executable_path = os.path.abspath(sys.argv[0])
executable_dir = os.path.dirname(executable_path)

# Construct the path to the chroma_db subdirectory
chroma_db_path = os.path.join(executable_dir, "chroma_db")
print(chroma_db_path)
# Check if the chroma_db directory exists, and create it if it doesn't
if not os.path.exists(chroma_db_path):
    os.makedirs(chroma_db_path)
    logger.info(f"Created chroma_db directory at: {chroma_db_path}")
else:
    logger.info(f"Using existing chroma_db directory at: {chroma_db_path}")

client = chromadb.PersistentClient(path=chroma_db_path, settings=Settings(
    allow_reset=True,
    anonymized_telemetry=False,
    persist_directory=chroma_db_path
))

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ChromaDB server is running"}

@app.post("/reset")
def reset_database():
    logger.info("Received reset request")
    client.reset()
    return {"message": "Database reset"}

@app.get("/health/")
async def health_check():
    logger.info("Received health check request")
    return {"status": "healthy"}

def run_server():
    config = uvicorn.Config(chromadb_app, host="0.0.0.0", port=8001)
    server = uvicorn.Server(config)
    server.run()

if __name__ == '__main__':
    run_server()
