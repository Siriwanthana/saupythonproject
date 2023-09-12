#คำนวนเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน แล้วคำนวนและแสดงเงินที่จะแชรืกันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชั่น ขอ 2 ฟังก์ชั่น
#cast/conversation
#cast/conversation-ำๅ
#รับค่าข้อมูล
def inputMoneyPerrson() :
    money = float(input ('ป้อนเงิน : ') )
    person = int(input('ป้อนคน : ') )
    return money,person

#คำนวน แล้วแสดงผลออกมา
def calAndShareMoneyShare(money, person) :  
    #เงิน ขอทศนิยม 2 ตำแหน่ง แชรืกันขอเป็นเลขจำนวนเต็มปัดขึ้น
    print(f'จำนวนเงิน {money} บาท คน {person} คน แชร์กันคนละ {money/person} บาท')
    print("จำนวนเงิน","%.2f" % money, "บาท คน",person,"คน แชร์คนละ", round(money/person),"บาท" )
    print("จำนวนเงิน"+"+str"("%.2f" % money) +""+"คน แชร์คนละ"+""+str(round(money)))
    print("จำนวนเงิน {} บาท คน {} คน แชร์คนละ {} บาท " .format("%.2f"%money,person,round(money,person)))
    print("จำนวนเงิน %s บาท คน %s คน แชร์คนละ %s บาท " %("%.2f"%money,person,round(money/person))) 

money, person = inputMoneyPerrson( )

calAndShareMoneyShare( money, person)