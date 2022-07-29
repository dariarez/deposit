n = int(input('введіть розмір вкладу: '))
years = int(input('на який термін робите вклад? : '))

def bank(n, years):
    for i in range(years):
        n = n*(1/10)+n
    return(n)


print(bank(n, years))



