from os import system

class Tabuada:

    def __init__(self):
        self.num = 0

    def Num(self):

        try:
            print()
            self.num = int(input('Introduza um número para ver a sua tabuada: '))
            print()
        except ValueError:
            print('Não é possivel ver a tabuada do número introduzido, tente novamente!')

    def CalcularTabuada(self):

        for i in range(1, 11):
            print('{} x {} = {}'.format(self.num, i, self.num * i))

###########################################################################################################

def main():

    Iniciar = Tabuada()
    escolha = 0

    while True:

        system('cls')

        print('============== MENU ==============')
        print()
        print('1 - Ver a tabuada de um número')
        print('2 - Créditos')
        print('3 - Sair')
        escolha = int(input('-> '))
        print()
        print('==================================')

        if escolha == 1:
            Iniciar.Num()
            Iniciar.CalcularTabuada()
            print()
            print('Pressione ENTER para voltar ao menu principal!')
            input()
        elif escolha == 2:
            print()
            print('Desenvoldido por: scr1pter')
            print()
            print('Pressione ENTER para voltar ao menu principal!')
            input()
        elif escolha == 3:
            break
        else:
            print()
            print('Opção inválida, tente novamente')
            print()
            print('Pressione ENTER para voltar ao menu principal!')
            input()

main()