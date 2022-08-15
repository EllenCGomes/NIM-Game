# funcao computador_escolhe_jogada(n,m) - recebe n e m e retorna o numero de pecas que vai retirar, deixando multiplo de (m+1)
def computador_escolhe_jogada(n,m):

    multiplo = True
    x = 1

    while x<=m and x>=1 and multiplo:
        y = n-x
        if y % (m+1) == 0:
            multiplo = True
            print("O computador retirou:", (n-y))
            return (n-y)
        else:
            multiplo = False 
            if x<m:
                x = x + 1
                multiplo = True
            else:
                print("O computador retirou:", m)
                return m           

# funcao usuario_escolhe_jogada(n,m) - recebe n e m, pede para o usuario inserir o num de pecas a retirar e verifica se eh valido (int !=n and >=1 and <=m). If int !=n and >=1, return int, else ("informe uma jogada valida")
def usuario_escolhe_jogada(n,m):

    valido = False
    count = 0
    primeira = True
    
    if primeira:
        if n>=m:
            while not valido and n>m:
                usu = int(input("Quantas peças você quer retirar?"))
                if usu!=n and usu>=1 and usu<=m:
                    valido = True
                    primeira = False   
                    print("Você retirou:", usu)
                    return usu
                else:
                    print("Erro: Este valor é inválido. Tente novamente!") 
                    count = count + 1
                    primeira = True

            while not valido and n == m:
                usu = int(input("Quantas peças você quer retirar?"))
                if usu<=n and usu>=1 and usu<=m:
                    valido = True
                    primeira = False   
                    print("Você retirou:")
                    return usu
                else:
                    print("Erro: Este valor é inválido. Tente novamente!") 
                    count = count + 1
                    primeira = True
        else:
            print("Erro: Este valor é inválido. Tente novamente!") 
            valido = False
            primeira = True
            count = count + 1
    
    if not primeira:
        while not valido:
            usu = int(input("Quantas peças você quer retirar?"))
            if usu>=1 and usu<=m:
                valido = True
                primeira = False   
                print("Você retirou:", usu)
                return usu
            else:
                print("Erro: Este valor é inválido. Tente novamente!") 
                count = count + 1
                primeira = True

# partida() - nao recebe parametro, input n e m, chama funcoes computador e usuario ate n == 0, if n eh multiplo de (m+1) - jogador comeca; else computador comeca, return numero de pecas que sobraram (novo n). Ao final print quem ganhou
def partida():
    
    n = int(input("Qual o número total de peças para este jogo?"))
    m = int(input("Qual o limite de peças por jogada?"))
    
    count = 0
    comp = False
    usuario = False 
    
    while n != 0 and comp == False and usuario == False:
        if count == 0:
            if n % (m+1) == 0:
                print("Você começa!")
                pecasusu = usuario_escolhe_jogada(n,m)
                n = n - pecasusu
                print("Restam", n, "peças no tabuleiro")
                count = count + 1
                usuario = True
            else:
                print("O computador começa!")
                pecascomp = computador_escolhe_jogada(n,m) 
                n = n - pecascomp
                print("Restam", n, "peças no tabuleiro")
                count = count + 1
                comp = True

    while n != 0 and comp == True or usuario == True:
            if comp == True:
                pecasusu2 = usuario_escolhe_jogada(n,m)
                n = n - pecasusu2
                print("Restam", n, "peças no tabuleiro")
                usuario = True
                comp = False
                count = count + 1
            else:
                pecascomp2 = computador_escolhe_jogada(n,m) 
                n = n - pecascomp2
                print("Restam", n, "peças no tabuleiro")
                comp = True 
                usuario = False
                count  = count + 1

    while n == 0:
        if comp == True:
            return "Fim de jogo! O computador ganhou"
        else: 
            return "Fim de jogo! Você ganhou" 

# campeonato() - realizar 3 partidas e mostrar ao final o placar voce X computador e print quem ganhou
def campeonato():
    
    placarcomp = 0
    placarusu = 0
    countpartidas = 0
    rodada = 1

    while countpartidas<3:
        print("***Rodada", rodada, "***")
        resultado = partida()
        if resultado == "Fim de jogo! O computador ganhou":
            placarcomp = placarcomp + 1
            countpartidas = countpartidas + 1
            rodada = rodada + 1
        else:
            placarusu = placarusu + 1
            countpartidas = countpartidas + 1
            rodada = rodada + 1

    if countpartidas == 3:
        print("Fim do campeonato!")
        print("Placar: Você", placarusu, "X", placarcomp, "Computador")            

# jogo() - abertura jogo        
def jogo():

    valido = True
    count = 0 

    while valido: 
        print("Bem-vindo ao jogo do NIM!\n")
        opcaojogo = int(input("Escolha 1 para jogar uma partida isolada ou 2 para um campeonato"))
        if opcaojogo == 1 or opcaojogo == 2:
            valido = True
            if opcaojogo == 1:
                print(partida())
            else:
                print(campeonato())    
        else:
            valido = False
            print("Erro: Este valor é inválido. Tente novamente!") 
            count = count + 1  
          
jogo()