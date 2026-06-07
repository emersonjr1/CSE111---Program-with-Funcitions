 # Exemplo 2
import csv


def main():
    # Abre o arquivo CSV para leitura e armazena uma referência
    # para o arquivo aberto em uma variável chamada arquivo_csv.
    
    with open("hinos.csv", "rt", encoding="utf-8") as arquivo_csv:
        
        # Usa o módulo csv para criar um objeto leitor
        # que será lido do arquivo CSV aberto.
        
        leitor = csv.reader(arquivo_csv)
        
        # Lê as linhas no arquivo CSV uma de cada vez.
        # O objeto leitor retorna cada linha como uma lista.
        
        for lista_da_linha in leitor:
            print(lista_da_linha)
# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()