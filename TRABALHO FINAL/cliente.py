#Funções Submenu Cliente
from time import sleep
from auxiliar import *

def existe_cliente(dic,chave):
    if chave in dic.keys():
        return True
    else:
        return False

def vazia(dado):
    tamanho = len(dado)
    if tamanho == 0:
        return True
    else:
        return False

def incluir_clientes(dic):
    print("-" * 40)
    print(F"|{'INCLUINDO CLIENTES': ^40}|")
    cpf = input("Digite o cpf: ").strip()
    validacao = vazia(cpf)
    while validacao == True:
        print("!" * 40)
        print("ERRO! ", end='')
        sleep(0.5)
        print('Nada foi digitado no campo apresentado!')
        sleep(0.5)
        print("!" * 40)
        cpf = input("Digite o cpf: ").strip()
        validacao = vazia(cpf)      

    if existe_cliente(dic, cpf):
        print("!" * 40)
        print("ERRO! ", end='')
        sleep(0.5)
        print('Cliente já cadastrado!')
        print('!' * 40)
        sleep(0.5)
        
    else:
        nome = input("Digite seu nome: ").strip()
        validacao = vazia(nome)
        while validacao == True:
            print("!" * 40)
            print("Digite pelo menos um nome!")
            print("!" * 40)
            sleep(0.5)
            nome = input("Digite seu nome: ").strip()
            validacao = vazia(nome)
            
        data_nasc = input("Digite a data do seu nascimento (00/00/0000): ").strip()
        validacao = vazia(data_nasc)
        while validacao == True:
            print("!" * 40)
            print("Digite pelo menos uma data de nascimento!")
            print("!" * 40)
            data_nasc = input("Digite a data do seu nascimento (00/00/0000): ").strip()
            validacao = vazia(data_nasc)
            
        salario = (input("Digite o seu salário: R$"))
        validacao = vazia(str(salario))
        while validacao == True:
            print("!" * 40)
            print("Digite pelo menos um salário!")
            print("!" * 40)
            salario = input("Digite o seu salário: R$").strip()
            validacao = vazia(str(salario))
            
        email = input("Digite o seu email: ").strip()
        validacao = vazia(email)
        while validacao == True:
            print("!" * 40)
            print("Digite pelo menos um email!")
            print("!" * 40)
            email = input("Digite o seu email: ").strip()
            validacao = vazia(email)
            
        telefone = input("Digite o seu telefone: ").strip()
        validacao = vazia(telefone)
        while validacao == True:
            print("!" * 40)
            print("Digite pelo menos um telefone!")
            print("!" * 40)
            telefone = input("Digite o seu telefone: ").strip()
            validacao = vazia(telefone)

        dic[cpf] = (nome, data_nasc, salario, email, telefone)

        print("+" * 40)
        print("Cliente cadastrado com sucesso!")
        print('+' * 40)
        sleep(0.5)

def listar_todos_clientes(dic):
    print("-+" * 20)
    print(f'|{"TODOS OS CLIENTES":-^40}|')
    print('-+' * 20)
    sleep(0.5)
    for chave in dic:
        sleep(0.5)
        dados = dic[chave]
        print("-" * 40)
        print(f"Nome: {dados[0]}")
        print(f"CPF: {chave}")
        print(f"Data de Nascimento: {dados[1]}")
        print(f"Salário: {dados[2]}")
        print(f"E-mail: {dados[3]}")
        print(f"Telefone: {dados[4]}")
        print('-' * 40)
        sleep(0.5)

def listar_elemento_clientes(dic,chave):
    if existe_cliente(dic,chave):
        dados = dic[chave]
        sleep(0.5)
        print('-' * 40)
        print(f'|{"DADOS DO CLIENTE":-^40}|')
        print('-' * 40)
        print(f'Nome: {dados[0]}')
        sleep(0.5)
        print(f'CPF: {chave}')
        sleep(0.5)
        print(f'Data de Nascimento: {dados[1]}')
        sleep(0.5)
        print(f'Salário: {dados[2]}')
        sleep(0.5)
        print(f'Email: {dados[3]}')
        sleep(0.5)
        print(f'Telefone: {dados[4]}')

    else:
        print("!" * 40)
        print("O cliente não está cadastrado!!")
        print('!' * 40)

def alterar_clientes(dic,chave):
    if existe_cliente(dic,chave):
        listar_elemento_clientes(dic,chave)
        print('¬' * 40)
        print(f'|{"ALTERANDO CLIENTES":-^40}|')
        print("¬" * 40)
        confirmacao = input("Tem certeza que deseja alterar? (s/n): ").lower()
        print("¬" * 40)
        while confirmacao != 's' and confirmacao != 'n':
            print("Digite S para sim e N para não!")
            confirmacao = input("Tem certeza que deseja alterar? (s/n): ").lower()
        
        if confirmacao == "s":
            print("-" * 40)
            nome = input("Digite seu nome: ").strip()
            validacao = vazia(nome)
            while validacao == True:
                print("!" * 40)
                print("Digite pelo menos um nome!")
                print("!" * 40)
                nome = input("Digite seu nome: ").strip()
                validacao = vazia(nome)
                
            data_nasc = input("Digite a data do seu nascimento (00/00/0000): ").strip()
            validacao = vazia(data_nasc)
            while validacao == True:
                print("!" * 40)
                print("Digite pelo menos uma data de nascimento!!")
                print("!" * 40)
                data_nasc = input("Digite a data do seu nascimento (00/00/0000): ").strip()
                validacao = vazia(data_nasc)
                
            salario = float(input("Digite o seu salário: R$"))
            validacao = vazia(str(salario))
            while validacao == True:
                print("!" * 40)
                print("Digite pelo menos um salário!")
                print("!" * 40)
                salario = input("Digite o seu salário: R$").strip()
                validacao = vazia(str(salario))
                
            email = input("Digite o seu email: ").strip()
            validacao = vazia(email)
            while validacao == True:
                print("!" * 40)
                print("Digite pelo menos um email!")
                print("!" * 40)
                email = input("Digite o seu email: ").strip()
                validacao = vazia(email)
                
            telefone = input("Digite o seu telefone: ").strip()
            validacao = vazia(telefone)
            while validacao == True:
                print("!" * 40)
                print("Digite pelo menos um telefone!")
                print("!" * 40)
                telefone = input("Digite o seu telefone: ").strip()
                validacao = vazia(telefone)

            dic[chave] = (nome, data_nasc, salario, email, telefone)

            print("+" * 40)
            print("Dados alterados com sucesso!!")
            print('+' * 40)

        else:
            print("!" * 40)
            print("OK! A operação foi cancelada!")
            print('!' * 40)

    else:
        print("!" * 40)
        print("O cliente não está cadastrado!")
        print('!' * 40)

def excluir_clientes(dic,chave):
    if existe_cliente(dic,chave):
        listar_elemento_clientes(dic,chave)
        print('!' * 40)
        print(f'|{"EXCLUINDO CLIENTES":-^40}|')
        print("!" * 40)
        confirmacao = input("Tem certeza que deseja excluir? (s/n): ").lower()
        print('!' * 40)
        while confirmacao != 's' and confirmacao != 'n':
            print("Digite S para sim e N para não!")
            confirmacao = input("Tem certeza que deseja alterar? (s/n): ").lower()

        if confirmacao == "s":
            del dic[chave]
            print("+" * 40)
            print("Cliente excluido com sucesso!")
            print('+' * 40)
        else:
            print("!" * 40)
            print("OK! A ação foi cancelada!")
            print('!' * 40)
    else:
        print("!" * 40)
        print("O cliente não está cadastrado!")
        print('!' * 40)

def arquivo_write(dic):
    arq = open("clientes.txt", "w")

    for chave in dic:
        dados = dic[chave]

        #linha = cpf#nome#data_de_nascimento#salario#email#telefone
        linha = chave + "#" + dados[0] + "#" + dados[1] + "#" + str(dados[2]) + "#" + dados[3] + "#" + dados[4] + "\n"
        
        arq.write(linha)

    arq.close()

def leitura_cliente(dic):
    if (existe_arquivo("clientes.txt")):
        
        arq = open("clientes.txt", "r")
        
        for linha in arq:
            linha = linha[:len(linha)-1]
            listinha = linha.split("#")
            cpf = listinha[0]
            nome = listinha[1]
            data_nasc = listinha[2]
            salario = float(listinha[3])
            email = listinha[4]
            telefone = listinha[5]
            
            dic[cpf] = (nome, data_nasc, salario, email, telefone)
