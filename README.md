Built with: Python 

 

Project Status: Concluded :heavy_check_mark: 

 

------------------------------------------------------------------------------------------------------------------------------------------------------- 

 

&nbsp; 🇺🇸 &nbsp; This assignment is part of Coursera's course "[Introduction to Computer Science with Python Part 1](https://www.coursera.org/learn/ciencia-computacao-python-conceitos) by University of São Paulo" programming assignments 

 

EXERCISE DESCRIPTION: In this game, **n** pieces are initially placed on a board. Two players play alternately, removing at least 1 and at most **m** pieces each. Whoever takes the last possible pieces wins the game. 
 
You must write a program that allows a person to play NIM against the computer. 
 
To ensure that the computer always wins, you need to consider the two possible scenarios for starting the game: 
 

- If **n** is a multiple of **(m+1)**, the computer must invite the player to start the game with the phrase "You start!" 
 
- Otherwise, the computer takes the initiative to start the game, declaring "Computer begins!" 
 
Once the game has started, the computer's strategy to win is to always leave a number of pieces that is a multiple of **(m+1)** to the player. If this is not possible, you should take out as many pieces as possible. 
 
The program must implement: 
 
1. A **computer_choose_move** function that receives, as parameters, the numbers **n** and **m** described above and returns an integer corresponding to the computer's next move according to the winning strategy. 
 
2. A function **user_choose_move** that receives the same parameters, asks the player to inform his move and checks if the value informed is valid. If the value entered is valid, the function must return it; otherwise, it must ask the user again to enter a valid move. 
 
3. A **game** function that does not receive any parameters, asks the user to inform the values of **n** and **m** and starts the game, alternating between computer and user moves. At each move, the current state of the game must be printed on the screen. When the last piece is removed, this function prints the message "The computer won!" or "You won!" as the case may be. 
 
4. A **championship** function that must play three games in a row and, at the end, show the score of these three games and indicate the winner of the championship. 
 
5. Since it is possible to play individual matches or championships, your program should start by asking the user to choose whether they prefer to play just one match (option 1) or a championship (option 2). 

 

 

------------------------------------------------------------------------------------------------------------------------------------------------------- 

 

 

&nbsp; 🇧🇷 &nbsp; Este exercício é parte da lista de exercícios do curso "[Introdução à Ciência da Computação com Python Parte 1](https://www.coursera.org/learn/ciencia-computacao-python-conceitos)" da Universidade de São Paulo (Coursera)  

 

 

DESCRIÇÃO: Nesse jogo, **n** peças são inicialmente dispostas em um tabuleiro. Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo **m** peças cada um. Quem tirar as últimas peças possíveis ganha o jogo. 

Você deverá escrever um programa que permita a uma pessoa jogar o NIM contra o computador.  

Para garantir que o computador sempre ganhe, é preciso considerar os dois cenários possíveis para o início do jogo: 

- Se **n** é múltiplo de **(m+1)**, o computador deve convidar o jogador a iniciar a partida com a frase "Você começa!" 

- Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!" 

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de **(m+1)** ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis. 

O programa deve implementar: 

1. Uma função **computador_escolhe_jogada** que recebe, como parâmetros, os números **n** e **m** descritos acima e devolve um inteiro correspondente à próxima jogada do computador de acordo com a estratégia vencedora. 

2. Uma função **usuario_escolhe_jogada** que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida. 

3. Uma função **partida** que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de **n** e **m** e inicia o jogo, alternando entre jogadas do computador e do usuário. A cada jogada, deve ser impresso na tela o estado atual do jogo. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso. 

4. Uma função **campeonato** que deve realizar três partidas seguidas e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato.  

5. Dado que é possível jogar partidas individuais ou campeonatos, seu programa deve começar solicitando ao usuário que escolha se prefere jogar apenas uma partida (opção 1) ou um campeonato (opção 2). 
