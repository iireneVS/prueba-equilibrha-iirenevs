import csv
import pandas as pd

file_path = "empleados.csv"

def datos_trabajadores(file_path):
    try:
        # Lee el archivo CSV con csv.DictReader y maneja en caso de errores
        with open(file_path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, delimiter=';')
            return [row for row in reader]
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def mostrar_informacion(datos):
    # Suma por un lado hombres y por otro lado mujeres
    hombres = sum(1 for row in datos if row['sexo'] == 'H')
    mujeres = sum(1 for row in datos if row['sexo'] == 'M')

    # Suma total de hombres y mujeres
    total_empleados = hombres + mujeres

    print(f"\nResumen general:\nTotal de hombres: {hombres}\nTotal de mujeres: {mujeres}")
    print(f"Todos los empleados (hombres + mujeres): {total_empleados}")


    # Suma salarios de Empresa 1 y Centro CT2
    suma_salarios = sum(
        int(row['salario bruto anual']) for row in datos 
        if row['ID Empresa'] == '1' and row['ID Centro trabajo'] == 'CT2'
    )
    print(f"\nSuma de los salarios brutos anuales (Empresa 1, Centro CT2): {suma_salarios}")

    # Filtrado de  empleados con salario > 28000 y Empresa 2
    empleados_filtrados = [
        row for row in datos 
        if int(row['salario bruto anual']) > 28000 and row['ID Empresa'] == '2'
    ]

    # Muestra los empleados filtrados en tabla con Pandas
    print("\nListado de empleados que cumplen las condiciones:")
    if empleados_filtrados:
        # Modifica la lista de diccionarios a un dataframe de pandas para poder visualizarlo
        df = pd.DataFrame(empleados_filtrados)
        print()
        print(df[['id empleado', 'nombre', 'apellido1', 'apellido2', 'salario bruto anual', 'Nombre empresa']])
    else:
        print("No se encontraron empleados que cumplan con las condiciones.")

# Ejecuta el programa
datos = datos_trabajadores(file_path)

if datos is not None:
    mostrar_informacion(datos)
else:
    print("\n[ERROR] No se pudieron procesar los datos.")
