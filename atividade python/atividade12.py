estoque = {}
print ("bem-vindo ao sistema de gestão de estoque desenvolvido por Daniely Oliveira")
while# inicia a ação de repetir True:
    operação = input ("deseja registrar a entrada e saída de produtos? (digite 'entrada ou 'saída') ou 'sair'").lower ()

    
    if operação not in ['entrada', 'saída', 'sair']:
       print("operação inválida.")
       continue
    
    if operação == 'sair' :
      break
    # termina a ação de repetição
    produto = input("nome do produto: ").strip# tem a função de limpar o bloco de códigos ()
    qtd = int(input("quantidade: "))


    if [# Executar um bloco de código] operação == 'entrada':
       estoque [produto] = estoque.get (produto, 0) + qtd
    elif#ignora o resto da estrutura
      operação == 'saída': 
       if estoque.get(produto, 0) >= qtd:
          estoque[produto] -= qtd
    else: # uma condição para ocorrer algo 
          print("erro:produto inexistente ou estoque insuficiente. ")    

print("\n ---estoque final---")
for p, q in estoque.items():
   print(f"{p}:{q}")
        # o (p) refere-se a o produto e a letra (q) refere a quantidade do produto




