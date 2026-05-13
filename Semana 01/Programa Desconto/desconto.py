from datetime import datetime;

valor_min =  50
porcent_Descunt = 0.1
imposto = 0.06

dt = datetime.now();
dia_semana = dt.weekday(); #Dia semana começa em 0(domingo) até 6(sabado) sendo 2 e 3 (Terça e Quarta)

valorProd = 1
while valorProd != 0:
        
        quantidade = int(input("Digite a quantidade: "));
        valorProd = float(input("Informe o valor do produto: "));
        subtotal = (valorProd * quantidade);
        print( " " *5 , "-" * 10);

        if subtotal >= valor_min :
            if dia_semana == 2 or dia_semana == 3:
                valor_desconto = (subtotal * porcent_Descunt);
                print(f"Desconto : {valor_desconto}");
                valor_devido = (subtotal - valor_desconto);
            

            else:
                print("Hoje não possui desconto ativo")
                print("-" * 40)
        else:
             print(f"Valor minimo para desconto nas Terças e Quartas é R$ {valor_min:.2f} ")
        valor_imposto = (valor_devido * imposto);
        print(f"Imposto : {valor_imposto}")

        valor_total = (valor_devido + valor_imposto);
        print(f"O valor total a pagar é R$ {valor_total:.2f}")
        print("-" * 40)
    
        pergCont = int(input("Gostaria de continuar? \n Digite o numero: 1 - Sim || 2 - Não \nResposta:  "))

        if pergCont == 2:
            valorProd = 0;
            print("Saindo...")
        else:
            print("Continuando")
            print("-" * 40)
        

 

