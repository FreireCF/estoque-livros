from db import conexao

cursor = conexao.cursor();

cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTO_INCREMENT, 
        titulo VARCHAR(50) NOT NULL,
        autor VARCHAR(50) NOT NULL,
        editora VARCHAR(50) NOT NULL,
        ano SMALLINT NOT NULL,
        categoria VARCHAR(50) NOT NULL,
        isbn VARCHAR(13) NOT NULL);
    """
)

conexao.commit()