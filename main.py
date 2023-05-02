
from time import time
import math

from random import randint

temposLinear = []
temposSort = []

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
    index = math.floor(len(a)/2) #round up
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
    total_time_linear = round((end_linear - start_linear) * 1000)
    temposLinear.append(total_time_linear)

    start_sort = time()
    result_sort = SortSelection(A, k)
    end_sort = time()
    total_time_sort = round((end_sort - start_sort) * 1000)
    temposSort.append(total_time_sort)
    
    if result_linear == result_sort:
        print("Resultado Correto!")
    else:
        print("Resultado Errado!")

    return


def main():

#2

    for size in range(1000, 10001, 1000):

        for j in range(10):    
            A = getLista(size)
            run_n_time(A,len(A)//2)
        
        # printa elementos dos vetores de tempo
        # media geometrica dos vetores de tempo



    return

main()