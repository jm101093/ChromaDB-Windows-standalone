import ast
import os

def find_imports(directory):
    imports = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        tree = ast.parse(f.read())
                        for node in ast.walk(tree):
                            if isinstance(node, ast.Import):
                                for n in node.names:
                                    imports.add(n.name.split('.')[0])
                            elif isinstance(node, ast.ImportFrom):
                                if node.module:
                                    imports.add(node.module.split('.')[0])
                    except Exception as e:
                        print(f"Error parsing {file}: {e}")
    return imports

if __name__ == "__main__":
    directory = "."  # Current directory
    imports = find_imports(directory)
    print("Found imports:")
    for imp in sorted(imports):
        print(f"--hidden-import={imp}")