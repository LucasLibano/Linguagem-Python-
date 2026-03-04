titulo = "Aprendendo Python do Zero a Pratica"

titulo = titulo.lower()   # deixa minusculo
titulo = titulo.strip()   # tira espaço extra

slug = titulo.replace(" ", "-")  # troca espaço por -

print(slug)