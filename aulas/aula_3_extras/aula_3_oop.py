import numpy as np

class ponto:
    def __init__(self,x,y):
        self.geometria = np.array([[x,y]])
    def comprimento(self):
        return 0

class linha:
    def __init__(self, lista_de_lista):
        self.geometria = np.array(lista_de_lista)
    def comprimento(self):
        comprimento_parcial = 0
        for i in range(1, len(self.geometria)):
            comprimento_parcial += np.linalg.norm(self.geometria[i] - self.geometria[i-1])
        return comprimento_parcial

class poligono:
    def __init__(self, lista_de_lista):
        self.geometria = np.array(lista_de_lista)
    def comprimento(self):
        comprimento_parcial = 0
        for i in range(1, len(self.geometria)):
            comprimento_parcial += np.linalg.norm(self.geometria[i] - self.geometria[i-1])
        return comprimento_parcial


ponto_obj = ponto(0,0)
linha_obj = linha([[0,0], [1,0], [1,1]])
poligono_obj = poligono([[0,0], [1,0], [1,1], [0,1]])


print(ponto_obj.comprimento())
print(linha_obj.comprimento())
print(poligono_obj.comprimento())