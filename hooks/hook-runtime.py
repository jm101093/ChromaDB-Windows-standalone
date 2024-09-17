import sys
import os

def runtime_hook():
    base_path = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    sys.path.insert(0, os.path.join(base_path, 'chroma_db'))
    sys.path.insert(0, os.path.join(base_path, 'chromadb'))
    sys.path.insert(0, os.path.join(base_path, 'chromadb', 'api'))
    sys.path.insert(0, os.path.join(base_path, 'chromadb', 'utils', 'embedding_functions'))
    
    # For Windows, you might want to set a different environment variable
    os.environ['USERPROFILE'] = os.path.expanduser('~')