import os
import time
tentativa = 0
tentativa2 = 0
tentativa3 = 0
tentativa4 = 0
free = ["A1","A2","A3","A4","A5","A6","B1","B2","B3","B4","B5","B6","C1","C2","C3","C4","C5","C6"]
while len(free) != 0:
    print(f'Temos essas vagas livres: {free}')
    vaga = input("escolha uma vaga:").upper()
    index = vaga[0:1]
    index2 = vaga[1:2]
    os.system("cls") or None
    while index != "A" and index != "B" and index != "C":
        tentativa2 +=1
        print("Erro!!")
        vaga = input("A fileira precisa ser igual a 'A' 'B' OU 'C':").upper()
        if tentativa2 == 3:
            print("burro")
            exit()
    while index2.isalpha() == True:
        tentativa4 +=1
        print("Erro!!")
        vaga = input("O segundo digito deve ser um numero").upper()
        if tentativa4 == 3:
            print("burro")
            exit()
    while int(index2) > 6 and int(index2) > 0:
        tentativa3+=1
        print("Erro!!")
        vaga = input("Escolha uma garagem entra 1 e 6").upper()
        if tentativa3 == 3:
            print("burro")
            exit()
    ocupados = vaga in free
    while ocupados == False :
        tentativa4+=1
        print("Erro!!")
        vaga = input(f"Essa garagem já foi escolhida!! Escolha outra garagem, vagas disponiveis : {free}").upper()
        ocupados = vaga in free
        os.system("cls") or None
        time.sleep(0.5)
        if tentativa4 == 3:
            print("burro")
            exit()
    for x in free:
        if x == vaga:
            free[free.index(x)] = "---"
            time.sleep(0.5)
            
            


        
    
    