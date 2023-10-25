import jogos

def acessar():
    palavra_chave = "ldT-2348"

    login = input("entra com a palavra de acesso: ")

    if(login == palavra_chave):
        print("você será encaminhado a página do jogo")
        jogos.escolhe_jogo()

    else:
        print("ocorreu um erro, tente novamente!")


if(__name__ == "__main__"):
    acessar()