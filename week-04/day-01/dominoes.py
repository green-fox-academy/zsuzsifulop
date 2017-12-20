from domino import Domino

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes


dominoes = initialize_dominoes()

for i in range(len(dominoes)):
    for j in range(1,len(dominoes)):
        if dominoes[i].values[1] == dominoes[j].values[0]:
            dominoes[i + 1], dominoes[j] = dominoes[j], dominoes[i + 1]
print(dominoes)


            