n = input("type a number:")
n = int(n) 
prime = True
for i in range(2,n):
        if (n %i) == 0:
            prime = False
 	break
if prime:
    print("its prime")
else:
    print("not prime")
