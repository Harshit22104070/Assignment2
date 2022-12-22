a=int(input("enter 1st side"))
b=int(input("enter 2nd side"))
c=int(input("emter 3rd side"))
if (a+b>c) and (b+c>a) and (c+a>b):
    print("Triangle is formed")
else:
    print("Triangle can't be formed")