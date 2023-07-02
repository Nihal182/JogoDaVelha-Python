## -----------------------------------------------------
#    Projeto: Jogo da Velha
#    Disciplina: Lógica de Programação
#    Turma: S.I & G.T.I - Noturno
#    Participantes: Nely Graça, Nayara Arruda, Diego Marques,
#    Gustavo Neves, Lívia Castro.
## -----------------------------------------------------

def criaMatriz():
      mat = [
		    [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
      return mat

def posicaoOcupada(matriz, posicao):
    i = 0
    while i < len(matriz):
     if posicao in matriz[i]:
         return False
     i += 1
    return True

def registraJogada(matriz, posicao, jogador):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            if matriz[i][j] == posicao:
                matriz[i][j] = jogador
            j += 1
        i += 1
    return matriz

def apresentaMatriz(matriz):
    print(matriz[0][0], "|", matriz[0][1], "|", matriz[0][2])
    print("-" * 10)
    print(matriz[1][0], "|", matriz[1][1], "|", matriz[1][2])
    print("-" * 10)
    print(matriz[2][0], "|", matriz[2][1], "|", matriz[2][2])
    return

def trocaJogador(jogador):
    if jogador == "X":
        return "O"
    else:
        return "X"

def verificaGanhador(matriz, jogador):
    i = 0
    while i < len(matriz):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == jogador:
            return True
        if matriz[0][i] == matriz[1][i] == matriz[2][i] == jogador:
            return True
        i += 1
        if matriz[0][0] == matriz[1][1] == matriz[2][2] == jogador or matriz[0][2] == matriz[1][1] == matriz[2][0] == jogador:
            return True
    return False

print("*** JOGO DA VELHA *** \n")
print("Desafie o seu colega no jogo da velha.\n")
print("Regras: a) O primeiro jogador participará com a letra X e o segundo com a letra O.")
print("        b) Os números de 1 a 9 representam os espaços que estão livres.")
print("        c) Você só poderá escolher as posições livres.")
print("        d) O vencedor será o primeiro Jogador a preencher uma linha, uma coluna ou uma diagonal.")

matriz = criaMatriz()
jogador = "X"
c = 0
while c < 9:
    apresentaMatriz(matriz)
    posicao = int(input(f"(Jogador {jogador}) Informe a posição desejada :"))
    if posicaoOcupada(matriz, posicao):
        print("\nVocê não pode escolher uma posição que já está ocupada. Tente novamente")
        continue
    else:
        matriz = registraJogada(matriz, posicao, jogador)
        if verificaGanhador(matriz, jogador):
            print(f"\nO jogador {jogador} venceu!")
            break
        jogador = trocaJogador(jogador)
    c += 1
if c == 9:
    print("\nTemos um empate!")
## ----- Final do Programa