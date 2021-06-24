import random


def resposta():
    respostas = ['Sim!', 'Não!', 'Acho que sim', 'Acho que não', 'Óbvio que sim', 'Óbvio que não', 'Claro que sim',
                 'Claro que não', 'Talvez', 'Talvez sim', 'Talvez não', 'Melhor não...', 'Com certeza!',
                 'Com certeza sim!', 'Com certeza não!', 'Não sei...', 'Sei lá', 'Não posso responder isso',
                 'Você que sabe', 'Se você quer...', 'A decisão é sua!']
    return random.choice(respostas)


def pergunta():
    while True:
        pergunta = str(input("\nFaça uma pergunta : "))
        if "?" in pergunta or pergunta == "SAIR":
            break
        else:
            print("Por favor, digite uma pergunta.\n")
    return pergunta


def jogar():
    print("-- Decida por mim --")
    print("Se quiser sair digite SAIR\n\n")

    while True:
        if not pergunta() == "SAIR":
            print(resposta())
        else:
            break

    print("\n\nAte mais!!")


jogar()