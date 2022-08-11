import csv

def PrimeiroMetodoLeitura_CSV(url):
    with open(url,'r',encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            header = next(leitor)
            for linha in leitor:
                if float(linha[2]) > 1:
                    print(linha)
            
# LENDO ARQUIVO CSV, **** SEM USAR BIBLIOTECA CSV*** 

def SegundoMetodoLeitura_CSV(url):
    with open(url,'r',encoding='utf-8') as arquivo_csv:
        linhas = arquivo_csv.read()
        linhas = linhas.split('\n')
        for linha in linhas:
            linha = linha.split(',')
            print(linha)
            
def TerceiroMetodoLeitura_CSV(url):
    with open(url,'r',encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv,delimiter=',')
            for linha in leitor:
                    print(linha)
            

def PrimeiroMetodoEscrita_CSV(header,dados):
    with open('users.csv','w',encoding='utf-8',newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(header)
        writer.writerow(dados)
        
    return 'users.csv'
        
def Cadastro_CSV():
    header = ['nome','sobrenome']
    dados=[]
    opt = input('O que deseja Fazer?\n1 - Cadastrar\n0 - Sair\n')
    while opt != '0':
        nome = input('Informe o Nome: ')
        sobrenome = input('Informe o Sobrenome: ')
        dados.append([nome,sobrenome])
        opt = input('O que deseja Fazer?\n1 - Cadastrar\n0 - Sair\n')
    
    print(dados)
    
    with open('users.csv','w',encoding='utf-8',newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(header)
        writer.writerows(dados)
    
    with open('users.csv','r',encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv,delimiter=',')
        for linha in leitor:
                print(linha)
    


Cadastro_CSV()
