from db import conexao
from table import cursor

livros_add=[
    ("Noites brancas", "Fiódor Dostoiévski", "Principia", 1848, "Romance", "6550970288"),
    ("Duna", "Frank Herbert", "Aleph", 1965, "Ficção Científica", "857657313X"),
    ("O Hobbit", "J. R. R. Tolkien", "HarperCollins", 1937, "Fantasia", "8595084742"),
    ("O caminho dos Reis", "Brandon Sanderson", "Trama", 2010, "Fantasia", "6589132682"),
    ("A morte de Ivan Ilitch", "Liev Tolstói", "Principia", 1886, "Ficção filosófica", "8573263598"),
    ("Técnicas de invasão", "Bruno Fraga", "Labrador", 2019, "Ciência e Tecnologia", "6550440181" ),
    ("O estranho caso do cachorro morto", "Mark Haddon", "Record", 2003, "Mistério", "8501066257")
]

cursor.executemany("""INSERT INTO livros (titulo, autor, editora, ano, categoria, isbn) 
    VALUES (%s, %s, %s, %s, %s, %s)""", livros_add
    )

conexao.commit()