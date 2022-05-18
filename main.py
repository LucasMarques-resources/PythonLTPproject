import os
import numpy as np
from tabulate import tabulate

equipas = []
numJogadoresEquipa = []
classificacaoEquipa = []
jogadores = []
idade = []
posicao = []

numJogos = 0
golos = []
golosEquipas = []
golosSofridos = []
jogos = []
equipasWin = []
equipasEmpate = []
equipaVencedora = " "
maxValuePos = 0
pontos = []

def printJogadores():
    infoJogadoresEquipa = [[]]

    for i in range(0, len(jogadores)):
        infoJogadoresEquipa[0].append(jogadores[i])

    print(tabulate(infoJogadoresEquipa, tablefmt="grid"))

def writeInFile():
    ficheiro = open(file_path, "w")

    # Write number of teams
    ficheiro.write(str(numEquipas))

    ficheiro.write("\n")

    # Write number of players in each team
    for i in range(0, numEquipas):
        ficheiro.write(str(numJogadoresEquipa[i]) + " ")

    ficheiro.write("\n")

    # Write teams
    for i in range(0, len(equipas)):
        ficheiro.write(equipas[i] + " ")

    ficheiro.write("\n")

    # Write players
    for i in range(0, len(jogadores)):
        ficheiro.write(jogadores[i] + " ")

    ficheiro.close()

def addJogador():
    jogadorGerir = str(input("Qual o nome do jogador que deseja adicionar: "))
    jogadorIdade = int(input("Qual a idade do jogador: "))

    for i in range(0, numEquipas):
        if (i == 0):
            num = numJogadoresEquipa[0]
        else:
            num += numJogadoresEquipa[i]

        if (i == (equipaGerir - 1)):
            jogadores.insert(num, jogadorGerir)
            idade.insert(num, jogadorIdade)
            numJogadoresEquipa[equipaGerir - 1] += 1

def removeJogador():
    while True:
        jogadorGerir = str(input("Qual o nome do jogador que deseja remover: "))
        if (jogadores.count(jogadorGerir) >= 1):
            break
        else:
            print("Introduza um nome válido!")

    numMax = 0
    numMin = 0

    index = jogadores.index(jogadorGerir)

    for i in range(0, numEquipas):
        numMax += numJogadoresEquipa[i]

        #print(numMax)

        if (i == (equipaGerir - 1)):
            #print(f"debug: {i} / {index} / {numMax - 1} / {numMin - 1}")
            if (index >= (numMin - 1) and index <= (numMax - 1)):
                jogadores.pop(index)
                numJogadoresEquipa[equipaGerir - 1] -= 1
            else:
                print(f"Esse jogador nao esta na equipa {equipaGerir}")

        numMin += numJogadoresEquipa[i]

file_path = "jogadores.txt"

if os.stat(file_path).st_size == 0:
    
    # File empty
    while True:
        numEquipas = int(input("Introduza o número de equipas: "))
        if (numEquipas >= 3):
            break;
        print("O número de equipas tem de ser maior ou igual a 3")

    for _equipa in range(0, numEquipas):
        nomeEquipa = str(input(f"Introduza o nome da equipa {_equipa + 1}: "))
        equipas.append(nomeEquipa)
        numJogEquipa = int(input("Introduza o número de jogadores da equipa: "))
        numJogadoresEquipa.append(numJogEquipa)

    for _equipa in range(0, len(equipas)):
        for _jogador in range(0, numJogadoresEquipa[_equipa]):
            _nome = str(input(f"Introduza o nome do jogador {_jogador + 1} da equipa {_equipa + 1}: "))
            #_idade = int(input("Introduza a idade do jogador: "))
            #_posicao = str(input("Introduza a posicao do jogador (suplente ou titular): "))
            _idade = 1
            _posicao = "titular"
            jogadores.append(_nome)
            idade.append(_idade)
            posicao.append(_posicao)

    writeInFile()

# Read file info
else:

    ficheiro = open(file_path, "r")

    # Read number of teams
    numEquipas = int(ficheiro.readline())

    # Read number of players in each team 
    texto = ficheiro.readline()
    textoSplit = texto.split()

    for i in range(0, len(textoSplit)):
        numJogadoresEquipa.append(int(textoSplit[i]))

    # Read teams
    texto = ficheiro.readline()
    textoSplit = texto.split()

    for i in range(0, len(textoSplit)):
        equipas.append(textoSplit[i])

    # Read players
    texto = ficheiro.readline()
    textoSplit = texto.split()

    for i in range(0, len(textoSplit)):
        jogadores.append(textoSplit[i])

    ficheiro.close()

print(equipas)
print(numEquipas)
print(numJogadoresEquipa)
print(jogadores)
print(idade)
print(posicao)

while True:
    print(" ----- M E N U ----- ")
    print(" 1 -> Gerir Equipas ")
    print(" 2 -> Gerir Jogos e Classificações ")
    print(" 3 -> Sair ")
    opcaoMenu1 = int(input("Introduza uma opção: "))

    if opcaoMenu1 == 1:
        
        infoJogadores = []

        for i in range(0, numEquipas):
            infoJogadores.append([])
            for j in range(0, max(numJogadoresEquipa) + 1):
                infoJogadores[i].append(0)

        for i in range(0, numEquipas):
            if (i == 0):
                aux = 0
            else:
                aux += numJogadoresEquipa[i - 1]
            
            for j in range(0, max(numJogadoresEquipa) + 1):
                if (j == 0):
                    infoJogadores[i][j] = equipas[i]
                else:
                    if ((j - 1) < numJogadoresEquipa[i]):
                        infoJogadores[i][j] = jogadores[(j - 1) + aux]               

        print(tabulate(infoJogadores, tablefmt="grid"))

        print(equipas)
        equipaGerir = int(input("Introduza qual o número da equipa que quer editar: "))

        print(" ----- M E N U ----- ")
        print(" 1 -> Adicionar jogador")
        print(" 2 -> Remover jogador")
        opcaoMenu2 = int(input("Introduza uma opção: "))

        if opcaoMenu2 == 1:
            addJogador()
        elif opcaoMenu2 == 2:
            removeJogador()

        writeInFile()

        printJogadores()
    
    elif opcaoMenu1 == 2:

        print("----- J O G O S -----")
        for equipa in range(len(equipas) - 1):
            for j in range(equipa + 1, len(equipas)):
                print(f"{equipas[equipa]} x {equipas[j]}")
                jogos.append(equipas[equipa])
                jogos.append(equipas[j])
                numJogos += 1

        print(jogos)

        jogoAtual = 0
        for i in range(0, len(jogos)):
            if i % 2 == 0:
                print(f"----- {jogos[i]} x {jogos[i + 1]} ----")
                jogoAtual += 1
            
            pontuacao = input(f"Introduza os golos da equipa {jogos[i]} do jogo {jogoAtual}: ")
            golos.append(int(pontuacao))


        print(golos)

        for i in range(0, numEquipas):
            pontos.append(0)
            golosEquipas.append(0)
            golosSofridos.append(0)
            for j in range(0, len(golos)):
                if (equipas[i] == jogos[j]):
                    golosEquipas[i] += golos[j]

        print(f"Golos por equipa: {golosEquipas}")

        for i in range(0, len(golos)):
            if i % 2 == 0:
                #print(golos[i])
                #print(golos[i + 1])
                maxValue = max(golos[i], golos[i + 1])

                if (maxValue == golos[i]):
                    maxValuePos = i
                elif (maxValue == golos[i + 1]):
                    maxValuePos = i + 1

                if (golos[i] == golos[i + 1]):
                    equipasEmpate.append(jogos[i])
                    equipasEmpate.append(jogos[i + 1])
                else: 
                    equipasWin.append(jogos[maxValuePos])

                golosSofridos[equipas.index(jogos[i])] += golos[i + 1]
            else:
                golosSofridos[equipas.index(jogos[i])] += golos[i - 1]

        #print(equipasWin)
        #print(equipasEmpate)

        for i in range(0, len(equipasWin)):
            #print(equipas.index(equipasWin[i]))
            pontos[equipas.index(equipasWin[i])] += 3

        for i in range(0, len(equipasEmpate)):
            pontos[equipas.index(equipasEmpate[i])] += 1

        info = []

        for i in range(0, numEquipas):
            info.append([])
            for j in range(0, 4):
                info[i].append(0)
                
        for i in range(0, numEquipas):
            for j in range(0, 4):
                if (j == 0):
                    info[i][j] = equipas[i]
                elif (j == 1):
                    info[i][j] = golosEquipas[i]
                elif (j == 2):
                    info[i][j] = golosSofridos[i]
                elif (j == 3):
                    info[i][j] = pontos[i]


        head = ["Equipa", "Golos", "Golos sofridos", "Pontuação"]
        print(tabulate(info, headers=head, tablefmt="grid"))

        #for i in range(0, numEquipas):
        maxPontos = max(pontos)
        maxPontosPos = pontos.index(maxPontos)
        equipaMaxPontos = equipas[maxPontosPos]

        equipaEmpate = []
        diferencaEmpate = []

        for i in range(0, numEquipas):
            if (pontos[i] == maxPontos):
                equipaEmpate.append(equipas[i])
            else:
                equipaEmpate.append(" ")

        #print(equipaEmpate)

        for i in range(0, numEquipas):
            if (equipaEmpate[i] == equipas[i]):
                diferencaEmpate.append(golosEquipas[i] - golosSofridos[i])
            else:
                diferencaEmpate.append(-9999)

        #print(diferencaEmpate)

        minDifEmpate = max(diferencaEmpate)
        for i in range(0, len(diferencaEmpate)):
            if diferencaEmpate.count(minDifEmpate) > 1:
                equipaVencedora = "Nao há vencedor"
            else:
                equipaVencedora = f"Equipa vencedor: {equipaEmpate[diferencaEmpate.index(minDifEmpate)]}"

        print(equipaVencedora)
    else:
        break 