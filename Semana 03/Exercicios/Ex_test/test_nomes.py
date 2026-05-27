from Ex_test.nomes import criar_nome_completo, extrair_sobrenome, extrair_primeiro_nome;
import pytest


def test_criar_nome_completo():
    primeiro_nome = "Eliane";
    sobrenome = "Oliveira";
    resultado = "Oliveira; Eliane"

    saida = criar_nome_completo(primeiro_nome, sobrenome)

    assert saida == resultado



def test_extrair_sobrenome():
    nome_completo = "Oliveira; Eliane"
    saida_esperada = "Oliveira"

    resultado = extrair_sobrenome(nome_completo)
    assert resultado == saida_esperada


def test_extrair_primeiro_nome():
    nome_completo = "Oliveira; Eliane"
    saida_esperada = "Eliane"
    resultado = extrair_primeiro_nome(nome_completo)

    assert resultado == saida_esperada







#----

pytest.main(["-v", "--tb=line", "-rN", __file__])


