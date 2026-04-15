import json
import re


def cargar_datos(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("❌ Archivo no encontrado")
        return []
    except json.JSONDecodeError:
        print("❌ JSON inválido")
        return []
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return []


def filtrar_mayores(datos):
    return [p for p in datos if p.get("edad", 0) >= 18]


def agrupar_por_ciudad(datos):
    resultado = {}
    for persona in datos:
        ciudad = persona.get("ciudad", "Desconocida")
        resultado.setdefault(ciudad, []).append(persona)
    return resultado


def validar_nombre(nombre):
    return bool(re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ]+$", nombre))


def procesar_persona(persona):
    match persona:
        case {"nombre": nombre, "edad": edad, "ciudad": ciudad} if validar_nombre(
            nombre
        ):
            return f"{nombre} ({edad}) - {ciudad}"
        case {"nombre": nombre}:
            return f"{nombre} (incompleto)"
        case _:
            return "Formato desconocido"


def main():
    ruta = "data.json"
    datos = cargar_datos(ruta)

    if not datos:
        print("No hay datos")
        return

    # LIST + DICT
    mayores = filtrar_mayores(datos)

    # SET (ciudades únicas)
    ciudades_unicas = {p.get("ciudad", "Desconocida") for p in datos}
    print("🌎 Ciudades únicas:", ciudades_unicas)

    # TUPLE (resumen)
    resumen = (len(datos), len(mayores))
    print("📊 Total / Mayores:", resumen)

    agrupados = agrupar_por_ciudad(mayores)

    print("\n📍 Personas mayores por ciudad:\n")

    # FOR
    for ciudad, personas in agrupados.items():
        print(f"🏙️ {ciudad}:")

        i = 0
        # WHILE
        while i < len(personas):
            p = personas[i]
            try:
                print(" -", procesar_persona(p))
            except Exception as e:
                print(f"⚠️ Error procesando: {e}")
            i += 1


if __name__ == "__main__":
    main()
