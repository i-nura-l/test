# 1- Which type of data can be used while creating a series object in pandas?
# Lists, Tuples, and Dictionaries, Strings, Boolean Values, and Datetime Objects and other.

# 2- Create a series having the month's number as data and assign name as their index values?
import pandas as pd
import numpy as np
def ex2():
    month_series = pd.Series(
        ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'],
        index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    )
    print(month_series, '\n')
#ex2()

#3-Write a program to create a series object using the dictionary which store the number of students in fresh batch groups ( MatMIE, Mat DAIS, COMIE, COMEC)?
def ex3():
    students = {
        "MatMIE": 30,
        "MatDAIS": 29,
        "COMIE": 60,
        "COMEC": 55
    }
    series = pd.Series(students)
    print(series)
#ex3()

# 4-  Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
def ex4():
    exam_data = {
        'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df =  pd.DataFrame(exam_data, index=labels)
    print(df)
#ex4()

# 5- Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
def ex5():
    exam_data = {
        'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df = pd.DataFrame(exam_data, index=labels)
    chosen= df[df['attempts']>2]
    print(chosen)

#ex5()