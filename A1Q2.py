# CCIT4020 Introduction to Computer Programming
# Fall 2024
# A1Q2.py
#

# ----------------Student work starts -----------------------
# Modify this section, replace sName & sID with your own
sName = "Chan Siu Ming"
sID = "20207878"
print(f"CCIT4020 ICP A1Q2 completed by\nStudent Name: {sName}; Student ID: {sID}\n")
#----------------------------------------------------------------------------------------
# Add your code to implement Section C Question 2
# 1. 创建一个变量，存储姓氏和学号
last_name = "Chan 20232245"

# 2. 请求用户输入一个不超过20个字符的简短消息
message = input("Enter a message of 20 chars or less:")

if len(message) > 20:
    print("太长了，需要更短的消息！")
    exit(0)

# 3. 将简短消息与姓氏和学号连接起来
full_message = f"{last_name} {message}"

# 4. 设置字段宽度为60
field_width = 60

# 根据新字符串的长度决定对齐方式
if len(full_message) <= 20:
    # 居中显示
    print(f"{full_message:^{field_width}}")
elif len(full_message) <= 40:
    # 左对齐显示
    print(f"{full_message:<{field_width}}")
else:
    # 右对齐显示
    print(f"{full_message:>{field_width}}")



# -------------- Student work ends --------------------------







