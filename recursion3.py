def sum_function(i,summ):
    if i<1:
        print(summ)
        return
    sum_function(i-1,summ+i)
print(sum_function(5,0))