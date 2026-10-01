def ordenar_eventos(eventos, expresion=False):
    if expresion:
        return sorted(eventos, key=str.lower, reverse=True)
    else:
        return sorted(eventos, key=str.lower)

eventos = ["kermes", "concurso de comida", "reunion del concejo municipal", "avenida siempre viva"]
print(ordenar_eventos(eventos))          
print(ordenar_eventos(eventos, False))   
print(ordenar_eventos(eventos, True))    
print(ordenar_eventos(eventos, 3 > 2))   
print(ordenar_eventos(eventos, 3 < 2))
