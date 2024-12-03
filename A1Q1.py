# CCIT4020 Introduction to Computer Programming
# Fall 2024
# A1Q1.py
#
import math

# -----------------Section Starts ------------------------
# modify this section to import module(s) as needed


# ------------------Section Ends --------------------------

# ----------------Student work starts -----------------------
# Modify this section, replace sName & sID with your own
sName = "Chan Siu Ming"
sID = "20207878"
print(f"CCIT4020 ICP A1Q2 completed by\nStudent Name: {sName}; Student ID: {sID}")
# ------------------------------------------------------------
# Add your code to implement Section C Question 1

# 获取用户输入
try:
    radius = input("请输入圆的半径（正数）：")
    radius = float(radius)
    if radius < 0:
        print("Not positive number, try again!")
        exit(0)

    # 计算点状区域的面积
    area = (math.pi - (3 * math.sqrt(3) / 4)) * radius ** 2
    dotted_area =  round(area, 2)

    print(f"点状区域的面积为: {dotted_area:.2f}")
except ValueError:
            print("Wrong inputs!")








# -------------- Student work ends --------------------------







