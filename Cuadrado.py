from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    '''
    Clase para crear Cuadrado
    '''

    def __init__(self, lado: float):
        # Usamos lado como alto y como ancho
        super().__init__(alto=lado, ancho=lado)

    '''
    Calcula el área del cuadrado
    '''
    def area(self) -> float:
        return self.ancho * self.alto

    '''
    Calcula el perímetro del cuadrado
    '''
    def perimetro(self) -> float:
        return 4 * self.ancho

    def __str__(self) -> str:
        return (f'Cuadrado(lado={self.ancho}, '
                f'area={self.area()}, perimetro={self.perimetro()})')


if __name__ == '__main__':
    cuadrado = Cuadrado(lado=5)
    print(cuadrado)
