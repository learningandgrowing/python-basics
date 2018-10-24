N = int(input())
for name_grade in range(N):
    names = input()
    grades = float(input())

my_list = []
for name in names:
    for grade in range(grades):
        
        my_list.append([names,grades])
print(my_list)
