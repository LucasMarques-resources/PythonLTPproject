import os
from tabulate import tabulate
import colorama
from termcolor import colored

colorama.init()

# TO DO
# Write "rules" for the game (ex: age of players)
# Historic of changes
# Adicionar à tabela final das pontuacoes o Numero de jogos, diferenca de jogos e (ordenar por ???)

idadeMin = 10
idadeMax = 35
jogMin = 5
jogMax = 11

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

def temNumeros(inputString):
    return any(char.isdigit() for char in inputString)

def printEquipas():
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

def printJogadores(_equipa):
    infoJogadoresEquipa = [[equipas[_equipa - 1]]]

    aux = 0
    aux2 = 0
    for i in range(0, numEquipas):
        aux += numJogadoresEquipa[i]
        if (i > 0):
            aux2 += numJogadoresEquipa[i - 1]

        if (i == (_equipa - 1)):
            for j in range(0, len(jogadores)):
                if (j >= aux2 and j < aux):
                    infoJogadoresEquipa[0].append(jogadores[j])

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
    if ((numJogadoresEquipa[equipaGerir - 1]) < jogMax):
        while True:
            jogadorGerir = str(input("Qual o nome do jogador que deseja adicionar: "))
            if (temNumeros(jogadorGerir) == False):
                break
            else:
                print(colored("Nome do jogador inválido!", "red"))
            
        while True:
            try:
                jogadorIdade = int(input("Qual a idade do jogador: "))
            except(ValueError):
                print(colored("Idade do jogador inválida!", "red"))
            else:
                if (jogadorIdade >= idadeMin and jogadorIdade <= idadeMax):
                    break
                else:
                    print(colored("Idade do jogador inválida!", "red"))


        for i in range(0, numEquipas):
            if (i == 0):
                num = numJogadoresEquipa[0]
            else:
                num += numJogadoresEquipa[i]

            if (i == (equipaGerir - 1)):
                jogadores.insert(num, jogadorGerir)
                idade.insert(num, jogadorIdade)
                numJogadoresEquipa[equipaGerir - 1] += 1

        printJogadores(equipaGerir)
        #printEquipas()
    else:
        print(colored("Limite máximo de jogadores 11", "red"))

def removeJogador():
    if ((numJogadoresEquipa[equipaGerir - 1] - 1) >= jogMin):
        while True:
            jogadorGerir = str(input("Qual o nome do jogador que deseja remover: "))
            if (jogadores.count(jogadorGerir) >= 1):
                break
            else:
                print(colored("Introduza um nome válido!", "red"))

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

        printJogadores(equipaGerir)
        #printEquipas()
    else:
        print(colored("Limite mínimo de jogadores 5", "red"))

file_path = "jogadores.txt"

if os.stat(file_path).st_size == 0:
    
    # File empty
    while True:
        try:
            numEquipas = int(input("Introduza o número de equipas: "))
        except(ValueError):
            print(colored("Numero de equipas inválido!", "red"))
        else:
            if (numEquipas >= 3):
                break;
            else:
                print("O número de equipas tem de ser maior ou igual a 3")

    for _equipa in range(0, numEquipas):
        nomeEquipa = str(input(f"Introduza o nome da equipa {_equipa + 1}: "))
        equipas.append(nomeEquipa)
        while True:
            try:
                numJogEquipa = int(input("Introduza o número de jogadores da equipa: "))
            except(ValueError):
                print(colored("Número de jogadores da equipa inválido!", "red"))
            else:
                if (numJogEquipa >= jogMin and numJogEquipa <= jogMax):
                    numJogadoresEquipa.append(numJogEquipa)
                    break
                else:
                    print(colored("O número de jogadores tem de ser entre 5 e 11", "red"))

    for _equipa in range(0, len(equipas)):
        for _jogador in range(0, numJogadoresEquipa[_equipa]):
            while True:
                _nome = str(input(f"Introduza o nome do jogador {_jogador + 1} da equipa {_equipa + 1}: "))
                if (temNumeros(_nome) == False):
                    break
                else:
                    print(colored("Nome do jogador inválido!", "red"))
            
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
    print(colored(" ----- M E N U ----- ", "green"))
    print(" 1 -> Gerir Equipas ")
    print(" 2 -> Gerir Jogos e Classificações ")
    print(" 3 -> Sair ")
    print(colored(" ------------------- ", "green"))

    while True:
        try:
            opcaoMenu1 = int(input("Introduza uma opção: "))
        except(ValueError):
            print(colored("Opção inválida", "red"))
        else:
            if (opcaoMenu1 >= 1 and opcaoMenu1 <= 3):
                break;
            else:
                print(colored("Opção inválida!", "red"))

    if opcaoMenu1 == 1:
        
        printEquipas()

        print(equipas)
        
        while True:
            try:
                equipaGerir = int(input("Introduza qual o número da equipa que quer editar: "))
            except(ValueError):
                print(colored("Número da equipa inválido!", "red"))
            else:
                if (equipaGerir > 0 and equipaGerir <= numEquipas):
                    break;
                else:
                    print(colored("Número da equipa inválido!", "red"))

        print(colored(" ----- M E N U ----- ", "green"))
        print(" 1 -> Adicionar jogador")
        print(" 2 -> Remover jogador")
        print(colored(" ------------------- ", "green"))

        while True:
            try:
                opcaoMenu2 = int(input("Introduza uma opção: "))
            except(ValueError):
                print(colored("Opção inválida!", "red"))
            else:
                if (opcaoMenu2 >= 1 and opcaoMenu2 <= 2):
                    break;
                else:
                    print(colored("Opção inválida!", "red"))

        if opcaoMenu2 == 1:
            addJogador()
        elif opcaoMenu2 == 2:
            removeJogador()

        writeInFile()
    
    elif opcaoMenu1 == 2:

        print(colored(" ----- J O G O S ----- ", "green"))
        for equipa in range(len(equipas) - 1):
            for j in range(equipa + 1, len(equipas)):
                print(f"{equipas[equipa]} x {equipas[j]}")
                jogos.append(equipas[equipa])
                jogos.append(equipas[j])
                numJogos += 1

        print(colored(" ------------------- ", "green"))

        jogoAtual = 0
        for i in range(0, len(jogos)):
            if i % 2 == 0:
                print(f"----- {jogos[i]} x {jogos[i + 1]} ----")
                jogoAtual += 1
            
            try:
                pontuacao = input(f"Introduza o número de golos da equipa {jogos[i]} do jogo {jogoAtual}: ")
            except(ValueError):
                print(colored("Número de golos inválido!", "red"))
            else:
                if (pontuacao >= 0):
                    golos.append(int(pontuacao))
                    break
                else:
                    print(colored("Número de golos inválido!", "red"))

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