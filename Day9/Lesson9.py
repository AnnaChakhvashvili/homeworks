def reverse_arr():
    students = ["Ana","Mari","Lika","Nani"] 
    new_arr=[]
    i= len(students)
    while i > 0 :
        new_arr.append(students[i-1])
        i -= 1
    print(new_arr)

def compare_scores(p1_score,p2_score):
    if p1_score > p2_score:
        print("{} მეტია {}-ზე , {}-ით".format(p1_score,p2_score,p1_score-p1_score))
    elif p2_score >p1_score:
        print("{} მეტია {}-ზე , {}-ით".format(p1_score,p2_score,p1_score-p1_score))

def multiply(a,b):
    return a*b


    