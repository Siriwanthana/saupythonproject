# คำสั่ง if + else + if
score = input('ป้อนคะแนน : ')
try :
    score = int(score)
    if score >= 80 :
        print('เกรด A')
    elif score >= 70 and score < 80 :
        print('เกรด B')
    elif score >= 60 and score < 70 :
        print('เกรด C')
    elif score >= 50 and score < 6 :
        print('เกรด D')
    else :
        print('เกรด F')
except ValueError :
    print('กรุณาป้อนเป็นตัวเลข')

print('____________________')
print('Created by DTI-SAu')