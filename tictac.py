print('#'*10+'*'*10+'#'*10)
print("Who want to start the game first enter their name first and who want to choose the icon first enter their name after first player")
print("if you enter a position for a previously filled position them game will be stop with a warning")
print('#'*10+'*'*10+'#'*10)


patterns={1:'   |   |   ',2:'-----------'}
mylist=[1,1,1,2,1,1,1,2,1,1,1]
dict1={1:[1,1],2:[1,5],3:[1,9],4:[5,1],5:[5,5],6:[5,9],7:[9,1],8:[9,5],9:[9,9]}

mylist3=[]
for j in mylist:
    mylist3.append(list(patterns[j]))


firstp=input()
secondp=input()
mark2=input(secondp+": choose the mark x or o \n ")
p2=secondp+"__"+mark2+"  enter the position of block"
print("\n")
if mark2=='x':
    mark1='o'
else:
    mark1='x'
p1=firstp+"__"+mark1+"  enter the position of block"


i=1
mylist4=[]
mylist6=[]
mylist7=[]

while i!=10:
    if i%2==0:
        position_no=int(input(p2 +"\n"))
        mylist7.append(position_no)
        mark=mark2
        p=secondp
    else:
        position_no=int(input(p1 +"\n"))
        mylist6.append(position_no)
        mark=mark1
        p=firstp
    print("\n")
    
    if position_no in mylist4:
        print("\n")
        print("you choose wrong position")
        print("\n")
        break
    else:
        mylist4.append(position_no)
    
      
     
    #code for place the mark at specific position
    x=dict1[position_no][0]
    y=dict1[position_no][1]
    mylist3[x][y]= mark
    for j in range(11):
        line1="".join(mylist3[j])
        print(line1)

    if i>4:
        mylist=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        if i%2==0:
            mylist5=mylist7
        else:
            mylist5=mylist6
    
        for t in mylist:
            k=0
            for j in t:
                if j in mylist5:
                    k+=1
            if k==3:
                print(" congrats! --",p, "\n you are winner of this round.")
                i=9
        
        
    
    i+=1
    
    
