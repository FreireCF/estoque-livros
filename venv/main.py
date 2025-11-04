import streamlit as stl
from datetime import datetime
from db import conexao

ano_atual = datetime.now().year 
anos = list(range(1500, ano_atual + 1))

with stl.form("my_form"):
  titulo = stl.text_input('Título')
  autor = stl.text_input('Autor')
  editora = stl.text_input('Editora')
  ano = stl.selectbox("Ano de lançamento: ",reversed(anos))
  categoria = stl.text_input('Categoria')
  isbn = stl.text_input('Código ISBN')

  enviar = stl.form_submit_button("Cadastar")
  if(enviar):
    # stl.write(f'Título: {titulo}')
    # stl.write(f'Autor: {autor}')
    # stl.write(f'Editora: {editora}')
    # stl.write(f'Ano de lançamento: {ano}')
    # stl.write(f'Categoria: {categoria}')
    # stl.write(f'ISBN: {isbn}')
    if all([titulo, autor, editora, ano, categoria, isbn]):
      cursor = conexao.cursor()

      cursor.execute("""
        INSERT INTO livros (titulo, autor, editora, ano, categoria, isbn) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (titulo, autor, editora, ano, categoria, isbn)
      )
      conexao.commit()

      stl.write("Livro cadastrado com sucesso!")

    else: 
      stl.write("Preencha todos os campos!")

#stl.write("Fora do formulário")

#enviar para o banco de dados:
