import openpyxl as px
import numpy
import math
from xlrd import open_workbook


print("\n      #K-Nearest Neighbour #\n ")

wb = open_workbook('KN.xlsx')

for sheet in wb.sheets():
    num_sample = sheet.nrows    # GETTING THE ROW NUM PRESENT IN THIS SHEET
    num_parameter = sheet.ncols    # GETTING NUM OF COL
    input_array = numpy.zeros(shape=(num_sample, num_parameter+1))   # NOW I KNOW WHAT SIZE OF 2D ARRAY SHOUL BE

    for i in range(0, num_sample):

        for j in range(0, num_parameter):
            input_array[i][j] = float((sheet.cell(i,j).value));      # READING INPUT FROM SHEET


print("Row Input From Sheet:\n")    #  PRINTING ROW INPUT SEPERATING ROW COL (IN 2D FORM )

for i in range(num_sample):
    print("U"+str(i+1),end=":   " )
    for j in range(num_parameter):
        print(input_array[i][j],end="    ")
    print()


wb = open_workbook('KN_test.xlsx')     # TO READ TEST CASES FOR WHICH WE NEED TO FIND NEARSET NEIGHBOUR

for sheet in wb.sheets():
    row = sheet.nrows
    col= sheet.ncols
    test = numpy.zeros(shape=(row, col + 1))
    for i in range(0, row):
        for j in range(0, col):
            test[i][j] = float((sheet.cell(i,j).value));
print("\nProgram Got These Test Case:\n")
for i in range(row):
    print("U"+str(i+1),end=":   " )
    for j in range(col):
        print(test[i][j],end="    ")
    print()

K = int(input("\nValue Of K: "))


for num_test in range(0,row):


    print("\nAll Distance & right Most Col. Value With Test_Case",(num_test+1),": \n")
    for i in range(0,num_sample):
        for j in range(0,num_parameter):
            input_array[i][num_parameter] += math.pow((input_array[i][j] - test[0][j]), 2);  # EUCLIDIAN DISTANCE

        input_array[i][num_parameter] = math.sqrt(input_array[i][num_parameter]);   # FINALLY DISTANCE GOES TO THE LAST COLOUM OF INP_ARRAY BY FOLLOWING IT'S RELATED ROW NUMBER/USER OF DATA SET
      #  print(input_array[i][num_parameter])
    #print("\n\n")

    k_picked_up = numpy.zeros(shape=(num_sample,2));  # NEW ARRAY TO OPERATE BUBBLE SORT EASILY

    for i in range(0,num_sample):
        k_picked_up[i][1] = input_array[i][num_parameter - 1];
        k_picked_up[i][0] = input_array[i][num_parameter];
        print(k_picked_up[i][0]," -->  ",k_picked_up[i][1])

    for i in range(0,num_sample):    # BUBBLE SORT FOR FINDING THE LOWEST DISTANCE
        for j in range(i+1,num_sample) :
            if (k_picked_up[i][0] > k_picked_up[j][0]):
                temp = k_picked_up[i][0];
                k_picked_up[i][0] = k_picked_up[j][0];
                k_picked_up[j][0] = temp;
                temp = k_picked_up[i][1]
                k_picked_up[i][1] = k_picked_up[j][1];
                k_picked_up[j][1] = temp

    print("\n      *.K_Nearest_N Suggest",K,"Nearest Neighbour:")
    print("\nFor Test Case",(num_test+1),", Value To Be Suggested At Left Side with It's Distance ")
    for i in range(0,K):
        print(k_picked_up[i][1] , " <<- " , k_picked_up[i][0]);
print("No More Cases In KN_test.xlsx")



