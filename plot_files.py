import matplotlib.pyplot as plt

import pandas as pd

ELLEVATION_HEADERS_PER_ASSESSMENT = [
    "NCESID", "StudentTestID", "StudentLocalID", "StudentGradeLevel", "TestDate", "TestName", "TestTypeName",
    "TestSubjectName", "TestGradeLevel", "Score1Label", "Score1Type", "Score1Value", "Score2Label", "Score2Type",
    "Score2Value", "Score3Label", "Score3Type", "Score3Value", "Score4Label", "Score4Type", "Score4Value",
]

def main():
    print("")
    print("Choose a format to view MCAS data in:")
    print("Make Histogram: Enter 1")
    print("Make Box Chart: Enter 2")
    print("Make simple terminal read-out: Enter 3")

    choice = int(input("Your choice: "))
    while choice not in [1,2,3]:
        choice = int(input("Choose 1, 2, or 3: "))
    if choice == 1:
        make_histogram()
    if choice == 2:
        make_box_and_whiskers_chart()
    if choice == 3:
        obtain_information_for_plotting()

    see_again = input("Would you like to see the data in another way? (y/n)")
    while see_again not in ["y", "n"]:
        see_again = input("Choose y or n: ")
    if see_again == "y":
        main()
    else:
        print("Have a great day.")

def make_histogram():
    one_file = pd.read_csv('ellevation_result.csv')

    a = plt.hist(one_file.Score2Value, bins=10)
    plt.ylabel("Number of Tests")
    plt.xlabel("Score on MCAS test")
    plt.show()

def make_box_and_whiskers_chart():
    one_file = pd.read_csv('ellevation_result.csv')

    plt.figure(figsize=(5,8))
    plt.style.use('default')

    ela = one_file.loc[one_file.TestTypeName == "MCAS ELA"]["Score2Value"]
    math = one_file.loc[one_file.TestTypeName == "MCAS Math"]["Score2Value"]
    sci = one_file.loc[one_file.TestTypeName == "MCAS Science"]["Score2Value"]

    box_plot = plt.boxplot(
        [ela, math, sci],
        labels=["ELA", "Math", "Science"],
        medianprops={'linewidth':2}
    )

    plt.title("MCAS Results per Standard")
    plt.ylabel("Scale Score")

    plt.show()


def obtain_information_for_plotting():
    one_file = pd.read_csv('ellevation_result.csv')
    i = 0

    all_tests_taken = []

    while i < len(one_file):

        student_id = one_file.iloc[i]['StudentTestID']
        grade_level = one_file.iloc[i]['StudentGradeLevel']
        test_taken = one_file.iloc[i]['TestTypeName']
        score_type = one_file.iloc[i]['Score2Label']
        score_value = one_file.iloc[i]['Score2Value']

        student_description = f"""*****
record {i}
StudentID: {student_id}
Grade Level: {grade_level}

Test Subject: {test_taken}
Scoring Type: {score_type}
Score Value: {score_value}
"""
        print(student_description)
        i += 1
        all_tests_taken.append([student_id, grade_level, test_taken, score_type, score_value])
    # return all_tests_taken

if __name__ == "__main__":
    main()


