conta_normal = True
conta_universitaria = False

saldo = 2500
saque = 2000

cheque_especial = 450

if conta_normal:
    if saldo >= saque:
       print("Sague realizado com sucesso!")

    elif saque <= (saldo- + cheque_especial):
         print("Saque ralizado com uso do cheque especial!")

    else:
         print("Não foi possivel realizar o saque!")

elif conta_universitaria:
    if saldo >= saque:
     print("Saque Realizado com sucesso")
    else:
     print("Saldo insuficiente")   

else:
    print("Sistema nao reconheceu seu tipo de conta!")
    print("Entre em contato com seu Gerente!")
    

