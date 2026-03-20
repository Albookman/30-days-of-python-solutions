# =============================================================================
# 30 Days of Python – Day 1: Introduction
# My Solutions + Comments
# Author: Alvaro
# Date: March 2026
# =============================================================================

# ────────────────────────────────────────────────
# Level 1
# ────────────────────────────────────────────────

# 1. Check the python version you are using
print("Python version:")
import sys
print(sys.version)
print()  # linha em branco para separar saídas

# 2. Operations with operands 3 and 4
print("Operations with 3 and 4:")
a = 3
b = 4

print(f"Addition:       {a} + {b} = {a + b}")
print(f"Subtraction:    {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Modulus:        {a} % {b} = {a % b}")
print(f"Division:       {a} / {b} = {a / b}")
print(f"Exponential:    {a} ** {b} = {a ** b}")
print(f"Floor division: {a} // {b} = {a // b}")
print()

# ────────────────────────────────────────────────
# Level 2
# ────────────────────────────────────────────────

# 1. Comment saying python is easy to learn
# Python is easy to learn!

# 2. Variables of different data types
first_name = "Alvaro"              # string
last_name = "Torres"               # string
age = 60                           # integer
height = 1.89                      # float (em metros)
complex_number = 1 + 2j            # complex
is_married = False                 # boolean
is_true = True                     # boolean
is_light_on = True                 # boolean

print("Variables declared (Level 2):")

# Cada linha usa uma f-string (f"...") para interpolar variáveis

# O {variavel} insere o valor da variável

# O {type(variavel).__name__} mostra o nome do tipo (ex.: str, int, float)

print(f"first_name:     {first_name} ({type(first_name).__name__})")
print(f"last_name:      {last_name} ({type(last_name).__name__})")
print(f"age:            {age} ({type(age).__name__})")
print(f"height:         {height} m ({type(height).__name__})")
print(f"complex_number: {complex_number} ({type(complex_number).__name__})")
print(f"is_married:     {is_married} ({type(is_married).__name__})")
print(f"is_true:        {is_true} ({type(is_true).__name__})")
print(f"is_light_on:    {is_light_on} ({type(is_light_on).__name__})")
print()

# Linha em branco no final apenas para separar visualmente a saída

# Multiple variables on one line
first_name, last_name, country, age_now, is_married_now, is_light_on_now = "Alvaro", "Torres", "Brazil", 60, False, True
print("Multiple variables on one line:")
print(f"{first_name} {last_name}, {country}, {age_now} anos, married? {is_married_now}")
print()

# ────────────────────────────────────────────────
# Level 3
# ────────────────────────────────────────────────

# 1 & 2. Length of first_name and last_name + comparison
len_first = len(first_name)
len_last = len(last_name)

print("Length of names:")
print(f"Length of first name '{first_name}': {len_first}")
print(f"Length of last name  '{last_name}':  {len_last}")
print(f"First name longer than last name? {len_first > len_last}")
print()

# 3. More variables (já declarei acima, mas adicionando city e year como exemplo)
city = "Ponta Grossa"
current_year = 2026

print("Additional variables:")
print(f"city: {city}")
print(f"current_year: {current_year}")
print()

# 4. Check types with type()
print("Checking types with type():")
print(f"type(first_name):     {type(first_name).__name__}")
print(f"type(age):             {type(age).__name__}")
print(f"type(height):          {type(height).__name__}")
print(f"type(complex_number):  {type(complex_number).__name__}")
print(f"type(is_married):      {type(is_married).__name__}")

print("\nDay 1 completed! 🎉")