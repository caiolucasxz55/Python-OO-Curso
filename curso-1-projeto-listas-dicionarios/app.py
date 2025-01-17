import os
restaurantes = []


def cadastro_restaurante():
    nome = input('nome do restaurante: ')
    tipo = input('qual o tipo do restaurante: ')
    dados = nome,tipo
    restaurantes.append(dados)
    
def listar_restaurantes():
    for i in restaurantes:
        print(i)


while True:
    print(" Sabor Express")
    print("[1]-Cadastrar Restaurante")
    print("[2]-Listar Restaurante")
    print("[3]-Ativar restaurante")
    print("[4]-Sair")
    opcao = input('escolha sua opção: ')
    
    if opcao == '1':
        cadastro_restaurante()
        os.system('cls')
        print('Cadastrar Restaurante:')
        
    elif opcao == '2':
        
        listar_restaurantes()
        os.system('cls')
        print('Lista de Restaurantes: ')
        
    elif opcao == '3':
        os.system('cls')
        print('Ativar Restaurante: ') 
               
    elif opcao == '4':
        os.system('cls')
        print('Saindo do programa...')
        break
    else:
        print('ERRO:opção invalida')