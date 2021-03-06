def faktorial(x): 
    if x == 1: 
        return 1 
    else: 
        return (x * faktorial(x-1)) 

bilangan = 10
print("Faktorial dari", bilangan, " adalah", faktorial(bilangan))