year = int(input())
if year % 4 == 0:
    if year>1949 and (year-1949)%10==0:
        print("Lucky year")
    elif year>1921 and (year-1921)%10==0:
        print("Lucky year")
    elif year%4==0 and year%100!=0 and year %400==0:
        print("Leap year")
else:
    print("Not a leap year")