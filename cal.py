
def add2value(a,b):
    try:
        if isinstance(a,str):
            a=float(a)
        if isinstance(b,str):
            b=float(b)
        return a+b
    except Exception as e:
        print(e)
        return None