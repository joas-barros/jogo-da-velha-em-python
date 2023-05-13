matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Printa a tabela
def mostrarvelha(matriz):
    print('\033[1;32;mJOGO DA VELHA\033[m')
    print("+---+---+---+")
    for l in range(0, 3):
        for c in range(0, 3):
            print("| ", matriz[l][c], end='')
        print("|")
        print("+---+---+---+")


# Muda o simbolo
def mudarjogador(Simb):
    if Simb == "X":
        Simb = "O"
    else:
        Simb = "X"
    return Simb


# Impede o jogador de jogar seguidas vezes uma mesma casa
def jogar(S, P, matriz):
    mudou = False
    for l in range(0, 3):
        for c in range(0, 3):
            if matriz[l][c] == P:
                matriz[l][c] = S
                mudou = True
    return mudou


# Verifica condições de finalização de jogo
def terminouvelha(matriz):
    terminou = False
    # Jogos em linha
    for l in range(0, 3):
        if matriz[l][0] == matriz[l][1] and matriz[l][1] == matriz[l][2]:
            terminou = True
    # Jogos em coluna
    for c in range(0, 3):
        if matriz[0][c] == matriz[1][c] and matriz[1][c] == matriz[2][c]:
            terminou = True
    # Jogos em diagonal
    if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2]:
        terminou = True
    if matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0]:
        terminou = True
    # Jogos em velha
    ocorr = 0
    for l in range(0, 3):
        for c in range(0, 3):
            if matriz[l][c] != "X" and matriz[l][c] != "O":
                ocorr += 1
    if ocorr == 0:
        terminou = True

    return terminou


# Programa principal
i = 1
l = c = 0
Simb = "X"
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = i
        i += 1

mostrarvelha(matriz)
while True:
    while True:
        Po = int(input(f"Vai jogar [{Simb}] em qual posição? "))
        R = jogar(Simb, Po, matriz)
        if not R:
            print("\033[1;31;mJOGADA INVÁLIDA\033[m")
        else:
            break
    Simb = mudarjogador(Simb)
    test = terminouvelha(matriz)
    mostrarvelha(matriz)
    if test:
        break
print('\033[1;34;mJOGO FINALIZADO!!!\033[m')




