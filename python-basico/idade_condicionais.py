Maior_Idade = 18
Idade_Especial = 17

idade = int (input("Informe sua idade: "))

if idade >= Maior_Idade:
   print("Maior de idade, pode tirar a CNH!")
   print("Pode da entrada no exame medico e pagar primera parcela!")

elif idade == Idade_Especial:
     print("Maior de idade, pode tirar a CNH!")
     print("Porém vai começar pelo curso teorico primeiro!")
     print("So pode fazer o exema medio apos completar os 18 anos!")

else:
    print("Ainda não pode tirar a CNH!")
    print("Precisa da autorização de um maior de idade!")
    
     