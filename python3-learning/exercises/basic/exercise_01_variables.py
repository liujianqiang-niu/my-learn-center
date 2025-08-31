#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3 基础练习题 01：变量和数据类型
难度：初学者
完成时间：30-45分钟
"""

def exercise_instructions():
    """练习说明"""
    print("=" * 60)
    print("Python3 基础练习题 01：变量和数据类型")
    print("=" * 60)
    print("练习目标：")
    print("1. 掌握变量的定义和使用")
    print("2. 理解不同数据类型的特点")
    print("3. 学会类型转换")
    print("4. 练习字符串操作")
    print("\n请完成以下练习题，每题都有提示和答案。")
    print("建议先自己思考，再查看答案。")
    print("=" * 60)

# ============== 练习题 ==============

def exercise_1():
    """
    练习1：基本变量操作
    要求：
    1. 创建一个变量存储你的姓名
    2. 创建一个变量存储你的年龄
    3. 创建一个变量存储你是否是学生（True/False）
    4. 打印这些变量
    """
    print("\n练习1：基本变量操作")
    print("-" * 30)
    
    # 在这里写你的代码
    # 提示：使用合适的变量名，如 my_name, my_age, is_student
    
    # 答案（删除注释查看）
    """
    my_name = "张三"
    my_age = 18
    is_student = True
    
    print(f"姓名: {my_name}")
    print(f"年龄: {my_age}")
    print(f"是否学生: {is_student}")
    """

def exercise_2():
    """
    练习2：数据类型识别
    要求：
    1. 创建以下变量：整数、浮点数、字符串、布尔值
    2. 使用type()函数查看每个变量的类型
    3. 打印变量和其类型
    """
    print("\n练习2：数据类型识别")
    print("-" * 30)
    
    # 在这里写你的代码
    # 提示：使用type()函数
    
    # 答案
    """
    num_int = 42
    num_float = 3.14
    text = "Hello Python"
    flag = True
    
    print(f"{num_int} 的类型是: {type(num_int)}")
    print(f"{num_float} 的类型是: {type(num_float)}")
    print(f"'{text}' 的类型是: {type(text)}")
    print(f"{flag} 的类型是: {type(flag)}")
    """

def exercise_3():
    """
    练习3：类型转换
    要求：
    1. 将字符串"123"转换为整数
    2. 将整数456转换为字符串
    3. 将字符串"3.14"转换为浮点数
    4. 将整数0转换为布尔值，观察结果
    """
    print("\n练习3：类型转换")
    print("-" * 30)
    
    # 在这里写你的代码
    # 提示：使用int(), str(), float(), bool()函数
    
    # 答案
    """
    str_num = "123"
    int_from_str = int(str_num)
    print(f"字符串'{str_num}'转整数: {int_from_str}")
    
    num = 456
    str_from_int = str(num)
    print(f"整数{num}转字符串: '{str_from_int}'")
    
    str_float = "3.14"
    float_from_str = float(str_float)
    print(f"字符串'{str_float}'转浮点数: {float_from_str}")
    
    zero = 0
    bool_from_zero = bool(zero)
    print(f"整数{zero}转布尔值: {bool_from_zero}")
    """

def exercise_4():
    """
    练习4：字符串操作
    要求：
    1. 创建一个包含你全名的字符串
    2. 将全名转换为大写
    3. 计算全名的长度
    4. 将全名分割为姓和名（假设用空格分隔）
    """
    print("\n练习4：字符串操作")
    print("-" * 30)
    
    # 在这里写你的代码
    # 提示：使用.upper(), len(), .split()方法
    
    # 答案
    """
    full_name = "张 三"
    upper_name = full_name.upper()
    name_length = len(full_name)
    name_parts = full_name.split(" ")
    
    print(f"全名: {full_name}")
    print(f"大写: {upper_name}")
    print(f"长度: {name_length}")
    print(f"姓: {name_parts[0]}, 名: {name_parts[1]}")
    """

def exercise_5():
    """
    练习5：综合应用
    要求：
    1. 创建一个程序，询问用户的姓名和出生年份
    2. 计算用户的年龄（假设当前是2024年）
    3. 根据年龄判断用户是否成年（18岁）
    4. 用格式化字符串输出结果
    """
    print("\n练习5：综合应用")
    print("-" * 30)
    
    # 在这里写你的代码
    # 提示：使用input(), int(), f-string
    
    # 答案
    """
    try:
        name = input("请输入您的姓名: ")
        birth_year = int(input("请输入您的出生年份: "))
        
        current_year = 2024
        age = current_year - birth_year
        
        if age >= 18:
            status = "已成年"
        else:
            years_to_adult = 18 - age
            status = f"未成年，还有{years_to_adult}年成年"
        
        print(f"您好，{name}！")
        print(f"您今年{age}岁，{status}。")
        
    except ValueError:
        print("请输入有效的年份！")
    """

def challenge_exercise():
    """
    挑战练习：个人信息管理器
    要求：
    创建一个简单的个人信息管理器，包含以下功能：
    1. 存储姓名、年龄、城市、爱好（列表）
    2. 显示完整信息
    3. 修改年龄
    4. 添加新爱好
    5. 计算到退休还有多少年（假设65岁退休）
    """
    print("\n挑战练习：个人信息管理器")
    print("-" * 40)
    
    # 在这里写你的代码
    # 提示：使用字典存储信息，函数来处理操作
    
    # 答案
    """
    def create_person_info():
        person = {
            "姓名": input("请输入姓名: "),
            "年龄": int(input("请输入年龄: ")),
            "城市": input("请输入城市: "),
            "爱好": input("请输入爱好（用逗号分隔）: ").split(",")
        }
        return person
    
    def display_info(person):
        print(f"\n个人信息:")
        print(f"姓名: {person['姓名']}")
        print(f"年龄: {person['年龄']}")
        print(f"城市: {person['城市']}")
        print(f"爱好: {', '.join(person['爱好'])}")
        
        retirement_age = 65
        years_to_retirement = retirement_age - person['年龄']
        if years_to_retirement > 0:
            print(f"距离退休还有: {years_to_retirement}年")
        else:
            print("已经退休了！")
    
    def update_age(person, new_age):
        person['年龄'] = new_age
        print(f"年龄已更新为: {new_age}")
    
    def add_hobby(person, new_hobby):
        person['爱好'].append(new_hobby)
        print(f"已添加爱好: {new_hobby}")
    
    # 使用示例
    try:
        person = create_person_info()
        display_info(person)
        
        # 测试功能
        update_age(person, person['年龄'] + 1)
        add_hobby(person, "编程")
        display_info(person)
        
    except ValueError:
        print("请输入有效的数字！")
    """

def check_answers():
    """检查答案功能"""
    print("\n" + "=" * 60)
    print("答案检查")
    print("=" * 60)
    print("如果您完成了所有练习，可以运行答案来对比结果。")
    print("建议先独立完成练习，再查看答案学习更好的写法。")
    
    # 运行答案示例
    print("\n练习1答案演示:")
    my_name = "张三"
    my_age = 18
    is_student = True
    
    print(f"姓名: {my_name}")
    print(f"年龄: {my_age}")
    print(f"是否学生: {is_student}")
    
    print("\n练习2答案演示:")
    num_int = 42
    num_float = 3.14
    text = "Hello Python"
    flag = True
    
    print(f"{num_int} 的类型是: {type(num_int)}")
    print(f"{num_float} 的类型是: {type(num_float)}")
    print(f"'{text}' 的类型是: {type(text)}")
    print(f"{flag} 的类型是: {type(flag)}")

if __name__ == "__main__":
    exercise_instructions()
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    challenge_exercise()
    
    # 询问是否查看答案
    show_answers = input("\n是否查看答案示例？(y/n): ").lower()
    if show_answers == 'y':
        check_answers()
    
    print("\n" + "=" * 60)
    print("练习完成！继续学习下一个章节吧！")
    print("=" * 60) 