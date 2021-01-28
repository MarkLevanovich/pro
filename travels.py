travels=open('travels.txt','r')

for i in travels:
    print(i)
    date=i[:9]
    l=i.split('/')
    print(date,l)

