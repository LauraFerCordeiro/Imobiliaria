from auxiliar import *
from cliente import *
from imovel import *
from datetime import *

def existe_aluguel(dic, chave):
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

def inserir_aluguel(dic_c, dic_i, dic_a):
    print('-' * 40)
    print(f'|{"INSERINDO ALUGUEL":-^40}|')
    print('-' * 40)
    cpf = input("Digite o cpf: ")
    print('-' * 40)
    validacao = vazia(cpf)
    while validacao == True:
        print("!" * 40)
        print("Digite pelo menos um cpf!!")
        print("!" * 40)
        cpf = input("Digite o cpf: ").strip()
        validacao = vazia(cpf)
        
    if existe_cliente(dic_c, cpf):
        codigo = input("Digite o código do imóvel: ")
        validacao = vazia(codigo)
        while validacao == True:
            print("!" * 40)
            print("Digite pelo menos um código de imóvel!!")
            print("!" * 40)
            codigo = input("Digite o código: ").strip()
            validacao = vazia(codigo)
            
        if existe_imovel(dic_i, codigo):
            data_entrada = input("Digite a data de entrada (00/00/0000): ")
            validacao = vazia(data_entrada)
            while validacao == True:
                print("!" * 40)
                print("Digite pelo menos uma data de entrada!!")
                print("!" * 40)
                data_entrada = input("Digite a data: ").strip()
                validacao = vazia(data_entrada)
                
            chave = (cpf, codigo, data_entrada)
            
            if existe_aluguel(dic_a, chave):
                print('!' * 40)
                print("Esse aluguel já existe!")
                print('!' * 40)
            else:
                nome_morador = input("Digite o nome do morador (fim para parar): ").lower()
                nomes_moradores = []
                while nome_morador != "fim":
                    nomes_moradores.append(nome_morador)
                    nome_morador = input("Digite o nome do morador (fim para parar): ").lower()
                valor_mensal = float(input("Digite o valor mensal: "))
                tupla = (nomes_moradores, valor_mensal)
                dic_a[chave] = tupla
                print('+' * 40)
                print("Cadastrado com sucesso!!")
                print('+' * 40)
        else:
            print('!' * 40)
            print("Esse imóvel não está cadastrado!!")
            print('!' * 40)
    else:
        print('!' * 40)
        print("Esse cliente não está cadastrado!!")
        print('!' * 40)

def exibir_aluguel(dic_c, dic_i, dic_a, cpf, codigo, data_entrada):
    chave = (cpf, codigo, data_entrada)

    if existe_aluguel(dic_a, chave):
        dados = dic_a[chave]
        print('-' * 40)
        print(f'|{"DADOS DO ALUGUEL": ^40}|')
        print("-" * 40)
        print()
        print("Cliente:")
        listar_elemento_clientes(dic_c, cpf)
        print()
        
        print("Imóvel:")
        listar_elemento_imoveis(dic_i, codigo)
        print()

        print(f"Data de entrada: {data_entrada}")
        print("Moradores: ")
        for elemento in dados[0]:
            print(elemento)
        print(f"Valor mensal: {dados[1]}")
        print()

    else:
        print("!" * 40)
        print("O aluguel informado não existe")
        print('!' * 40)

def alterar_aluguel(dic_c, dic_i, dic_a, cpf, codigo, data_entrada):
    chave = (cpf, codigo, data_entrada)
    if existe_aluguel(dic_a, chave):
        exibir_aluguel(dic_c, dic_i, dic_a, cpf, codigo, data_entrada)
        confirma = input("Tem certeza que deseja alterar? (s/n): ").lower()
        while confirma != 's' and confirma != 'n':
            print("Digite S para sim e N para não!")
            confirma = input("Tem certeza que deseja alterar? (s/n): ").lower()
        if confirma == "s":
            print()
            nome_morador = input("Digite o nome do morador (fim para parar): ").lower()
            nomes_moradores = []
            while nome_morador != "fim":
                nomes_moradores.append(nome_morador)
                nome_morador = input("Digite o nome do morador (fim para parar): ").lower()
            valor_mensal = float(input("Digite o valor mensal: "))
            tupla = (nomes_moradores, valor_mensal)
            dic_a[chave] = tupla
            print()
            print("Dados alterados com sucesso!!")
            print()
        else:
            print()
            print("Ação cancelada!")
            print()
    else:
        print()
        print("Esse aluguel não existe")
        print()

def excluir_aluguel(dic_c, dic_i, dic_a, cpf, codigo, data_entrada):
    chave = (cpf, codigo, data_entrada)
    if existe_aluguel(dic_a, chave):
        exibir_aluguel(dic_c, dic_i, dic_a, cpf, codigo, data_entrada)
        confirma = input("Tem certeza que deseja apagar? (s/n):").lower()
        while confirma != 's' and confirma != 'n':
            print("Digite S para sim e N para não!")
            confirma = input("Tem certeza que deseja alterar? (s/n):").lower()
        if confirma == "s":
            del dic_a[chave]
            print()
            print("Dados apagados")
            print()
        else:
            print()
            print("A ação de deletar foi cancelada!")
            print()
    else:
        print()
        print("O aluguel informado não existe!!")
        print()

def exibir_todos_alugueis(dic_c, dic_i, dic_a):
    print()
    print("----------------------------")
    print("TODAS AS LOTAÇÕES")
    print("----------------------------")

    for chave in dic_a:
        cpf = chave[0]
        codigo = chave[1]
        data_entrada = chave[2]

        exibir_aluguel(dic_c, dic_i, dic_a, cpf, codigo, data_entrada)

        print("----------------------------")

    print("")

def grava_aluguel(dic):
    arq = open("alugueis.txt", "w")
    
    for chave in dic:
        cpf = chave[0]
        codigo = chave[1]
        data_entrada = chave[2]
        data = str(data_entrada)

        tupla = dic[chave]
        lista = tupla[0]
        lista = ','.join(lista)
        valor_mensal = tupla[1]
        valor = str(valor_mensal)

        linha = cpf + "#" + codigo + "#" + data + "#" + lista + "#" + valor + "\n"

        arq.write(linha)
        
    arq.close()

def leitura_alugueis(dic):
    if existe_arquivo("alugueis.txt"):
        arq = open("alugueis.txt", "r")
        for linha in arq:
            linha = linha[:len(linha)-1]
            lista_moradores = linha.split(",")
            lista_completa = linha.split("#")
            cpf = lista_completa[0]
            codigo = lista_completa[1]
            data_entrada = lista_completa[2]
            valor_mensal = float(lista_completa[4])

            chave = (cpf, codigo, data_entrada)

            dic[chave] = (lista_moradores, valor_mensal)

def relatorio(dic_c, dic_i, dic_a, x ,y):
    flag = False
    print(f"Relatório: Alugueis com ano entre {x} e {y}")
    print("--------------------------------------------")
    
    for chave in dic_a:
        data_entrada = datetime.strptime(chave[2], '%d/%m/%Y')   
        if data_entrada >= x and data_entrada <= y:
            flag = True
            cpf = chave[0]
            codigo = chave[1]
            data = chave[2]
            exibir_aluguel(dic_c, dic_i, dic_a, cpf, codigo, data)

    if flag == False:
        print("Não há alugueis nesse intervalo de tempo!")
        
    
            
            
    


    

    
            
            
    
    
    
        
        
        
    
        
                    
                
                
                
            
