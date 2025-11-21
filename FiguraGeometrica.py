class FiguraGeometrica:
    '''
    Esta clase representa una figura geométrica
    '''

    def __init__(self, alto: int, ancho: int):
        self.alto = alto
        self.ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if alto <= 0:
            raise ValueError("El alto debe ser mayor a 0")
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if ancho <= 0:
            raise ValueError("El ancho debe ser mayor a 0")
        self._ancho = ancho

    '''
    Calcula el área
    '''
    def area(self) -> float:
        return self.ancho * self.alto

    '''
    Método sin implementar
    '''
    def perimetro(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica(alto={self.alto}, ancho={self.ancho}, area={self.area()})'
if __name__ == '__main__':
        Figura = FiguraGeometrica(alto=10, ancho=5)
        print(Figura)