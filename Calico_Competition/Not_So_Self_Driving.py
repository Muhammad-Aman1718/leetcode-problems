# Not So Self-Driving


# Problem ID: car - Not So Self-Driving

T = int(input())  # number of test cases

for _ in range(T):
    v, x = input().split(":")  # split input like 23.15:98.34
    v = float(v)
    x = float(x)

    # Handle special case: if speed = 0
    if v == 0:
        print("SAFE")
        continue

    time = x / v  # time = distance / speed

    if time <= 1:
        print("SWERVE")
    elif time <= 5:
        print("BRAKE")
    else:
        print("SAFE")
