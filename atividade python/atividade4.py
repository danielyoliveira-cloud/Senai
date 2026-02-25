nota1 = float(input("insira o primeiro nota"))
nota2 = float(input("insira o segunda nota"))
nota3 = float(input("insira o terceira nota"))
nota4 = float(input("insira o quarta nota"))
media= (nota1+nota2+nota3+nota4)/4
print("a media foi", media)
if media >= 7:
    print("aluno esta aprovado")
else:
    print("aluno esta reprovado")