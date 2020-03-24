def main():
    print('Enter a string :')
    x = input()
    # .split return a list 
    x = x.split();
    for i in x:
        # reverse it from last
        i=i[len(i)::-1] 
        print(i,end=" ")

main()