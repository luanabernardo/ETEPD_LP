import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='****',
    password='****',
    database='coleta_seletiva',
)
cursor = conexao.cursor()
#create
titulo_coleta = 'seletiva'
ponto_coleta='recife'
data_criacao= '2000-10-10'
nome_cidadao='denys'
descricao_coleta='plastico'
status='aberta'
comando = f'INSERT INTO coleta (titulo_coleta, ponto_coleta, data_criacao, nome_cidadao, descricao_coleta, status) VALUES ("{titulo_coleta}", "{ponto_coleta}", "{data_criacao}","{nome_cidadao}", "{descricao_coleta}","{status}")'
cursor.execute(comando)
conexao.commit()

#read
comando= f'SELECT * FROM coleta_seletiva.coleta'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#update
status = "fechado"
titulo_coleta = "seletiva"
comando = f'UPDATE coleta SET status="{status}" WHERE titulo_coleta = "{titulo_coleta}"'
cursor.execute(comando)
conexao.commit()

#delete
titulo_coleta = "2"
comando = f'DELETE FROM coleta WHERE titulo_coleta = "{titulo_coleta}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
