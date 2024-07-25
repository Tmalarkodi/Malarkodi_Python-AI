import os
sample=input('Enter 1 to write,2 to read,3 to append')
if sample=='1':
    allfile=os.listdir()
    while True:
        print([x for x in allfile if x.endswith('.txt')])
        fname=input('Enter file name')
        if fname in allfile:
            print('file already exists')
        else:
            data=input('Enter data to write')
            file=open(fname,'w')
            file.write(data)
            file.close()
            break
elif sample=='2':
    allfile=os.listdir()
    while True:
        print([x for x in allfile if x.endswith('.txt')])
        fname=input('Enter file name')
        if fname in allfile:
            file=open(fname,'r')
            print(file.read())
            break
        else:
            print('No such file exists')
elif sample=='3':
    allfile=os.listdir()
    while True:
        print([x for x in allfile if x.endswith('.txt')])
        fname=input('Enter file name')
        if fname in allfile:
            data=input('Enter data to write')
            file=open(fname,'a')
            file.write(data)
            file.close()
            break
        else:
            print('No such file exists')

    
