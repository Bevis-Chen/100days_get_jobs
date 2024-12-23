# 100 days practice 
# Go to python!!
# JobS!!!

# Day2 語言元素
# 練習1：華氏溫度轉換為攝氏溫度。
# _F = eval(input("輸入華氏溫度 : "))
# _C = (_F - 32) / 1.8
# print("華氏溫度: ", _F,  "\n攝氏溫度: ", _C)

# 練習2：輸入圓的半徑計算計算周長和麵積。
# r = eval(input("輸入圓的半徑: "))
# perimeter = 2 * r * 3.14159
# area = r * r *3.14159
# print("周長是: ", perimeter, "\n", "面積是: ", area)

# 練習3：輸入年份判斷是不是閏年。
    # 公元年份非4的倍數，為365天平年。
    # 公元年份為4的倍數但非100的倍數，為366天閏年。
    # 公元年份為100的倍數但非400的倍數（1700年、1800年及1900年）為平年。
    # 公元年份為400的倍數（1600年及2000年）為閏年。
# yr = eval(input("輸入年分: "))
# if (yr % 4 == 0 and yr % 100 !=0) or (yr % 400 == 0 and yr % 100 ==0) :
#     print(yr, "是閏年")
# else:
#     print(yr, "不是閏年")

# Day3 分支結構
# 練習1：英制單位英寸與公制單位釐米互換。
# try:
#     value = eval(input("輸入數字: "))
#     unit = input("輸入單位: ")
#     if (unit == "inch") or (unit == "英吋"):
#         print("{} 英吋(inch) = {} 釐米(cm)".format(value, round(value/2.54, 2)))
#     elif (unit == "cm") or (unit == "釐米"):
#         print("{} 釐米(cm) = {} 英吋(inch)".format(value, round(value*2.54, 2)))
#     else:
#         print("輸入異常!")
# except Exception as e:
#     print(e)

# 練習3：輸入三條邊長，如果能構成三角形就計算周長和麵積。

# a = eval(input("輸入邊長(a): "))
# b = eval(input("輸入邊長(b): "))
# c = eval(input("輸入邊長(c): "))

# if (a + b >= c) or (a + c >= b) or (b + c >= a):
#     perimeter = a + b + c
#     s = perimeter / 2
#     area =  (s * (s-a) * (s - b) * (s - c)) * 0.5
#     print("周長: {}, 面積: {}".format(perimeter, round(area, 2)))
# else:
#     print("條件不符合三角形")

# Day 5 構造程式邏輯
# 1. 尋找水仙花數。
# 說明：水仙花數也被稱為超完全數字不變數、自戀數、自冪數、阿姆斯特朗數，
# 它是一個3位數，該數字每個位上數字的立方之和正好等於它本身，
# 例如：$1^3 + 5^3+ 3^3=153$。

for i in range(100, 1000):
    str_i = str(i)
    a = eval(str_i[0])
    b = eval(str_i[1])
    c = eval(str_i[2])
    # print(c, type(c))
    if i == (a**3 + b**3 + c**3):
        print(i)  
