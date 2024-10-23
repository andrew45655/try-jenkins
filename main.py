from cal import *

def main():
    '''
    add 2 values
    :return:
    '''
    result = input("enter 2 numbers with space to separate")
    a,b=result.split(' ')
    res=add2value(a,b)
    print(res)


if __name__=='__main__':
    main()
