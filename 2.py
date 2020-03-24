def main():
    print('Enter a num :')
    # force int input
    x = int(input('Input : '))
    # 暫時把3，5固定
    a = 3
    b = 5
    count = 0
    for i in range(1,x+1):
        if (isThreeOrFive(i,a,b) == False) and (isAmB(i,a,b) == False):
            pass
        else :
            count += 1
            print(i,end=" ")
            
    print('\nOutput : ',count)

def isThreeOrFive(num,a,b):
    if num % a == 0 or num % b == 0 :
        return False
    else :
        return True

def isAmB(num,a,b):
    if a * b == num:
        return True
    else :
        return False

main()