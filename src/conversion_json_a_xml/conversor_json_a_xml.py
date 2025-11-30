import json
import xmltodict

def convertir():
    try:

        with open("usuarios.json", "r") as archivo_json:
            datos_dict = json.load(archivo_json)

        xml_string = xmltodict.unparse(datos_dict, pretty=True)


        with open("usuarios.xml", "w") as archivo_xml:
            archivo_xml.write(xml_string)

        print("Conversión completada exitosamente.")

    except FileNotFoundError:
        print("*ERROR* Archivo no encontrado.")
    except json.JSONDecodeError:
        print("*ERROR* Problemas al analizar el archivo JSON.")
    except Exception as e:
        print(f"*ERROR* {e}.")

def main():
    convertir()

if __name__ == "__main__":
    main()
