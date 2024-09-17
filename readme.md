#install
#nuitka --onefile --include-package=chromadb --include-package=uvicorn --include-package=fastapi --include-package=starlette --include-package=click --include-package=h11 --include-package=typing_extensions --include-package=bcrypt --include-package=httpx --include-package=mmh3 --include-package=numpy --include-package=onnxruntime --include-package=overrides --include-package=posthog --include-package=pydantic --include-package=tokenizers --include-package=tqdm --include-package=typer --include-package=google --include-module=opentelemetry.context.contextvars_context --include-data-dir=.\chroma_db=chroma_db --follow-imports --show-progress .\pychroma.py --output-dir=.\dist


#still working on getting pyinstaller working.