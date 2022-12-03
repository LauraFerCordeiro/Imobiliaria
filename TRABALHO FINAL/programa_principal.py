#MENU#
from time import sleep
from cliente import *
from imovel import *
from aluguel import *
from datetime import*

# Ornamentos:
# ! -> Mensagens de erro
# # -> Início do programa
# = -> Entrando em um submenu
# - -> Entrando em uma subopção de um submenu/Retorno de submenu
# + -> Operação realizada com sucesso
# ¬ -> Tirando algo
# ¨ -> Adicionando algo
# * -> Alterando algo

BD_Cliente = {}
BD_Imovel = {}
BD_Aluguel = {}

leitura_cliente(BD_Cliente)
leitura_imoveis(BD_Imovel)
leitura_alugueis(BD_Aluguel)

print('#' * 40)
print(f"{'Sem-Teto Imóveis': ^40}")
sleep(0.1)
print(f'{"Os melhores preços!": ^40}')
sleep(0.1)
print(f'{"Se não há o que pagar...": ^40}')
sleep(0.1)
print(f'{"Sai de graça!": ^40}')
print('#' * 40)
sleep(0.1)

def retorno():
    sleep(0.1)
    print('Retornando', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    
    
def print_menuprincipal():
    print("-=" * 40)
    print(f'{"Menu de Opções":-^40}')
    print('_' * 40)
    print(f'|{"[1] - Submenu de Clientes": ^40}|')
    print(f'|{"[2] - Submenu de Imóveis": ^40}|')
    print(f'|{"[3] - Submenu de Aluguéis": ^40}|')
    print(f'|{"[4] - Relatório": ^40}|')
    print(f'|{"[5] - Finalizar o programa": ^40}|')
    print('-=' * 40)

def print_submenu():
    print(f'{" Opções ":-^40}')
    print("_" * 40)
    print(f'|{"[1] - Listar Todos": ^40}|')
    print(f'|{"[2] - Listar um elemento específico": ^40}|')
    print(f'|{"[3] - Incluir um elemento": ^40}|')
    print(f'|{"[4] - Alterar um elemento": ^40}|')
    print(f'|{"[5] - Excluir um elemento": ^40}|')
    print(f'|{"[6] - Sair (retornar ao menu principal)": ^40}|')
    
def menuprincipal():
    print_menuprincipal()
    opcao = input("Digite a opção desejada: ").lower()
    while opcao != "5":
        if opcao == "1":
            submenu_cliente()
        elif opcao == "2":
            submenu_imoveis()
        elif opcao == "3":
            submenu_alugueis()
        elif opcao == "4":
            print()
            data_i = input("Digite a data inicial(00/00/0000):")
            data_f = input("Digite a data final(00/00/0000):")
            x = datetime.strptime(data_i, '%d/%m/%Y')
            y = datetime.strptime(data_f, '%d/%m/%Y')
            relatorio(BD_Cliente, BD_Imovel, BD_Aluguel, x, y)
        else:
            print("!" * 40)
            print("Digite uma opção válida!!!")
            print("!" * 40)
        print_menuprincipal()
        opcao = input("Digite a opção desejada: ").lower()
    if opcao == "5":
        print("-" * 40)
        print(f'|{"- Obrigado por usar! - Ass: Laura e Luis ": ^40}|')
        print('-' * 40)

        
def submenu_cliente():
    print('=' * 40)
    print(f'|{"Submenu De Clientes": ^40}|')
    print('=' * 40)
    print_submenu()
    sub_opcao = input("Digite a opção desejada: ")
    while sub_opcao != "6":
        if sub_opcao == "1":
            listar_todos_clientes(BD_Cliente)
        elif sub_opcao == "2":
            print("-" * 40)
            cpf = input("Digite o CPF para a consulta: ")
            print('-' * 40)
            listar_elemento_clientes(BD_Cliente,cpf)
        elif sub_opcao == "3":
            incluir_clientes(BD_Cliente)
        elif sub_opcao == "4":
            print("*" * 40)
            cpf = input("Digite o CPF para alterar: ")
            validacao = vazia(cpf)
            while validacao == True:
                print("!" * 40)
                print("ERRO! ", end='')
                sleep(0.5)
                print('Nada foi digitado no campo apresentado!')
                sleep(0.5)
                print("!" * 40)
                cpf = input("Digite o CPF para alterar: ").strip()
                validacao = vazia(cpf)      
            print('*' * 40)
            alterar_clientes(BD_Cliente,cpf)
        elif sub_opcao == "5":
            print("¬" * 40)
            cpf = input("Digite o CPF a ser removido: ")
            print('¬' * 40)
            excluir_clientes(BD_Cliente,cpf)
        else:
            print("!" * 40)
            print("Digite uma opção válida!!!")
            print("!" * 40)
        print("=" * 40)
        print(f'|{"Submenu de Clientes": ^40}|')
        print('=' * 40)
        print_submenu()
        sub_opcao = input("Digite a opção desejada: ")
    if sub_opcao == "6":
        retorno()
        arquivo_write(BD_Cliente)

def submenu_imoveis():
    print("=" * 40)
    print(f'|{"Submenu de Imóveis": ^40}|')
    print('=' * 40)
    print_submenu()
    sub_opcao = input("Digite a opção desejada: ")
    while sub_opcao != "6":
        if sub_opcao == "1":
            listar_todos_imoveis(BD_Imovel)
        elif sub_opcao == "2":
            print("-" * 40)
            codigo = input("Digite o código para a consulta: ")
            print('-' * 40)
            listar_elemento_imoveis(BD_Imovel, codigo)
        elif sub_opcao == "3":
            incluir_imoveis(BD_Imovel)
        elif sub_opcao == "4":
            print("-" * 40)
            codigo = input("Digite o código para alterar: ")
            print('-' * 40)
            alterar_imoveis(BD_Imovel, codigo)
        elif sub_opcao == "5":
            print("-" * 40)
            codigo = input("Digite o código para excluir: ")
            print('-' * 40)
            excluir_imoveis(BD_Imovel, codigo)
        else:
            print("!" * 40)
            print("Digite uma opção válida!!!")
            print("!" * 40)
        print("=" * 40)
        print(f'|{"Submenu de Imóveis": ^40}|')
        print_submenu()
        sub_opcao = input("Digite a opção desejada: ")
    if sub_opcao == "6":
        retorno()
        gravar_imoveis(BD_Imovel)

def submenu_alugueis():
    print("-" * 40)
    print(f"|{'Submenu de Aluguéis': ^40}|")
    print('-' * 40)
    print_submenu()
    sub_opcao = input("Digite a opção desejada: ")
    while sub_opcao != "6":
        if sub_opcao == "1":
            exibir_todos_alugueis(BD_Cliente, BD_Imovel, BD_Aluguel)
        elif sub_opcao == "2":
            print("-" * 40)
            cpf = input("Informe o cpf cadastrado no aluguel: ")
            codigo = input("Informe o codigo do imóvel: ")
            data = input("Informe a data de entrada do aluguel: ")
            print('-' * 40)
            exibir_aluguel(BD_Cliente, BD_Imovel, BD_Aluguel, cpf, codigo, data)
        elif sub_opcao == "3":
            inserir_aluguel(BD_Cliente, BD_Imovel, BD_Aluguel)
        elif sub_opcao == "4":
            print()
            cpf = input("Informe o cpf cadastrado no aluguel:")
            codigo = input("Informe o codigo do imóvel:")
            data = input("Informe a data de entrada do aluguel:")
            alterar_aluguel(BD_Cliente, BD_Imovel, BD_Aluguel, cpf, codigo, data)
        elif sub_opcao == "5":
            print()
            cpf = input("Informe o cpf cadastrado no aluguel:")
            codigo = input("Informe o codigo do imóvel:")
            data = input("Informe a data de entrada do aluguel:")
            excluir_aluguel(BD_Cliente, BD_Imovel, BD_Aluguel, cpf, codigo, data)
        else:
            print("!" * 40)
            print("Digite uma opção válida!!!")
            print("!" * 40)
        print("-" * 40)
        print(f'|{"Submenu de Aluguéis": ^40}|')
        print('-' * 40)
        print_submenu()
        sub_opcao = input("Digite a opção desejada: ")
    if sub_opcao == "6":
        retorno()
        grava_aluguel(BD_Aluguel)    

menuprincipal()
            
