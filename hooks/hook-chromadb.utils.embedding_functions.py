from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hiddenimports = collect_submodules('chromadb.utils.embedding_functions')
hiddenimports += ['importlib', 'pathlib', 'onnxruntime', 'tokenizers', 'tqdm']
datas = collect_data_files('chromadb.utils.embedding_functions')