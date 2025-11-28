import xml.etree.ElementTree as ET
import json
import xmltodict

def convertir():
    try:
        with open("src/conversion_xml_a_json/usuarios.xml", "r") as archivo_xml:
            xml_string = archivo_xml.read()

            datos_dict = xmltodict.parse(xml_string)

        with open("src/conversion_xml_a_json/usuarios_ejercicio_externo.json", "w") as archivo: 
            json.dump(datos_dict, archivo, indent = 4)

    except FileNotFoundError:
        print("*ERROR* Archivo no encontrado.")
    except ET.ParseError:
        print("*ERROR* Problemas al analizar el archivo XML.")
    except Exception as e:
        print(f"*ERROR* {e}.")

def main():
    convertir()

if __name__ == "__main__":
    main()
