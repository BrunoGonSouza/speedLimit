'''Universidade Cruzeiro
   Bruno Gonçalves
   30.02.22
   02 – Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, 
   exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da multa, cobrando R$ 
   5,00 por km acima de 80 km/h.'''

velocidade = int(input("Digite a velocidade (Ex:80): "))
limite = 80
valor = 5.00

if (velocidade > limite):   
    print("Você foi multado")

    diferenca = velocidade - limite
    multa = diferenca * valor
    print(f"Velocidade: {velocidade} km/h : {diferenca} km/h acima do permitido")
    print(f"R$ 5,00 por Km acima do permitido - Valor da Multa: R$ {multa:.2f}")
else:
    print("Deu sorte hein")
