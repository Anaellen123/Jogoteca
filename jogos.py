import forca
import ADIVINHACAO

def escolhe_jogo():
    print("******************************")
    print("*******escolhe seu jogo*******")
    print("******************************")

    print("(1)forca (2)Adivinhação")

    jogo = int(input("qual jogo?"))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando adivinhação")
        ADIVINHACAO.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
