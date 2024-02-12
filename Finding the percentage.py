if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
  #storing score of queried name
    query_scores = student_marks[query_name]
    A=sum(query_scores)/len(query_scores)#average = sum(score)/len 
    print(format(A,".2f"))#as need to print 2 number after decimal
