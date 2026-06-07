import os;
import csv;

os.system('cls');

def criar_dicionario_estudantes(arquivo_csv, chave_id, nome):
    dicionario = {}
    with open(arquivo_csv, 'rt', encoding="utf-8") as arquivo_de_estudante:
        leitor_de_arquivo = csv.reader(arquivo_de_estudante)
        next(leitor_de_arquivo)

        for linha in leitor_de_arquivo:
            id_estudante = linha[chave_id]
            dicionario[id_estudante] = linha[nome]

        return dicionario

def main():
    INDICE_ID = 0
    INDICE_NOME = 1

    dados_estudante = criar_dicionario_estudantes('estudantes.csv', INDICE_ID, INDICE_NOME)
    
    id = input("Por favor, informe uqal o ID do estudante que você deseja saer o nome: \n>> ")
    id= id.replace("-","") #Verifica se tem - e transforma em nada ('');



    if id in dados_estudante:
        print(f"O nom do aluno é {dados_estudante[id]}.")

    elif not id.isdigit: #se não for digito.
        print("Numero de identificação inválido.")

    elif len(id) < 9:
        print("Numero de indentificação inválido: digitos insuficiente.")
    elif len(id) > 9:
        print( "Numero de identificação inválido: ultrapassa o limite de digitos.")

    else:
        print("Estudante inexistente.")



if __name__ == '__main__':
    main();
