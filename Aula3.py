'''1'''
v1 = int(input("Informe o primeiro valor: "))
v2 = int(input("Informe o segundo valor: "))

soma = v1 + v2
subt = v1 - v2
mult = v1 * v2
div = v1 / v2
divExata = v1 // v2
modResto = v1 % v2

print(f"A soma é {soma} \nA subtração é {subt} \nA multiplicação é {mult} \nA divisão é {div:.2f}")
print(f"A divisão exata é {divExata} \nO resto da divisão exata é {modResto}")

print("\n")

'''2'''
cavalos = int(input("Informe a quantidade de cavalos: "))
qntdFerraduras = cavalos * 4

print(f"Com a quantidade de {cavalos} cavalos, será necessário comprar {qntdFerraduras} ferraduras")

print("\n")

'''3'''
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade:"))

dias = idade * 365

print(f"Boa tarde {nome} você viveu um total de {dias} dias")

print("\n")

'''4'''
peso = float(input("Informe o peso (em Kg) do seu prato: "))
valorPagar = peso * 12

print(f" Com o peso {peso}, você terá que pagar {valorPagar:.2f} reais")

print("\n")

'''5'''
qntdPaes = int(input("Informe a quantidade de pães à comprar: "))
qntdBroas = int(input("Informe a quantidade de broas à comprar: "))

qntdTtal = qntdPaes * 0.12
qntdTtal_1 = qntdBroas * 1.50

qntTotal = (qntdTtal + qntdTtal_1) * 0.10


print(f"O valor de 10% à ser colocada na poupança deverá ser {qntTotal:.2f} reais")


print("\n")

'''6'''
dia = int(input("Informe o dia do mês em que você está: "))
mes = int(input("Informe o mês que você está: "))

total_dias = (mes - 1) * 30 + dia

print(f"Você está aproximadamente no dia {total_dias} do ano.")