import sys 

tabuleiro = [['| |', '| |', '| |'],['| |', '| |', '| |'],['| |', '| |', '| |']]

print('O BOM E VELHO JOGO DA VELHA' + '\n')

for i in range(len(tabuleiro)):
    print(''.join(tabuleiro[i]))

print()

################################# Início da escolha da linha do jogador O
def jogador1_linha(linha1):
    """
    Retornará a escolha da linha do jogador O
    """
    
    while True:
        if not linha1:
            print('FIM')
            break
        while linha1 not in ['1','2','3']:
            linha1 = input('Digite uma linha válida: ')
        print('Jogador O, escolheu a linha ' + linha1 + '\n')
        break

    return linha1
################################# Fim da escolha da linha do jogador O

################################# Início da escolha da coluna do jogador O
def jogador1_coluna(coluna1):
    """
    Retornará a escolha da lcoluna do jogador O
    """
    
    while True:
        if not coluna1:
            print('FIM')
            break
        while coluna1 not in ['1','2','3']:
            coluna1 = input('Digite uma coluna válida: ')
        print('Jogador O, escolheu a coluna ' + coluna1 + '\n')
        break

    return coluna1
################################ Fim da escolha da coluna do jogador O

################################Incio da escolha de linha do jogador X
def jogador2_linha(linha2):
    """
    Retornará a escolha da linha do jogador X
    """
    
    while True:
        if not linha2:
            print('FIM')
            break
        while linha2 not in ['1','2','3']:
            linha2 = input('Digite uma linha válida: ')
        print('Jogador X, escolheu a linha ' + linha2 + '\n')
        break

    return linha2
################################Fim da escolha de linha do jogador X

################################Incio da escolha de coluna do jogador X
def jogador2_coluna(coluna2):
    """
    Retornará a escolha da coluna do jogador X
    """
    
    while True:
        if not coluna2:
            print('FIM')
            break
        while coluna2 not in ['1','2','3']:
            coluna2 = input('Digite uma coluna válida: ')
        print('Jogador X, escolheu a coluna ' + coluna2 + '\n')
        break
        
    return coluna2
################################Fim da escolha de coluna do jogador X

################################Início de atualizaço de tabuleiro para jogador 0
def tabuleiro_jogador1():
    """
    Retornará o desenho atualizado do tabuleiro para o jogador O
    """
    linhaO = int(jogada_linha1) - 1

    colunaO = int(jogada_coluna1) - 1

    nova_jogada = tabuleiro[linhaO]

    del tabuleiro[linhaO]

    del nova_jogada[colunaO]

    nova_jogada.insert(colunaO, "|O|")

    tabuleiro.insert(linhaO, nova_jogada)

    for i in range(len(tabuleiro)):
        print(''.join(tabuleiro[i]))
    
    return tabuleiro
#############################Fim de atualizaço de tabuleiro para jogador O

############################# Início de atualização de tabuleiro para jogador X
def tabuleiro_jogador2():
    """
    Retornará o desenho atualizado do tabuleiro para o jogador X
    """
    linhaX = int(jogada_linha2) - 1

    colunaX = int(jogada_coluna2) - 1

    nova_jogada = tabuleiro[linhaX]

    del tabuleiro[linhaX]

    del nova_jogada[colunaX]

    nova_jogada.insert(colunaX, "|X|")

    tabuleiro.insert(linhaX, nova_jogada)

    for i in range(len(tabuleiro)):
        print(''.join(tabuleiro[i]))
    
    return tabuleiro
############################## Fim de atualização de tabuleiro para jogador X

while True:
    entrada_linha1 =  input('Jogador O, digite a linha que deseja jogar: 1, 2 ou 3. Deixe em branco e tecle "Enter" se deseja encerar: ')
    jogada_linha1 = jogador1_linha(entrada_linha1)

    if not entrada_linha1:
        print('FIM')
        break
        
    entrada_coluna1 = input('Agora digite a coluna que deseja: 1, 2 ou 3. Deixe em branco e tecle enter se deseja encerrar: ')
    jogada_coluna1 = jogador1_coluna(entrada_coluna1)

    tabuleiro_jogador1()
    
    if tabuleiro[0][0] == '|O|' and tabuleiro[0][1] == '|O|' and tabuleiro[0][2] == '|O|':
        print('Jogador O, venceu!')
        break
                
    elif tabuleiro[1][0] == '|O|' and tabuleiro[1][1] == '|O|' and tabuleiro[1][2] == '|O|':
        print('Jogador O, venceu!')
        break
                
    elif tabuleiro[2][0] == '|O|' and tabuleiro[2][1] == '|O|' and tabuleiro[2][2] == '|O|':
        print('Jogador O, venceu!')
        break
                
    elif tabuleiro[0][0] == '|O|' and tabuleiro[1][0] == '|O|' and tabuleiro[2][0] == '|O|':
        print('Jogador O, venceu!')
        break
                
    elif tabuleiro[0][1] == '|O|' and tabuleiro[1][1] == '|O|' and tabuleiro[2][1] == '|O|':
        print('Jogador O, venceu!')
        break
                
    elif tabuleiro[0][2] == '|O|' and tabuleiro[1][2] == '|O|' and tabuleiro[2][2] == '|O|':
        print('Jogador O, venceu!')
        break
                
    elif tabuleiro[0][0] == '|O|' and tabuleiro[1][1] == '|O|' and tabuleiro[2][2] == '|O|':
        print('Jogador O, venceu!')
        break
                
    elif tabuleiro[0][2] == '|O|' and tabuleiro[1][1] == '|O|' and tabuleiro[2][0] == '|O|':
        print('Jogador O, venceu!')
        break
    
    
    entrada_linha2 = input('Jogador X, digite a linha que deseja jogar: 1, 2 ou 3. Deixe em branco e tecle "Enter" se deseja encerar: ')
    jogada_linha2 = jogador2_linha(entrada_linha2)
    

    if tabuleiro[0][0] == '|X|' and tabuleiro[0][1] == '|X|' and tabuleiro[0][2] == '|X|':
        print('Jogador X, venceu!')
        break
            
    elif tabuleiro[1][0] == '|X|' and tabuleiro[1][1] == '|X|' and tabuleiro[1][2] == '|X|':
        print('Jogador X, venceu!')
        break
            
    elif tabuleiro[2][0] == '|X|' and tabuleiro[2][1] == '|X|' and tabuleiro[2][2] == '|X|':
        print('Jogador X, venceu!')
        break
            
    elif tabuleiro[0][0] == '|X|' and tabuleiro[1][0] == '|X|' and tabuleiro[2][0] == '|X|':
        print('Jogador X, venceu!')
        break
            
    elif tabuleiro[0][1] == '|X|' and tabuleiro[1][1] == '|X|' and tabuleiro[2][1] == '|X|':
        print('Jogador X, venceu!')
        break
            
    elif tabuleiro[0][2] == '|X|' and tabuleiro[1][2] == '|X|' and tabuleiro[2][2] == '|X|':
        print('Jogador X, venceu!')
        break
            
    elif tabuleiro[0][0] == '|X|' and tabuleiro[1][1] == '|X|' and tabuleiro[2][2] == '|X|':
        print('Jogador X, venceu!')
        break
            
    elif tabuleiro[0][2] == '|X|' and tabuleiro[1][1] == '|X|' and tabuleiro[2][0] == '|X|':
        print('Jogador X, venceu!')
        break
    
    entrada_coluna2 = input('Agora digite a coluna que deseja: 1, 2 ou 3. Deixe em branco e tecle enter se deseja encerrar: ')
    jogada_coluna2 = jogador2_coluna(entrada_coluna2)

    tabuleiro_jogador2()
    
    if resultado == 'X':
        print('Jogador X, venceu!')
        break
    
######################################Início da verificação de preenchimento
#linha1 = int(jogada_linha1) - 1 
#coluna1 = int(jogada_coluna1) - 1  
#linhaX = int(jogada_linha2) - 1
#colunaX = int(jogada_coluna2) - 1

#while True:    
#    if linhaX == linha1:
#        if colunaX == coluna1:
#            print('Posição já está preenchida\n')
#            entrada_linha2 = input('Jogador X, digite a linha que deseja jogar: 1, 2 ou 3. Deixe em branco e tecle "Enter" se deseja encerar: ')
#            if not entrada_linha2:
#                print('FIM')
#                sys.exit('Você optou por encerrar.')
#            jogada_linha2 = jogador2_linha(entrada_linha2)
#        entrada_coluna2 = input('Agora digite a coluna que deseja: 1, 2 ou 3. Deixe em branco e tecle enter se deseja encerrar: ')
#        jogada_coluna2 = jogador2_coluna(entrada_coluna2)
#        break        
######################################Fim da verificação de preenchimento
