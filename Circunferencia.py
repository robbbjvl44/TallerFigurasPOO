from FiguraGeometrica import FiguraGeometrica
import math


class Circunferencia(FiguraGeometrica):
    """
    Clase Circunferencia hereda de FiguraGeometrica
    """

    def __init__(self, radio: float):
        # Usamos radio como alto y como ancho
        super().__init__(alto=radio, ancho=radio)

    '''
    Calcula el área de la circunferencia
    '''
    def area(self) -> float:
        radio = self.ancho
        return math.pi * (radio ** 2)

    '''
    Calcula el perímetro (longitud de la circunferencia)
    '''
    def perimetro(self) -> float:
        radio = self.ancho
        return 2 * math.pi * radio

    def __str__(self) -> str:
        return (f'Circunferencia(radio={self.ancho}, '
                f'area={self.area():.2f}, perimetro={self.perimetro():.2f})')


if __name__ == '__main__':
    circ = Circunferencia(radio=3)
    print(circ)
