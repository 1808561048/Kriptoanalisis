def hitung_FPB(x, y):
    if x > y:
        terkecil = y
    else:
        terkecil = x
    for i in range(1, terkecil+1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i
            
    return fpb
bilangan1 = 98
bilangan2 = 62
print("FPB dari", bilangan1,"dan", bilangan2," =", hitung_FPB(bilangan1, bilangan2))