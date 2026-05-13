

#LISTAS
MINUSCULAS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
MAIUSCULAS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
ESPECIAIS=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

#Cabecalho Global
tema = "\n-- Validação de Segurança da senha --\n"
qtdHifen = "-" * len(tema)


#----------
#Verificar se a palavra esta nos arquivos TXT
def procurar_palavra(palavra, nome_do_arquivo, maiusculas_e_minusculas):
    with open(f"{nome_do_arquivo}", "r", encoding="utf-8") as a:

            if maiusculas_e_minusculas is True: #verifica se a palavra correspondente existe
                for linha in a:
                    if linha.strip() == palavra:
                        print("Palavra correspondente encontrada na lista de senhas. 1")
                        return True
                         
            else: #Se maiusculas_e_minusculas for falso - verifica se possui lista palavras
                palavra_minuscula = palavra.lower();
                for linha in a:
                    if linha.strip().lower() == palavra_minuscula:
                        print("A senha é comumente usada e não é segura.1") 
                        return True
                    
    return False;

#----------

def palavra_tem_caractere(palavra, lista_caractere):
    for caractere in palavra:
            if caractere in lista_caractere:
               return True;
            
    return False;

#--
def calcular_complexidade(palavra):
    
    complexidade = 0

    if palavra_tem_caractere(palavra, MINUSCULAS): 
        complexidade = complexidade + 1
                 
    if palavra_tem_caractere(palavra, MAIUSCULAS):
        complexidade = complexidade + 1
        
    if palavra_tem_caractere(palavra, DIGITOS):
        complexidade = complexidade + 1
        
    if palavra_tem_caractere(palavra, ESPECIAIS):
        complexidade = complexidade + 1
    
    return int(complexidade)

#--
 
def validar_senha(senha, comprimento_min, comprimento_forte):
    
    if procurar_palavra(senha,"lista_de_palavras.txt", False):
        return 0
        
    if procurar_palavra(senha,"senhas_mais_comuns.txt", True):
        return 0

    if len(senha) <= comprimento_min:
        return 1 #se for menor que o comprimento retorna 1 direto

    elif len(senha) >= comprimento_forte:
        return 5 #se for menor que o comprimento retorna 5 direto
        

    
    #Para somar a força
    complexidade = calcular_complexidade(senha)
    forca = 1 + complexidade;
    
    print(f"A força da sua senha é: {forca} ")
        
    return forca
    
#----------

def main():
    while True:
        print("\n" + qtdHifen + tema + qtdHifen)
        senha = input("\nDigite a senha para teste de segurança:\n> ");

        if senha.lower() == "q":
            break

        else:
            forca = validar_senha(senha,10,16)

            if forca == 0:
                print(f"Força: {forca}/5 - Senha insegura\n")
            elif forca == 1:
                print(f"Força: {forca}/5 - Senha muito fraca\n")
            elif forca == 2:
                print(f"Força: {forca}/5 - Senha fraca\n")
            elif forca == 3:
                print(f"Força: {forca}/5 - Senha média\n")
            elif forca == 4:
                print(f"Força: {forca}/5 - Senha forte\n")
            elif forca == 5:
                print(f"Força: {forca}/5 - Senha muito forte\n")
                
        
       

if __name__ == "__main__":
    main()