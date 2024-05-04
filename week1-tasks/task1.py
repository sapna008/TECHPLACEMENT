import random
def randomPaswordGenrator(n):
    cptltr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smltr="abcdefghijklmnopqrstuvwxyz"
    digit="0123456789"
    spclchrtr="!@#$%^&*()+:><?/|"
    if n<4:
        return "you have to take atleast 4 length for satisfying all requirement"
    else:
        temp=n//4
        a="".join(random.sample(cptltr,temp))
        b="".join(random.sample(smltr,temp))
        c="".join(random.sample(digit,temp))
        d="".join(random.sample(spclchrtr,(n-(3*temp))))
        print("YOUR RANDOM PASSWORD IS :")
        
    
    return a+b+c+d

length=int(input("Enter the length of password: "))
print(randomPaswordGenrator(length))
