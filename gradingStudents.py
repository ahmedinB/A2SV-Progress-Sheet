
def gradingStudents(grades):
    # Write your code here
    for grade in grades:
        if grade <= 37:
            continue
        elif grade%5 >= 3:
            grades[grades.index(grade)]=5*(grade//5)+5
    
    return grades 
