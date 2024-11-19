n=1
sum=0
smallest=0.0000000000001

while True:
    term = 1 / (n ** 2)
    if smallest>term:
        quit()
    sum+=term
    n+=1
    print("the sum is ",sum)
