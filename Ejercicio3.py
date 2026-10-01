def interrupciones_recursivo(a, b):
    if b == 1:
        return a
    return a + interrupciones_recursivo(a, b - 1)

print(interrupciones_recursivo(6, 4))  
print(interrupciones_recursivo(5, 1))  