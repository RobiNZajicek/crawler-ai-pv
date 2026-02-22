# PV projekt – ML klasifikace článků

Projekt do předmětu PV: klasifikace kategorie článků pomocí strojového učení.

## Data

- **Zdroj:** Vlastní crawl z idnes.cz, novinky.cz, aktualne.cz, irozhlas.cz (vlastní crawler).
- **V repu:** Vzorek 2000 článků v `data/articles_sample.jsonl` – stačí ke spuštění notebooku i k trénování modelu.

## Plán
- **Předzpracování:** Čištění, sloučení textu, odstranění duplicit.
- **Model:** Klasifikace (např. logistická regrese) na TF-IDF vektorech textu.

## Struktura

- `data/articles_sample.jsonl` – vzorek dat pro běh projektu (2000 záznamů z crawlu).
- `ml_clanky_notebook.ipynb` – Jupyter notebook s postupem vytvoření modelu (načtení → předzpracování → trénování → vyhodnocení).
- `predict.py` – Skript pro predikci kategorie z textu (vyžaduje `model.joblib` z notebooku). Spuštění: `python predict.py "text článku"`.
- `requirements.txt` – Závislosti (pandas, scikit-learn, joblib).
- `README_NOTEBOOK.txt` – Návod k notebooku (lokálně / Colab).
- `CHECKLIST_ODEVZDANI.md` – Kontrolní seznam před odevzdáním.
