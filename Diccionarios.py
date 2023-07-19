planeta = { # creacion de un diccionario llamado planet
    'nombre': 'Tierra',
    'lunas': 1
}

planeta.update({'nombre':'Marte'})

print(planeta.get('nombre'))