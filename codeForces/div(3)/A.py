import sys

def solve():
    # Reading input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    
    results = []
    for _ in range(t):
        n = int(input_data[pointer])
        s = input_data[pointer + 1]
        pointer += 2
        
        stack = []
        
        for char in s:
            # Agar stack khali nahi hai aur top element current char ke barabar hai
            if stack and stack[-1] == char:
                stack.pop() # Match mil gaya, dono ko '*' bana diya
            else:
                stack.append(char) # Match nahi mila, stack mein daal do
        
        
        
        # Agar stack khali hai to YES, warna NO
        if not stack:
            results.append("YES")
        else:
            results.append("NO")
            
    print("\n".join(results))

if __name__ == "__main__":
    solve()