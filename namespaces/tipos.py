import this

a = 5


def f(a=3):
    b = 4
    print(globals())
    print(locals())
    print(a)


#f()


class A:
    a = 8
    a+=1
    print(a)
    print(globals())
    print(locals())
    pass