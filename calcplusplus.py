#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 23:45:08 2018

@author: victor
"""

import sys
from calcoohija import CalculadoraHija

if __name__ == "__main__":

    mi_calcu = CalculadoraHija()
    with open("fichero.csv", "r") as fich:
        lista = fich.readlines()

    for line in lista:
        listasin = line.split(",")
        listasin[-1] = listasin[-1][:-1]
        operacion = listasin[0]
        operandos = listasin[1:]
        print(operandos)

        if operacion == "suma":
            op_aux = int(operandos[0])
            for operando in operandos[1:]:
                op_aux = mi_calcu.plus(op_aux, int(operando))
            print("El resultado de la suma es:", op_aux)

        elif operacion == "resta":
            op_aux = int(operandos[0])
            for operando in operandos[1:]:
                op_aux = mi_calcu.minus(op_aux, int(operando))
            print("El resultado de la resta es:", op_aux)

        elif operacion == "multiplica":
            op_aux = int(operandos[0])
            for operando in operandos[1:]:
                op_aux = mi_calcu.multi(op_aux, int(operando))
            print("El resultado de la multiplicacion es:", op_aux)

        elif operacion == "divide":
            op_aux = int(operandos[0])

            try:
                    for operando in operandos[1:]:
                        op_aux = mi_calcu.division(op_aux, int(operando))
                    print("El resultado de la division es:", op_aux)

            except ZeroDivisionError:
                sys.exit("Error: Division by zero is not allowed")

        else:

                print("Operacion no valida")
