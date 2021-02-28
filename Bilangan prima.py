batas_awal = 1
batas_akhir = 19
print("Bilangan prima",batas_awal,"sampai",batas_akhir,":") 
for bilangan in range(batas_awal,batas_akhir + 1): 
    if bilangan > 1: 
        for i in range(2,bilangan): 
            if (bilangan % i) == 0: 
                break 
        else: 
            print(bilangan) 