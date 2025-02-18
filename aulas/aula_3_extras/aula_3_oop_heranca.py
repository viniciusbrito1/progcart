import numpy as np
import abc

class geometria:
    def __init__(self,lista_de_lista):
        self.coordenadas = np.array(lista_de_lista)
    
    @abc.abstractmethod
    def comprimento(self):
        pass
    @abc.abstractmethod
    def imprimir_texto(self,texto):
        print(texto)

class ponto (geometria):
    def comprimento(self):
        return 0
    def imprimir_como_texto(self):
        texto = f"PONTO({self.coordenadas[0,0]}, {self.coordenadas[0,0]})"
        super().imprimir_texto(texto)


class linha (geometria):
    def comprimento(self):
        comprimento_parcial = 0
        for i in range(1, len(self.coordenadas)):
            comprimento_parcial += np.linalg.norm(self.coordenadas[i] - self.coordenadas[i-1])
        return comprimento_parcial

    def imprimir_como_texto(self):
        texto = "LINHA("
        for coordenada in self.coordenadas:
            texto += f"({coordenada[0]}, {coordenada[1]}), "
        texto = texto[:-2] + ")" #removendo a ultima virgula
        super().imprimir_texto(texto)

class poligono (linha):
    def __init__(self,lista_de_lista):
        #repete o primeiro ponto para fechar o poligono
        lista_de_lista.append(lista_de_lista[0])
        super().__init__(lista_de_lista )

    def imprimir_como_texto(self):
        texto = "POLIGONO("
        for coordenada in self.coordenadas:
            texto += f"({coordenada[0]}, {coordenada[1]}), "
        texto = texto[:-2] + ")" #removendo a ultima virgula
        super().imprimir_texto(texto)

if __name__ == "__main__":
    ponto_obj = ponto([[0,0]])
    linha_obj = linha([[0,0], [1,0], [1,1]])
    poligono_obj = poligono([[0,0], [1,0], [1,1], [0,1]])


    print(ponto_obj.comprimento())
    print(linha_obj.comprimento())
    print(poligono_obj.comprimento())

    ponto_obj.imprimir_como_texto()
    linha_obj.imprimir_como_texto()
    poligono_obj.imprimir_como_texto()