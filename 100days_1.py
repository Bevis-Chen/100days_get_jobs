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
# for i in range(100, 1000):
#     str_i = str(i)
#     a = eval(str_i[0])
#     b = eval(str_i[1])
#     c = eval(str_i[2])
#     # print(c, type(c))
#     if i == (a**3 + b**3 + c**3):
#         print(i)  

# ex :輸出100以內所有的素數。
# 說明：素數指的是隻能被1和自身整除的正整數（不包括1）。
# for num in range(2, 101):
#     time = 0
#     for i in range(1, num+1):
#         if (num % i) == 0:
#             time += 1
#     if time == 2:
#         print(num, end = ", ")
# print()

# ex: 找出10000以內的完美數。
# 說明：完美數又稱為完全數或完備數，
#      它的所有的真因子（即除了自身以外的因子）的和（即因子函式）恰好等於它本身。
#      例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美數。
#      完美數有很多神奇的特性，有興趣的可以自行了解。
# for num in range(2, 10000):
#     temp = 0
#     for i in range(1, num):
#         if (num % i) == 0:
#             temp += i
#     if num == temp:
#         print(temp)
        
#ex: 生成斐波那契數列的前20個數。
# 說明：斐波那契數列（Fibonacci sequence），
# 又稱黃金分割數列，是義大利數學家萊昂納多·斐波那契（Leonardoda Fibonacci）
# 在《計算之書》中提出一個在理想假設條件下兔子成長率的問題而引入的數列，
# 所以這個數列也被戲稱為"兔子數列"。
# 斐波那契數列的特點是數列的前兩個數都是1，
# 從第三個數開始，每個數都是它前面兩個數的和，
# 形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
# 斐波那契數列在現代物理、準晶體結構、化學等領域都有直接的應用。
# a = 1
# b = 1
# print(a, b, sep = ", ", end = ", ")
# for i in range(20 - 2):
#     c = a + b
#     print(c, end = ", ")
#     a = b
#     b = c

# Day 6 >> 函式和模組的使用
# 練習3：實現判斷一個數是不是素數的函式。

# def _prime_num(num):
#     time = 0
#     for i in range(1, num+1):
#         if (num % i) == 0:
#             time += 1
#     if time == 2:
#         print(num, "是個素數")
#     else:
#         print(num, "不是個素數")
# _prime_num(4)

# 練習1：實現計算求最大公約數和最小公倍數的函式。
# 最大公因數（英語：highest common factor，hcf）
# 最小公倍數（英語：least common multiple，lcm）

# def main():
#     def hcf(a, b):
#         for number in range(2, a+1):
#             if (a % number == 0) and (b % number == 0):
#                 print(number)
#     def lmc(a, b):
#         print(a * b)

#     hcf(6, 18)
#     print("----------------")
#     lmc(6, 18)

# if __name__ == "__main__":
#     main()

# Day07.字符串和常用数据结构.md
# s1 = "\"hello, world!\""
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2 ,end="")
# s1 = r'\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)

# ex01: 在螢幕上顯示跑馬燈文字。
# import os
# import time

# def main():
#     content = '北京歡迎你為你開天闢地…………'
#     while True:
#         # 清理螢幕上的輸出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]
# if __name__ == '__main__':
#     main()

# 練習2：設計一個函式產生指定長度的驗證碼，驗證碼由大小寫字母和數字構成。

