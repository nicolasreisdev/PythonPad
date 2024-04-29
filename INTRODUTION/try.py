def verify(x, y):
    if y == 0:
        exception = ZeroDivisionError
    elif isinstance(y, int):    
        exception = ValueError
        



n = int(input())
for i in range(n):
    x = str(input())
    y = str(input())
    try:
        verify(x, y)
    except ZeroDivisionError as e:
        print("Error Code: ", e)
    except ValueError as e:
        print("Error Code: ", e)
        