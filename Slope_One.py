import openpyxl as px
import numpy
import math
from xlrd import open_workbook


print("\n      #Item Based Similarity #\n ")

wb = open_workbook('Slope_One.xlsx')

for sheet in wb.sheets():
    num_of_user = sheet.nrows
    num_of_item = sheet.ncols
    input_array = numpy.zeros(shape=(num_of_user, num_of_item))

    for row in range( num_of_user):

        for col in range(num_of_item):
            value = (sheet.cell(row, col).value)
            if(value=="?"):
                 value= 63
            input_array[row][col] = value

print("Row Input From Sheet:\n")

for i in range(num_of_user):
    print("U",(i+1),end=":   " )
    for j in range(num_of_item):
        if(input_array[i][j]==63.0):
            print("?",end="    ")
        else:
            print(input_array[i][j],end="    ")
    print()


avg_rating = numpy.zeros(shape=(num_of_item, num_of_item))
row_col = numpy.zeros(shape=(100,2))
que_count=0
for col in range(num_of_item):
    sign=False
    for col2 in range(col+1,num_of_item):
        avg = 0
       # print(col, "       ?    ????? ",col2)
        for row in range(num_of_user):
            if(input_array[row][col]!=63.0 and input_array[row][col2]!=63.0):
               # print(input_array[row][col],"  ",input_array[row][col2])
                avg += input_array[row][col]-input_array[row][col2]
            elif (input_array[row][col] == 63.0 and sign==False):
                row_col[que_count][0] = int(row)
                row_col[que_count][1] = int(col)
                que_count += 1
                sign=True
              #  print(row,"  ????  ",col)

        avg_rating[col][col2]=avg/2
"""
for i in range(row_col.size):
    for j in range(2):
        print(int(row_col[i][j]))
"""
for i in range(num_of_user):
    if(input_array[i][num_of_item-1]==63.0):
        row_col[que_count][0] = i
        row_col[que_count][1] = num_of_item-1

        que_count+=1

     #   avg = avg/2
     #   print(avg)

factor_arr = []
sum=0

for i in range(que_count):
    factor = 0
    sum=0
    for j in range(num_of_item):

        if(input_array[int(row_col[i][0])][j]!=63.0):
            if(j<row_col[i][1]):
              #  rating_compared.append((input_array[int(row_col[i][0])][j]-avg_rating[j][int(row_col[i][1])])*2)
                sum += (input_array[int(row_col[i][0])][j]-avg_rating[j][int(row_col[i][1])])*2
             #   print(input_array[int(row_col[i][0])][j]," <<<<< ",avg_rating[j][int(row_col[i][1])])
            if (j > row_col[i][1]):

                sum+= (input_array[int(row_col[i][0])][j]+avg_rating[int(row_col[i][1])][j])*2
            factor+=2

    sum = sum/factor
    #print(input_array[int(row_col[i][0])][int(row_col[i][1])])
    input_array[int(row_col[i][0])][int(row_col[i][1])] = sum
    #print(row_col[i][0],"  rc ",row_col[i][1])
print("\nModified Input Arrray After Done implementing Slope One Algo")
for i in range(num_of_user):
    print()
    for j in range(num_of_item):
        print(input_array[i][j],end="   ")


print("\n\n     # Cosine Similarity Measure To Be Implemented #\n")

print("\nRecommendation For Which User: ", end="( ")
for i in range(num_of_user):
    print(i+1, end="/")
print(")")

user_to_be_recomended = int(input())-1


distances = []
distances.clear();
for i in range(0, num_of_user):

    total = 0;
    temp, temp2 = 0, 0;
    if (i == user_to_be_recomended):
        continue;
    for j in range(0, num_of_item):
        temp += input_array[i][j] * input_array[i][j];
        temp2 += input_array[user_to_be_recomended][j] * input_array[user_to_be_recomended][j]
        if (input_array[i][j] != 0 and input_array[user_to_be_recomended][j] != 0):
            total += input_array[i][j] * input_array[user_to_be_recomended][j];
    try:
        distances.append([total / math.sqrt(temp * temp2), i]);
    except:
        continue;
    print("Cosine( U" + str(user_to_be_recomended + 1), ", U" + str(i + 1), "): ",distances[distances.__len__() - 1][0])


temp = -1000;

for i in range(0, distances.__len__()):
    if (distances[i][0] > temp):
        temp = distances[i][0];
        temp2 = distances[i][1];

print("\n\n     --> As Cosine Similarity Suggest\n  User U" + str(user_to_be_recomended+1)
      + " Have Most Similarity With U" + str(temp2+1) + "\n")













