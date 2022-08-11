
def PrimeiroMetodoLeitura():
    arquivo = open('DomCasmurro.txt','r', encoding='utf-8')
    texto = arquivo.read()
    print(texto)
    arquivo.close()

def SegundoMetodoLeitura():
    arquivo = open('DomCasmurro.txt', 'r', encoding='utf-8')
    linha = arquivo.readline()
    while linha != '':
        print(linha,end='')
        linha=arquivo.readline()
    arquivo.close()

def TerceiraMetodoLeitura():
    arquivo = open('DomCasmurro.txt', 'r', encoding='utf-8')
    for linha in arquivo:
        print(linha, end='')
    arquivo.close()

def QuartoMetodoLeitura(url):
    with open(url, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
        print(texto)

def PrimeiroMetodoEscrita(url):
    with open(url, 'w', encoding='utf-8') as arquivo:
        arquivo.write('Essa é uma linha que escrevi para testar o comando de escrita em Python \n')
        arquivo.write('Essa é a Segunda linha que escrevi para testar o comando de escrita em Python \n')
    return url

def SegundoMetodoEscrita(url):
    with open(url, 'a', encoding='utf-8') as arquivo:
        arquivo.write('Essa é a Terceira linha que escrevi para testar o comando de escrita em Python \n')

    return url


#PrimeiroMetodoLeitura()

#SegundoMetodoLeitura()

#TerceiraMetodoLeitura()

Texto_criado = PrimeiroMetodoEscrita('Texte.txt')
QuartoMetodoLeitura(Texto_criado)

Texto_criado = SegundoMetodoEscrita('Texte.txt')

QuartoMetodoLeitura(Texto_criado)