
def main():
    N = int(input())
    students = []
    for i in range(N):
        name = input()
        mark = float(input())
        students.append([name, mark])
    
    students.sort(key=lambda student: (student[1], student[0]))
    l = []
    for i in students:
        l.append(i[1])
    l1 = list(set(l))
    l1.sort()
    
    for s in [student for student in students if student[1] == l1[1]]:
        print(s[0])
    
if __name__ == '__main__':
    main()
