from random import randint
def random():
    while True:
        n=str(randint(100,999))
        if not(n[0]==n[1] or n[1]==n[2] or n[0]==n[2]):
            return n

name=input("welcome to the cow and bulls game\\n please entre you name:")
print("hi",name)
chance=8 
bulls=0
cows=0
num=str(random())   
while chance>0:
    print("you have",chance,"chance left.")
    n=str(input("entre your guess:")) 
    if num==n:
        print("ereat! you can go hea.")
        break
    else:  
        for i in range(0,3):
            if n[i]==num[i]:
                bulls=bulls+1
            elif n[i] in num:
                 cows=cows+1   
        print("keep going.you have ",bulls,"bulls and",cows,"cows.")
        
        bulls=0
        cows=0
        chance=chance-1
        
print("the correct answer is ",num)                       