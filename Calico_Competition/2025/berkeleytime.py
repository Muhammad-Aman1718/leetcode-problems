# berkeleytime

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 0:
        print("haha good one")
    elif n > 0 and n < 180:
        print("berkeley" * (n // 10) + "time")
    else:
        print("canceled")
