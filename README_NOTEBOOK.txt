Jupyter notebook (ML) – návod
=============================

• Notebook: ml_clanky_notebook.ipynb

Lokálně (Cursor / VS Code):
  Otevři soubor, spouštěj buňky (Shift+Enter).
  Data: nastav DATA_PATH na cestu k articles_part1.jsonl (např. C:\Users\Robin\Desktop\crawl\articles_part1.jsonl).

Google Colab:
  Soubor → Nahrát notebook → vyber ml_clanky_notebook.ipynb.
  Data: nahraj articles_part1.jsonl (nebo .gz) na Colab / Disk a v první buňce změň DATA_PATH.

Export modelu:
  Po doběhnutí všech buněk včetně poslední se vytvoří model.joblib. Ten použije predict.py.
