import os
board = [0,0,0,0,0,0,0,0,0]

def zeraBoard():
  for posicao in range(9):
    board[posicao]=0


def menu():
  zeraBoard()
  continuar = int(input("0. Sair. \n" + "1. Iniciar o jogo. \n"))
  if continuar == 1:
    game()
    
  else:
    print("Saindo...")


def deixaBonito(valor):
    if(valor == 0):
      return " "
    elif(valor == 1):
      return "X"
    else:
      return "O"
    


def ganhou():
  linha1 =board[0]+board[1]+board[2]
  linha2 =board[3]+board[4]+board[5]
  linha3 =board[6]+board[7]+board[8]
  coluna1 =board[0]+board[3]+board[6]
  coluna2 =board[1]+board[4]+board[7]
  coluna3 =board[2]+board[5]+board[8]
  diagonal1 =board[0]+board[4]+board[8]
  diagonal2 =board[2]+board[4]+board[6]
  if linha2 ==3 or linha2 ==-3 or linha1 ==3 or linha1 == -3 or linha3 ==3 or linha3 ==-3 or diagonal1 ==3 or diagonal1==-3 or diagonal2 ==3 or diagonal2 ==-3 or coluna1 ==3 or coluna1 ==-3 or coluna2 ==3 or coluna2==-3 or coluna3==3 or coluna3==-3:
    return 1
    
  
  return 0
  


def printBoard():
  print("")
  print("{}|{}|{}".format(deixaBonito(board[0]), deixaBonito(board[1]), deixaBonito(board[2])))
  print("-+-+-")
  print("{}|{}|{}".format(deixaBonito(board[3]),deixaBonito(board[4]),deixaBonito(board[5])))
  print("-+-+-")
  print("{}|{}|{}".format(deixaBonito(board[6]),deixaBonito(board[7]),deixaBonito(board[8])))
  print("")

def trocajogador(j):
  if j == 1:
    return -1
  else:
    return 1

def estaocupado(posicao):
  if board[posicao] == 0:
    return False
  else:
    return True

def verificaVencedor():
  linha1 =board[0]+board[1]+board[2]
  linha2 =board[3]+board[4]+board[5]
  linha3 =board[6]+board[7]+board[8]
  coluna1 =board[0]+board[3]+board[6]
  coluna2 =board[1]+board[4]+board[7]
  coluna3 =board[2]+board[5]+board[8]
  diagonal1 =board[0]+board[4]+board[8]
  diagonal2 =board[2]+board[4]+board[6]
  if linha2 ==3 or linha1 ==3 or linha3 ==3 or diagonal1 ==3 or diagonal2 ==3 or coluna1 ==3 or coluna2 ==3 or coluna3==3:
    print("Jogador 1 ganhou!!!")
  elif linha2 ==-3 or linha1 ==-3 or linha3 ==-3 or diagonal1==-3 or diagonal2 ==-3 or coluna1 ==-3 or coluna2==-3 or coluna3==-3:
    print("Jogador 2 ganhou!!!")
  

def game():
  jogador = 1 
  jogada = 0
  while ganhou() ==  0:
    printBoard()
    if jogador == 1:
      position = int(input("Jogador 1: "))
    else:
      position = int(input("Jogador 2: "))
    if (estaocupado(position-1)):
      print("Está ocupado!")
    else:
      board[position-1] = jogador
      jogador=trocajogador(jogador)
      jogada +=1
      os.system('cls')
    if ganhou():
      printBoard()
      verificaVencedor()
      jogar = int(input("Deseja jogar novamente? \n 0:Sair \n 1:continuar \n" ))
      if jogar == 1:
        menu()
      break
    if jogada == 9:
      printBoard()
      print("Empatou!!!")
      jogar = int(input("Deseja jogar novamente? \n 0:Sair \n 1:continuar \n" ))
      if jogar == 1:
        menu()


      break
menu()