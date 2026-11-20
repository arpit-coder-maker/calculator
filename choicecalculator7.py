def sum(a,b):
    
    c=a+b
    return(c)
def diff(a,b):

    c=a-b
    return(c)



def multiply(a,b):

    c=a*b
    return(c)

def div(a,b):

    c=a/b
    return(c)

def rem(a,b):

    c=(a%b)
    return(c)

z= str(input("enter what operation to be performed : "))

x= float(input("enter 1st no. "))
y= float(input("enter 1st no. "))

if z=="+":
    print(sum(x,y))
elif z=="-":
    print(diff(x,y))

elif z=="*":
    print(multiply(x,y))
elif z=="/":
    if y==0:
        print("Are you serious bruh!")
    else:
        print(div(x,y))
else:
    print("calculator is not advanced")
