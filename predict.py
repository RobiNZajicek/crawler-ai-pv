"""
Predikce kategorie článku z textu. Spuštění bez IDE:
  python predict.py "Text článku nebo nadpis a obsah..."
  nebo: echo "Text..." | python predict.py
"""
import sys
import joblib

MODEL_PATH = "model.joblib"


def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = sys.stdin.read().strip()
    if not text:
        print("Usage: python predict.py \"text článku\"", file=sys.stderr)
        sys.exit(1)

    data = joblib.load(MODEL_PATH)
    model = data["model"]
    vec = data["vectorizer"]
    le = data["label_encoder"]

    X = vec.transform([text])
    pred_id = model.predict(X)[0]
    kategorie = le.inverse_transform([pred_id])[0]
    print(kategorie)


if __name__ == "__main__":
    main()
