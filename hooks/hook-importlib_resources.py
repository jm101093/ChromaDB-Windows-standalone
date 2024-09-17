from PyInstaller.utils.hooks import collect_all, collect_data_files

datas, binaries, hiddenimports = collect_all('importlib_resources')
datas += collect_data_files('importlib_resources', include_py_files=True)

hiddenimports += ['importlib_resources.files']