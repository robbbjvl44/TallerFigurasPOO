
from Cuadrado import Cuadrado
from rectangulo import Rectangulo
from Circunferencia import Circunferencia


if __name__ == '__main__':
    # Cuadrado Funcion
    cuadrado1 = Cuadrado(lado=5)
    print("=== CUADRADO 1 ===")
    print(cuadrado1)
    print()

    cuadrado2 = Cuadrado(lado=8)
    print("=== CUADRADO 2 ===")
    print(cuadrado2)
    print()

    # Rectangulo Funcion
    rectangulo1 = Rectangulo(alto=4, ancho=6)
    print("=== RECTÁNGULO 1 ===")
    print(rectangulo1)
    print()

    rectangulo2 = Rectangulo(alto=2, ancho=10)
    print("=== RECTÁNGULO 2 ===")
    print(rectangulo2)
    print()

    # Circunferencia Funcion
    circunferencia1 = Circunferencia(radio=3)
    print("=== CIRCUNFERENCIA 1 ===")
    print(circunferencia1)
    print()

    circunferencia2 = Circunferencia(radio=5)
    print("=== CIRCUNFERENCIA 2 ===")
    print(circunferencia2)
    print()
