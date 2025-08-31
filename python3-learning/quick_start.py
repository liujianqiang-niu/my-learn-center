#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3 快速开始指南
为初学者提供Python学习的第一步
"""

def welcome():
    """欢迎信息"""
    print("🐍" * 20)
    print("  欢迎来到Python3学习世界！")
    print("🐍" * 20)
    print()
    print("Python是什么？")
    print("- Python是一种简单易学的编程语言")
    print("- 它的语法接近英语，容易理解")
    print("- 被广泛用于网站开发、数据分析、人工智能等领域")
    print()
    print("学完Python你能做什么？")
    print("✨ 制作网站和应用")
    print("✨ 分析数据，制作图表")
    print("✨ 开发游戏")
    print("✨ 自动化日常任务")
    print("✨ 人工智能和机器学习")

def first_python_program():
    """第一个Python程序"""
    print("\n" + "="*40)
    print("🚀 您的第一个Python程序")
    print("="*40)
    
    print("让我们从最简单的开始：")
    print('1. print("Hello, World!")  # 在屏幕上显示文字')
    print()
    
    # 演示
    print("运行结果：")
    print("Hello, World!")
    
    print("\n让我们分解这行代码：")
    print("- print() 是一个函数，用来显示内容")
    print("- 'Hello, World!' 是字符串，用引号包围")
    print("- # 后面的是注释，程序会忽略")

def interactive_demo():
    """交互式演示"""
    print("\n" + "="*40)
    print("🎯 交互式学习演示")
    print("="*40)
    
    # 基础概念演示
    print("1. 变量就像存放东西的盒子：")
    name = "小明"
    age = 15
    print(f"   name = '{name}'    # 在名叫'name'的盒子里放入'小明'")
    print(f"   age = {age}           # 在名叫'age'的盒子里放入15")
    print(f"   现在我们可以使用这些盒子：{name}今年{age}岁")
    
    print("\n2. 数据类型就像不同种类的盒子：")
    integer_box = 42           # 整数盒子
    float_box = 3.14          # 小数盒子
    string_box = "Hello"      # 文字盒子
    boolean_box = True        # 真假盒子
    
    print(f"   整数盒子: {integer_box} (类型: {type(integer_box).__name__})")
    print(f"   小数盒子: {float_box} (类型: {type(float_box).__name__})")
    print(f"   文字盒子: '{string_box}' (类型: {type(string_box).__name__})")
    print(f"   真假盒子: {boolean_box} (类型: {type(boolean_box).__name__})")
    
    print("\n3. 简单的计算：")
    a = 10
    b = 3
    print(f"   a = {a}, b = {b}")
    print(f"   a + b = {a + b}")
    print(f"   a * b = {a * b}")
    print(f"   a > b 是 {a > b} 吗？")
    
    print("\n4. 条件判断（if语句）：")
    score = 85
    print(f"   如果成绩是{score}分：")
    if score >= 90:
        result = "优秀！"
    elif score >= 60:
        result = "及格"
    else:
        result = "需要努力"
    print(f"   结果是：{result}")

def hands_on_practice():
    """动手练习"""
    print("\n" + "="*40)
    print("🔥 现在轮到您动手了！")
    print("="*40)
    
    print("简单练习：让我们创建一个小程序")
    print("这个程序会：")
    print("1. 询问您的姓名")
    print("2. 询问您最喜欢的数字")
    print("3. 计算这个数字的平方")
    print("4. 给出个性化的回复")
    
    try:
        # 用户交互
        user_name = input("\n👋 请输入您的姓名: ")
        
        # 验证输入
        if not user_name.strip():
            print("❌ 姓名不能为空！")
            return
        
        favorite_number = input(f"嗨，{user_name}！请输入您最喜欢的数字: ")
        
        # 类型转换和错误处理
        try:
            num = int(favorite_number)
        except ValueError:
            print("❌ 请输入一个有效的数字！")
            return
        
        # 计算和输出
        square = num * num
        
        print(f"\n🎉 太棒了，{user_name}！")
        print(f"您最喜欢的数字是 {num}")
        print(f"{num} 的平方是 {square}")
        
        # 添加一些有趣的判断
        if num == square:
            print("🤔 有趣！您的数字和它的平方相等！")
        elif square > 100:
            print("🚀 这是一个很大的平方数！")
        elif square < 10:
            print("🌱 这是一个小巧的平方数！")
        else:
            print("📐 很棒的数字选择！")
            
        print(f"\n恭喜您完成了第一个交互式Python程序！🎊")
        
    except KeyboardInterrupt:
        print("\n\n👋 程序被中断，没关系，继续学习吧！")

def learning_path():
    """学习路径指导"""
    print("\n" + "="*50)
    print("🗺️  Python学习路径指导")
    print("="*50)
    
    path = [
        ("第1周", "基础语法和变量", "学会创建变量，理解数据类型"),
        ("第2周", "控制流程", "掌握if条件判断和for/while循环"),
        ("第3周", "数据结构", "学会使用列表、字典、元组、集合"),
        ("第4周", "函数", "编写可重用的代码块"),
        ("第5-6周", "面向对象编程", "理解类和对象的概念"),
        ("第7周", "模块和文件操作", "学会代码组织和数据存储"),
        ("第8周", "错误处理", "让程序更稳定"),
        ("第9-10周", "高级特性和项目实践", "成为Python高手")
    ]
    
    print("推荐学习计划：")
    for week, topic, description in path:
        print(f"📅 {week}: {topic}")
        print(f"   目标：{description}")
        print()
    
    print("💡 学习建议：")
    tips = [
        "每天至少练习30分钟",
        "理论学习后一定要动手实践",
        "遇到错误不要害怕，这是学习的一部分",
        "多看别人的代码，学习不同的写法",
        "加入Python社区，与其他学习者交流",
        "做小项目巩固所学知识"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"  {i}. {tip}")

def next_steps():
    """接下来的步骤"""
    print("\n" + "="*40)
    print("🎯 接下来该做什么？")
    print("="*40)
    
    steps = [
        ("阅读学习文档", "python3_syntax_guide.md", "系统学习Python语法"),
        ("运行示例代码", "examples/ 目录", "看看Python能做什么"),
        ("完成练习题", "exercises/ 目录", "巩固所学知识"),
        ("跟踪学习进度", "study_tracker.py", "监控学习效果"),
        ("实践综合项目", "examples/project_example.py", "应用所学技能")
    ]
    
    print("推荐顺序：")
    for i, (action, file, description) in enumerate(steps, 1):
        print(f"{i}. {action}")
        print(f"   文件：{file}")
        print(f"   说明：{description}")
        print()
    
    print("🔧 如何运行Python文件：")
    print("在终端中输入：python3 文件名.py")
    print("例如：python3 quick_start.py")

def main():
    """主函数"""
    welcome()
    first_python_program()
    interactive_demo()
    hands_on_practice()
    learning_path()
    next_steps()
    
    print("\n" + "🎉"*20)
    print("  Python学习之旅正式开始！")
    print("🎉"*20)
    print("\n记住：编程最重要的是实践！")
    print("不要只是阅读，要动手写代码！")
    print("每一行代码都是向成为优秀工程师迈进的一步！")

if __name__ == "__main__":
    main() 