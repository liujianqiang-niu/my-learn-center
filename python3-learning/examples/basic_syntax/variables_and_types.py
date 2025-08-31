#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3 基础语法示例：变量和数据类型
作者：Python学习助手
日期：2024
"""

def main():
    """主函数：演示Python基础语法"""
    
    print("=" * 50)
    print("Python3 变量和数据类型演示")
    print("=" * 50)
    
    # 1. 变量定义和使用
    print("\n1. 变量定义：")
    name = "小明"           # 字符串变量
    age = 18               # 整数变量
    height = 1.75          # 浮点数变量
    is_student = True      # 布尔值变量
    
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"身高: {height}米")
    print(f"是否是学生: {is_student}")
    
    # 2. 数据类型检查
    print("\n2. 数据类型检查：")
    print(f"name的类型: {type(name)}")
    print(f"age的类型: {type(age)}")
    print(f"height的类型: {type(height)}")
    print(f"is_student的类型: {type(is_student)}")
    
    # 3. 类型转换
    print("\n3. 类型转换：")
    age_str = str(age)              # 数字转字符串
    height_int = int(height)        # 浮点数转整数
    age_from_str = int("25")        # 字符串转数字
    
    print(f"年龄转字符串: '{age_str}' (类型: {type(age_str)})")
    print(f"身高转整数: {height_int} (类型: {type(height_int)})")
    print(f"字符串转数字: {age_from_str} (类型: {type(age_from_str)})")
    
    # 4. 字符串操作
    print("\n4. 字符串操作：")
    greeting = "Hello"
    target = "World"
    
    # 字符串拼接
    message1 = greeting + ", " + target + "!"
    message2 = f"{greeting}, {target}!"      # f-string（推荐）
    message3 = "{}, {}!".format(greeting, target)
    
    print(f"拼接方式1: {message1}")
    print(f"拼接方式2: {message2}")
    print(f"拼接方式3: {message3}")
    
    # 字符串方法
    text = "  Python Programming  "
    print(f"原始字符串: '{text}'")
    print(f"去除空格: '{text.strip()}'")
    print(f"转大写: '{text.upper()}'")
    print(f"转小写: '{text.lower()}'")
    print(f"替换: '{text.replace('Python', 'Java')}'")
    
    # 5. 用户输入
    print("\n5. 用户交互示例：")
    try:
        user_name = input("请输入您的姓名: ")
        user_age = int(input("请输入您的年龄: "))
        
        print(f"很高兴认识您，{user_name}！")
        print(f"您今年{user_age}岁，")
        
        if user_age >= 18:
            print("您已经成年了！")
        else:
            print(f"还有{18 - user_age}年就成年了！")
            
    except ValueError:
        print("年龄必须是数字！")
    except KeyboardInterrupt:
        print("\n程序被用户中断")

if __name__ == "__main__":
    main() 