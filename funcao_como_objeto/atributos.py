def dobro(x):
    return x * 2

dobro2 = lambda x : x*2

print(dobro.__name__)
print()
print(dobro.__module__)
print()

for p in dir(dobro):
    print(p)

    