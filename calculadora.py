#!/usr/bin/python3
"""
Rodrigo Pacheco Martinez-Atienza
Doble Grado Ing. Tecnología de las Telecomunicaciones
e Ing. Aeroespacial en Aeronavegación
r.pachecom @ alumnos.urjc.es

Ejercicio: Calculadora
"""

import sys
import operator

NUM_ARGS = 4

operaciones = {'suma': operator.add,
               'resta': operator.sub,
               'multiplica': operator.mul,
               'divide': operator.truediv}

def calcula(param):
    if len(param) != NUM_ARGS:
        sys.exit("Usage error: [operator] [number1] [number2]")

    try:
        resultado = operaciones[param[1]](float(param[2]), float(param[3]))
        return("Resultado: " + str(resultado))
    except IndexError:
        sys.exit("Usage error: [operator] [number1] [number2]")
    except KeyError:
        sys.exit("Opción no soportada. Usage: [operator] [number1] [number2]")
    except ZeroDivisionError:
        return("División por 0. Ten cuidado, el mundo podría haber explotado ;)")
    except ValueError:
        sys.exit("Valor introducido erróneo. Debe ser número")

if __name__ == "__main__":
    param = sys.argv

    print("\nUso: python3 calculadora.py 'opción' valor1 valor2\n\n",
          "Opciones de calculadora:\n",
          "- Suma\n", "- Resta\n", "- Multiplica\n", "- Divide\n")

    print(calcula(param))
