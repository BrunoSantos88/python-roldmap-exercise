opçao = -1

while opçao != 0:
    opçao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opçao == 1:
        print("Sacando....")
    elif opçao == 2:
        print("Exibindo o extrato.....")
else:
    print("Obrigado por usar nosso sistema bancario, ate logo!")
