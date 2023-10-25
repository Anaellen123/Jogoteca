import random
def jogar():
    print("********************************")
    print("Bem Vindo ao Jogo de Adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Qual o nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2)Médio (3)Díficil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("digite um dúmero entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if(acertou):
            print("você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("você errou!Seu chute foi maior do que o número secreto".format(pontos))
            elif(menor):
                print("você errou!Seu numero foi menor do que o número secreto. pontos {}".format(pontos))
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos





if(__name__=="__main__"):
    jogar()


