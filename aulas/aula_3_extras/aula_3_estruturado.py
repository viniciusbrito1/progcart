import numpy as np

def comprimento(geometria):
    """ Calcula o comprimento de uma geometria representada com uma matriz."""
    if len(geometria)==1: #ponto
        return 0
    else:
        comprimento_parcial = 0
        for i in range(1, len(geometria)):
            comprimento_parcial += np.linalg.norm(geometria[i] - geometria[i-1])
        return comprimento_parcial

if __name__ == "__main__":
    # Coordenadas serão representadas por um array de 2x1:
    ponto = np.array([[0,0]])

    # Linhas e poligonos serão representados por arrays de Nx2.
    linha = np.array([[0,0], [1,0], [1,1]])
    # Linhas e poligonos serão representados por arrays de Nx2 e a última linha é igual a primeira.
    poligono = np.array([[0,0], [1,0], [1,1], [0,1]])
    
    print(comprimento(ponto))
    print(comprimento(linha))
    print(comprimento(poligono))

