def sub_two_numbers(a=1,b=2):
    result=a-b
    return result

def sum_two_numbers(a=1,b=2):
    result=a+b
    return result

def convert_currency(inr,rate):
    return inr*rate

def print_count_Down(n=10):
    if n==101:
        return
    print(n)
    b=n+1
    print_count_Down(b)

def print_test():
    print("Hi")