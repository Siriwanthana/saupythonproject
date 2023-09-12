#function 4 : have parameters/have returns
def dtil(a,b) :
    print(f'{a} ยกกำลัง {b} = {a**b}')
    return a**b 

def dti2( a,b,x,y) :
    return a + b + x + y + dtil(2,3), 'Wow Wow Wow'


x,y = dti2(2,4,6,8)

print(f'{x} ^_^ {y}')