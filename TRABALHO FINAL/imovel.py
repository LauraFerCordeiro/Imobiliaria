#Submenu Imovel

from auxiliar import *
from time import sleep
def existe_imovel(dic, chave):
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

def listar_todos_imoveis(dic):
    print('-+' * 20)
    print(f'|{"TODOS OS IMÓVEIS":-^40}|')
    print('-+' * 20)
    for chave in dic:
        sleep(0.5)
        dados = dic[chave]
        print("-" * 40)
        print(f"Código: {chave}")
        print(f"Descrição: {dados[0]}")
        print(f"Endereço: {dados[1]}")
        print(f"Tipo: {dados[2]}")
        print(f"Valor: {dados[3]}")
        print("-" * 40)
        sleep(0.5)
def listar_elemento_imoveis(dic, chave):
    if existe_imovel(dic,chave):
        dados = dic[chave]
        sleep(0.5)
        print("-" * 40)
        print(f'|{"DADOS DO IMÓVEL":-^40}|')
        sleep(0.5)
        print(f'Código: {chave}')
        sleep(0.5)
        print(f'Descrição: {dados[0]}')
        sleep(0.5)
        print(f'Endereço: {dados[1]}')
        sleep(0.5)
        print(f'Tipo: {dados[2]}')
        sleep(0.5)
        print(f'Valor: {dados[3]}')

    else:
        print("!" * 40)
        print("O imóvel não está cadastrado!")
        print('!' * 40)

def incluir_imoveis(dic):
    print("-" * 40)
    print(f'|{"INCLUINDO IMÓVEIS":-^40}|')
    print('-' * 40)
    codigo = input("Digite o código do imóvel: ").strip()
    validacao = vazia(codigo)
    while validacao == True:
        print("!" * 40)
        print("Digite pelo menos um código!")
        print("!" * 40)
        codigo = input("Digite o código do imóvel: ").strip()
        validacao = vazia(codigo)

    if existe_imovel(dic, codigo):
        print("!" * 40)
        print("Imóvel já cadastrado!")
        print('!' * 40)
        
    else:
        descricao = input("Digite a descrição do imóvel: "). strip()
        validacao = vazia(descricao)
        while validacao == True:
            print("!" * 40)
            print("Digite pelo menos uma breve descrição!!")
            print("!" * 40)
            descricao = input("Digite a descrição do imóvel: ").strip()
            validacao = vazia(descricao)
            
        endereco = input("Digite o endereço do imóvel: ").strip()
        validacao = vazia(endereco)
        while validacao == True:
            print("!" * 40)
            print("Digite pelo o endereço!")
            print("!" * 40)
            endereco = input("Digite o endereço do imóvel: ").strip()
            validacao = vazia(endereco)
            
        tipo = input("Digite o tipo de imóvel (comercial/residencial): ").strip()
        validacao = vazia(tipo)
        while validacao == True:
            print("!" * 40)
            print("Digite pelo menos um tipo de imóvel!")
            print("!" * 40)
            tipo = input("Digite o tipo de imóvel (comercial/residencial): ").strip()
            validacao = vazia(tipo)
        tipo = tipo.lower()
        while tipo != "comercial" and tipo != "residencial":
            print("!" * 40)
            print("Por favor, digite um tipo de imóvel válido (comercial ou residencial)!!")
            print("!" * 40)
            tipo = input("Digite o tipo de imóvel (comercial/residencial): ").strip()
            tipo = tipo.lower()
            
        valor_aluguel = float(input("Digite o valor do aluguel: R$"))

        dic[codigo] = (descricao, endereco, tipo, valor_aluguel)

        print("+" * 40)
        print("Imóvel cadastrado com sucesso!")
        print('+' * 40)

def alterar_imoveis(dic, chave):
    if existe_imovel(dic, chave):
        listar_elemento_imoveis(dic, chave)
        print("¬" * 40)
        print(f'|{"ALTERANDO IMÓVEIS":-^40}|')
        print('¬' * 40)
        confirmacao = input("Tem certeza que deseja alterar? (s/n): ").lower()
        while confirmacao != 's' and confirmacao != 'n':
            print("Digite S para sim e N para não!")
            confirmacao = input("Tem certeza que deseja alterar? (s/n): ").lower()

        if confirmacao == "s":
            print("-" * 40)
            descricao = input("Digite a descrição do imóvel: ").strip()
            validacao = vazia(descricao)
            while validacao == True:
                print("!" * 40)
                print("Digite pelo menos uma descrição!!")
                print("!" * 40)
                descricao = input("Digite a descrição do imóvel: ").strip()
                validacao = vazia(descricao)

            endereco = input("Digite o endereço do imóvel: ").strip()
            validacao = vazia(endereco)
            while validacao == True:
                print("!" * 40)
                print("Digite pelo menos um endereço!!")
                print("!" * 40)
                endereco = input("Digite o endereço do imóvel: ").strip()
                validacao = vazia(endereco)

            tipo = input("Digite o tipo de imóvel (comercial/residencial): ").strip()
            validacao = vazia(tipo)
            while validacao == True:
                print("!" * 40)
                print("Digite pelo menos um tipo de imóvel!!")
                print("!" * 40)
                tipo = input("Digite o tipo de imóvel (comercial/residencial): ").strip()
                validacao = vazia(tipo)
            tipo = tipo.lower()
            while tipo != "comercial" and tipo != "residencial":
                print("!" * 40)
                print("Por favor, digite um tipo de imóvel válido (comercial ou residencial)!!")
                print("!" * 40)
                tipo = input("Digite o tipo de imóvel (comercial/residencial): ").strip()
                tipo = tipo.lower()

            valor_aluguel = float(input("Digite o valor do aluguel: R$"))

            dic[chave] = (descricao, endereco, tipo, valor_aluguel)

            print("+" * 40)
            print("Dados alterados com sucesso!!")
            print('+' * 40)
        else:
            print("!" * 40)
            print("Operação cancelada!")
            print('!' * 40)
    else:
        print("!" * 40)
        print("O imóvel não está cadastrado!")
        print('!' * 40)
            
def excluir_imoveis(dic, chave):
    if existe_imovel(dic, chave):
        listar_elemento_imoveis(dic, chave)
        print("-" * 40)
        print(f'|{"EXCLUINDO IMÓVEIS":-^40}|')
        print('-' * 40)
        confirmacao = input("Tem certeza que deseja excluir? (s/n): ").lower()
        while confirmacao != 's' and confirmacao != 'n':
            print("Digite S para sim e N para não!")
            confirmacao = input("Tem certeza que deseja alterar? (s/n): ").lower()

        if confirmacao == "s":
            del dic[chave]
            print("!" * 40)
            print("Imóvel deletado com sucesso!!")
            print('!' * 40)
        else:
            print("!" * 40)
            print("OK! A ação foi cancelada!!")
            print('!' * 40)
    else:
        print("!" * 40)
        print("O imóvel não está cadastrado!")
        print('!' * 40)

def gravar_imoveis(dic):
    arq = open("imoveis.txt", "w")

    for chave in dic:
        dados = dic[chave]

        #linha = codigo + descrição + endereço + tipo + valor
        linha = chave + "#" + dados[0] +"#" + dados[1] + "#" + dados[2] + "#" + str(dados[3]) + "\n"

        arq.write(linha)

    arq.close()

def leitura_imoveis(dic):
    if (existe_arquivo("imoveis.txt")):
        
        arq = open("imoveis.txt", "r")

        for linha in arq:
            linha = linha[:len(linha)-1]
            listinha = linha.split("#")
            codigo = listinha[0]
            descricao = listinha[1]
            endereco = listinha[2]
            tipo = listinha[3]
            valor_aluguel = listinha[4]

            dic[codigo] = (descricao, endereco, tipo, valor_aluguel)
            

