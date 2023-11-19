
from prettytable import PrettyTable
import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academia_turma_c"
)


cursor = conexao.cursor()
print(conexao)
print("")
print (f"=-=-=-="*5,"CRUD","=-=-=-="*5)
print("")
print("")
print("Escolha a tabela que você deseja : ")
print("")
tabelas = int(input("digite: 1-Alunos / 2-Funcionarioa / 3-Matriculado / 4-Modalidades / 5-Personal"))
rep = 1

#CRUD
while True:
    if rep == 1:
        while True:
            if tabelas > 1:
                print("Escolha a tabela que você deseja : ")
                print("")
                print("")
                print("ainda nao programei essa parte do banco : ")
                print("")
                tabelas = int(input("digite: 1-Alunos / 2-Funcionarioa / 3-Matriculado / 4-Modalidades / 5-Personal"))
                print("")
                
            else:
                campos = int(input("digite: 1- inserir / 2- Deleta / 3-Ler  "))

                while True:
                    if campos > 3:
                        print("")
                        print("Nao existe essa opção")
                        print("")
                        campos = int(input("digite: 1- inserir / 2- Deleta / 3-Ler / ou 4 PARA SAIR!  "))
                        
                        if campos == 4:
                            break

                    elif campos == 1:
                        print("")
                        print("opção de inserir")
                        print("")
                        nome = input("digite seu nome : ")
                        print("")
                        email = input("digite seu email : ")
                        print("")
                        cpf = input("Digite seu CPF: ")
                        print("")
                        comando = f'insert into alunos(nome,email,cpf) values ("{nome}","{email}","{cpf}")' 
                        cursor.execute(comando)
                        conexao.commit()
                        rep = int(input("quer repetir ? \n\n 1-Sim / 2-Nao"))
                        break
                            

                    elif campos == 2:
                        print("Você escolheu excluir")
                        print("")
                        x = int(input("digite o ID do aluno que voce quer excluir : "))
                        comando = f'delete from alunos where ID_alunos = {x} '
                        cursor.execute(comando)
                        conexao.commit()
                        print("apagado com sucesso")
                        rep = int(input("quer repetir ? \n\n 1-Sim / 2-Nao"))
                        break

                    elif campos == 3:
                        print("Você escolheu visualizar ")
                        print("")
                        comando = 'select * from alunos'
                        cursor.execute(comando)
                        resultado = cursor.fetchall()

                        if resultado:
                            colunas = [desc[0] for desc in cursor.description]
                            
                            tabela = PrettyTable(colunas)
                            for linha in resultado:
                                tabela.add_row(linha)

                            print(tabela)
                        else:
                            print("Nenhum resultado encontrado.")

                        rep = int(input("Quer repetir? \n\n 1-Sim / 2-Não"))
                        

                    else:
                        print("Nao existe essa opção")
                        print("")
                        campos = int(input("digite: 1- inserir / 2- Deleta / 3-Ler  "))

    elif rep ==2:
        conexao.commit()
        cursor.close()
        conexao.close()
        break
        




