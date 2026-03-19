# =============================================================================
# 30 Days of Python – Day 1: Introduction
# My Solutions
# Author: Alvaro Torres (@alvarotorresjr)
# Date: March 2025
# =============================================================================

# Level 1 - Operações básicas

print("Python version check:")
import sys
print(sys.version)
print()  # linha em branco para separar

print("Operações com 3 e 4:")
a = 3
b = 4

print(f"Addition:       {a} + {b} = {a + b}")
print(f"Subtraction:    {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division:       {a} / {b} = {a / b}")
print(f"Modulus:        {a} % {b} = {a % b}")
print(f"Exponential:    {a} ** {b} = {a ** b}")
print(f"Floor division: {a} // {b} = {a // b}")

# Level 2 - Comentários e variáveis
print("\nPython is easy to learn!")  # comentário inline

# Exemplos de tipos de dados
nome = "Alvaro Torres"       # string
idade = 60                   # integer
altura = 1.89                # float
complexo = 2 + 3j            # complex
eh_programador = True        # boolean

print("\nVariáveis declaradas:")
print(f"nome: {nome} ({type(nome)})")
print(f"idade: {idade} ({type(idade)})")
print(f"altura: {altura} ({type(altura)})")
print(f"complexo: {complexo} ({type(complexo)})")
print(f"eh_programador: {eh_programador} ({type(eh_programador)})")