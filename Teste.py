from Atividade import conectarBanco
from Atividade import printBanco
from sqlite3 import Connection
import os

    
# def test_conecta_banco():
#     conexao = conectarBanco()
#     assert isinstance(conexao, Connection)


# def test_database_file():
#     assert os.path.isfile('unoesc_bd.db')
    
def test_print_banco():
    conexao = conectarBanco()
    assert (printBanco(conexao)) == True