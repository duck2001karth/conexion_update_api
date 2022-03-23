import requests

"""
Crear un programa en python que consuma tu propia AP
I y que permita elegir un menu:
1. Mostrar datos (tareas)
2. Crear tarea
3. Salir
"""

def show_task():
    try:
        response = requests.get(url)
        print(response.status_code)
        return response.json()['tasks']
    except requests.exceptions.HTTPError as err:
        print("Error.")
        raise SystemExit(err)
    except requests.exceptions.ConnectionError as err:
        print(f"----- Error: {err}") 
    except requests.exceptions.JSONDecodeError as err:  
        print(f"----- Error de JSONDecodeError {err}") 
def create_task(task):
    try:
        response = requests.post(url, json={"name": task})
        print(response.status_code)
        return response.json()['tasks']
    except requests.exceptions.HTTPError as err:
        print("Error...")
        raise SystemExit(err)
    except requests.exceptions.ConnectionError as err:
        print(f"----- ERROR : {err}")
    except requests.exceptions.JSONDecodeError as err:
        print(f"----- ERROR JSONDecodeError: {err}")


url = 'http://127.0.0.1:5000/api/tasks'
op_salir = True

#Data = show_tasks( )

while op_salir:
    print("--- Menu de mi API ---")
    print("1. Mostrar tarea: ")
    print("2. Crear tarea: ")
    print("3. Salir del programa: ")
    print("\n")
    op = int(input("Escoga una opcion: \n"))
    #except ValueError as e:
     #  op = 0

    if(op == 1):
        data = show_task()
        for task in data:
            print(task)
    elif(op == 2):
        data = create_task(input("Ingrese la tarea:  \n"))
        for task in data:
            print(task) 
    elif(op == 3):
        op_salir = False
        print("Saliendo del programa...")  
    else:
         print("La opcion que ingresaste es invalida")                


