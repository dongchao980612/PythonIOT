def f1(*x):
    for i in x:
        print(i)
def f2(x,y,*n):
    print("x,y:",x,y)
    for i in n:
        print(i)

if __name__ == '__main__':
    f1(1,'a',3,'b',5,'c')
    print("*"*20)
    f2(1,2,3,4,5,6,7)
    print("*"*20)
    f2(1,2)