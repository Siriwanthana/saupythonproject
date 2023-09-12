#Funtion 1 : no parameter/no return
def funcA( ) :
    print('AAA')
    #funcB( ) ไม่ควรเรียงฟังก์ชันกันไปมา
    print('BBB')
    #No return คือไม่มีคำสั่ง return

def funcB() :
    print(123)
    funcA( )

funcA()
funcB()
funcB()
funcA()
