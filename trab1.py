import numpy as np

def readFile(datasetName): #Função que retorna a matriz desejada a partir de um arquivo .txt e salva numa variável numpy
    caminho = 'C:\\Users\\Bárbara Souza\Documents\\2025-1\\grafos\\grafos_datasets\\' + datasetName + '.txt'
    matriz = np.loadtxt(caminho)
    return matriz

def dimensoes(matriz): #Função que retorna as dimensões da matriz
    linhas, colunas = matriz.shape
    return linhas,colunas

def salvaArquivo(texto): #Função que salva no arquivo resultado.txt o texto desejado
    caminho = 'C:\\Users\\Bárbara Souza\Documents\\2025-1\\grafos\\grafos_datasets\\resultado.txt'

    with open (caminho, 'w') as f:
        f.write(texto)
    print(texto)
    
def main(): #Função main responsável por chamar as outras funções
    instancia = input("Digite o nome da matriz: ")
    nome_instancia = readFile(instancia)
    qtd_linhas, qtd_colunas = dimensoes(nome_instancia)
    nome = instancia + ' ' + str(qtd_linhas) + ' ' + str(qtd_colunas)
    salvaArquivo(nome)
    
if __name__ == '__main__':
    main()