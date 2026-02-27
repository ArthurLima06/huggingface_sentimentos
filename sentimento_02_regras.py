from transformers import pipeline
sentiment = pipeline("sentiment-analysis")
def responder(texto: str) -> str:
r = sentiment(texto)[0]
label = r["label"]
score = r["score"]
# regra simples de confiança (você pode ajustar)
if score < 0.70:
return "Não tenho certeza do sentimento. Pode explicar melhor?"
if label == "NEGATIVE":
return "Entendi. Sinto muito por isso. Vamos resolver juntos: o que exatamente aconteceu?"
else:
return "Que bom! Quer dar mais detalhes do que funcionou bem?"
while True:
texto = input("\nDigite uma frase (ou ENTER para sair): ").strip()
if not texto:
break
print("Resposta:", responder(texto))