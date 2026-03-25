# Day 3: Operators

# ==================== Exercícios Básicos ====================

age = 60                    # int
height = 1.89               # float
complex_number = 1 + 1j     # número complexo

print(f"Idade: {age} anos (tipo: {type(age)})")
print(f"Altura: {height} m (tipo: {type(height)})")
print(f"Número complexo: {complex_number} (tipo: {type(complex_number)})\n")

# Triângulo - Área
print("=== Área do Triângulo ===")
base = float(input("Digite a base do triângulo: "))
height_tri = float(input("Digite a altura do triângulo: "))
area_tri = 0.5 * base * height_tri
print(f"A área do triângulo é: {area_tri:.2f} m²\n")

# Triângulo - Perímetro
print("=== Perímetro do Triângulo ===")
a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))
perimeter = a + b + c
print(f"O perímetro do triângulo é: {perimeter:.2f} m\n")

# Retângulo
print("=== Retângulo ===")
length = float(input("Comprimento do retângulo: "))
width = float(input("Largura do retângulo: "))
area_rect = length * width
perimeter_rect = 2 * (length + width)
print(f"Área: {area_rect:.2f} m² | Perímetro: {perimeter_rect:.2f} m\n")

# Círculo
print("=== Círculo ===")
radius = float(input("Digite o raio do círculo: "))
pi = 3.14
area_circle = pi * radius ** 2
circum = 2 * pi * radius
print(f"Área: {area_circle:.2f} m² | Circunferência: {circum:.2f} m\n")

# Equação y = 2x - 2
print("=== Equação y = 2x - 2 ===")
x = 5  # exemplo
y = 2 * x - 2
print(f"Para x = {x}, y = {y}")
print(f"Inclinação (slope) = 2")
print(f"Intercepto em x = 1")
print(f"Intercepto em y = -2\n")

# Pontos (2,2) e (6,10)
print("=== Distância Euclidiana e Slope ===")
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f"Inclinação entre pontos: {slope}")
print(f"Distância euclidiana: {distance:.2f}\n")

# y = x² + 6x + 9
print("=== y = x² + 6x + 9 ===")
for x in range(-10, 6):
    y = x**2 + 6*x + 9
    print(f"x = {x:2} → y = {y:3}")
print("y = 0 quando x = -3\n")

# Strings e operadores
print("=== Operadores com strings ===")
python = "python"
dragon = "dragon"
print(f"Comprimento 'python': {len(python)} | 'dragon': {len(dragon)}")
print(f"'on' está em ambos? {('on' in python) and ('on' in dragon)}")
print(f"'jargon' na frase? {'jargon' in 'I hope this course is not full of jargon'}")
print(f"Não existe 'on' em ambos? {('on' not in python) and ('on' not in dragon)}\n")

# Conversões e verificações
print("=== Conversões e verificações ===")
print(f"Comprimento 'python' como float: {float(len(python))}")
print(f"Como string: {str(len(python))}")
print(f"7 // 3 == int(2.7)? {7 // 3 == int(2.7)}")
print(f"type('10') == type(10)? {type('10') == type(10)}")
print(f"int('9.8') == 10? {int(9.8) == 10}\n")

# Pagamento semanal
print("=== Pagamento Semanal ===")
hours = float(input("Horas trabalhadas: "))
rate = float(input("Taxa por hora (R$): "))
pay = hours * rate
print(f"Seu pagamento semanal é: R$ {pay:,.2f}\n")

# Segundos vividos
print("=== Segundos vividos ===")
years = int(input("Quantos anos você viveu? "))
seconds_lived = years * 365 * 24 * 60 * 60
print(f"Você viveu aproximadamente {seconds_lived:,} segundos.\n")

# Tabela final
print("=== Tabela solicitada ===")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")