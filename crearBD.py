import sqlite3

conexion = sqlite3.connect('usuarios.db')

cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    password TEXT NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conexion.commit()

conexion.close()

print("Base de datos creada.")