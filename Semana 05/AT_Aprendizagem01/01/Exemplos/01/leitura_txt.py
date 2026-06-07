# Exemplo 1
def main():
    # Lê o conteúdo de um arquivo de texto
    # chamado plantas.txt em uma lista.
    lista_de_texto = lista_de_leitura("plantas.txt")
    # Exibe a lista inteira.
    print(lista_de_texto)



def lista_de_leitura(nomedoarquivo):
    """Lê o conteúdo de um arquivo de texto em uma lista e
    retorna a lista. Cada elemento da lista conterá
    uma linha de texto do arquivo de texto.
    Parâmetro filename: o nome do arquivo de texto a ser lido
    Retorno: uma lista de strings
    """
    # Cria uma lista vazia que armazenará
    # as linhas de texto do arquivo de texto.
    lista_de_texto = []
    # Abre o arquivo de texto para leitura e armazena uma referência
    # para o arquivo aberto em uma variável chamada arquivo_de_texto.
    with open(nomedoarquivo, "rt", encoding="utf-8") as arquivo_de_texto:
        # Lê o conteúdo do arquivo
        # de texto uma linha de cada vez.
        for linha in arquivo_de_texto:
            # Remove os espaços em branco, se houver,
            # do início e do fim da linha.
            linha_limpa = linha.strip()
            # Adiciona a linha limpa do texto
            # ao final da lista.
            lista_de_texto.append(linha_limpa)
    # Retorna a lista que contém as linhas de texto.
    return lista_de_texto
# Chama main para iniciar este programa.
if __name__ == "__main__":
    main();

