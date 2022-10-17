print (True and True and True)
print (True and False and True)
print(False and False and False)
print(True or True or True)
print (True or False or False)
print(False or False or False)


saldo = 10000
sague = 200
limite = 100
conta_especial = True


saldo = 1000
sague = 250
limite = 200

exp = saldo >= sague and sague >= sague
exp_2 = (saldo >= sague <= limite) or (conta_especial and saldo >= sague)

conta_normal_com_saldo_suficiente = saldo >= sague and sague <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= sague

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(exp_3)


