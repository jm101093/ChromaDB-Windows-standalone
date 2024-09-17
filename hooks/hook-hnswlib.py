from PyInstaller.utils.hooks import collect_all, collect_data_files
import os

# Collect all the files related to hnswlib
datas, binaries, hiddenimports = collect_all('hnswlib')

# Add additional packages that Chroma DB might need
additional_packages = ['numpy', 'chromadb', 'fastapi', 'pydantic']

for package in additional_packages:
    try:
        package_datas, package_binaries, package_hiddenimports = collect_all(package)
        datas += package_datas
        binaries += package_binaries
        hiddenimports += package_hiddenimports
    except ImportError:
        print(f"Warning: Unable to collect files for {package}. Make sure it's installed.")

# Ensure hnswlib's .so file is included (for Linux/macOS)
hnswlib_so = collect_data_files('hnswlib', include_py_files=True)
datas += hnswlib_so

# Add the root directory of hnswlib to the search path
try:
    import hnswlib
    hnswlib_root = os.path.dirname(hnswlib.__file__)
    datas.append((hnswlib_root, 'hnswlib'))
except ImportError:
    print("Warning: Unable to import hnswlib. Make sure it's installed.")

# Remove any duplicate entries
datas = list(set(datas))
binaries = list(set(binaries))
hiddenimports = list(set(hiddenimports))