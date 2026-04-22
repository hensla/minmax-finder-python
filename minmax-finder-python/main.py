num = int(input("Informe o 1° número: "))
menor = num
maior = num

for i in range(2, 11):
    num = int(input(f"Informe o {i}° número: "))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f"O maior número digitado foi: {maior}\nO menor número foi: {menor}")