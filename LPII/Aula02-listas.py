#toda lista começa com indice 0; 
#dicionários sempre seguem com chaves precedendo valo - ex {1: 'item a'}

clientes = []

clientes.append("ABNER") #a função append apenciona à lista um novo item
clientes.append("LUCAS")
clientes.append("MARIA")

clientes.insert(1, "ABGAIL") #a funcao insert serve para adicionar um item em determinado indice da lista; Sempre precede o indice indicando o local e posteriormente o item; 

print(clientes)

clientes.sort() #a função sort ordena os itens dentro da lista

print(clientes)

clientes.remove("LUCAS") #funcao remove serve para remover itens da lista; 

print(clientes)

clientes.clear()

print(clientes)








