from tkinter import *
import sqlite3

principal = Tk()
principal.title("Jogos da Copa")
principal.geometry("400x400+250+250")
principal.iconbitmap("icon.ico")

def banco():
  global conexao, cursor
  try:
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
  except:
    print("Erro ao conectar")
  else:
    print("Conexão realizada com sucesso!")

def criar_tabela():
  banco()
  cursor.execute("CREATE TABLE IF NOT EXISTS `selecao` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT, grupo text)")
  print("Tabela criada com sucesso!")

criar_tabela()
def cadastrar():

  cursor.execute("INSERT INTO selecao (grupo, nome) values (?, ?)", (str(entry_grupo.get()), str(entry_selecao1.get())))
  cursor.execute("INSERT INTO selecao (grupo, nome) values (?, ?)", (str(entry_grupo.get()), str(entry_selecao2.get())))
  cursor.execute("INSERT INTO selecao (grupo, nome) values (?, ?)", (str(entry_grupo.get()), str(entry_selecao3.get())))
  cursor.execute("INSERT INTO selecao (grupo, nome) values (?, ?)", (str(entry_grupo.get()), str(entry_selecao4.get())))
  conexao.commit()
  print("Dados cadastrados com sucesso!")
  conexao.close
  entry_grupo.delete(0,"end")
  entry_selecao1.delete(0,"end")
  entry_selecao2.delete(0,"end")

def listar_console():
  banco()
  cursor.execute("SELECT grupo, nome from selecao")
  selecao = cursor.fetchall()
  for i in selecao:
    print(i)
  conexao.close()

def cancelar():
  entry_grupo.delete(0,"end")
  entry_selecao1.delete(0,"end")
  entry_selecao2.delete(0,"end")

label_grupo = Label(principal, text="Digite o grupo:")
label_grupo.place(x=50,y=10)
entry_grupo = Entry(principal)
entry_grupo.place(x=200, y=10)
label_selecao1 = Label(principal, text='Digite a primeira seleção:')
label_selecao1.place(x=50,y=40)
label_selecao2 = Label(principal, text="Digite a segunda seleção:")
label_selecao2.place(x=50,y=70)
label_selecao3 = Label(principal, text='Digite a terceira seleção:')
label_selecao3.place(x=50,y=100)
label_selecao4 = Label(principal, text='Digite a quarta seleção:')
label_selecao4.place(x=50,y=130)
entry_selecao1 = Entry(principal)
entry_selecao1.place(x=200,y=40)
entry_selecao2 = Entry(principal)
entry_selecao2.place(x=200,y=70)
entry_selecao3 = Entry(principal)
entry_selecao3.place(x=200,y=100)
entry_selecao4 = Entry(principal)
entry_selecao4.place(x=200,y=130)
botao_salvar = Button(principal,text="Salvar", command=cadastrar)
botao_salvar.place(x=200,y=170)
botao_cancelar = Button(principal,text="Cancelar", command=cancelar)
botao_cancelar.place(x=250,y=170)
botao_listar = Button (principal, text="Listar seleções", command=listar_console)
botao_listar.place(x=100, y=170)

principal.mainloop()