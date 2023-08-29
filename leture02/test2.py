#ต่อข้อมูลหลายๆ ประเภทเข้าด้วยกัน
#ใช้ ,
score = 500
print('Hello...',20,True,658,75,10/2,"Hi...",score)
#ใช้
print('Hello...'+str(20)+str(true)+str(658.75)+str(10/2)+"Hi..."+str(score))
#ใช้ เมธอด format
print('Hello...{}{}{}{} Hi...{}'.format(20,True,658.75,10/2,score))
#ใช้ f-string
print(f'Hello... {20} {True} {658.75} {10/2} Hi...{score}')
#ใช้ modular operatr %
print('Hello... %d %f %s Hi...' % (20, 17.5 , "SAU"))
