def push(v):
    global Top
    global Max
    if Top==Max-1:
        print("overflow")
    else:
        Top=Top+1
        stack.append(v)
        print(stack)
def pop():
    global Top
    global Max
    if Top==-1:
        print("underflow")
    else:
        Top=Top-1
        return(stack.pop())
stack=[]
Top=-1
Max=5
while(1):
    print(".......MENU.......\n1.Push\n2.Pop\n3.Exit")
    choice=int(input("Enter choice"))
    if choice==1:
        v=int(input("Enter a value of push"))
        push(v)
    elif choice==2:
        print("popped element=",pop())
    elif choice==3:
        break
    else:
        print("Enter a valid choice")
