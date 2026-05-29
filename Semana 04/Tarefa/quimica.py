import csv
from formula import interpretar_formula
 

# Inicializa o dicionário composto vazio
tabela_periodica = {}


'''Leitura do arquivo CSV e transformação em lista '''

def criar_tabela_periodica():

    with open("elementos.csv", mode="r", encoding="utf-8") as arquivo:
        planilha = csv.reader(arquivo)
        next(planilha) #Pular a primeira linha do excel

        for linha in planilha:
            
            chave = linha[0]  # SIMBOLO 
            nome = linha[1]  # NOME
            massa = float(linha[2])  # MASSA ATOMICA 
            
            # "SIMBOLO": [NOME, MASSA] Dicionario Composto
            #{'Ac': ['Actínio', 227.0], 'Ag': ['Prata', 107.8682],...
            tabela_periodica[chave] = [nome, massa]
            

         
        return tabela_periodica


def calcular_massa_molar(lista_quantidade_simbolos, dic_da_tabela_periodica):
    massa_total = 0
    #LISTAS são mutaveis / TUPLAS são imutaveis
    #O interpetrar_formula gera uma lista de tuplas [(c,2), (h,13)]
    print(lista_quantidade_simbolos)
    #essa funcao traz a formula já transformada como c2 o2 h3 ...
    for item in lista_quantidade_simbolos:
        simbolo = item[0]; # dentro da lista composta já Nome
        quantidade = item[1]; 
        print(f"{simbolo}:{quantidade}")

        massa_atomica = dic_da_tabela_periodica[simbolo][1]
        massa_total += massa_atomica * quantidade

    return float(massa_total);

def main():
    formula = input("Digite uma formula:\n> ");
    amostra = float(input("Digite o tamanho da amostra:\n> "));
    dic_tabela = criar_tabela_periodica();

    int_form = interpretar_formula(formula, dic_tabela)

    massa_molar = calcular_massa_molar(int_form, dic_tabela)

    print(f"Massa molar é : {massa_molar}");

    numero_mols = amostra / massa_molar
    print(f"O numero de mols é: {numero_mols} ")


if __name__ == "__main__":
    main()