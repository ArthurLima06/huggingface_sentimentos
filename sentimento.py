from transformers import pipeline

# pipeline = forma mais simples de usar um modelo pronto

sentiment = pipeline("sentiment-analysis")

frases = [

    "Eu adorei o curso, foi muito bom!",

    "Isso foi péssimo, não funcionou.",

    "Foi ok, nada demais.",

    "Gostei mais ou menos, mais para menos do que para mais!!"

]

for f in frases:

    r = sentiment(f)[0]

    print(f"\nTexto: {f}")

    print(f"Label: {r['label']}")

    print(f"Score: {r['score']:.4f}")