from PyInstaller.utils.hooks import collect_all

# Collect all files and dependencies related to the module
datas, binaries, hiddenimports = collect_all('chromadb.db.impl')

# Ensure all required hidden imports are added
hiddenimports += [
    'chromadb.db.impl'
]
