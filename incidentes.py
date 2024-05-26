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

def eliminar_incidente(id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM incidentes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print("Incidente eliminado exitosamente.")

def editar_incidente(id, nuevo_titulo, nueva_descripcion, nueva_fecha):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE incidentes SET titulo = ?, descripcion = ?, fecha = ?
        WHERE id = ?
    ''', (nuevo_titulo, nueva_descripcion, nueva_fecha, id))
    conn.commit()
    conn.close()
    print("Incidente actualizado exitosamente.")

import csv

def exportar_incidentes():
    incidentes = ver_incidentes()
    with open('incidentes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Título', 'Descripción', 'Fecha'])
        for inc in incidentes:
            writer.writerow(inc)
    print("Incidentes exportados a CSV exitosamente.")


def menu():
    print("Bienvenido al sistema de registro de incidentes")
    while True:
        print("\nOpciones:")
        print("1. Agregar incidente")
        print("2. Ver incidentes")
        print("3. Buscar incidente por título")
        print("4. Eliminar incidente")
        print("5. Editar incidente")
        print("6. Exportar incidentes a CSV")
        print("7. Salir")
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
            id_incidente = int(input("Ingrese el ID del incidente a eliminar: "))
            eliminar_incidente(id_incidente)
        elif opcion == '5':
            id_incidente = int(input("Ingrese el ID del incidente a editar: "))
            nuevo_titulo = input("Ingrese el nuevo título del incidente: ")
            nueva_descripcion = input("Ingrese la nueva descripción del incidente: ")
            nueva_fecha = input("Ingrese la nueva fecha del incidente (YYYY-MM-DD): ")
            editar_incidente(id_incidente, nuevo_titulo, nueva_descripcion, nueva_fecha)
        elif opcion == '6':
            exportar_incidentes()
        elif opcion == '7':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

if __name__ == '__main__':
    crear_tabla()
    menu()