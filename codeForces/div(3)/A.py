import sys

# Input lene ka fast tariqa
input = sys.stdin.read().split()
t = int(input[0])

for i in range(1, t + 1):
    x = int(input[i])
    
    # Hum different digit lengths (L) check karenge
    for L in range(1, 11):
    
        y = (10**L) - 1 - x
        
        # Check karein ke y positive hai aur uske digits ki length L hi hai
        if y > 0 and len(str(y)) == L:
            # Final check as per problem
            if (x * (10**L) + y) % (x + y) == 0:
                print(y)
                break