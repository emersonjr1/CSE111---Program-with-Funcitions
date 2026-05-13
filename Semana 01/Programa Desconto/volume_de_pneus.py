import math;
import datetime as dt;

dataHoje = dt.date.today().strftime("%d/%m/%y");

print(dataHoje)

activeProgram = 1
while activeProgram != 0:
        print("-" * 40)
        print("-" * 12 + " Volume de Pneu " + "-" *12)
        print("-" * 40)
        w = int(input("Digite a largura do PNEU em milímetros \n(165, 175, 185, 195, 205, 215, 225,265,285)\nDigite : \n"));
        a = int(input("Digite a proporção do PNEU (45, 50, 55, 60, 70, 75): \n"));
        d = int(input("Digite o diâmetro da roda em polegadas (Aro: 13, 14, 15, 16, 17) : \n"));

        volume = (math.pi * (w**2) * a *(w * a + 2540 * d ))/10**10;


        if a == 45:
                valor = 160.00
        elif a==50:
                valor = 200.00
        elif a==55:
                valor = 240.00
        elif a==60:
                valor = 280.00
        elif a==70:
                valor = 320.00
        elif a==75:
                valor = 360.00
        else:   
                valor= None
                print("Tamanho não identificado.");


        print(f"Volume: {volume:.2f} ");
        print("-" * 40);

        print(f"O valor do pneu é R$ {valor}");
        print("-" * 40)
        
        if valor != None or valor == 0:
                wishBuy = input("Deseja comprar o Pneu? \n  1- SIM | 2-Não \nDigite o numero:  ");
                print("-" * 40)
                if wishBuy == '1':
                        nome = input("Digite seu Nome: ");
                        telefone = input("Digite seu telefone: ");
                        print("-" * 40)

                        with open("volumes.txt", 'at', encoding="utf-8") as arquivo:    
                                arquivo.write(f" Data: {dataHoje}, Nome: {nome}, Telefone: {telefone}, Pneu: {w} {a}R/{d} Valor: {valor}, Volume: {volume:.2f}\n")
                        
                        with open("volumes.txt", 'rt', encoding='utf-8')as arquivo_leitura:
                                for numLinha,linha in enumerate(arquivo_leitura, start=1):
                                        print(f"{numLinha} - {linha.strip()}")
                        
                        print("-" * 40)

                        continuar =  int(input("Deseja continuar comprando? \n  1- SIM | 2-Não \nDigite o numero: "));
                        if continuar != 1:
                                print("Consulta finalizada")
                                activeProgram = 0
                                print("-" * 40)
                        
                else: 
                        print("Consulta finalizada")
                        print("Achei1")
                        activeProgram = 0
        else:
                print("Consulta finalizada!")
                print("Achei2")
                activeProgram = 0