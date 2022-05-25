import os
from tabulate import tabulate
import colored
from colored import stylize

# Variables
programON = True
equipasJaJogaram = False

idadeMin = 12
idadeMax = 18
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
numJogosEquipas = []
jogos = []
equipasWin = []
equipasEmpate = []
equipaVencedora = " "
maxValuePos = 0
pontos = []

file_path = "jogadores.txt"
readFileInfo = True
informacaoInserida = False

regras = {
  "Idade": f"Mínima: {idadeMin} Máxima: {idadeMax}",
  "Jogadores": "Mínimo: 5 Máximo: 11",
  "Equipas": "Mínimo: 3"
}

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
                print(stylize("Nome do jogador inválido", colored.fg("red")))
            
        while True:
            try:
                jogadorIdade = int(input("Qual a idade do jogador: "))
            except(ValueError):
                print(stylize("Idade do jogador inválida", colored.fg("red")))
            else:
                if (jogadorIdade >= idadeMin and jogadorIdade <= idadeMax):
                    break
                else:
                    print(stylize(f"Idade do jogador tem que ser entre {idadeMin} e {idadeMax}", colored.fg("red")))


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
    else:
        print(stylize("Limite máximo de jogadores 11", colored.fg("red")))

def removeJogador():
    if ((numJogadoresEquipa[equipaGerir - 1] - 1) >= jogMin):
        while True:
            jogadorGerir = str(input("Qual o nome do jogador que deseja remover: "))
            if (jogadores.count(jogadorGerir) >= 1):
                break
            else:
                print(stylize("Introduza um nome válido", colored.fg("red")))

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
    else:
        print(stylize("Limite mínimo de jogadores 5", colored.fg("red")))

def printLeaderboard():
    head = ["Equipa", "Golos", "Golos sofridos", "Número de jogos", "Diferenca de golos", "Pontuação"]
    print(tabulate(info, headers=head, tablefmt="grid"))

# If file is not empty
if os.stat(file_path).st_size != 0:
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

    informacaoInserida = True
    readFileInfo = False

    ficheiro.close()

while programON:
    while True:
        print(stylize(" ----- M E N U ----- ", colored.fg("green")))
        print(" 1 -> Gerir Equipas ")
        print(" 2 -> Gerir Jogos e Classificações ")
        print(" 3 -> Regras ")
        print(" 4 -> Sair ")
        print(stylize(" ------------------- ", colored.fg("green")))

        # Menu 1 options
        while True:
            try:
                opcaoMenu1 = int(input("Introduza uma opção: "))
            except(ValueError):
                print(stylize("Opção inválida", colored.fg("red")))
            else:
                if (opcaoMenu1 >= 1 and opcaoMenu1 <= 4):
                    break;
                else:
                    print(stylize("Opção inválida", colored.fg("red")))

        # Manage teams
        if opcaoMenu1 == 1:
            
            # If file is empty
            if os.stat(file_path).st_size == 0:
                while True:
                    try:
                        numEquipas = int(input("Introduza o número de equipas: "))
                    except(ValueError):
                        print(stylize("Numero de equipas inválido", colored.fg("red")))
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
                            print(stylize("Número de jogadores da equipa inválido", colored.fg("red")))
                        else:
                            if (numJogEquipa >= jogMin and numJogEquipa <= jogMax):
                                numJogadoresEquipa.append(numJogEquipa)
                                break
                            else:
                                print(stylize(f"O número de jogadores tem de ser entre {jogMin} e {jogMax}", colored.fg("red")))

                for _equipa in range(0, len(equipas)):
                    for _jogador in range(0, numJogadoresEquipa[_equipa]):
                        while True:
                            _nome = str(input(f"Introduza o nome do jogador {_jogador + 1} da equipa {equipas[_equipa]}: "))
                            if (temNumeros(_nome) == False):
                                break
                            else:
                                print(stylize("Nome do jogador inválido", colored.fg("red")))
                        
                        while True:
                            try:
                                _idade = int(input("Introduza a idade do jogador: "))
                            except(ValueError):
                                print(stylize("Idade inválida", colored.fg("red")))
                            else:
                                if (_idade >= idadeMin and _idade <= idadeMax):
                                    break
                                else:
                                    print(stylize(f"A idade do jogador tem de ser entre {idadeMin} e {idadeMax}", colored.fg("red")))
                        
                        while True:
                            _posicao = str(input("Introduza a posicao do jogador (suplente ou titular): "))
                            if (_posicao == "suplente" or _posicao == "titular"):
                                break
                            else:
                                print(stylize("Posição inválida", colored.fg("red")))

                        jogadores.append(_nome)
                        idade.append(_idade)
                        posicao.append(_posicao)

                informacaoInserida = True

                writeInFile()

            # Print teams
            printEquipas()
            
            # What team to manage
            while True:
                equipaGerirStr = input("Introduza qual o nome da equipa que quer editar: ")
                if (equipas.count(equipaGerirStr) >= 1):
                    equipaGerir = equipas.index(equipaGerirStr) + 1
                    break;
                else:
                    print(stylize("Nome da equipa inválido", colored.fg("red")))

            print(stylize(" ----- M E N U ----- ", colored.fg("green")))
            print(" 1 -> Adicionar jogador")
            print(" 2 -> Remover jogador")
            print(" 3 -> Voltar")
            print(stylize(" ------------------- ", colored.fg("green")))

            # Menu 2 options
            while True:
                try:
                    opcaoMenu2 = int(input("Introduza uma opção: "))
                except(ValueError):
                    print(stylize("Opção inválida", colored.fg("red")))
                else:
                    if (opcaoMenu2 >= 1 and opcaoMenu2 <= 3):
                        break;
                    else:
                        print(stylize("Opção inválida", colored.fg("red")))

            # Add player
            if opcaoMenu2 == 1:
                addJogador()
            # Remove player
            elif opcaoMenu2 == 2:
                removeJogador()
            # Go back to menu 1
            elif opcaoMenu2 == 3:
                break
            
            # Save new info in file
            writeInFile()
        
        # Manage games and leaderboards
        elif (opcaoMenu1 == 2):
            if (informacaoInserida):
                while True:
                    print(stylize(" ----- M E N U ----- ", colored.fg("green")))
                    print(" 1 -> Gerir jogos")
                    print(" 2 -> Deletar jogos")
                    print(" 3 -> Voltar")
                    print(stylize(" ------------------- ", colored.fg("green")))

                    # Menu 3 options
                    while True:
                        try:
                            opcaoMenu3 = int(input("Introduza uma opção: "))
                        except(ValueError):
                            print(stylize("Opção inválida", colored.fg("red")))
                        else:
                            if (opcaoMenu3 >= 1 and opcaoMenu3 <= 3):
                                break;
                            else:
                                print(stylize("Opção inválida", colored.fg("red")))

                    if (opcaoMenu3 == 1) and (equipasJaJogaram == False):
                        # Print the games
                        print(stylize(" ----- J O G O S ----- ", colored.fg("green")))
                        for equipa in range(len(equipas) - 1):
                            for j in range(equipa + 1, len(equipas)):
                                print(f"{equipas[equipa]} x {equipas[j]}")
                                jogos.append(equipas[equipa])
                                jogos.append(equipas[j])
                                numJogos += 1
                        print(stylize(" ------------------- ", colored.fg("green")))

                        for i in range(0, len(jogos)):
                            if i % 2 == 0:
                                print(stylize(f"----- {jogos[i]} x {jogos[i + 1]} ----", colored.fg("light_magenta")))

                            # Ask for the goals
                            while True:
                                try:
                                    golosInput = int(input(f"Introduza número de golos da equipa {jogos[i]}: "))
                                except(ValueError):
                                    print(stylize("Número de golos inválido", colored.fg("red")))
                                else:
                                    if (golosInput >= 0):
                                        golos.append(golosInput)
                                        break
                                    else:
                                        print(stylize("Número de golos inválido", colored.fg("red")))

                        for i in range(0, numEquipas):
                            pontos.append(0)
                            golosEquipas.append(0)
                            golosSofridos.append(0)
                            numJogosEquipas.append(0)
                            for j in range(0, len(golos)):
                                if (equipas[i] == jogos[j]):
                                    golosEquipas[i] += golos[j]

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

                        # Add 3 points
                        for i in range(0, len(equipasWin)):
                            #print(equipas.index(equipasWin[i]))
                            pontos[equipas.index(equipasWin[i])] += 3

                        # Add 1 point
                        for i in range(0, len(equipasEmpate)):
                            pontos[equipas.index(equipasEmpate[i])] += 1

                        # Number of games of each team
                        for i in range(0, numEquipas):
                            aux = jogos.count(equipas[i])
                            numJogosEquipas[i] = aux

                        info = []

                        for i in range(0, numEquipas):
                            info.append([])
                            for j in range(0, 6):
                                info[i].append(0)

                        for i in range(0, numEquipas):
                            for j in range(0, 6):
                                if (j == 0):
                                    info[i][j] = equipas[i]
                                elif (j == 1):
                                    info[i][j] = golosEquipas[i]
                                elif (j == 2):
                                    info[i][j] = golosSofridos[i]
                                elif (j == 3):
                                    info[i][j] = numJogosEquipas[i]
                                elif (j == 4):
                                    info[i][j] = golosEquipas[i]-golosSofridos[i]
                                elif (j == 5):
                                    info[i][j] = pontos[i]

                        # Print info
                        printLeaderboard()

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

                        for i in range(0, numEquipas):
                            if (equipaEmpate[i] == equipas[i]):
                                diferencaEmpate.append(golosEquipas[i] - golosSofridos[i])
                            else:
                                diferencaEmpate.append(-9999)

                        minDifEmpate = max(diferencaEmpate)
                        for i in range(0, len(diferencaEmpate)):
                            if diferencaEmpate.count(minDifEmpate) > 1:
                                equipaVencedora = "Nao há vencedor"
                            else:
                                equipaVencedora = f"Equipa vencedora: {equipaEmpate[diferencaEmpate.index(minDifEmpate)]}"

                        equipasJaJogaram = True

                        print(stylize(equipaVencedora, colored.fg("green")))

                    # Reset leaderboard
                    elif (opcaoMenu3 == 2):
                        jogos = []
                        golos = []
                        golosEquipas = []
                        golosSofridos = []
                        numJogosEquipas = []
                        equipasEmpate = []
                        equipasWin = []
                        pontos = []
                        equipasJaJogaram = False
                        print(stylize("Informações dos jogos eleminadas", colored.fg("red")))

                    # Go back
                    elif (opcaoMenu3 == 3):
                        break

                    # The teams already played
                    else:
                        # Print leaderboard
                        printLeaderboard()

                        print(stylize("As equipas já jogaram", colored.fg("red")))
            else:
                print(stylize("As equipas ainda nao foram criadas", colored.fg("red")))
                
        elif (opcaoMenu1 == 3):
            print(stylize(" ------------------- ", colored.fg("red")))
            print(f"Idades dos jogadores -> {regras['Idade']}")
            print(f"Número de jogadores  -> {regras['Jogadores']}")
            print(f"Número de equipas    -> {regras['Equipas']}")
            print(stylize(" ------------------- ", colored.fg("red")))

        # Close program
        else:
            programON = False
            print(stylize("Programa encerrado", colored.fg("red")))
            break