def func(x,y=[]):
    y.append(x)//append
    return y
print(func(1))
print(func(2,[]))
print(func(3))
