import time

print('helo wrold')
with open('file.txt' , 'r') as f:
    wrd=input("enter word")
    wrd_replace=input("enter word to replace")
    words=f.read()
    l=words.split()
    for i in range (len(l)):
        if l[i]==wrd:
            l[i]=wrd_replace
update_file=' '.join(l)
print(update_file)  


def overridemf():
    with open('file.txt' , 'w') as p:
        p.write(update_file)
    print('\nfiles override')
    print("exiting", end='',flush=True)
    for i in range(0,4):
        time.sleep(0.2)
        print('.', end='',flush=True)

 
ch=input("\n do you want to override the file.txt to the changed version (y/n) ")
if ch.lower()=='y':
    overridemf()
else:
    print("exiting", end='',flush=True)
    for i in range (0,4):
        print('.' , end='',flush=True)
