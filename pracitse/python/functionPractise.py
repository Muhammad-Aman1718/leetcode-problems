# *args example
def fun(*args: int) -> int:
    return sum(args)

print(fun(1, 2, 3, 4)) 
print(fun(5, 10, 15))   

# **kwargs example
def run(**kwargs: int) -> None:
    for k, val in kwargs.items():
        print(k, val)

run(a=1, b=2, c=3)