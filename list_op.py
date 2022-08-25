def find_max(a):
    b=0
    for i in a:
        if i>b:
            b = i
    return b
    
def find_sum(a):
    b = 0
    for i in a:
        b = b + i
    return b
    
def find_mult(a):
    b = 1
    for i in a:
        b = b*i
    return b
    
def str_rev(a):
    n_str =""
    for j in range(len(a)-1,-1,-1):
        n_str = n_str + a[j]
    return n_str
    
def get_even(a):
    ls = []
    for i in a:
        if i%2 == 0:
            ls.append(i)
    return ls

def unique_(a):
    b =[]
    for i in a:
        if i in b:
            pass
        else:
            b.append(i)
    return b

lst = []
n = int(input("Enter number of integers : "))
for i in range(n):
    inp = int(input("Enter "+str(i+1)+" Element : "))
    lst.append(inp)
print("\n")
print("Max number : ",find_max(lst))
print("Sum of numbers : ",find_sum(lst))
print("multiplication of numbers : ",find_mult(lst))
un_lst = unique_(lst)
print("Unique Numbers from list : ",un_lst)
print("Even Numbers from list : ",get_even(un_lst))

str_inp = input("\nEnter String : ")
rev_str = str_rev(str_inp)
print("Reversed String : ",rev_str)
if str_inp == rev_str:
    print("\nGiven String is Pallindrome")
else:
    print("\nGiven String is not Pallindrome")