import math  

def main():
    A = int(input("enter A:"))
    B = int(input("enter B:"))
    result=pythag(A,B)
    print("The result is :", result)

def pythag(A,B):
    result_1=A**2 + B**2
    return math.isqrt(result_1)

main()
