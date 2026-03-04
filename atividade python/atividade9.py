maior = float()
menor = float()
soma = 0
acima_100 = 0
for cont in range(11):
    temperatura = float (input(f"digite a {cont + 1} temperatura:"))
    soma += temperatura
    if cont == 0:
       maior = temperatura
       menor = temperatura
       
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
    if temperatura > 100:
        acima_100 += 1
media =  soma/cont

print(f"a maior temperatura foi {maior}")
print(f"a menor temperatura foi {menor}")
print(f"a media temperatura foi {media}")
print(f"a maior temperatura ultrapassou 100°c {acima_100}vezes")
