opçao = int(input("Informe uma opeçao: [1] Sacar \n [2] Extrato:"))

if opçao == 1:
   valor = float(input("Informe a quantia para o sague: "))
   # ...


elif opçao == 2:
     print ("Exibindo o extrato ...")

else:
    sys.exit("Opçao invalida")

#saldo = 2000.0
#sague = float (input("Informe o valor do seu saque:"))

#if saldo >= sague:
#   print ("Realizando Sague!")

#if saldo < sague:
#  print("Saldo Insuficiente!")
