'''1'''
v1 = int(input("Informe o primeiro valor: "))
v2 = int(input("Informe o segundo valor: "))

print(v1 == v2)
print(v1 != v2)
print(v1 >= v2)
print(v1 <= v2)
print(v1 > v2)
print(v1 < v2)


'''5'''
celcius = float(input("Informe a quantidade de graus celcius: "))

fahrenheit = (celcius * 1.8) + 32

print(f"A quantidade informada de celcius em Fahrenheit é {fahrenheit} Fahrenheits")

print("\n")

'''6'''
salario1 = float(input("Informe quantas horas fixas de trabalho: "))
salario2 = float(input("Informe quantas horas extras trabalhadas: "))

salrio = salario1 * 10
salrio2 = salario2 * 15

salrio3 = salrio + salrio2
salrio4 = (salrio + salrio2) * 0.10
salrio5 = salrio3 - salrio4

print(f"O salário bruto é {salrio3}, mas considerando os impostos seu salário será de {salrio5} reais")

print("\n")

'''7'''
meiaCola1 = 0.35
meiaCola2 = 0.6
meiaCola3 = 2

qntdMeiaCola1 = int(input("Informe a quantidade de latas de 350ml à comprar:"))
qntdMeiaCola2 = int(input("Informe a quantidade de  garrafas de 600ml à comprar: "))
qntdMeiaCola3 = int(input("Informe a quantidade de  garrafas de 2 litros à comprar: "))

cola1 = qntdMeiaCola1 * 0.35
cola2 = qntdMeiaCola2 * 0.6
cola3 = qntdMeiaCola3 * 2

print(f"Com a quantidade de {qntdMeiaCola1} de latas de 350ml, {qntdMeiaCola2} de garrafas de 600ml e {qntdMeiaCola3} de garrafas de 2L.\n Você comprou {cola1 + cola2 + cola3} litros de refrigerante!")

print("\n")

'''8'''
total = float(input("Informe a quantidade total à ser pago:"))

parte = total / 3

carlos = int(parte)
andre = int(parte)

felipe = total - (carlos + andre)

print(f"Carlos deverá pagar {carlos} reais, André {andre} reais e Felipe {felipe:.2f} reais")
