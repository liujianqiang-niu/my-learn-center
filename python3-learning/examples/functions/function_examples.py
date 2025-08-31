#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3 函数示例：从基础到高级
"""

def basic_functions():
    """基础函数示例"""
    print("=" * 40)
    print("基础函数演示")
    print("=" * 40)
    
    # 1. 简单函数
    def greet():
        """无参数函数"""
        return "Hello, Python!"
    
    print(f"问候: {greet()}")
    
    # 2. 带参数的函数
    def add(a, b):
        """两数相加"""
        return a + b
    
    result = add(5, 3)
    print(f"5 + 3 = {result}")
    
    # 3. 带默认参数的函数
    def power(base, exponent=2):
        """计算幂次，默认平方"""
        return base ** exponent
    
    print(f"3的平方: {power(3)}")
    print(f"2的3次方: {power(2, 3)}")
    
    # 4. 多返回值函数
    def get_name_age():
        """返回多个值"""
        return "张三", 25
    
    name, age = get_name_age()
    print(f"姓名: {name}, 年龄: {age}")

def advanced_parameters():
    """高级参数用法"""
    print("\n" + "=" * 40)
    print("高级参数演示")
    print("=" * 40)
    
    # 1. 可变位置参数 (*args)
    def sum_all(*numbers):
        """计算所有数字的和"""
        print(f"接收到的参数: {numbers}")
        return sum(numbers)
    
    result1 = sum_all(1, 2, 3)
    result2 = sum_all(1, 2, 3, 4, 5, 6)
    print(f"求和结果1: {result1}")
    print(f"求和结果2: {result2}")
    
    # 2. 可变关键字参数 (**kwargs)
    def create_profile(name, **details):
        """创建用户档案"""
        print(f"用户: {name}")
        print("详细信息:")
        for key, value in details.items():
            print(f"  {key}: {value}")
    
    create_profile("张三", 年龄=25, 城市="北京", 职业="工程师")
    
    # 3. 混合参数类型
    def complex_function(required, default="默认值", *args, **kwargs):
        """复杂参数函数"""
        print(f"必需参数: {required}")
        print(f"默认参数: {default}")
        print(f"可变参数: {args}")
        print(f"关键字参数: {kwargs}")
    
    complex_function("必需", "自定义", 1, 2, 3, name="张三", age=25)

def lambda_examples():
    """Lambda函数示例"""
    print("\n" + "=" * 40)
    print("Lambda函数演示")
    print("=" * 40)
    
    # 基本lambda
    square = lambda x: x * x
    print(f"5的平方: {square(5)}")
    
    # 与内置函数配合
    numbers = [1, 2, 3, 4, 5]
    
    # map: 对每个元素应用函数
    squares = list(map(lambda x: x * x, numbers))
    print(f"平方列表: {squares}")
    
    # filter: 过滤元素
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"偶数列表: {evens}")
    
    # sorted: 自定义排序
    students = [("张三", 85), ("李四", 90), ("王五", 78)]
    sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
    print(f"按成绩排序: {sorted_by_score}")

def scope_examples():
    """变量作用域示例"""
    print("\n" + "=" * 40)
    print("变量作用域演示")
    print("=" * 40)
    
    global_var = "我是全局变量"
    
    def outer_function():
        """外层函数"""
        outer_var = "我是外层变量"
        
        def inner_function():
            """内层函数"""
            inner_var = "我是内层变量"
            print(f"内层访问: {global_var}")
            print(f"内层访问: {outer_var}")
            print(f"内层访问: {inner_var}")
        
        inner_function()
        print(f"外层访问: {global_var}")
        print(f"外层访问: {outer_var}")
        # print(inner_var)  # 错误！不能访问内层变量
    
    outer_function()
    print(f"全局访问: {global_var}")
    
    # nonlocal和global关键字
    counter = 0
    
    def increment():
        global counter
        counter += 1
        print(f"计数器: {counter}")
    
    increment()
    increment()

def decorator_examples():
    """装饰器示例"""
    print("\n" + "=" * 40)
    print("装饰器演示")
    print("=" * 40)
    
    # 简单装饰器
    def my_decorator(func):
        """简单装饰器"""
        def wrapper():
            print("函数执行前")
            result = func()
            print("函数执行后")
            return result
        return wrapper
    
    @my_decorator
    def say_hello():
        print("Hello!")
        return "完成"
    
    result = say_hello()
    print(f"返回值: {result}")
    
    # 带参数的装饰器
    def repeat(times):
        """重复执行装饰器"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                for i in range(times):
                    print(f"第{i+1}次执行:")
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
    
    @repeat(3)
    def count_to_five():
        for i in range(1, 6):
            print(f"  数字: {i}")
    
    count_to_five()

def practical_functions():
    """实用函数示例"""
    print("\n" + "=" * 40)
    print("实用函数示例")
    print("=" * 40)
    
    # 计算器函数
    def calculator():
        """简单计算器"""
        def add(a, b):
            return a + b
        
        def subtract(a, b):
            return a - b
        
        def multiply(a, b):
            return a * b
        
        def divide(a, b):
            if b == 0:
                return "错误：不能除以0"
            return a / b
        
        # 返回包含所有操作的字典
        return {
            "加法": add,
            "减法": subtract,
            "乘法": multiply,
            "除法": divide
        }
    
    calc = calculator()
    print(f"加法 10 + 5 = {calc['加法'](10, 5)}")
    print(f"除法 10 / 3 = {calc['除法'](10, 3):.2f}")
    
    # 数据处理函数
    def process_scores(scores):
        """处理成绩数据"""
        if not scores:
            return None
        
        total = sum(scores)
        average = total / len(scores)
        highest = max(scores)
        lowest = min(scores)
        
        return {
            "总分": total,
            "平均分": round(average, 2),
            "最高分": highest,
            "最低分": lowest,
            "及格人数": len([s for s in scores if s >= 60])
        }
    
    test_scores = [85, 92, 78, 90, 88, 76, 95]
    stats = process_scores(test_scores)
    print(f"\n成绩统计: {stats}")
    
    # 文本处理函数
    def clean_text(text):
        """清理文本"""
        # 去除首尾空格，转换为小写
        cleaned = text.strip().lower()
        # 移除标点符号
        import string
        for punct in string.punctuation:
            cleaned = cleaned.replace(punct, "")
        return cleaned
    
    messy_text = "  Hello, World! How Are You?  "
    clean = clean_text(messy_text)
    print(f"原文本: '{messy_text}'")
    print(f"清理后: '{clean}'")

if __name__ == "__main__":
    basic_functions()
    advanced_parameters()
    lambda_examples()
    scope_examples()
    decorator_examples()
    practical_functions() 