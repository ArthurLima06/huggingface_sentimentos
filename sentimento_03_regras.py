from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

feedbacks = [
    "A aula foi excelente, aprendi muito!",
    "Não gostei, achei confuso.",
    "Foi razoável.",
    "Professor explicou muito bem.",
    "Péssima didática.",
    "Gostei bastante, mas poderia ter mais exemplos.",
    "Não entendi quase nada.",
    "Muito bom, quero mais aulas assim!",
    "Foi ok.",
    "Extremamente frustrante."
]


def classificar(texto):
    resultado = sentiment(texto)[0]
    label = resultado["label"]
    score = float(resultado["score"])

    if score < 0.70:
        categoria = "INCERTO"
    elif label == "NEGATIVE" and score >= 0.85:
        categoria = "CRITICO"
    elif label == "NEGATIVE" and 0.70 <= score < 0.85:
        categoria = "ATENCAO"
    elif label == "POSITIVE" and score >= 0.85:
        categoria = "POSITIVO FORTE"
    else:
        categoria = "POSITIVO"

    return label, score, categoria


contagem = {
    "CRITICO": 0,
    "ATENCAO": 0,
    "INCERTO": 0,
    "POSITIVO FORTE": 0,
    "POSITIVO": 0,
}

for texto in feedbacks:
    label, score, categoria = classificar(texto)
    contagem[categoria] += 1

    print(f"Texto: {texto}")
    print(f"Label: {label}")
    print(f"Score: {score:.4f}")
    print(f"Categoria: {categoria}")
    print("-" * 50)

print("\nRELATORIO FINAL")
for categoria, total in contagem.items():
    print(f"{categoria}: {total}")
