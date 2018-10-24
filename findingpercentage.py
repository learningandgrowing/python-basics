if __name__ == '__main__':
    student_record =  {}
    for _ in range(int(input())):
        name, *marks= input().split()
        scores = list(map(float, marks))
        student_record[name] = scores
    query_name = input()
    
    if student_record.keys():
        average = sum(student_record[query_name])/3
        print('{:.2f}'.format(average))
    
    
    
