#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:36:31 2018

@author: victor
"""
import sys
from calcoohija import CalculadoraHija 

if __name__ == "__main__":

    mi_calcu = CalculadoraHija()
    fich = open(sys.argv[1], "r")
    lista = fich.readlines()
    fich.close()
    
    
    for line in lista:
        listasin = line.split(",")
        listasin[-1] = listasin[-1][:-1]
        operacion = listasin[0]
        operando = listasin[1:]
        
        if operacion == "suma":
            
    
    
    
    
    
    

