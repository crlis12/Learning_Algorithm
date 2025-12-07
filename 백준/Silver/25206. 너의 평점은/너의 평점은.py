'''

전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

gpa = (credit * num_grade)의 합을 학점의 총합
'''
gpa = 0
credit_sum  = 0
for _ in range(20):
    
    subject, credit, grade = input().split()
    credit = float(credit)
    num_grade = 0.0
    
    if grade == "A+":
        num_grade = 4.5
    elif grade == "A0":
        num_grade = 4.0
    elif grade == "B+":
        num_grade = 3.5
    elif grade == "B0":
        num_grade = 3.0
    elif grade == "C+":
        num_grade = 2.5
    elif grade == "C0":
        num_grade = 2.0
    elif grade == "D+":
        num_grade = 1.5
    elif grade == "D0":
        num_grade = 1.0
    elif grade == "F":
        num_grade = 0.0
    elif grade == "P":
        continue  # P는 계산 제외

    # GPA 누적
    gpa += credit * num_grade
    credit_sum += credit
    
gpa = gpa / credit_sum if credit_sum != 0 else 0.0
print(f"{gpa:.6f}")  
    
