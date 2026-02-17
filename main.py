import math

def calcular_volumen_esfera(radio):
    """
    Calcula el volumen de una esfera dado su radio.
    
    :param radio: Radio de la esfera (float o int)
    :return: Volumen de la esfera (float)
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    volumen = (4 / 3) * math.pi * (radio ** 3)
    return volumen

def main():
    try:
        radio = float(input("Introduce el radio de la esfera: "))
        volumen = calcular_volumen_esfera(radio)
        print(f"El volumen de la esfera con radio {radio} es: {volumen:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



