import numpy
import math
from xlrd import open_workbook

step_count=0

print("      # Mini-Batch Stochastic Gradient Descent #\n")
print("Orientation: 1.True output --> Y\n             2.Input --> X (x1,x2,..)\n",
      "            3.Learning Rate --> @ (alternative for 'Alpha')\n")
print("Program Output: 1.Error/Cost At Every step\n                2.Updated Theta Value By Step\n",
      "               3.Total Num Of Step To Get Into Below 10% Error\n"
      ,"               4.Satisfying Final Hypothiesis\n")



while(1):

    if(step_count==0):

        wb = open_workbook('MBSGD.xlsx')

        for sheet in wb.sheets():
            num_inp_sample = sheet.nrows
            num_inp_prmtr = sheet.ncols
        print(num_inp_prmtr,"  <--col , row-->  ",num_inp_sample)

        inp_array = numpy.zeros(shape=(num_inp_sample, num_inp_prmtr + 1))

        for i in range(num_inp_sample):

            for j in range(num_inp_prmtr):
                value = (sheet.cell(i,j).value)
                inp_array[i][j] = value

        #print("\nLearning Rate: ",end="")
        #learning_rate = eval(input())
        learning_rate = 0.001
        step_count = 1
        thetas = numpy.zeros(shape=(num_inp_prmtr))

    error=0

    for i in range(0,num_inp_sample):
        error += math.pow(inp_array[i][num_inp_prmtr]-inp_array[i][num_inp_prmtr-1],2)
    error = error/2
    print("\n\n        # Step "+str(step_count),"# \n Error: ",error)

    if (error < 10):
        print("\nSatisfying Hypothesis Found At Step", step_count-1)
        print("\n1.Try With Different Learning rate:\n2.Exit")
        option = int(input())
        if (option == 1):
            learning_rate = eval(input());
            step_count = 0;
        if (option == 2):
            break;
    step_count += 1
    for i in range(0,thetas.__len__()):
        true_out_minus_hyp_intox_j_i = 0
        for j in range(0,num_inp_sample):
            if(i==0):
                true_out_minus_hyp_intox_j_i += (inp_array[j][num_inp_prmtr-1]-inp_array[j][num_inp_prmtr])*1;
            else:
                true_out_minus_hyp_intox_j_i += (inp_array[j][num_inp_prmtr-1] - inp_array[j][num_inp_prmtr])*inp_array[j][i-1]
        thetas[i] = thetas[i]+learning_rate*true_out_minus_hyp_intox_j_i
        print(" theta"+str(i)+" --> "+str(thetas[i]))
    print("")
    print(thetas)
    # hypothesis output calculation
    for i in range(0,num_inp_sample):
        for j in range(0,thetas.__len__()):
            if(j==0):
             #   print(inp_array[i][num_inp_prmtr+1],"  ",thetas[j]," ",j)
                inp_array[i][num_inp_prmtr] += 1*thetas[j];
            else:
             #   print(inp_array[i][num_inp_prmtr + 1], "  ", thetas[j], " ", j," ",inp_array[i][j-1])
                inp_array[i][num_inp_prmtr] += inp_array[i][j-1]* thetas[j];
        print(" h("+str(i)+")= ",inp_array[i][num_inp_prmtr])




