# a=int(input("enter a:"))
# b=int(input("enter b"))
def safe_divide(a,b):
    try:
        result=a//b
        return result
    except ZeroDivisionError:
        print("can't divide by zero")
        # return None

       
    # except Exception as e:
    #     print(f"something went wrong{e}")
    #     return None
print(safe_divide(10, 2))    
print(safe_divide(10, 0))    
        