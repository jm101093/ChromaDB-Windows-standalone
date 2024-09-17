from PyInstaller.utils.hooks import collect_all

# Collect all files and dependencies related to the module
datas, binaries, hiddenimports = collect_all('chromadb.utils.embedding_functions.onnx_mini_lm_l6_v2')

# Ensure all required hidden imports are added
hiddenimports += [
    'onnxruntime', 
    'tokenizers', 
    'tqdm'
]