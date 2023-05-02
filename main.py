
from time import time
import math
from random import randint


will_plot = True
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    while(1):
        print("ERROR: Precisa instalar modulo pra plotar: pip install matplotlib")
        i = input("Continuar sem plotar? [y/n]")
        if i == "n":
            quit()
        elif i == "y":
            will_plot = False
            break


temposLinear = []
temposSort = []


def geo_mean(lst):
    total_mult = 1
    for i in lst:
        total_mult *= i
    return total_mult ** (1/len(lst))


def getLista(size):
    L = []
    for count in range(size):
        n = randint(0,100000)
        L.append(n)
    return L


def bubblesort(list):
    # algorithm taken from https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    return list


def get_median(a):
    bubblesort(a)
    index = len(a)//2
    return a[index]


def LinearSelection(A, k): # precisa funcionar com floats repetidos
    aux_lst = A.copy()
    median_list = []
    len_5_list = []
    aux = 0
    distr_flag = 0

    if k < 0 or k > len(aux_lst):
        print("Invalid k")
        quit()

    if len(aux_lst) <= 1:
        return get_median(aux_lst)

    for i in aux_lst:
        len_5_list.append(i)
        aux += 1
        if aux % 5 == 0 or aux == len(aux_lst):

            median_list.append(get_median(len_5_list))
            len_5_list.clear()

    m = LinearSelection(median_list, len(median_list)//2)
    aux_lst.remove(m)

    R = []
    L = []

    for i in aux_lst:
        if (i < m) or (i == m and distr_flag == 0):
            L.append(i)
            distr_flag = 1
        elif (i > m) or (i == m and distr_flag == 1):
            R.append(i)
            distr_flag = 0

    tamL = len(L)
    if tamL == k - 1:
        return m
    elif tamL > k - 1:
        return LinearSelection(L,k)
    else:
        return LinearSelection(R,k - tamL - 1)


def SortSelection(A, k):
    Aord = bubblesort(A)
    return Aord[k-1]


def run_n_time(A,k):

    start_linear = time()
    result_linear = LinearSelection(A, k)
    end_linear = time()
    total_time_linear = round((end_linear - start_linear) * 1000, 2)
    temposLinear.append(total_time_linear)

    start_sort = time()
    result_sort = SortSelection(A, k)
    end_sort = time()
    total_time_sort = round((end_sort - start_sort) * 1000, 2)
    temposSort.append(total_time_sort)
    
    if result_linear != result_sort:
        print("Resultado Errado!")
        print("Error: n =", len(A))
        quit()

    return


def main():

    all_linear_means = []
    all_sort_means = []

    f = open("relatorio.txt", "w")

    for size in range(1000, 10001, 1000):
        s = "===  n = " + str(size) + "  ===\n"
        f.write(s)

        for j in range(10):

            s = "- Instancia = " + str(j + 1) + "\n"
            f.write(s)

            A = getLista(size)
            run_n_time(A,len(A)//2)
            
            s = "Tempo de exec. LinearSelection = " + str(temposLinear[j]) + "ms\n" + "Tempo de exec. SortSelect = " + str(temposSort[j]) + "ms\n\n"
            f.write(s)

        g_mean_linear = round(geo_mean(temposLinear), 2)
        g_mean_sort = round(geo_mean(temposSort), 2)

        all_linear_means.append(g_mean_linear)
        all_sort_means.append(g_mean_sort)

        s = "--- Media geometrica LinearSelection = " + str(g_mean_linear) + "ms\n" + "--- Media geometrica SortSelection = " + str(g_mean_sort) + "ms\n\n"
        f.write(s)

        temposSort.clear()
        temposLinear.clear()
    f.write("\n=======================================================================\n")
    f.write("Todas medias geometricas das execucoes da funcao LinearSelection: \n")
    for i in range(10):
        s = "n" + str((i+1)*1000) + " = " + str(all_linear_means[i]) + "\n"
        f.write(s)

    f.write("\n=======================================================================\n")
    f.write("Todas medias geometricas das execucoes da funcao SortSelection: \n")
    for i in range(10):
        s = "n" + str((i+1)*1000) + " = " + str(all_sort_means[i]) + "\n"
        f.write(s)

    #plot all_mean_lst
    if (will_plot == True):
        i = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

        plt.subplots(1, 3, figsize = (12, 5))
        
        plt.subplot(1, 3, 1).set_ylim(0,25)
        plt.subplot(1, 3, 1).set_box_aspect(1)

        plt.plot(i, all_linear_means, color = "blue", marker = 'o')
        plt.ylabel("Tempo em ms")
        plt.xlabel("Tamanho do vetor")
        plt.title("Media de tempos LinearSelection")

        plt.subplot(1, 3, 2).set_ylim(0, 7500)
        plt.subplot(1, 3, 2).set_box_aspect(1)
        plt.plot(i, all_sort_means, color = "red", marker = 'o')
        plt.xlabel("Tamanho do vetor")
        plt.ylabel("Tempo em ms")
        plt.title("Media de tempos SortSelection")
        
        plt.subplot(1, 3, 3).set_ylim(0, 7500)
        plt.subplot(1, 3, 3).set_box_aspect(1)
        plt.plot(i, all_sort_means, color = "red", marker = 'o')
        plt.plot(i, all_linear_means, color = "blue", marker = 'o')
        plt.xlabel("Tamanho do vetor")
        plt.ylabel("Tempo em ms")
        plt.title("Medias Sobrepostas")

        # fig, ax1 = plt.subplots()

        # ax1.set_xlabel('tamanho vetor')
        # ax1.set_ylabel('tempo em ms', color="blue")
        # ax1.plot(i, all_linear_means, color = "blue", marker = 'o')
        # ax1.tick_params(axis='y', labelcolor="blue")

        # ax2 = ax1.twinx()
        # ax2.set_ylabel('tempo em ms', color="red") 
        # ax2.plot(i, all_sort_means, color = "red", marker = 'o')
        # ax2.tick_params(axis='y', labelcolor="red")

        # fig.tight_layout()

        plt.show()
        

    f.close()

    return

main()