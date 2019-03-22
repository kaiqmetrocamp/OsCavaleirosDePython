VAR_GLOBAL="Os Cavaleiros de Python"
def escreve_texto():
    global VAR_GLOBAL
    VAR_LOCAL="Saga de Hades"
    print("Variável global: ", VAR_GLOBAL)
    print("Variável local: ", VAR_LOCAL)
print("Athena nossa Deusa:")

escreve_texto()

print("O filho chora, a mae nao ve:")
print("Variável global: ", VAR_GLOBAL)
