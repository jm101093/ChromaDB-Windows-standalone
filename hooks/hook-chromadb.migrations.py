from PyInstaller.utils.hooks import collect_all, collect_data_files

datas, binaries, hiddenimports = collect_all('chromadb.migrations')
datas += collect_data_files('chromadb.migrations', include_py_files=True)

hiddenimports += [
    'chromadb.migrations.embeddings_queue',
    'chromadb.migrations.embeddings_queue.embeddings_queue'
]