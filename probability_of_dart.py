import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import pandas as pd



def prob_of_dart(sect1 , sect2, sect3 , sect4, sect5):
    area_sect1 = math.pi * (sect1**2)
    area_sect2 = math.pi * (sect2**2)
    area_sect3 = math.pi * (sect3**2)
    area_sect4 = math.pi * (sect4**2)
    total_area = math.pi * (sect5**2)

    prob_of_sect1 = area_sect1 / total_area
    prob_of_sect2 = area_sect2 / total_area
    prob_of_sect3 = area_sect3 / total_area
    prob_of_sect4 = area_sect4 / total_area

#calculating the probability of speciic sections

    area_sect2_sect1 = area_sect2 - area_sect1
    prob_sect2_sect1 = area_sect2_sect1 / total_area

    area_sect3_sect2 = area_sect3 - area_sect2
    prob_sect3_sect2 = area_sect3_sect2 / total_area

    area_sect4_sect3 = area_sect4 - area_sect3
    prob_sect4_sect3 = area_sect4_sect3 / total_area

    area_sect5_sect4 = total_area - area_sect4
    prob_sect5_sect4 = area_sect5_sect4 / total_area

    mean_probability_center = (prob_of_sect1 +prob_of_sect2 +prob_of_sect3 +prob_of_sect4) / 5

    mean_probability_ind = (prob_sect2_sect1 + prob_sect3_sect2 + prob_sect4_sect3+prob_sect5_sect4) / 5


# create table
    table1 = PrettyTable()
    table1.field_names = ["Sections", "Probability of Sections from Center (C)", "Mean Probability of C", "Probability of Actual Sections (A)",
    "Mean Probability of I" ] 

# add data to table
    table1.add_row(["Section 1", round(prob_of_sect1, 3), ' ', "NA", ' '])
    table1.add_row(["Section 2", round(prob_of_sect2, 3), round(mean_probability_center,3),  round(prob_sect2_sect1, 3), round(mean_probability_ind, 3)])
    table1.add_row(["Section 3", round(prob_of_sect3, 3) ,' ', round(prob_sect3_sect2, 3), ' '])
    table1.add_row(["Section 4", round(prob_of_sect4, 3) ,' ', round(prob_sect4_sect3,3), ' '])
    table1.add_row(["Section 5", "NA" , ' ', round(prob_sect5_sect4, 3), ' '])

#print the table 

    print(table1)
    print('\n')


    data = {"Probability of Sections from Center": [prob_of_sect1, prob_of_sect2, prob_of_sect3, prob_of_sect4, 0 ], 
    "Probability of Actual Sections" : [ 0 , prob_sect2_sect1,prob_sect3_sect2, prob_sect4_sect3, prob_sect5_sect4  ]}

    df = pd.DataFrame(data)

    std_of_C = df['Probability of Sections from Center'].std()
    median_of_C = df['Probability of Sections from Center'].median()


    std_of_A = df['Probability of Actual Sections'].std()
    median_of_A = df['Probability of Actual Sections'].median()

    table2 = PrettyTable()
    table2.field_names = ["Statistics", "Standard Deviation", "Median"]

#add data to table 
    table2.add_row(['Probability of Sections from Center', round(std_of_C, 3), round(median_of_C, 3)])
    table2.add_row(['Probability of Actual Sections', round(std_of_A, 3), round(median_of_A, 3)])

    print(table2)




#line chart to check the distribution of probabilities

    prob_sect_center = [prob_of_sect1 , prob_of_sect2, prob_of_sect3, prob_of_sect4]

    prob_ind_sect = [prob_sect2_sect1 , prob_sect3_sect2, prob_sect4_sect3 , prob_sect5_sect4]

    prob_sect_center_labels = ['Section 1' , 'Section 2', 'Section 3', 'Section 4']


    plt.plot( prob_sect_center_labels, prob_sect_center ,label='Probability of Sections from Center', linestyle='--', marker='o', color='r')
    plt.plot(prob_sect_center_labels, prob_ind_sect , label='Probability of Actual Sections', linestyle='--', marker='o', color='r')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("Line Plot")
    

sect1 = float(input('Enter the radius of Section 1: '))
sect2 = float(input('Enter the radius of Section 2: '))
sect3 = float(input('Enter the radius of Section 3: '))
sect4 = float(input('Enter the radius of Section 4: '))
sect5 = float(input('Enter the radius of Circular dart board: '))



result = prob_of_dart(sect1, sect2, sect3, sect4 , sect5)

user_request = input('Would you like to view graphical representation of probabilities (Y/N) ').lower()
if user_request == 'y':
    plt.show()
else:
    pass