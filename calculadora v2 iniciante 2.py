def soma (n1,n2):
    op = n1 + n2
    return op
def subtracao (n1, n2):
    op = n1 - n2
    return op
def divisao (n1,n2):
    if n2==0:
        return "numero invalidao digite novamente"
    op = n1 / n2
    return op
def multiplicacao (n1,n2):
    op = n1 * n2
    return op
def letra (mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("digite apenas numero sem letras")
def semletra (mensagem):
        while True:
            try:
                numero = int(input(mensagem))
                return numero
            except ValueError:
                print("digite apenas numero sem letras")


opc = semletra("escolha uma opção 1-começar 2-sair : ")

while opc == 1:
    print("escolha uma opção ")
    vl = semletra("\n 1 - soma\n 2 - subtração\n 3 - divisão\n 4 - multiplicação\n 5 - sair\n digite a seleção :  ")
    if vl == 1:
        n1 = letra("digite o primeiro numero : ")
        n2 = letra("digite o segundo numero : ")
        res = soma(n1,n2)
        print(f"o primeiro numero é {n1}\n o segundo numero é {n2}\n o resultado é de = {res}")
    elif vl ==2:
        n1 = letra("digite o primeiro numero : ")
        n2 = letra("digite o segundo numero : ")
        res = subtracao(n1,n2)
        print(f"o primeiro numero é {n1}\n o segundo numero é {n2}\n o resultado é de = {res}")
    elif vl ==3:
        n1 = 0
        n2 = 0
        while n2 == 0:
            n1 = letra("digite o primeiro numero : ")
            n2 = letra("digite o segundo numero : ")
            if n2 == 0:
                print("Não é possível dividir por 0. Digite novamente!")
        res = divisao(n1,n2)
        print(f"o primeiro numero é {n1}\n o segundo numero é {n2}\n o resultado é de = {res}")
    elif vl ==4:
        n1 = letra("digite o primeiro numero : ")
        n2 = letra("digite o segundo numero : ")
        res = multiplicacao(n1,n2)
        print(f"o primeiro numero é {n1}\n o segundo numero é {n2}\n o resultado é de = {res}")
    elif vl == 5:
        print("selecionado sair")
        break
    else:
        print("opção invalida")