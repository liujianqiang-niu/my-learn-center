#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3 数据结构示例：列表、字典、元组、集合
"""

def list_operations():
    """演示列表操作"""
    print("=" * 30)
    print("列表（List）操作演示")
    print("=" * 30)
    
    # 创建列表
    fruits = ["苹果", "香蕉", "橙子"]
    numbers = [1, 2, 3, 4, 5]
    
    print(f"水果列表: {fruits}")
    print(f"数字列表: {numbers}")
    
    # 访问元素
    print(f"第一个水果: {fruits[0]}")
    print(f"最后一个水果: {fruits[-1]}")
    
    # 修改元素
    fruits[1] = "葡萄"
    print(f"修改后的水果列表: {fruits}")
    
    # 添加元素
    fruits.append("西瓜")
    fruits.insert(1, "草莓")
    print(f"添加水果后: {fruits}")
    
    # 删除元素
    fruits.remove("苹果")
    last_fruit = fruits.pop()
    print(f"删除操作后: {fruits}")
    print(f"被删除的水果: {last_fruit}")
    
    # 列表切片
    print(f"前两个水果: {fruits[:2]}")
    print(f"后两个水果: {fruits[-2:]}")
    
    # 列表方法
    numbers = [3, 1, 4, 1, 5, 9, 2]
    print(f"原始数字: {numbers}")
    print(f"列表长度: {len(numbers)}")
    print(f"最大值: {max(numbers)}")
    print(f"最小值: {min(numbers)}")
    print(f"求和: {sum(numbers)}")
    print(f"1出现次数: {numbers.count(1)}")
    
    numbers.sort()
    print(f"排序后: {numbers}")

def dict_operations():
    """演示字典操作"""
    print("\n" + "=" * 30)
    print("字典（Dictionary）操作演示")
    print("=" * 30)
    
    # 创建字典
    student = {
        "姓名": "张三",
        "年龄": 18,
        "成绩": [85, 90, 88],
        "班级": "三年一班"
    }
    
    print(f"学生信息: {student}")
    
    # 访问值
    print(f"姓名: {student['姓名']}")
    print(f"年龄: {student.get('年龄', '未知')}")  # 安全访问
    
    # 修改和添加
    student["年龄"] = 19
    student["爱好"] = ["篮球", "读书"]
    print(f"更新后: {student}")
    
    # 删除
    removed_class = student.pop("班级")
    print(f"删除班级信息: {removed_class}")
    print(f"删除后: {student}")
    
    # 遍历字典
    print("\n遍历学生信息:")
    for key, value in student.items():
        print(f"  {key}: {value}")
    
    # 字典方法
    print(f"所有键: {list(student.keys())}")
    print(f"所有值: {list(student.values())}")

def tuple_operations():
    """演示元组操作"""
    print("\n" + "=" * 30)
    print("元组（Tuple）操作演示")
    print("=" * 30)
    
    # 创建元组
    point = (10, 20)
    colors = ("红", "绿", "蓝")
    mixed = ("张三", 18, True)
    
    print(f"坐标点: {point}")
    print(f"颜色: {colors}")
    print(f"混合数据: {mixed}")
    
    # 访问元素
    print(f"X坐标: {point[0]}")
    print(f"Y坐标: {point[1]}")
    
    # 元组解包
    x, y = point
    name, age, is_student = mixed
    print(f"解包结果: x={x}, y={y}")
    print(f"解包结果: 姓名={name}, 年龄={age}, 学生={is_student}")
    
    # 元组的不可变性
    try:
        point[0] = 30  # 这会引发错误
    except TypeError as e:
        print(f"错误：元组不可修改 - {e}")

def set_operations():
    """演示集合操作"""
    print("\n" + "=" * 30)
    print("集合（Set）操作演示")
    print("=" * 30)
    
    # 创建集合
    fruits = {"苹果", "香蕉", "橙子"}
    numbers = {1, 2, 3, 3, 4, 4, 5}  # 重复元素会自动去除
    
    print(f"水果集合: {fruits}")
    print(f"数字集合: {numbers}")  # 输出: {1, 2, 3, 4, 5}
    
    # 添加和删除
    fruits.add("西瓜")
    fruits.add("苹果")  # 重复添加无效
    print(f"添加西瓜后: {fruits}")
    
    fruits.remove("香蕉")
    fruits.discard("葡萄")  # 删除不存在的元素不会报错
    print(f"删除后: {fruits}")
    
    # 集合运算
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    print(f"集合1: {set1}")
    print(f"集合2: {set2}")
    print(f"并集: {set1 | set2}")        # {1, 2, 3, 4, 5, 6}
    print(f"交集: {set1 & set2}")        # {3, 4}
    print(f"差集: {set1 - set2}")        # {1, 2}
    print(f"对称差集: {set1 ^ set2}")    # {1, 2, 5, 6}

def practical_examples():
    """实际应用示例"""
    print("\n" + "=" * 30)
    print("实际应用示例")
    print("=" * 30)
    
    # 示例1：学生成绩管理
    students = [
        {"姓名": "张三", "数学": 85, "英语": 90},
        {"姓名": "李四", "数学": 78, "英语": 85},
        {"姓名": "王五", "数学": 92, "英语": 88}
    ]
    
    print("学生成绩统计:")
    for student in students:
        total = student["数学"] + student["英语"]
        average = total / 2
        print(f"{student['姓名']}: 总分{total}, 平均分{average:.1f}")
    
    # 示例2：去重统计
    votes = ["苹果", "香蕉", "苹果", "橙子", "香蕉", "苹果"]
    unique_votes = set(votes)
    vote_count = {fruit: votes.count(fruit) for fruit in unique_votes}
    
    print(f"\n投票结果统计:")
    for fruit, count in vote_count.items():
        print(f"{fruit}: {count}票")
    
    # 示例3：坐标点处理
    points = [(0, 0), (1, 2), (3, 4), (5, 6)]
    print(f"\n坐标点: {points}")
    
    # 计算距离原点的距离
    distances = []
    for x, y in points:
        distance = (x**2 + y**2)**0.5
        distances.append(round(distance, 2))
    
    print(f"到原点距离: {distances}")

if __name__ == "__main__":
    list_operations()
    dict_operations()
    tuple_operations()
    set_operations()
    practical_examples() 