# gpa calculation
def main():
    courses = int(input("Enter the number of courses: "))
    def credit_hours(courses):
        total_credit_hours = 0
        for i in range(courses):
            credit = int(input(f"Enter credit hours for course {i + 1}: "))
            total_credit_hours += credit
        return total_credit_hours
    credit_hours_total = credit_hours(courses)

    





    course_marks = int(input("Enter your Marks: "))
    def calculate_gpa(marks):
        for i in range(courses):
            marks = int(input(f"Enter marks for course {i + 1}: "))
        if marks >= 80:
            return 'A : 4.0'
        elif marks >= 75:
            return 'B+ : 3.5'
        elif marks >= 70:
            return 'B : 3.0'
        elif marks >= 60:
            return 'C : 2.0'
        elif marks >= 50:
            return 'D : 1.0'
        else:
            return 'F : 0.0'

    gpa = calculate_gpa(course_marks)
    print(f"The calculated GPA is: {gpa}")
    print(f"Total credit hours: {credit_hours_total}")

main()