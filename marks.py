import matplotlib.pyplot as plt

students_marks=["sanjay", "Rahul,","Karan", "Ramesh", "Ajay", "Sartaj,", "Priya"]
students_marks=[35, 50, 20, 45, 25, 40, 25, 40]

marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)

def line_chart_of_students_and_marks():
    plt.plot(students_names, students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students names")
    plt.ylabel("Students Marks")
    plt.show()

line_chart_of_students_and_marks()

# bar chart
def percentange_bar_chart():
    plt.bar(students_names, marks_perc)
    plt.title("Students' Percentange Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student percentage")
    plt.show()

percentange_bar_chart()