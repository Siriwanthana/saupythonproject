#dtiworkshop01.py
#โปรแกรมคำนวนหาพื้นที่สามเหลี่ยม โดยรับค่าฐาน และสูงทางแป้นพิมพ์ และแสดงผลพื้นที่สามเหลี่ยมที่คำนวนได้ทางหน้าจอ

#วิเคราะห์
#มองหา feature การทำงานว่ามีอะไรบ้าง
#1. รับค่า ฐาน สูง
#2. คำนวนพื้นที่ และแสดงผลออกมา

def inputBaseHigh() :
    base = float(input('ป้อนฐาน :') )
    high = float(input('ป้อนสูง :') )
    return base,high
def calAndShowTriangleArea(base,high) :
    are = base * high / 2
    print(f'สามเหลี่ยมฐาน {base :.2f} สูง {high:.2f} มีพื้นที่ {are:.2f}')

print('-------------------------------')
print('--* Calculate ')