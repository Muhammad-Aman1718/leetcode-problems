# The Case of the Missing Book

# t = int(input())

# for _ in range(t):
#     name, n = input().split(" ")
#     print(type(name), type(n))

#     allNames: list[list[str]] = []

#     for i in range(int(n)):
#         line = input()
#         # names: list[str] = []
#         names = line.split(" ")
#         print("this is line  ", i, "  ", line)
#         print(names)
#         allNames.append([names[0], names[3]])

#     print(allNames)

#     for i in allNames:
#         firstName = i[0]
#         for n in range(int(n)):
#             if firstName != allNames[i][1]:


T = int(input())

for _ in range(T):
    line = input().strip()
    while line == "":  # handle blank lines
        line = input().strip()

    absent, n = line.split()
    n = int(n)

    returned_to = {}
    all_students = set()
    returned_books = set()

    for _ in range(n):
        record = input().strip()
        name, _, _, owner_part = record.split()
        owner = owner_part[:-2]  # remove "'s"
        returned_to[owner] = name
        all_students.add(name)
        all_students.add(owner)
        returned_books.add(owner)

    # Blank line between test cases (optional)
    if _ != T - 1:
        input()

    # Find the missing book owner
    missing_owner = (all_students - returned_books).pop()
    print(f"{absent} HAS {missing_owner}'s BOOK")
