import mysql.connector
import csv

# CONEXÃO BANCO DE DADOS MySQL
database_conex = {
    'host': 'localhost',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'sua_base_de_dados'
}

# LEITURA DOS DADOS
def ler_csv(arquivo_csv):
    with open(arquivo_csv, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Lê o cabeçalho
        data = [row for row in reader]
    return header, data

# VERIFICAÇÃO DE COERÊNCIA DOS DADOS
def verificar_coerencia(csv_data, db_connection):
    cursor = db_connection.cursor()
    for row in csv_data:
        
        nome, idade = row  
        query = f"SELECT * FROM sua_tabela WHERE nome = '{nome}' AND idade = {idade}"
        cursor.execute(query)
        result = cursor.fetchall()
        if not result:
            print(f"Dados inconsistentes encontrados: Nome: {nome}, Idade: {idade}")

if __name__ == "__main__":
    arquivo_csv = 'seu_arquivo.csv'
    db_connection = mysql.connector.connect(**database_conex)
    header, csv_data = ler_csv(arquivo_csv)
    verificar_coerencia(csv_data, db_connection)
    db_connection.close()
