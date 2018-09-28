#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:32:57 2018

@author: victor
"""

import sys


class Calculadora():
    def plus(self, op1, op2):
        """ Function to sum the operands. Ops have to be ints """
        return op1 + op2

    def minus(self, op1, op2):
        """ Function to substract the operands """
        return op1 - op2


class CalculadoraHija(Calculadora):
    def multi(self, op1, op2):
        """Funcion que multiplica operandos. Ops tienen que ser ints"""
        return op1 * op2

    def division(self, op1, op2):
        """Funcion que divide el op1 entre op2. Ops tienen que ser ints"""
        return op1 / op2


if __name__ == "__main__":

    mi_calcu = CalculadoraHija()

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = mi_calcu.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = mi_calcu.minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = mi_calcu.multi(operando1, operando2)
    elif sys.argv[2] == "divide":
        if operando2 == 0:
            sys.exit("Error: Division by zero is not allowed")
        else:
            result = mi_calcu.division(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar,restar,multiplicar o dividir')

    print(result)
