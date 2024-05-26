import sqlite3

def conectar_db():
    conn = sqlite3.connect('incidentes.db')
    return conn

def crear_tabla():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS incidentes (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def agregar_incidente(titulo, descripcion, fecha):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO incidentes (titulo, descripcion, fecha) VALUES (?, ?, ?)',
                   (titulo, descripcion, fecha))
    conn.commit()
    conn.close()

def ver_incidentes():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM incidentes')
    incidentes = cursor.fetchall()
    conn.close()
    return incidentes

def buscar_incidente_por_titulo(titulo):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM incidentes WHERE titulo = ?', (titulo,))
    incidentes = cursor.fetchall()
    conn.close()
    return incidentes

def menu():
    print("Bienvenido al sistema de registro de incidentes")
    while True:
        print("\nOpciones:")
        print("1. Agregar incidente")
        print("2. Ver incidentes")
        print("3. Buscar incidente por título")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            titulo = input("Ingrese el título del incidente: ")
            descripcion = input("Ingrese la descripción del incidente: ")
            fecha = input("Ingrese la fecha del incidente (YYYY-MM-DD): ")
            agregar_incidente(titulo, descripcion, fecha)
            print("Incidente agregado exitosamente.")
        elif opcion == '2':
            incidentes = ver_incidentes()
            print("\nListado de Incidentes:")
            for inc in incidentes:
                print(f"ID: {inc[0]}, Título: {inc[1]}, Descripción: {inc[2]}, Fecha: {inc[3]}")
        elif opcion == '3':
            titulo = input("Ingrese el título del incidente a buscar: ")
            incidentes = buscar_incidente_por_titulo(titulo)
            print("\nIncidentes encontrados:")
            for inc in incidentes:
                print(f"ID: {inc[0]}, Título: {inc[1]}, Descripción: {inc[2]}, Fecha: {inc[3]}")
        elif opcion == '4':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

if __name__ == '__main__':
    crear_tabla()
    menu()