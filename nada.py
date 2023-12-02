from random import randint
from time import sleep

def green(string):
    return '\033[32m' + string + '\033[0m'

def red(string):
    return '\033[31m' + string + '\033[0m'

def sleepmain():
    sleep(0.001)

def line():
    finalline = []
    for _ in range(1):
        line = []
        for _ in range(7):
            line.append(str(randint(10, 99)))
            line.append(' ')
        finalline.extend(line)
        finalline.append('    ')
    return ''.join(str(x) for x in finalline)

def main():
    print(green("Bem vindo ao NADA - NASA\'s Automatic Data Algorithm\nPara que a visualização se adeque a seu monitor, é importante escolher a quantidade de colunas de dados que deseja ver. Veja os exemplos e escolha:"))
    print(red('_______________________________________________________________________________________________________'))
    print(red("ATENÇÃO, OS DADOS GERADOS PARA AMOSTRAGEM NÃO SÃO SENSÍVEIS"))
    print(red("TODOS OS DADOS SENSÍVEIS EXPLOITADOS AQUI PASSAM RÁPIDO DEMAIS PARA O OLHO HUMANO CONSEGUIR DISTINGUIR"))
    print(red("ISSO É APENAS UMA AMOSTRAGEM IN-HACKEÁVEL DOS DADOS SENSÍVEIS DA NASA!!!"))
    print(red('_______________________________________________________________________________________________________'))
    for i in range(1,11):
        print(green(f"{i} Colunas:"))
        for i in range(i):
            thisline = line()
            print(green(thisline), end='')
        print('')
        print()
    print(green('___________________________________________________________________'))
    columns = int(input(green('Eai, quantas vão ser? ')))
    print(green('___________________________________________________________________'))
    print(green('Obrigado por escolher o NADA - NASA\'s Authomatic de Data Algorithm\nAguarde enquanto o programa é carregado...'))
    sleep(2)
    print(green('\nAperte Enter para começar e Ctrl+C para parar'))
    input()
    while True:
        counter = 0
        while True:
            thisline = line()
            print(green(thisline), end='')
            sleepmain()
            counter += 1
            if counter == columns:
                print('')
                counter = 0
                break

if __name__ == '__main__':
    main()
