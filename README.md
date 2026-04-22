🔢 minmax-finder
Ferramenta simples em Python que lê 10 números digitados pelo usuário e retorna o maior e o menor valor.
📋 Descrição
minmax-finder solicita que o usuário insira 10 números um por um e, ao final, exibe o maior e o menor entre eles — sem ordenação, sem bibliotecas externas, só lógica pura.
🚀 Como usar
bashpython minmax.py
Exemplo de execução:
Informe o 1° número: 4
Informe o 2° número: 17
Informe o 3° número: 3
Informe o 4° número: 99
Informe o 5° número: 42
Informe o 6° número: 8
Informe o 7° número: 55
Informe o 8° número: 1
Informe o 9° número: 23
Informe o 10° número: 7

O maior número digitado foi: 99
O menor número foi: 1
🐛 Código
pythonnum = int(input("Informe o 1° número: "))
menor = num
maior = num

for i in range(2, 11):
    num = int(input(f"Informe o {i}° número: "))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f"O maior número digitado foi: {maior}\nO menor número foi: {menor}")
💡 Como funciona

Lê o primeiro número e o define como maior e menor ao mesmo tempo.
Percorre os 9 números seguintes com um laço for.
Atualiza maior se o novo número for maior, ou menor se for menor.
Exibe os dois resultados ao final.

📁 Estrutura do projeto
minmax-finder/
└── minmax.py   # Script principal
🛠️ Requisitos

Python 3.x
Nenhuma biblioteca externa necessária

📄 Licença
MIT
