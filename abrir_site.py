#Abrir Browser/Navegador
import webbrowser

def main(url=0, url2=0, url3=0):
    while True:
        print('>>>>>>> ABRE SITES <<<<<<<<<')
        print('OPÇÕES: ')
        print("""    [1] - Abrir uma Janela
        [2] - Abrir Duas Janelas
        [3] - Abrir Três Janelas
        [4] - Encerrar Programa""")

        opção = int(input('Escolha: '))
        if opção == 1:
            link = str(input('Sua Url: '))
            url = link 
            webbrowser.open(url)
        elif opção == 2:
            link = str(input('Sua Url: '))
            link2 = str(input('Sua Url: '))
            url = link 
            url2 = link2 
            for s in range(0, 1):
                webbrowser.open(url)
            for site in range(0, 1):
                webbrowser.open(url2)
        elif opção == 3:
            link = str(input('Sua Url: '))
            link2 = str(input('Sua Url: '))
            link3 = str(input('Sua Url: '))
            url = link 
            url2 = link2 
            url3 = link3 
            for i in range(0, 1):
                webbrowser.open(url)
            for s in range(0, 1):
                webbrowser.open(url2)
            for t in range(0, 1):
                webbrowser.open(url3)
        elif opção == 4:
            break 
        else:
            print('Opção Inválida. Tente novamente!')
            main()




main()




