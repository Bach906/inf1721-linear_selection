
from time import time
import math
from random import randint


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
    index = math.floor(len(a)/2) #round up
    return a[index - 1]


def LinearSelection(A, k): # precisa funcionar com floats repetidos
    aux_lst = A.copy()
    median_list = []
    distr_flag = 0
    len_5_list = []
    aux = 0

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

    m = LinearSelection(median_list, math.floor(len(median_list)/2))
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

    if k == len(L) + 1:
        return m
    elif k <= len(L):
        return LinearSelection(L, k)
    else: #elif k > len(L):
        return LinearSelection(R, k - len(L) - 1)


def SortSelection(A, k):
    Aord = bubblesort(A)
    return Aord[k-1]


def run_n_time(A):



    return

def main():
    A = []

    f = open("n2000.txt", "r")
    for line in f:
        i = int(line)
        A.append(i)


    k = 200

    start_linear = time()
    result_linear = LinearSelection(A, k)
    end_linear = time()
    total_time_linear = end_linear - start_linear



    start_sort = time()
    result_sort = SortSelection(A, k)
    end_sort = time()
    total_time_sort = end_sort - start_sort


    if result_linear == result_sort:
        print("Resultado Correto!")
    else:
        print(result_linear, result_sort)
        print("Resultado Errado!")

    # run_n_time(A)






    # print("tempo linear = ", total_time_linear)
    # print("tempo sort = ", total_time_sort)

    return

main()