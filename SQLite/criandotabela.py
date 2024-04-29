import sqlite3 # Importação da biblioteca
import random

Conexao = sqlite3.connect('DataBase') # Conexão com o banco de dados
Cursor = Conexao.cursor() # Criação de um cursor

# Função CREATE TABLE
"""a criação da tabela está comentada pois ela só precisa ser executada uma vez, caso contrário, o programa irá retornar um erro"""
#Cursor.execute( # Execução de um comando
#   'CREATE TABLE My_Table ( Data TEXT, Nome TEXT, Idade INTEGER)' # Criação de uma tabela (Comando SQL)
    # CREATE TABLE = Comando para criar uma tabela
    # My_Table = Nome da tabela
    # ( Data TEXT, Nome TEXT, Idade INTEGER) = Colunas da tabela
#)

Conexao.commit() # Salva as alterações (Fazer commit)

# Inserindo valores
# Função INSERT INTO
Cursor.execute(
    'INSERT INTO My_Table VALUES ("01/01/2021", "João", 20)' # Inserindo valores (Comando SQL)
        # INSERT INTO = Comando para inserir valores em uma tabela
        # My_Table = Nome da tabela
        # VALUES = Comando para inserir valores
        # ("01/01/2021", "João", 20) = Valores a serem inseridos
)


for i in range(10):
    Cursor.execute(
        f'INSERT INTO My_Table VALUES ("21/04/2024", "Nicolas", {random.randint(0, 100)})' # Inserindo valores (Comando SQL)
        # para alocar valores de forma dinãmica, é necessário ultilizar o {variavel}
    )
    
    
# Exibindo valores
# Função SELECT
Consulta = Cursor.execute('SELECT * FROM My_Table').fetchall() # Consulta de valores (Comando SQL)
                            # SELECT * = Comando para selecionar todos os valores
                            # FROM My_Table = Comando para selecionar a tabela
                            # fetchall() = Comando para retornar todos os valores

for i in Consulta: # Loop para exibir os valores
    print(i) # Exibição de valores (Data, Nome, Idade)
    
ConsultaNome = Cursor.execute('SELECT Nome FROM My_Table').fetchall() # Consulta de valores (Comando SQL)
                            # SELECT Nome = Comando para selecionar a coluna Nome

#for i in ConsultaNome: # Loop para exibir os valores
#    print(i) # Exibição de valores (Nome)
    
print("\n")
#Função WHERE
ConsultaIdade = Cursor.execute(
    """
    SELECT * FROM My_Table
    WHERE Idade = Idade > 50
    """
    # SELECT * = Comando para selecionar todos os valores
    # FROM My_Table = Comando para selecionar a tabela
    # WHERE Idade > 50 = Comando para selecionar valores com idade maior que 50
    ).fetchall() # Consulta de valores (Comando SQL)

#for i in ConsultaIdade: # Loop para exibir os valores
#    print(i) # Exibição de valores (Data, Nome, Idade)
    
# BETWEEN 
ConsultaIdade = Cursor.execute(
    """
    SELECT * FROM My_Table
    WHERE Idade BETWEEN 10 AND 50
    """
    # SELECT * = Comando para selecionar todos os valores
    # FROM My_Table = Comando para selecionar a tabela
    # WHERE Idade BETWEEN 10 AND 50 = Comando para selecionar valores com idade entre 10 e 50
    ).fetchall() # Consulta de valores (Comando SQL)

#for i in ConsultaIdade: # Loop para exibir os valores
#    print(i) # Exibição de valores (Data, Nome, Idade)

# LIKE

ConsultaNome = Cursor.execute(
    """
    SELECT * FROM My_Table
    WHERE Nome LIKE 'N%'
    """
    # SELECT * = Comando para selecionar todos os valores
    # FROM My_Table = Comando para selecionar a tabela
    # WHERE Nome LIKE 'N%' = Comando para selecionar valores com Nome começando com N
    ).fetchall() # Consulta de valores (Comando SQL)

ConsultaNome = Cursor.execute(
    """
    SELECT * FROM My_Table
    WHERE Nome LIKE '%s'
    """
    # SELECT * = Comando para selecionar todos os valores
    # FROM My_Table = Comando para selecionar a tabela
    # WHERE Nome LIKE '%s' = Comando para selecionar valores com Nome terminando com s
    ).fetchall() # Consulta de valores (Comando SQL)

#for i in ConsultaNome: # Loop para exibir os valores
#    print(i) # Exibição de valores (Data, Nome, Idade)

# IN

ConsultaNome = Cursor.execute(
    """
    SELECT * FROM My_Table
    WHERE Idade IN (20, 30)
    """
    # SELECT * = Comando para selecionar todos os valores
    # FROM My_Table = Comando para selecionar a tabela
    # WHERE Idade IN (20,30) = Comando para selecionar valores com Idade sendo 20 ou 30
    ).fetchall() # Consulta de valores (Comando SQL)

for i in ConsultaNome: # Loop para exibir os valores
    print(i) # Exibição de valores (Data, Nome, Idade)