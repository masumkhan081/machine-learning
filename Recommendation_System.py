from asyncore import dispatcher
import openpyxl as px
from xlrd import open_workbook
import numpy
import math



wb = open_workbook('RS.xlsx')

print("\n  Note: \"No Rating\" Is Equivalent To -1\n       0 is valid rating")

for sheet in wb.sheets():

    num_of_user = sheet.nrows
    num_of_item = sheet.ncols
    input_array = numpy.zeros(shape=(num_of_user, num_of_item))
    print(num_of_user," <- row col ->  ",num_of_item)

    for row in range( num_of_user):

        for col in range(num_of_item):
            value = (sheet.cell(row, col).value)
            try:
                value = float(value)
            except:
                input_array[row][col] = 0
                continue;
            input_array[row][col] =  value

inp = numpy.zeros(shape=(num_of_user,num_of_item))
print("Row Input From Sheet:\n")

for i in range(num_of_user):
    print("U"+str(i+1),end=":  " )
    for j in range(num_of_item):
        print(input_array[i][j],end="    ")
        inp[i][j] = input_array[i][j]
    print()

user_identifier = 65;

print("\nRecommendation For Which User: ", end="( ")
for i in range(num_of_user):
    print(i+1, end="/")
print(")")

user_to_be_recomended = int(input())-1
#print(user_to_be_recomended);



print("     # Jaccard Distance Formula # \n")

distances = [];
for i in range(num_of_user):
    total = 0;
    match = 0;
    if (i == user_to_be_recomended):
        continue;
    for j in range(num_of_item):
        if ((input_array[i][j] != 0) and (input_array[user_to_be_recomended][j] != 0)):
            match += 1;
            #print(input_array[i][j],"  ? ",input_array[user_to_be_recomended][j],"  ",i,"  ",j,"  ",user_to_be_recomended)
        if ((input_array[i][j] != 0) or (input_array[user_to_be_recomended][j] != 0)):
            total += 1;
            #print(input_array[i][j], "  # ", input_array[user_to_be_recomended][j], "  ", i, "  ", j, "  ",user_to_be_recomended)
    distances.append([((total - match) / total), i]);

    print("(U"+str(user_to_be_recomended+1),", U"+str(i+1),"):  ", distances[distances.__len__() - 1][0])


temp = 1000

for i in range(0, distances.__len__()):  # finding least distance and with whome
    if (distances[i][0] < temp):
        temp = distances[i][0];
        temp2 = distances[i][1];

print("\n\nAs Jaccard Distance Suggest\n Result: U"+str(user_to_be_recomended+1),"  Have Lowest Dist. With U"+str(temp2+1))

#  COSINE SIMILARITY PART BEGINGS FROM BELOW ON GIVEN INPUT .

print("\n\n      # Cosine Similarity Measure #\n")

distances.clear();
for i in range(0, num_of_user):

    total = 0;
    temp, temp2 = 0, 0;
    if (i == user_to_be_recomended):
        continue;
    for j in range(0, num_of_item):
        temp += input_array[i][j] * input_array[i][j];   #  A Square
        temp2 += input_array[user_to_be_recomended][j] * input_array[user_to_be_recomended][j]   # B Square
        if (input_array[i][j] != 0 and input_array[user_to_be_recomended][j] != 0):
            total += input_array[i][j] * input_array[user_to_be_recomended][j];

    distances.append([total / math.sqrt(temp * temp2), i]);    # List of similarity With It's related index
    print("Cosine( U"+str(user_to_be_recomended+1), ", U"+str(i+1),"): ",distances[distances.__len__() - 1][0])

temp = -1000;

for i in range(0, distances.__len__()):
    if (distances[i][0] > temp):
        temp = distances[i][0];
        temp2 = distances[i][1];

print("\n\n     --> As Cosine Similarity Suggest\n  User U"+str(user_to_be_recomended+1)
      + "\' Have Most Similarity With U" + str(temp2+1) + "\'\n")


# 00000000000000000000000000000000000000(((Normalize Rating + Cosine)))0000000000000000000000000000000000000000000000000



print("\n\n      #Normalize Rating + Cosine Similarity")
distances.clear();
for i in range(0,num_of_user):
    total=0;
    temp=0
    for j in range(0,num_of_item):
        if(input_array[i][j]!=0):
            total+=input_array[i][j]
            temp+=1
    temp = total / temp;   #    finding   average
   # print(">>>>>>>   ",temp)
    for j in range(0,num_of_item):
        if(input_array[i][j]!=0):
            input_array[i][j]-=temp    #    SUBSTRACTING THE AVERAGE FROM PARTICULAR VALUE


print("Normalized Utility Matrix:     *** 4")

for i in range(num_of_user):
    print()
    for j in range(num_of_item):
        print(input_array[i][j],end="   ")
print("\n\n")

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

    distances.append([total / math.sqrt(temp * temp2), i]);
    print("Cosine( U"+ str(user_to_be_recomended+1),", U"+str(i+1),"): ",distances[distances.__len__() - 1][0])

temp = -10000;

for i in range(0, distances.__len__()):
    if (distances[i][0] > temp):
        temp = distances[i][0];
        temp2 = distances[i][1];

print("\n\n--> Cosine Similarity After Normalize Rating Suggest\n  User U" + str(user_to_be_recomended+1)
          + " Have Most Similarity With U" + str(temp2+1) + "\'\n")

# 00000000000000000000000000000000000000(((Rounding + Cosine)))0000000000000000000000000000000000000000000000000


print("\n     # Rounding Data + Cosine Similarity #\n")

for i in range(num_of_user):
    print()
    for j in range(num_of_item):
        print(inp[i][j],end="   ")
print()

print("\n Least/Lowest Value For Rounding 1:", end=" ")
lower_limit = int(input())
print("")
for i in range(0, num_of_user):
    for j in range(0, num_of_item):
        if (inp[i][j] < lower_limit):
            inp[i][j] = 0;
        else:
            inp[i][j] = 1;
print("Rounded Utility Matrix:     *** ")
for i in range(num_of_user):
    print()
    for j in range(num_of_item):
        print(inp[i][j],end="   ")
print()

distances.clear();
for i in range(0,num_of_user):
    total = 0;
    temp, temp2 = 0, 0;
    if (i == user_to_be_recomended):
        continue;
    for j in range(0, num_of_item):
        temp += inp[i][j] * inp[i][j];
        temp2 += inp[user_to_be_recomended][j] * inp[user_to_be_recomended][j]
        if (inp[i][j] == 1 and inp[user_to_be_recomended][j] == 1):
            total += 1;
    try:
        distances.append([(total / math.sqrt(temp * temp2)), i]);
    except:
        continue;
    print("Cosine(", chr(65 + user_to_be_recomended), ",", chr(65 + i), "): ",
          distances[distances.__len__() - 1][0])
temp = -1000;
for i in range(0, distances.__len__()):
    if (distances[i][0] > temp):
        temp = distances[i][0];
        temp2 = distances[i][1];

print("\n\nCosine Similarity On Binary Utility Matrix Suggest\n    User \'" + chr(65 + user_to_be_recomended)
      + "\' Have Most Similarity With \'" + chr(65 + temp2) + "\'\n")

# 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

