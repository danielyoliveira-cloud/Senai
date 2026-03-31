print("Bem-vindo ao sistema de controle de acesso do coworking!")
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

dia = input("Digite o dia da semana (segunda, terça, quarta, quinta, sexta, sábado ou domingo): ").lower()

hora = int(input("Digite a hora de entrada (apenas a hora inteira, ex: 10 para 10h): "))

tipo_usuario = input("Você é membro ou visitante? ").lower()

acesso_permitido = False
motivo = ""

if dia == "sábado" or dia == "domingo":
    
    if tipo_usuario == "membro":
        acesso_permitido = True
    else:
        motivo = "Apenas membros podem acessar o espaço no fim de semana."