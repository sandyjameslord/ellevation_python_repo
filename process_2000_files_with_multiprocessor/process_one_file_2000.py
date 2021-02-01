"""
Author: Sandy Lord
Date: January 31, 2021
Purpose: To align data and create output for the Ellevation Data Challenge: Standardized Test Score File Processing.
This file is imported by process_2000_files_multi.
"""

# import the Pandas library
import pandas as pd

# define the constant column headers required by ellevation's internal canonical template, PER ONE ASSESSMENT
ELLEVATION_HEADERS_PER_ASSESSMENT = [
    "NCESID", "StudentTestID", "StudentLocalID", "StudentGradeLevel", "TestDate", "TestName", "TestTypeName",
    "TestSubjectName", "TestGradeLevel", "Score1Label", "Score1Type", "Score1Value", "Score2Label", "Score2Type",
    "Score2Value", "Score3Label", "Score3Type", "Score3Value", "Score4Label", "Score4Type", "Score4Value",
]

# define the constants used for extrapolating all values an individual student's record may show
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


def create_df_from_csv(csv_file):
    """reads client csv, returns a pandas dataframe of the client's data"""
    df = pd.read_csv(csv_file)
    return df


def align_single_student(student):
    """Reads data on a single student and aligns it to ELLEVATION_HEADERS_ALL"""

    # initialize an empty list to house the data for an individual student
    aligned_data_for_each_student = []


    # now take a 'student' and align each data point individually

    # append a default of 373737 if NCESID is DistrictX, otherwise set to value of 'district'
    if student[0] == "DistrictX":
        aligned_data_for_each_student.append("373737")
    else:
        aligned_data_for_each_student.append(student[0])

    # append value of 'sasid' to StudentTestID index
    aligned_data_for_each_student.append(student[1])

    # append default 'missing' to StudentLocalID index
    aligned_data_for_each_student.append("missing")

    # append value of 'grade' to StudentGradeLevel index
    aligned_data_for_each_student.append(student[2])

    # using the 'adminyear' value, append value of ENG test date to the ENG-TestDate index, default to April 1 for current year
    aligned_data_for_each_student.append(f"4/1/{str(student[3])[-2:]}")

    # append 'MCAS' to the ENG-TestName index
    aligned_data_for_each_student.append("MCAS")

    # append 'MCAS ELA' to the ENG-TestTypeName index
    aligned_data_for_each_student.append("MCAS ELA")

    # append 'ELA' to the ENG-TestSubjectName index
    aligned_data_for_each_student.append("ELA")

    # append value of 'grade' to the ENG-TestGradeLevel index
    aligned_data_for_each_student.append(student[2])

    # append 'Performance Level' to the ENG-Score1Label index
    aligned_data_for_each_student.append("Performance Level")

    # append 'Level' to the ENG-Score1Type index
    aligned_data_for_each_student.append("Level")

    # append converted 'eperf2' value to the ENG-Score1Value index
    # convert provided value to ellevation defined value, if it exists
    if student[4] != " ":
        value = PERFORMANCE_LEVEL_MAP[student[4]]
        aligned_data_for_each_student.append(value)
    else:
        aligned_data_for_each_student.append("")

    # append 'Scaled Score' to the ENG-Score2Label index
    aligned_data_for_each_student.append("Scaled Score")

    # append 'Scale' to the ENG-Score2Type index
    aligned_data_for_each_student.append("Scale")

    # append 'escaleds' to the ENG-Score2Value index
    aligned_data_for_each_student.append(student[5])

    # append 'CPI' to the ENG-Score3Label index
    aligned_data_for_each_student.append("CPI")

    # append 'Scale' to the ENG-Score3Type index
    aligned_data_for_each_student.append("Scale")

    # append 'ecpi' to the ENG-Score3Value index
    aligned_data_for_each_student.append(student[6])

    # append '' to the ENG-Score4Label index
    aligned_data_for_each_student.append("")

    # append '' to the ENG-Score4Type index
    aligned_data_for_each_student.append("")

    # append '' to the ENG-Score4Value index
    aligned_data_for_each_student.append("")

    # using the 'adminyear' value, append value of Math test date to the MA-TestDate index, default to May 1 for current year
    aligned_data_for_each_student.append(f"5/1/{str(student[3])[-2:]}")

    # append 'MCAS' to the MA-TestName index
    aligned_data_for_each_student.append("MCAS")

    # append 'MCAS Math' to the MA-TestTypeName index
    aligned_data_for_each_student.append("MCAS Math")

    # append Math to the MA-TestSubjectName index
    aligned_data_for_each_student.append("Math")

    # append value of 'grade' to the MA-TestGradeLevel index
    aligned_data_for_each_student.append(student[2])

    # append 'Performance Level' to the MA-Score1Label index
    aligned_data_for_each_student.append("Performance Level")

    # append 'Level' to the MA-Score1Type index
    aligned_data_for_each_student.append("Level")

    # append converted 'mperf2' value to the MA-Score1Value index
    # convert provided value to ellevation defined value, if it exists
    if student[7] != " ":
        value = PERFORMANCE_LEVEL_MAP[student[7]]
        aligned_data_for_each_student.append(value)
    else:
        aligned_data_for_each_student.append("")

    # append 'Scaled Score' to the MA-Score2Label index
    aligned_data_for_each_student.append("Scaled Score")

    # append 'Scale' to the MA-Score2Type index
    aligned_data_for_each_student.append("Scale")

    # append value of 'mscaleds' to the MA-Score2Value index
    aligned_data_for_each_student.append(student[8])

    # append 'CPI' to the MA-Score3Label index
    aligned_data_for_each_student.append("CPI")

    # append 'Scale to the MA-Score3Type index
    aligned_data_for_each_student.append("Scale")

    # append value of 'mcpi' to the MA-Score3Value index
    aligned_data_for_each_student.append(student[9])

    # append '' to the MA-Score4Label index
    aligned_data_for_each_student.append("")

    # append '' to the MA-Score4Type index
    aligned_data_for_each_student.append("")

    # append '' to the MA-Score4Value index
    aligned_data_for_each_student.append("")

    # using the 'adminyear' value, append value of Science test date to the SCI-TestDate index, default to May 1 for current year
    aligned_data_for_each_student.append(f"6/1/{str(student[3])[-2:]}")

    # append 'MCAS' to the SCI-TestName index
    aligned_data_for_each_student.append("MCAS")

    # append 'MCAS Science' to the SCI-TestTypeName index
    aligned_data_for_each_student.append("MCAS Science")

    # append Science to the SCI-TestSubjectName index
    aligned_data_for_each_student.append("Science")

    # append value of 'grade' to the SCI-TestGradeLevel index
    aligned_data_for_each_student.append(student[2])

    # append 'Performance Level' to the SCI-Score1Label index
    aligned_data_for_each_student.append("Performance Level")

    # append 'Level' to the SCI-Score1Type index
    aligned_data_for_each_student.append("Level")

    # append converted 'sperf2' value to the SCI-Score1Value index
    # convert provided value to ellevation defined value, if it exists
    if student[10] != " ":
        value = PERFORMANCE_LEVEL_MAP[student[10]]
        aligned_data_for_each_student.append(value)
    else:
        aligned_data_for_each_student.append("")

    # append 'Scaled Score' to the SCI-Score2Label index
    aligned_data_for_each_student.append("Scaled Score")

    # append 'Scale' to the SCI-Score2Type index
    aligned_data_for_each_student.append("Scale")

    # append 'sscaleds' value to the SCI-Score2Value index
    aligned_data_for_each_student.append(student[11])

    # append 'CPI' to the SCI-Score3Label index
    aligned_data_for_each_student.append("CPI")

    # append 'Scale' to the SCI-Score3Type index
    aligned_data_for_each_student.append("Scale")

    # append 'scpi' value to the SCI-Score3Value index
    aligned_data_for_each_student.append(student[12])

    # append '' to the SCI-Score4Label index
    aligned_data_for_each_student.append("")

    # append '' to the SCI-Score4Type index
    aligned_data_for_each_student.append("")

    # append '' to the SCI-Score4Value index
    aligned_data_for_each_student.append("")

    # return a properly aligned list of student information
    return aligned_data_for_each_student


def obtain_necessary_information_from_client_dataframe(client_df):
    """Take a data frame and line by line process it into the same shape as ELLEVATION_HEADERS_ALL"""

    # houses every student's data aligned to CLIENT_HEADERS_TO_USE
    end_data = []

    # houses a single student's data aligned to CLIENT_HEADERS_TO_USE
    data_for_each_student = []

    # initialize a counter
    i = 0

    # while the counter is less than the length of the client_df, append to data_for_each_student
    # each student's value of the header keys from CLIENT_HEADERS_TO_USE
    while i < len(client_df):
    # while i < 4:
        for header in CLIENT_HEADERS_TO_USE:
            data_for_each_student.append(client_df.iloc[i][header])
        end_data.append(data_for_each_student)
        data_for_each_student = []
        i += 1

    # end_aligned_data houses the records produced from sending each student's data in end_data to
    # the align_single_student(student) function.
    end_aligned_data = []

    # for each student in the data aligned to CLIENT_HEADERS_TO_USE
    for student in end_data:
        # align that student to ELLEVATION_HEADERS_ALL
        st = align_single_student(student)
        # append the data to return together
        end_aligned_data.append(st)

    return end_aligned_data


def turn_aligned_data_into_records(aligned_data):
    """Take a single student record aligned to ELLEVATION_HEADERS_ALL and create 1, 2, or 3
    records, depending on how many tests an individual student took."""

    # records will house every student record aligned with ELLEVATION_HEADERS_PER_ASSESSMENT.
    # This number will be between 1 and 3 times the total number of tests, again, depending on
    # how many individual tests were taken
    records = []

    # take the ELLEVATION_HEADERS_ALL aligned data for each student
    for student in aligned_data:
        # create a list of 3 flags to determine which tests a student took, ENG, Math, or Science
        tests_taken = [False, False, False]

        # to see if a student took the ENG test, check its escaleds value in ENG-Score2Value index.
        # If it's not the string " ", flag that the student took the test in tests_taken
        if student[14] != " ":
            tests_taken[0] = True

        # to see if a student took the Math test, check its mscaleds value in MA-Score2Value index.
        # If it's not the string " ", flag that the student took the test in tests_taken
        if student[31] != " ":
            tests_taken[1] = True

        # to see if a student took the Science test, check its sscaleds value in SCI-Score2Value index.
        # If it's not the string " ", flag that the student took the test in tests_taken
        if student[48] != " ":
            tests_taken[2] = True

        # iterate over tests_taken and bring the index along
        for idx, test_taken in enumerate(tests_taken):
            # if the index is 0 and test_taken == True, organize data for an individual English assessment
            # aligned to ELLEVATION_HEADERS_PER_ASSESSMENT
            if idx == 0 and test_taken:

                # initialize a list to house English assessment test data
                ENG_test_data = []

                # initialize a variable to iterate over the first 21 indices of a student. The first 21
                # indices of a student, aligned to ELLEVATION_HEADERS_FOR_ALL, are the same data that will
                # form the English test record
                j = 0
                while j < 21:
                    ENG_test_data.append(student[j])
                    j += 1
                records.append(ENG_test_data)

            # if the index is 1 and test_taken == True, organize data for an individual Math assessment
            # aligned to ELLEVATION_HEADERS_PER_ASSESSMENT
            if idx == 1 and test_taken:

                # initialize a list to house Math assessment test data
                MA_test_data = []

                # initialize a variable to iterate 21 times. The first 4 indices of a student,
                # aligned to ELLEVATION_HEADERS_FOR_ALL, are student information, and are appended to
                # the MA_test_data. Then, in order to skip over the potential data for ENG assessments,
                # initialize a new index variable 17 indices deeper.
                j = 0
                while j < 21:
                    if j < 4:
                        MA_test_data.append(student[j])
                    else:
                        k = j + 17
                        MA_test_data.append((student[k]))
                    j += 1
                records.append(MA_test_data)

            # if the index is 2 and test_taken == True, organize data for an individual Science assessment
            # aligned to ELLEVATION_HEADERS_PER_ASSESSMENT
            if idx == 2 and test_taken:

                # initialize a list to house Science assessment test data
                SCI_test_data = []

                # initialize a variable to iterate 21 times. The first 4 indices of a student,
                # aligned to ELLEVATION_HEADERS_FOR_ALL, are student information, and are appended to
                # the MA_test_data. Then, in order to skip over the potential data for ENG and MA assessments,
                # initialize a new index variable 34 indices deeper.
                j = 0
                while j < 21:
                    if j < 4:
                        SCI_test_data.append(student[j])
                    else:
                        k = j + 34
                        SCI_test_data.append((student[k]))
                    j += 1
                records.append(SCI_test_data)
    # return a list of lists representing all assessments taken
    return records


def turn_records_into_data_frame(records):
    """Take the list of lists representing all assessments taken and feed it to Pandas dataframe constructor.
    Return a single dataframe."""

    # initialize a single dataframe. Pass records as the data and ELLEVATION_HEADERS_PER_ASSESSMENT as the
    # column headers
    df = pd.DataFrame(
        records,
        columns=ELLEVATION_HEADERS_PER_ASSESSMENT
    )
    return df


def create_csv_from_data_frame(data_frame, index):
    """Use pandas .to_csv() function to create a csv file of the processed records. Name the new file with an
    index passed to it to have unique names."""

    # create the csv, choose to not include indices, as they are not necessary
    csv_file = data_frame.to_csv(fr'ellevation_result{index}.csv', index=False)


def process_one_client(client_provided_csv, index):

    """This is the main method. It uses the functionalities described above to process the data as required
    by the Data Challenge: Standardized Test Score File Processing."""

    # initialize dataframe with client supplied information
    client_df = create_df_from_csv(client_provided_csv)

    # process client dataframe into an array of values with aligned data ready for ellevation's canonical template
    aligned_data = obtain_necessary_information_from_client_dataframe(client_df)

    # create a record for each test taken
    records = turn_aligned_data_into_records(aligned_data)

    # converted_data_frame from the list of records
    data_frame = turn_records_into_data_frame(records)

    # create a csv for final output
    create_csv_from_data_frame(data_frame, index)


