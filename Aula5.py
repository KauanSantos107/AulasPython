'''1'''
total1 = int(input("Informe a quantidade de moedas de 1 centavo: "))
total5 = int(input("Informe a quantidade de moedas de 5 centavos: "))
total10 = int(input("Informe a quantidade de moedas de 10 centavos: "))
total25 = int(input("Informe a quantidade de moedas de 25 centavos: "))
total50 = int(input("Informe a quantidade de moedas de 50 centavos: "))
total1R = int(input("Informe a quantidade de moedas de 1 real: "))

cent1 = total1 * 0.01
cent5 = total5 * 0.05
cent10 = total10 * 0.10
cent25 = total25 * 0.25
cent50 = total50 * 0.50
real1 = total1R * 1

print(f"O valor economizado será de {cent1 + cent5 + cent10 + cent25 + cent50 + real1:.2f} reais")

print("\n")

'''2'''
litroRefresco = float(input("Informe a quantidade de litros do refresco: "))

aguaM = (8 * litroRefresco) / 10
suco = (2 * litroRefresco) / 10

print(f"Serão necessários {aguaM} litros de água e {suco}  litros de suco para o refresco")

print("\n")

'''3'''
precoA = float(input("Informe o preço antigo: "))
desconto = precoA * 0.10
precoN = precoA - desconto

print(f"Com o desconto de 10% o novo preço será {precoN} reais")

print("\n")

'''4'''
salarioFix = float(input("Informe a quantia do seu salário fixo: "))
totalVendas = float (input("Informe quantos reais adquiriu com suas vendas: "))

comissaoVendas = totalVendas * 0.04
salarioT = salarioFix + comissaoVendas

print(f"Seu salário total será de {salarioT} reais")

print("\n")

'''5'''
peso = float(input("Informe seu peso: "))

pesoEn = peso * 0.15
pesoF = peso + pesoEn

pesoEm = peso * 0.20
pesoF2 = peso - pesoEm

print(f"Seu peso caso você engorde 15% será de {pesoF}\nAgora se você emagrecer 20% seu peso será de {pesoF2}")

print("\n")

'''6'''
salarioFuncionario = float(input("Informe seu salário: "))
salarioMin = float(input("Informe o salário mínimo: "))

qntdsalariomin = salarioFuncionario / salarioMin

print(f"Você recebe {qntdsalariomin:.2f} salarios mínimos")

print("\n")

'''7'''
numero = int(input("Informe um número da tabuada: "))

numero1 = numero * 1
numero2 = numero * 2
numero3 = numero * 3
numero4 = numero * 4
numero5 = numero * 5
numero6 = numero * 6
numero7 = numero * 7
numero8 = numero * 8
numero9 = numero * 9
numero10 = numero * 10

print(f"Com o número informado os valores serão\n {numero1}\n{numero2}\n{numero3}\n{numero4}\n{numero5}\n{numero6}\n{numero7}\n{numero8}\n{numero9}\n{numero10}")

print("\n")

'''8'''
anoNasc = int(input("Informe o seu ano de nascimento: "))
anoAtual = int(input("Informe o ano atual:"))

a = anoAtual - anoNasc
b = anoAtual * 12
c = a * 365
d = a * 52

print(f"Você tem {a} anos de idade\nVocê tem {b} meses de idade\nVocê tem {c} dias de idade\nVocê tem {d} semanas de idade")

print("\n")

'''9'''
salario = 1200
c1 = 200
c2 = 120

multa1 = c1 * 0.02
multa2 = c2 * 0.02

total_c1 = c1 + multa1
total_c2 = c2 + multa2

restante = salario - (total_c1 + total_c2)


print(f"Sobrará na conta de João {restante} reais")