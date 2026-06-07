import csv
from datetime import datetime

# Realizado a leitura dos arquivos conforme solicitado, realizado a leitura dos produtos, realizado os descontos conforme solicitado. 

def ler_dicionario(filename, indice_coluna_chave):
    dicionario = {}
    
    with open(filename, "rt", encoding="utf-8") as arquivo:
        leitor_arquivo = csv.reader(arquivo)
        
        next(leitor_arquivo)  # Pula cabeçalho
        
        for linha in leitor_arquivo:
            cod_produto = linha[indice_coluna_chave]
            dicionario[cod_produto] = linha  # ou outro valor relevante
    
    return dicionario



def main():
    INDICE_ID = 0
    INDICE_NOME = 1
    INDICE_PRECO = 2
    IMPOSTO = 0.06
    CSV_PRODUTOS = "produtos.csv"
    CSV_PEDIDO = "pedido.csv"
    
    # Obter data e hora atual
    try:
        agora = datetime.now()
        print(f"Data: {agora.strftime('%d/%m/%Y')}")
        print(f"Hora: {agora.strftime('%H:%M:%S')}")
        print()
    except Exception as e:
        print(f"Erro ao obter data/hora: {e}")
    
    try:
        dic_produto = ler_dicionario(CSV_PRODUTOS, INDICE_ID)
    except FileNotFoundError as e:
        print(f"Arquivo não encontrado \nERRO: {e}")
        return
    except PermissionError as e:
        print(f"Permissão negada \nERRO: {e}")
        return
    except KeyError as e:
        print(f"Chave não encontrada \nERRO: {e}")
        return

    try:
        with open(CSV_PEDIDO, "rt", encoding="utf-8") as arquivo_pedido:
            leitor_pedido = csv.reader(arquivo_pedido)

            next(leitor_pedido)

            print("-" *30)
            print("Imporio inkon")
            print("-" *30)
            
            sub_total_pedido = 0
            desconto_total = 0
            
            for linha_item in leitor_pedido:
                id_produto = linha_item[0]
                quantidade = int(linha_item[1])
                
                if id_produto in dic_produto:
                    id_dados = dic_produto[id_produto]
                    preco = float(id_dados[INDICE_PRECO])
                    nome = id_dados[INDICE_NOME]
                     
                    if quantidade == 2 or quantidade == 3 or quantidade == 4:
                        desconto = preco * 0.5
                        total_ind = (preco * quantidade)
                        print(f">ID: {id_produto} - {nome} - Qtd: {quantidade} - Preço/un: R$ {preco:.2f} - SubTotal: R$ {total_ind:.2f} - Desconto: R${desconto:.2f}")
                
                    
                    else:
                        total_ind = quantidade * preco
                        desconto = 0
                        print(f">ID: {id_produto} - {nome} - Qtd: {quantidade}; - Preço/un:R$ {preco:.2f} - SubTotal: R$ {total_ind:.2f}")
                        

                    desconto_total += desconto
                    sub_total_pedido += total_ind    
                    
                else:
                    print(f"Produto {id_produto} não encontrado no catálogo! Item ignorado.\n")

            
            print(f"Desconto de itens: - {desconto_total:.2f} ")

            sub_com_desconto = (sub_total_pedido - desconto_total)
            valor_taxa = sub_com_desconto *IMPOSTO
            print(f"Imposto sobre pedido: + {valor_taxa:.2f}\n")
            
            
            total_pedido = sub_com_desconto + valor_taxa
          

            print(f"Total a ser pago do seu produto é : R$ {total_pedido:.2f}")
            
            print("-" *30)
            print(f"Obrigado pela compra!")
            print("-" *30)
    
    except FileNotFoundError as e:
        print(f"Arquivo de pedido não encontrado \nERRO: {e}")
    except PermissionError as e:
        print(f"Permissão negada ao ler pedido \nERRO: {e}")
    except KeyError as e:
        print(f"Chave não encontrada no pedido \nERRO: {e}")


if __name__ == "__main__":
    main()