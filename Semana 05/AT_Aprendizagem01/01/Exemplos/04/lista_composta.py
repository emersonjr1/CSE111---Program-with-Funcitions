# Exemplo 4
import csv


def main():
    # Lê o conteúdo do arquivo dentistas.csv
    # em uma lista composta.
    lista_de_dentistas = ler_lista_composta("dentistas.csv")
    # Exibe a lista inteira.
    print(lista_de_dentistas)


def ler_lista_composta(nomedoarquivo):
    """Lê o conteúdo de um arquivo CSV em uma lista 
    composta e retorna a lista. Cada elemento na
    lista composta será uma pequena lista que contém
    os valores de uma linha do arquivo CSV.
    Parâmetro filename: o nome do arquivo CSV a ser lido
    Retorno: uma lista de listas que contêm strings
    """
    # Cria uma lista vazia que armazenará
    # os dados do arquivo CSV.
    lista_composta = []
    # Abre o arquivo CSV para leitura e armazena uma referência
    # para o arquivo aberto em uma variável chamada arquivo_csv.
    with open(nomedoarquivo, "rt", encoding="utf-8") as arquivo_csv:
        # Usa o módulo csv para criar um objeto leitor
        # que será lido do arquivo CSV aberto.
        leitor = csv.reader(arquivo_csv)
        # Lê as linhas no arquivo CSV uma de cada vez.
        # O objeto leitor retorna cada linha como uma lista.
        for lista_da_linha in leitor:
            # Se a linha atual não estiver em branco,
            # anexa a linha à lista_composta.
            if len(lista_da_linha) != 0:
                # Adiciona uma linha do arquivo CSV
                # à lista composta.
                lista_composta.append(lista_da_linha)
    # Retorna a lista composta.
    return lista_composta


# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()