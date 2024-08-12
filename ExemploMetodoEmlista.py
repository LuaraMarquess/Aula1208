#Demomstração de metódos em listas...

inss = ["Maria", "Manoel","José","Isabela"]
print("Eis, a fila do inss: ", inss)

novo = input("Insira mais uma pessoa: ")
inss.append(novo) #Adiciona uma pessoa no final da lista
print("Conferindo a nova lista: ",inss)

print("Vou tirar a última pessoa desta lista...")
especial = inss.pop() #Remove a ultima pessoa da lista/ Especial está recebendo o valor que saiu

print("Agora,vou colocá-la na frente de todos!")
inss.insert(0,especial) #Insere um valor na primeira posição
print("Conferdindo a lista: ", inss)

print("Maria não gostou e reclamou...")
inss.remove("Maria")
print("E agora, ele saiu 'Pé da vida'",inss)

print("Para não ter mais reclamação,vamos atender...")
inss.sort() #Ordena em ordem alfabética
print("...em ordem alfabética",inss)

print("Onde está nova pessoa chamada", especial, " ? ")
print("Ela agora ficou na posição  ",inss.index(especial)+1, "!")