def donasconsumidas(a, b):
    total = 0
    for persona in range(b):
        total += a
    return total

print(donasconsumidas(3, 5))   
print(donasconsumidas(4, 1))   
print(donasconsumidas(2, 10))