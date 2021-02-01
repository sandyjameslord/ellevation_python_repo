# import the Pandas library
import pandas as pd

import timeit

# define the constant column headers required by ellevation's internal canonical template
ELLEVATION_HEADERS_PER_ASSESSMENT = [
    "NCESID", "StudentTestID", "StudentLocalID", "StudentGradeLevel", "TestDate", "TestName", "TestTypeName",
    "TestSubjectName", "TestGradeLevel", "Score1Label", "Score1Type", "Score1Value", "Score2Label", "Score2Type",
    "Score2Value", "Score3Label", "Score3Type", "Score3Value", "Score4Label", "Score4Type", "Score4Value",
]

ELLEVATION_HEADERS_ALL = [
    "NCESID", "StudentTestID", "StudentLocalID", "StudentGradeLevel", "ENG-TestDate", "ENG-TestName",
    "ENG-TestTypeName", "ENG-TestSubjectName", "ENG-TestGradeLevel", "ENG-Score1Label", "ENG-Score1Type",
    "ENG-Score1Value", "ENG-Score2Label", "ENG-Score2Type", "ENG-Score2Value", "ENG-Score3Label", "ENG-Score3Type",
    "ENG-Score3Value", "ENG-Score4Label", "ENG-Score4Type", "ENG-Score4Value", "MA-TestDate", "MA-TestName",
    "MA-TestTypeName", "MA-TestSubjectName", "MA-TestGradeLevel", "MA-Score1Label", "MA-Score1Type", "MA-Score1Value",
    "MA-Score2Label", "MA-Score2Type", "MA-Score2Value", "MA-Score3Label", "MA-Score3Type", "MA-Score3Value",
    "MA-Score4Label", "MA-Score4Type", "MA-Score4Value", "SCI-TestDate", "SCI-TestName",
    "SCI-TestTypeName", "SCI-TestSubjectName", "SCI-TestGradeLevel", "SCI-Score1Label", "SCI-Score1Type",
    "SCI-Score1Value", "SCI-Score2Label", "SCI-Score2Type", "SCI-Score2Value", "SCI-Score3Label", "SCI-Score3Type",
    "SCI-Score3Value", "SCI-Score4Label", "SCI-Score4Type", "SCI-Score4Value"
]

# define the constant column headers to access into the client's dataframe
CLIENT_HEADERS_TO_USE = [
    "district",  "sasid", "grade", "adminyear", "eperf2", "escaleds", "ecpi", "mperf2", "mscaleds", "mcpi", "sperf2",
    "sscaleds", "scpi"
]

# constant to map client's performance level values to ellevation's formatting of performance level values
PERFORMANCE_LEVEL_MAP = {
    "F": "1-F",
    "W": "2-W",
    "NI": "3-NI",
    "P": "4-P",
    "A": "5-A",
    "P+": "6-P+"
}

# reads client csv, returns a pandas dataframe of the client's data
def create_df_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df


def obtain_necessary_information_from_client_dataframe(client_df):
    end_data = []
    data_for_each_student = []

    i = 0
    while i < len(client_df):
    # while i < 4:
        for header in CLIENT_HEADERS_TO_USE:
            data_for_each_student.append(client_df.iloc[i][header])
        end_data.append((data_for_each_student))
        data_for_each_student = []
        i += 1

    #entire alignment per student, not for each assessment
    end_aligned_data = []
    aligned_data_for_each_student = []

    for student in end_data:
        # print("student:::", student)
        # append district aligned data to NCESID index
        if student[0] == "DistrictX":
            aligned_data_for_each_student.append("373737")
        else:
            aligned_data_for_each_student.append(student[0])

        #append sasid aligned data to StudentTestID index
        aligned_data_for_each_student.append(student[1])

        # append default 'missing' to StudentLocalID index
        aligned_data_for_each_student.append("missing")

        # append grade level to StudentGradeLevel index
        aligned_data_for_each_student.append(student[2])

        # append ENG test date to the ENG-TestDate index, default to April 1 for current year
        # print("STUDENT 3:::",student[3])
        aligned_data_for_each_student.append(f"4/1/{str(student[3])[-2:]}")

        # append MCAS to the ENG-TestName index
        aligned_data_for_each_student.append("MCAS")

        # append MCAS ELA to the ENG-TestTypeName index
        aligned_data_for_each_student.append("MCAS ELA")

        # append MCAS to the ENG-TestSubjectName index
        aligned_data_for_each_student.append("ELA")

        # append MCAS to the ENG-TestGradeLevel index
        aligned_data_for_each_student.append(student[2])

        # append MCAS to the ENG-Score1Label index
        aligned_data_for_each_student.append("Performance Level")

        # append MCAS to the ENG-Score1Type index
        aligned_data_for_each_student.append("Level")

        # append MCAS to the ENG-Score1Value index
        #convert provided value to ellevations defined value, if it exists
        if student[4] != " ":
            value = PERFORMANCE_LEVEL_MAP[student[4]]
            aligned_data_for_each_student.append(value)
        else:
            aligned_data_for_each_student.append("")

        # append MCAS to the ENG-Score2Label index
        aligned_data_for_each_student.append("Scaled Score")

        # append MCAS to the ENG-Score2Type index
        aligned_data_for_each_student.append("Scale")

        # append MCAS to the ENG-Score2Value index
        aligned_data_for_each_student.append(student[5])

        # append MCAS to the ENG-Score3Label index
        aligned_data_for_each_student.append("CPI")

        # append MCAS to the ENG-Score3Type index
        aligned_data_for_each_student.append("Scale")

        # append MCAS to the ENG-Score3Value index
        aligned_data_for_each_student.append(student[6])

        # append MCAS to the ENG-Score4Label index
        aligned_data_for_each_student.append("")

        # append MCAS to the ENG-Score4Type index
        aligned_data_for_each_student.append("")

        # append MCAS to the ENG-Score4Value index
        aligned_data_for_each_student.append("")

        #
        ###
        #



        # append MA test date to the MA-TestDate index, default to May 1 for current year
        # print("STUDENT 3:::",student[3])
        aligned_data_for_each_student.append(f"5/1/{str(student[3])[-2:]}")

        # append MCAS to the MA-TestName index
        aligned_data_for_each_student.append("MCAS")

        # append MCAS ELA to the MA-TestTypeName index
        aligned_data_for_each_student.append("MCAS Math")

        # append MCAS to the MA-TestSubjectName index
        aligned_data_for_each_student.append("Math")

        # append MCAS to the MA-TestGradeLevel index
        aligned_data_for_each_student.append(student[2])

        # append MCAS to the MA-Score1Label index
        aligned_data_for_each_student.append("Performance Level")

        # append MCAS to the MA-Score1Type index
        aligned_data_for_each_student.append("Level")

        # append MCAS to the MA-Score1Value index
        #convert provided value to ellevations defined value, if it exists
        if student[7] != " ":
            value = PERFORMANCE_LEVEL_MAP[student[7]]
            aligned_data_for_each_student.append(value)
        else:
            aligned_data_for_each_student.append("")

        # append MCAS to the MA-Score2Label index
        aligned_data_for_each_student.append("Scaled Score")

        # append MCAS to the MA-Score2Type index
        aligned_data_for_each_student.append("Scale")

        # append MCAS to the MA-Score2Value index
        aligned_data_for_each_student.append(student[8])

        # append MCAS to the MA-Score3Label index
        aligned_data_for_each_student.append("CPI")

        # append MCAS to the MA-Score3Type index
        aligned_data_for_each_student.append("Scale")

        # append MCAS to the MA-Score3Value index
        aligned_data_for_each_student.append(student[9])

        # append MCAS to the MA-Score4Label index
        aligned_data_for_each_student.append("")

        # append MCAS to the MA-Score4Type index
        aligned_data_for_each_student.append("")

        # append MCAS to the MA-Score4Value index
        aligned_data_for_each_student.append("")

        #
        ###
        #



        # append SCI test date to the SCI-TestDate index, default to May 1 for current year
        # print("STUDENT 3:::",student[3])
        aligned_data_for_each_student.append(f"6/1/{str(student[3])[-2:]}")

        # append MCAS to the SCI-TestName index
        aligned_data_for_each_student.append("MCAS")

        # append MCAS ELA to the SCI-TestTypeName index
        aligned_data_for_each_student.append("MCAS Science")

        # append MCAS to the SCI-TestSubjectName index
        aligned_data_for_each_student.append("Science")

        # append MCAS to the SCI-TestGradeLevel index
        aligned_data_for_each_student.append(student[2])

        # append MCAS to the SCI-Score1Label index
        aligned_data_for_each_student.append("Performance Level")

        # append MCAS to the SCI-Score1Type index
        aligned_data_for_each_student.append("Level")

        # append MCAS to the SCI-Score1Value index
        # convert provided value to ellevations defined value, if it exists
        if student[10] != " ":
            value = PERFORMANCE_LEVEL_MAP[student[10]]
            aligned_data_for_each_student.append(value)
        else:
            aligned_data_for_each_student.append("")
        # append MCAS to the SCI-Score2Label index
        aligned_data_for_each_student.append("Scaled Score")

        # append MCAS to the SCI-Score2Type index
        aligned_data_for_each_student.append("Scale")

        # append MCAS to the SCI-Score2Value index
        aligned_data_for_each_student.append(student[11])

        # append MCAS to the SCI-Score3Label index
        aligned_data_for_each_student.append("CPI")

        # append MCAS to the SCI-Score3Type index
        aligned_data_for_each_student.append("Scale")

        # append MCAS to the SCI-Score3Value index
        aligned_data_for_each_student.append(student[12])

        # append MCAS to the SCI-Score4Label index
        aligned_data_for_each_student.append("")

        # append MCAS to the SCI-Score4Type index
        aligned_data_for_each_student.append("")

        # append MCAS to the SCI-Score4Value index
        aligned_data_for_each_student.append("")

        end_aligned_data.append(aligned_data_for_each_student)
        aligned_data_for_each_student = []

    return end_aligned_data


def turn_filtered_data_into_records(filtered_data):
    records = []
    for student in filtered_data:
        tests_taken = [False, False, False]
        if student[14] != " ":
            tests_taken[0] = True
        if student[31] != " ":
            tests_taken[1] = True
        if student[48] != " ":
            tests_taken[2] = True
        for idx, test_taken in enumerate(tests_taken):
            if idx == 0 and test_taken:
                ENG_test_data = []
                j = 0
                while j < 21:
                    ENG_test_data.append(student[j])
                    j += 1
                records.append(ENG_test_data)
                # record = create_new_ellevation_data_frame()
                # record.append(ENG_test_data)
            # records.append(record)
            if idx == 1 and test_taken:
                MA_test_data = []
                j = 0
                while j < 21:
                    if j < 4:
                        MA_test_data.append(student[j])
                    else:
                        k = j + 17
                        MA_test_data.append((student[k]))
                    j += 1
                records.append(MA_test_data)
                # record = create_new_ellevation_data_frame()
                # record.append(MA_test_data)
                # records.append(record)
            if idx == 2 and test_taken:
                SCI_test_data = []
                j = 0
                while j < 21:
                    if j < 4:
                        SCI_test_data.append(student[j])
                    else:
                        k = j + 34
                        SCI_test_data.append((student[k]))
                    j += 1
                records.append(SCI_test_data)
                # record = create_new_ellevation_data_frame()
                # record.append(SCI_test_data)
                # records.append(record)
    return records


def turn_records_into_data_frame(records):
    df = pd.DataFrame(
        records,
        # index=list(range(0, len(records))),
        columns=ELLEVATION_HEADERS_PER_ASSESSMENT
    )
    return df


def create_csv_from_data_frame(data_frame):
    csv_file = data_frame.to_csv(r'ellevation.csv', index=False)

# organize main
def main():
    # initialize dataframe with client supplied information
    client_df = create_df_from_csv("./DI Data Challenge (Post zoom activity)/sample-mcas.csv")

    # process client dataframe into an array of values with filtered data ready for ellevation's canonical template
    filtered_data = obtain_necessary_information_from_client_dataframe(client_df)

    # create an array of values for each test taken
    records = turn_filtered_data_into_records(filtered_data)

    # converted_data_frame
    data_frame = turn_records_into_data_frame(records)

    create_csv_from_data_frame(data_frame)



print("time to process csv(2672x212) into csv(6053x20):", timeit.timeit(main, number=1))

# main()

