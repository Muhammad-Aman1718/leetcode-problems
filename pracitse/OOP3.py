
#tight bond O(1),Θ(n)
# 🧩 Example 1:
def get_first_element(arr: list[int]):
    return arr[0]

# 🧪 Mock input:
numbers = [10, 20, 30, 40]
print(get_first_element(numbers))



#tight bond O(1),Θ(n)
# 🧩 Example 2:
def check_even(num: int):
    if num % 2 == 0:
        return True
    else:
        return False

# 🧪 Mock input:
print(check_even(42))
print(check_even(17))




#tight bond O(1),Θ(n)
# 🧩 Example 3:
def swap(a: int, b: int):
    temp = a
    a = b
    b = temp
    return a, b

# 🧪 Mock input:
x, y = 5, 9
print(swap(x, y))



#tight bond o(1),Θ(n)
# 🧩 Example 4:
def add_two_numbers(a: int, b: int):
    return a + b

# 🧪 Mock input:
print(add_two_numbers(15, 25))




# upper bond o(n)
# 🧩 Example 5:
def find_max_of_three(a: int, b: int, c: int):
    return max(a, b, c)

# 🧪 Mock input:
print(find_max_of_three(12, 7, 19))




# upper bond o(n)
# 🧩 Example 6:
def print_elements(arr: list[int]):
    for item in arr:
        print(item)


# 🧪 Mock input:
data = [1, 2, 3, 4, 5]
print_elements(data)




# upper bond o(n)

# 🧩 Example 7:
def find_sum(arr: list[int]):
    total = 0
    for num in arr:
        total += num
    return total

# 🧪 Mock input:
numbers = [5, 10, 15, 20]
print(find_sum(numbers))



#upper bond o(n)
# 🧩 Example 8:
def find_element(arr: list[int], target: int):
    for num in arr:
        if num == target:
            return True
    return False

# 🧪 Mock input:
arr = [3, 6, 9, 12, 15]
print(find_element(arr, 9))
print(find_element(arr, 20))



#upper bond o(n)
# 🧩 Example 9:
def double_each(arr: list[int]):
    result: list[int] = []
    for num in arr:
        result.append(num * 2)
    return result

# 🧪 Mock input:
data = [1, 4, 7, 10]
print(double_each(data))



#upper bond o(n)
# 🧩 Example 10:
def count_positives(arr: list[int]):
    count = 0
    for num in arr:
        if num > 0:
            count += 1
    return count

# 🧪 Mock input:
nums = [-5, 3, 0, 7, -2, 9]
print(count_positives(nums))
