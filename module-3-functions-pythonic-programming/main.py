import random

from batch import batch_generator
from retry import retry
from timer import Timer


@retry(max_retries=3)
def prueba(nombre, edad):  # 👈 función con parámetros normales
    if random.random() < 0.7:
        raise Exception("Falló")
    return f"Hola {nombre}, tienes {edad} años"


# 🔹 Probando retry + *args y **kwargs
print("== RETRY ==")
print(prueba("Eduardo", edad=25))  # 👈 mezcla de args y kwargs


# 🔹 Probando generador
print("\n== BATCH ==")
for lote in batch_generator(list(range(10)), 3):
    print(lote)


# 🔹 Probando context manager
print("\n== TIMER ==")
with Timer():
    sum(range(10000000))
