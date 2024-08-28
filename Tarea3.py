Diccionario_modelos = {"nombre": "Clau", "edad":21, "ciudad": "Puebla"}
print(Diccionario_modelos)
# 1. pop()
edad = Diccionario_modelos.pop("edad")
print(f"pop: {edad}")  # Imprime 21
print(f"Diccionario después de pop: {Diccionario_modelos.pop}")

# 2. get()
ciudad = Diccionario_modelos.get("ciudad")
print(f"get: {ciudad}")
# 3. copy()
copia_diccionario = Diccionario_modelos.copy()
print(f"copy: {copia_diccionario}")

# 4. keys()
claves = Diccionario_modelos.keys()
print(f"keys: {claves}")

# 5. items()
items = Diccionario_modelos.items()
print(f"items: {items}")  #

# 6. clear()
Diccionario_modelos.clear()
print(f"clear: {Diccionario_modelos}")

# Reiniciando el diccionario
Diccionario_modelos = {"nombre": "Clau", "edad": 21, "ciudad": "Puebla"}
# 7. fromkeys()
nuevas_claves = ["a", "b", "c"]
nuevo_diccionario = dict.fromkeys(nuevas_claves, 0)
print(f"fromkeys: {nuevo_diccionario}")

# 8. popitem()
ultima_clave, ultimo_valor = Diccionario_modelos.popitem()
print(f"popitem: Clave - {ultima_clave}, Valor - {ultimo_valor}")
print(f"Diccionario después de popitem: {Diccionario_modelos}")

# 9. setdefault()
pais = Diccionario_modelos.setdefault("pais", "España")
print(f"setdefault: {pais}")
print(f"Diccionario después de setdefault: {Diccionario_modelos}")

# 10. update()
Diccionario_modelos.update({"edad": 22, "ciudad": "Querétaro"})
print(f"update: {Diccionario_modelos}")

# 11. values()
valores = Diccionario_modelos.values()
print(f"values: {valores}")