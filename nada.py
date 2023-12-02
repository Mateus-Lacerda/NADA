from random import randint
from time import sleep

def green(string):
    return '\033[32m' + string + '\033[0m'

def red(string):
    return '\033[31m' + string + '\033[0m'

def yellow(string):
    return '\033[33m' + string + '\033[0m'

def blue(string):
    return '\033[34m' + string + '\033[0m'

def purple(string):
    return '\033[35m' + string + '\033[0m'

def cyan(string):
    return '\033[36m' + string + '\033[0m'

def white(string):
    return '\033[37m' + string + '\033[0m'

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def sleepmain(speed):
    sleep(speed)

def line(numbersLines=7, spacesBetween=3):
    line = []
    for _ in range(numbersLines):
        line.append(str(randint(10, 99)))
        line.append(' ')
    line.pop(-1)
    for _ in range(spacesBetween):
        line.append(' ')
    return ''.join(str(x) for x in line)

def options(columns):
    print(green('___________________________________________________________________'))
    print(green('Agora você pode escolher a velocidade de atualização dos dados.'))
    print(green('Quanto menor o número, mais rápido os dados serão atualizados.'))
    print(green('Recomendo que escolha um número entre 0.001 e 0.1'))
    print(green('___________________________________________________________________'))
    speed = input(green('Escolha a velocidade de atualização (Digite enter para usar o valor padrão): '))
    if speed.isnumeric():
        speed = float(speed)
    else:
        print(green('___________________________________________________________________'))
        print(green('Você não escolheu um número válido.'))
        print(green('A velocidade padrão será usada.'))
        print(green('___________________________________________________________________'))
        speed = 0.001
    print(green('___________________________________________________________________'))
    print(green('Agora você pode escolher a cor dos dados.'))
    print(green('1 - Verde'))
    print(red('2 - Vermelho'))
    print(yellow('3 - Amarelo'))
    print(blue('4 - Azul'))
    print(purple('5 - Roxo'))
    print(cyan('6 - Ciano'))
    print(white('7 - Branco'))
    print(green('___________________________________________________________________'))
    color = input(green('Escolha a cor dos dados: '))
    if color == '1':
        color = green
    elif color == '2':
        color = red
    elif color == '3':
        color = yellow
    elif color == '4':
        color = blue
    elif color == '5':
        color = purple
    elif color == '6':
        color = cyan
    elif color == '7':
        color = white
    else:
        print(green('___________________________________________________________________'))
        print(green('Você não escolheu uma cor válida.'))
        print(green('A cor padrão será usada.'))
        print(green('___________________________________________________________________'))
        color = green
    print(color('___________________________________________________________________'))
    print(color('Agora escolha quantos números quer ver por linha.'))
    print(color('Recomendo que escolha um número entre 1 e 10'))
    print(color('___________________________________________________________________'))
    numbersLines = input(color('Escolha quantos números quer ver por linha (Digite enter para usar o valor padrão): '))
    if is_integer(numbersLines):
        numbersLines = int(numbersLines)
    else:
        print(color('___________________________________________________________________'))
        print(color('Você não escolheu um número válido.'))
        print(color('O número padrão será usado.'))
        print(color('___________________________________________________________________'))
        numbersLines = 7
    print(color('___________________________________________________________________'))
    print(color('Agora escolha quantos espaços quer deixar entre cada coluna.'))
    print(color('Recomendo que escolha um número entre 1 e 10'))
    print(color('___________________________________________________________________'))
    spacesBetween = input(color('Escolha quantos espaços quer deixar entre cada coluna (Digite enter para usar o valor padrão): '))
    if is_integer(spacesBetween):
        spacesBetween = int(spacesBetween)
    else:
        print(color('___________________________________________________________________'))
        print(color('Você não escolheu um número válido.'))
        print(color('O número padrão será usado.'))
        print(color('___________________________________________________________________'))
        spacesBetween = 3
    print(color('___________________________________________________________________'))
    print(color('Resumo das configurações:'))
    print(color(f'Velocidade: {speed}'))
    print(color(f'Números por linha: {numbersLines}'))
    print(color(f'Espaços entre colunas: {spacesBetween}'))
    print(color('___________________________________________________________________'))
    print(color('Resultado:'))
    for _ in range(columns):
        thisline = line(numbersLines, spacesBetween)
        print(color(thisline), end='')
    print(color('___________________________________________________________________'))
    choice = input(color('Satisfeito?')).strip().lower()[0]
    if choice == 'n':
        options(columns)
    return speed, color, numbersLines, spacesBetween

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
    choice = int(input(green('Para realizar configurções avançadas, digite 1. Para continuar, digite 0: ')))
    if choice == 1:
        opts = options(columns)
        speed = opts[0]
        color = opts[1]
        numbersLines = opts[2]
        spacesBetween = opts[3]
    else:
        speed = 0.001
        color = green
        numbersLines = 7
        spacesBetween = 3
    print(color('___________________________________________________________________'))
    print(color('Obrigado por escolher o NADA - NASA\'s Authomatic Data Algorithm\nAguarde enquanto o programa é carregado...'))
    sleep(2)
    print(color('\nAperte Enter para começar e Ctrl+C para parar'))
    input()
    while True:
        counter = 0
        while True:
            thisline = line(numbersLines, spacesBetween)
            print(color(thisline), end='')
            sleepmain(speed)
            counter += 1
            if counter == columns:
                print('')
                counter = 0
                break

if __name__ == '__main__':
    main()
