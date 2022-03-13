# Problem: 

def print_rangoli(size):
    alorder = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alorder = ''.join([i.lower() for i in alorder])
    string, width , side_l, side_str = alorder[:size], (size-1)*4+1, [], ''
    # top half
    for i in range(size-1):
        print((side_str + '-' + string[size-1-i] + '-' + side_str[::-1]).center(width,'-'))
        side_l.append(string[size-1-i])
        side_str = '-'.join(side_l)
    # middle
    if size == 1:
        print(string[0])
    else: print(side_str+'-'+string[0]+'-'+side_str[::-1]) 
    
    # lower
    for i in range(size-1):
        center_str = side_l.pop()
        side_str = '-'.join(side_l)
        print((side_str + '-' + center_str + '-' + side_str[::-1]).center(width,'-'))

n = int(input("Enter alphabet rangoli's size: "))
print_rangoli(n)