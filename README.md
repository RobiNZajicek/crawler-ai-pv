# PV projekt – ML klasifikace článků

Projekt do předmětu PV: klasifikace kategorie článků pomocí strojového učení.

## Plán

- **Data:** Vlastní crawl z idnes.cz, novinky.cz, aktualne.cz, irozhlas.cz (JSONL).
- **Předzpracování:** Čištění, sloučení textu, odstranění duplicit.
- **Model:** Klasifikace (např. logistická regrese) na TF-IDF vektorech textu.

## Struktura

- `ml_clanky_notebook.ipynb` – Jupyter notebook s postupem vytvoření modelu (načtení → předzpracování → trénování → vyhodnocení).
