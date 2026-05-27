from Ex_test.endereco import extrair_cidade, extrair_estado, extrair_cep;
import pytest

def test_extrair_cidade():
    endereco_completo = "Av. Centenário, 2200, Mangueirão, Belém - PA, 66640-658"

    cidade = "Belém"

    resultado = extrair_cidade(endereco_completo)

    assert cidade == resultado


def test_extrair_estado():
    endereco_completo = "Av. Centenário, 2200, Mangueirão, Belém - PA, 66640-658"
    estado = "PA"

    resultado = extrair_estado(endereco_completo)

    assert estado == resultado


def test_extrair_cep():
    endereco_completo = "Av. Centenário, 2200, Mangueirão, Belém - PA, 66640-658"
    cep = "66640-658"

    resultado = extrair_cep(endereco_completo);

    assert cep == resultado;



#----

pytest.main(["-v", "--tb=line", "-rN", __file__])


