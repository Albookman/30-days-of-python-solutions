# Day 2: 30 Days of Python programming

# ==================== LEVEL 1 ====================

first_name = "Alvaro"
last_name = "Torres"
full_name = f"{first_name} {last_name}"
country = "Brasil"
city = "Ponta Grossa"
age = 60
year = 2026
is_married = False
is_true = True
is_light_on = True

# Declarando múltiplas variáveis em uma linha
first_name, last_name, country, city, age = "Alvaro", "Torres", "Brasil", "Ponta Grossa", 60

print(f"Nome completo: {full_name}")
print(f"País: {country} | Cidade: {city}")
print(f"Idade: {age} anos | Ano atual: {year}")
print(f"Casado: {is_married} | is_true: {is_true} | Luz ligada: {is_light_on}\n")

# ==================== LEVEL 2 ====================

# 1. Verificar tipos
print("=== Tipos das variáveis ===")
print(f"first_name   → {type(first_name)}")
print(f"age          → {type(age)}")
print(f"is_married   → {type(is_married)}")
print(f"full_name    → {type(full_name)}\n")

# 2. Comprimento do primeiro nome
print(f"Comprimento do primeiro nome '{first_name}': {len(first_name)} caracteres")

# 3. Comparação de comprimentos
len_first = len(first_name)
len_last = len(last_name)
print(f"Comprimento do sobrenome '{last_name}': {len_last} caracteres")

if len_first > len_last:
    print(f"O primeiro nome é mais longo ({len_first} > {len_last})")
elif len_last > len_first:
    print(f"O sobrenome é mais longo ({len_last} > {len_first})")
else:
    print("Primeiro nome e sobrenome têm o mesmo comprimento")

# Operações matemáticas com num_one e num_two
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(f"\n=== Operações matemáticas ===")
print(f"{num_one} + {num_two} = {total}")
print(f"{num_one} - {num_two} = {diff}")
print(f"{num_one} * {num_two} = {product}")
print(f"{num_one} / {num_two} = {division}")
print(f"{num_two} % {num_one} = {remainder}")
print(f"{num_one} ** {num_two} = {exp}")
print(f"{num_one} // {num_two} = {floor_division}")

# Círculo
radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

print(f"\n=== Círculo (raio = {radius}m) ===")
print(f"Área do círculo: {area_of_circle:.2f} m²")
print(f"Circunferência: {circum_of_circle:.2f} m")

# Área com input do usuário
print("\n--- Calculando área com input ---")
radius_input = float(input("Digite o raio do círculo (em metros): "))
area_input = 3.14 * radius_input ** 2
print(f"Área do círculo com raio {radius_input} m = {area_input:.2f} m²")

# Input do usuário (Level 2 - exercício 13)
print("\n=== Dados do usuário via input ===")
user_first_name = input("Digite seu primeiro nome: ")
user_last_name = input("Digite seu sobrenome: ")
user_country = input("Digite seu país: ")
user_age = int(input("Digite sua idade: "))

print(f"\nOlá {user_first_name} {user_last_name}!")
print(f"Você tem {user_age} anos e mora em {user_country}.")

# Palavras reservadas
print("\n=== Palavras reservadas do Python ===")
help('keywords')