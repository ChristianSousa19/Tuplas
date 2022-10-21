num=int(input("Digite um numero entre 0 e 20: "))
numero="zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quartoze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"
while num not in range(0,20 +1):
    num=int(input("Error,por favor digite novamente: "))
print(f"Você digitou {num} por extenso fica {numero[num]}")