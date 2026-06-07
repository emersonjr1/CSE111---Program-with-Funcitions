# Exemplo 3
import csv
# Índices de algumas das colunas
# no arquivo dentistas.csv.
INDICE_NOME_DA_EMPRESA = 0
INDICE_NUM_DE_FUNC = 3
INDICE_NUM_DE_PACIENTES = 4
def main():
    # Abre um arquivo chamado dentistas.csv e armazena uma referência
    # para o arquivo aberto em uma variável chamada arquivo_de_dentistas.
    with open("dentistas.csv", "rt", encoding="utf-8") as arquivo_de_dentistas:
        # Usa o módulo csv para criar um objeto
        # leitor que será lido do arquivo aberto.
        leitor = csv.reader(arquivo_de_dentistas)
        # Como a primeira linha do arquivo CSV contém apenas o cabeçalho
        # (nomes das colunas), usamos next(leitor) para avançar uma linha
        # e começar a leitura diretamente pelos dados dos dentistas.
        next(leitor)
        max_registrado = 0
        maior_consultorio = None
        # Lê as linhas no arquivo CSV, uma de cada vez.
        # O objeto leitor retorna cada linha como uma lista.
        for lista_da_linha in leitor:
            # Para a linha atual, recupere os
            # valores nas colunas 0, 3 e 4.
            empresa = lista_da_linha[INDICE_NOME_DA_EMPRESA ]
            num_de_funcionarios = int(lista_da_linha[INDICE_NUM_DE_FUNC])
            num_de_pacientes = int(lista_da_linha[INDICE_NUM_DE_PACIENTES])
            # Calcula o número de pacientes por
            # funcionário do consultório atual.
            pacientes_por_funcionario = num_de_pacientes / num_de_funcionarios
            # Se o consultório atual tiver mais
            # pacientes por funcionário do que o número registrado
            # máximo, atribui max_registrado e maior_consultorio
            # para ser o atual consultório.
            if pacientes_por_funcionario > max_registrado:
                max_registrado = pacientes_por_funcionario
                maior_consultorio = empresa
    # Exibe os resultados para o usuário.
    print(f"{maior_consultorio} tem {max_registrado:.1f}"
            " pacientes por funcionário")
# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()