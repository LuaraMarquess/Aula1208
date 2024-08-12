#Demonstração de funções em listas...
numeros = [7,2,9,6,5,0,3,8,1,4]
palavras = ["Olá","Alô","Hei","uai","ops"]

print("Quantas variáveis possui: ")
print("Números:" ,len(numeros)) #Retorna o número de váriaveis
print("palavras: ", len(palavras))

print("Vamos reordenar estas listas? ")
print(sorted(numeros)) # Coloca em ordem
print(sorted(palavras))

print("O somatório de números: ", sum(numeros)) #soma valores
print("Qual é o maior valor? ",max(numeros))  #Pega valor máximo da lista
print("Qual é a primeira palavra?", min(palavras)) #Pega em ordem 