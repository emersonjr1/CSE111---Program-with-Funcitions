#Consumo de combustivel S02

def form_consumo(a,b,c): 
    #final #inicial #qtd combustivel
    r = (a - b)/(c); #Consumo por litro
    g = c * 0.26417; #qtd Galao
    d_m = (a - b) / 1.609 ; #Milhas
    m_g = d_m / g; #Milhas por Galao

    return r, g, d_m, m_g;

 
def main():
    
    tema = " -- Programa Consumo de Combustive --\n"
    pontos = "-" * len(tema) + "\n";

    print(f"{pontos}{tema}{pontos}")
    odometro_inicial = float(input("Digite o valor inicial do ODOMETRO: \nR: "))
    odometro_final = float(input("Digite o valor final do ODOMETRO:\nR: "))
    qtd_combustivel = float(input("Qual a quantidade de combustivel em Litros (L)?\nR: "))

    consumo, galao, milhas, mi_galao = form_consumo(odometro_final,odometro_inicial,qtd_combustivel);
    print(f"Consumo: {consumo:.2f} km/l \nQuantidade de Galão: {galao:.2f} un\nMilhas: {milhas:.3f} milha(s)\nMilhas por Galão: {mi_galao:.3f}")

if __name__ == "__main__":
    main()