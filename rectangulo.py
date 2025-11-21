
from FiguraGeometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    """
    Clase Rectangulo hereda de FiguraGeometrica
    """

    def __init__(self, alto: float, ancho: float):
        super().__init__(alto=alto, ancho=ancho)

    '''
    Calcula el área del rectángulo
    '''
    def area(self) -> float:
        return self.ancho * self.alto

    '''
    Calcula el perímetro del rectángulo
    '''
    def perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)

    def __str__(self) -> str:
        return (f'Rectangulo(alto={self.alto}, ancho={self.ancho}, '
                f'area={self.area()}, perimetro={self.perimetro()})')


if __name__ == '__main__':
    rect = Rectangulo(alto=4, ancho=6)
    print(rect)
