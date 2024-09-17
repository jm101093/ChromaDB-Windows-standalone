from PyInstaller.utils.hooks import collect_all, collect_data_files, collect_submodules, copy_metadata
import os
import sys
import importlib.util

# Collect all files and dependencies related to the chromadb package
datas, binaries, hiddenimports = collect_all('chromadb')

# Explicitly collect hnswlib
try:
    spec = importlib.util.find_spec("hnswlib")
    if spec is not None:
        hnswlib_path = os.path.dirname(spec.origin)
        datas.append((hnswlib_path, 'hnswlib'))
    else:
        print("Warning: hnswlib spec not found")
except ImportError:
    print("Warning: hnswlib not found")

# Explicitly collect posthog
try:
    spec = importlib.util.find_spec("posthog")
    if spec is not None:
        posthog_path = os.path.dirname(spec.origin)
        datas.append((posthog_path, 'posthog'))
    else:
        print("Warning: posthog spec not found")
except ImportError:
    print("Warning: posthog not found")

# Collect metadata for hnswlib and posthog
datas += copy_metadata('hnswlib')
datas += copy_metadata('posthog')

# Include hidden imports for specific submodules
hiddenimports += [
    'chromadb.db.impl',
    'chromadb.api.segment',
    'chromadb.utils.embedding_functions.onnx_mini_lm_l6_v2',
    'chromadb.migrations',
    'chromadb.migrations.embeddings_queue',
    'chromadb.db.impl.sqlite',
    'chromadb.segment',
    'chromadb.migrations.embeddings_queue.embeddings_queue',
    'importlib_resources.files',
    'chromadb.segment.impl.vector.local_hnsw',
    'chromadb.segment.impl.vector.local_persistent_hnsw',
    'hnswlib',
    'posthog'
]

# Collect all submodules of chromadb
hiddenimports += collect_submodules('chromadb')

# Collect all modules and data files from 'chromadb'
datas.extend(collect_data_files('chromadb', include_py_files=True))

# Collect all modules and data files from 'importlib_resources'
datas += collect_data_files('importlib_resources')

# Add numpy as a hidden import
hiddenimports.append('numpy')

# Add the project-specific config.py file
project_root = os.path.dirname(os.path.abspath(__file__))  # Assumes the hook file is in the project root
config_file = os.path.join(project_root, 'chromadb', 'config.py')
if os.path.exists(config_file):
    datas.append((config_file, 'chromadb'))
else:
    print(f"Warning: config.py not found at {config_file}")

# Explicitly add hnswlib and posthog to hiddenimports
if 'hnswlib' not in hiddenimports:
    hiddenimports.append('hnswlib')
if 'posthog' not in hiddenimports:
    hiddenimports.append('posthog')

# Print debug information
print("Datas:", datas)
print("Binaries:", binaries)
print("Hidden imports:", hiddenimports)