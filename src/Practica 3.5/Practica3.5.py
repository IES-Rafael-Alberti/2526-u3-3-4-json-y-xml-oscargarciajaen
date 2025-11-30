import xml.etree.ElementTree as ET
import os

def limpiar_pantala():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def inicializar_datos():

    origen = "datos_usuarios_orig.xml"
    destino = "datos_usuarios.xml"

    try:
        arbol = ET.parse(origen)
        arbol.write(destino, encoding="utf-8", xml_declaration=True)

        print(f"Datos inicializados desde '{origen}' a '{destino}'\n")

    except FileNotFoundError:
        print(f"ERROR El archivo origen '{origen}' no existe. No se realizó la copia.")

    except ET.ParseError:
        print(f"ERROR El archivo origen '{origen}' tiene un formato XML inválido.")

    except Exception as e:
        print(f"ERROR Problemas al cargar el XML: {e}")



def crear_arbol(nombre_raiz):
    raiz = ET.Element(nombre_raiz)
    arbol = ET.ElementTree(raiz)
    return arbol

def cargar_xml(nombre_fichero: str) -> ET.ElementTree:
    """
    Carga el contenido de un archivo XML.

    Args:
        nombre_fichero (str): Nombre del archivo XML.

    Returns:
        ET.ElementTree: Árbol del XML.
    """
    try:
        return ET.parse(nombre_fichero)

    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")

    except ET.ParseError:
        print("*ERROR* El archivo XML tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar el XML: {e}")

    return None


def guardar_xml(arbol: ET.ElementTree, nombre_fichero: str) -> bool:
    """
    Guarda un árbol XML en un archivo.

    Args:
        arbol (ET.ElementTree): Árbol XML.
        nombre_fichero (str): Nombre del archivo de salida.

    Returns:
        (bool): True si se guardó correctamente y False si se produjo algún problema.
    """
    try:
        arbol.write(nombre_fichero, encoding = "utf-8", xml_declaration = True)

        return True

    except FileNotFoundError:
        print(f"*ERROR* La ruta especificada '{nombre_fichero}' no existe.")

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except Exception as e:
        print(f"*ERROR* Problemas al guardar el archivo XML: {e}")

    return False


def actualizar_usuario(raiz: ET.Element, id_usuario: int, nueva_edad: int):
    """
    Actualiza la edad de un usuario dado su ID.

    Args:
        raiz (ET.Element): Nodo raíz del XML.
        id_usuario (int): ID del usuario a actualizar.
        nueva_edad (int): Nueva edad.
    """
    for usuario in raiz.findall("usuario"):
        if usuario.find("id").text == str(id_usuario):
            usuario.find("edad").text = str(nueva_edad)
            print(f"Usuario con ID {id_usuario} actualizado.")
            return

    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(raiz: ET.Element, nuevo_usuario: dict):
    """
    Inserta un nuevo usuario en el XML.

    Args:
        raiz (ET.Element): Nodo raíz del XML.
        nuevo_usuario (dict): Datos del nuevo usuario.
    """
    usuario = ET.SubElement(raiz, "usuario")
    ET.SubElement(usuario, "id").text = str(nuevo_usuario["id"])
    ET.SubElement(usuario, "nombre").text = nuevo_usuario["nombre"]
    ET.SubElement(usuario, "edad").text = str(nuevo_usuario["edad"])

    print(f"Usuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(raiz: ET.Element, id_usuario: int):
    """
    Elimina un usuario por su ID.

    Args:
        raiz (ET.Element): Nodo raíz del XML.
        id_usuario (int): ID del usuario a eliminar.
    """
    for usuario in raiz.findall("usuario"):
        if usuario.find("id").text == str(id_usuario):
            raiz.remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return

    print(f"Usuario con ID {id_usuario} no encontrado.")

def mostrar_datos(raiz: ET.Element):
    usuarios = raiz.findall('usuario')

    if not usuarios:
        print("ERROR No hay usuarios en el archivo XML.\n")
        return

    print("--- Contenido Actual del XML ---")

    for elemento in usuarios:
        id = elemento.find('id').text
        nombre = elemento.find('nombre').text
        edad = elemento.find('edad').text
    
        print(f"ID:  {id}, Nombre: {nombre}, Edad: {edad}")
        
    print("--- Fin del Contenido ---\n")

def main():
    limpiar_pantala()

    inicializar_datos()
    input("--- Fichero inicializado. Pulsa Enter para continuar ---")

    nombre_fichero = "datos_usuarios.xml"
    arbol = cargar_xml(nombre_fichero)

    if arbol is None:
        raiz = ET.Element("usuarios")
        arbol = ET.ElementTree(raiz)
    else:
        raiz = arbol.getroot()

    mostrar_datos(raiz)
    input("--- Pulsa Enter para continuar ---")
    limpiar_pantala()

    actualizar_usuario(raiz, id_usuario=1, nueva_edad=31)
    mostrar_datos(raiz)
    input("--- Pulsa Enter para continuar ---")
    limpiar_pantala()

    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(raiz, nuevo_usuario)
    mostrar_datos(raiz)
    input("--- Pulsa Enter para continuar ---")
    limpiar_pantala()

    eliminar_usuario(raiz, id_usuario=2)
    mostrar_datos(raiz)

    guardar_xml(arbol, nombre_fichero)

    print("Operaciones completadas. Archivo actualizado.\n")

if __name__ == "__main__":
    main()