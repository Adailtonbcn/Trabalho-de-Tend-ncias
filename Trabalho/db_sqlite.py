import sqlite3

DB_NAME = "dados.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cidades (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, estado TEXT)''')
    conn.commit()
    conn.close()

def add_cidade_estado(nome, estado):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO cidades (nome, estado) VALUES (?, ?)", (nome, estado))
    conn.commit()
    conn.close()

def get_cidades():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT nome FROM cidades")
    cidades = c.fetchall()
    conn.close()
    return cidades
