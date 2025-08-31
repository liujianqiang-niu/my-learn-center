#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3 综合项目示例：简单的学生成绩管理系统
这个项目综合运用了Python的各种语法特性
"""

import json
import datetime
from pathlib import Path

class Student:
    """学生类"""
    
    def __init__(self, student_id, name, grade, age):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.age = age
        self.subjects = {}  # 学科成绩字典
        self.created_date = datetime.datetime.now()
    
    def add_score(self, subject, score):
        """添加学科成绩"""
        if not isinstance(score, (int, float)):
            raise ValueError("成绩必须是数字")
        
        if not 0 <= score <= 100:
            raise ValueError("成绩必须在0-100之间")
        
        self.subjects[subject] = score
        return True
    
    def get_average(self):
        """计算平均分"""
        if not self.subjects:
            return 0
        return round(sum(self.subjects.values()) / len(self.subjects), 2)
    
    def get_grade_level(self):
        """获取成绩等级"""
        avg = self.get_average()
        if avg >= 90:
            return "优秀"
        elif avg >= 80:
            return "良好"
        elif avg >= 60:
            return "及格"
        else:
            return "需要努力"
    
    def to_dict(self):
        """转换为字典（用于JSON序列化）"""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade,
            "age": self.age,
            "subjects": self.subjects,
            "created_date": self.created_date.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建学生对象"""
        student = cls(data["student_id"], data["name"], data["grade"], data["age"])
        student.subjects = data.get("subjects", {})
        if "created_date" in data:
            student.created_date = datetime.datetime.fromisoformat(data["created_date"])
        return student
    
    def __str__(self):
        return f"Student(ID:{self.student_id}, 姓名:{self.name}, 平均分:{self.get_average()})"

class StudentManager:
    """学生管理系统"""
    
    def __init__(self, data_file="students_data.json"):
        self.data_file = data_file
        self.students = []
        self.load_data()
    
    def load_data(self):
        """从文件加载学生数据"""
        try:
            if Path(self.data_file).exists():
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.students = [Student.from_dict(student_data) for student_data in data]
                print(f"✅ 成功加载 {len(self.students)} 名学生的数据")
            else:
                print("📁 数据文件不存在，将创建新的数据文件")
        except Exception as e:
            print(f"❌ 加载数据失败：{e}")
            self.students = []
    
    def save_data(self):
        """保存学生数据到文件"""
        try:
            data = [student.to_dict() for student in self.students]
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("💾 数据已保存")
            return True
        except Exception as e:
            print(f"❌ 保存数据失败：{e}")
            return False
    
    def add_student(self, student_id, name, grade, age):
        """添加学生"""
        # 检查学号是否已存在
        if self.find_student(student_id):
            print(f"❌ 学号 {student_id} 已存在！")
            return False
        
        try:
            student = Student(student_id, name, grade, int(age))
            self.students.append(student)
            print(f"✅ 成功添加学生：{name}")
            return True
        except ValueError as e:
            print(f"❌ 添加学生失败：{e}")
            return False
    
    def find_student(self, student_id):
        """查找学生"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def remove_student(self, student_id):
        """删除学生"""
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print(f"✅ 成功删除学生：{student.name}")
            return True
        else:
            print(f"❌ 找不到学号为 {student_id} 的学生")
            return False
    
    def add_student_score(self, student_id, subject, score):
        """为学生添加成绩"""
        student = self.find_student(student_id)
        if student:
            try:
                student.add_score(subject, float(score))
                print(f"✅ 成功为 {student.name} 添加 {subject} 成绩：{score}分")
                return True
            except ValueError as e:
                print(f"❌ 添加成绩失败：{e}")
                return False
        else:
            print(f"❌ 找不到学号为 {student_id} 的学生")
            return False
    
    def show_all_students(self):
        """显示所有学生信息"""
        if not self.students:
            print("📝 暂无学生数据")
            return
        
        print(f"\n📋 学生名单（共{len(self.students)}人）：")
        print("-" * 80)
        print(f"{'学号':<10} {'姓名':<10} {'年级':<10} {'年龄':<8} {'平均分':<10} {'等级':<10}")
        print("-" * 80)
        
        for student in self.students:
            avg = student.get_average()
            level = student.get_grade_level()
            print(f"{student.student_id:<10} {student.name:<10} {student.grade:<10} "
                  f"{student.age:<8} {avg:<10} {level:<10}")
    
    def show_student_detail(self, student_id):
        """显示学生详细信息"""
        student = self.find_student(student_id)
        if not student:
            print(f"❌ 找不到学号为 {student_id} 的学生")
            return
        
        print(f"\n👤 学生详细信息：")
        print("-" * 40)
        print(f"学号：{student.student_id}")
        print(f"姓名：{student.name}")
        print(f"年级：{student.grade}")
        print(f"年龄：{student.age}")
        print(f"入学时间：{student.created_date.strftime('%Y-%m-%d')}")
        print(f"平均分：{student.get_average()}")
        print(f"等级：{student.get_grade_level()}")
        
        if student.subjects:
            print("\n📊 各科成绩：")
            for subject, score in student.subjects.items():
                print(f"  {subject}: {score}分")
        else:
            print("\n📊 暂无成绩记录")
    
    def get_class_statistics(self):
        """获取班级统计信息"""
        if not self.students:
            return "暂无数据"
        
        # 计算各种统计信息
        total_students = len(self.students)
        avg_scores = [student.get_average() for student in self.students if student.get_average() > 0]
        
        if not avg_scores:
            return "暂无有效成绩数据"
        
        class_average = round(sum(avg_scores) / len(avg_scores), 2)
        highest_score = max(avg_scores)
        lowest_score = min(avg_scores)
        
        # 等级分布
        grade_counts = {"优秀": 0, "良好": 0, "及格": 0, "需要努力": 0}
        for student in self.students:
            if student.get_average() > 0:
                grade_counts[student.get_grade_level()] += 1
        
        return {
            "总学生数": total_students,
            "班级平均分": class_average,
            "最高分": highest_score,
            "最低分": lowest_score,
            "等级分布": grade_counts
        }

def main_menu():
    """主菜单"""
    manager = StudentManager()
    
    while True:
        print("\n" + "🎓" * 20)
        print("    学生成绩管理系统")
        print("🎓" * 20)
        print("1. 显示所有学生")
        print("2. 添加学生")
        print("3. 删除学生")
        print("4. 查看学生详情")
        print("5. 添加成绩")
        print("6. 班级统计")
        print("7. 保存数据")
        print("8. 退出系统")
        print("=" * 40)
        
        try:
            choice = input("请选择操作 (1-8): ").strip()
            
            if choice == "1":
                manager.show_all_students()
            
            elif choice == "2":
                print("\n➕ 添加新学生：")
                student_id = input("学号: ").strip()
                name = input("姓名: ").strip()
                grade = input("年级: ").strip()
                age = input("年龄: ").strip()
                
                if all([student_id, name, grade, age]):
                    manager.add_student(student_id, name, grade, age)
                else:
                    print("❌ 所有信息都不能为空！")
            
            elif choice == "3":
                student_id = input("\n🗑️  请输入要删除的学生学号: ").strip()
                if student_id:
                    manager.remove_student(student_id)
                else:
                    print("❌ 学号不能为空！")
            
            elif choice == "4":
                student_id = input("\n🔍 请输入要查看的学生学号: ").strip()
                if student_id:
                    manager.show_student_detail(student_id)
                else:
                    print("❌ 学号不能为空！")
            
            elif choice == "5":
                print("\n📝 添加成绩：")
                student_id = input("学号: ").strip()
                subject = input("科目: ").strip()
                score = input("成绩: ").strip()
                
                if all([student_id, subject, score]):
                    manager.add_student_score(student_id, subject, score)
                else:
                    print("❌ 所有信息都不能为空！")
            
            elif choice == "6":
                stats = manager.get_class_statistics()
                if isinstance(stats, dict):
                    print("\n📊 班级统计信息：")
                    print("-" * 30)
                    for key, value in stats.items():
                        if key == "等级分布":
                            print(f"{key}:")
                            for grade, count in value.items():
                                print(f"  {grade}: {count}人")
                        else:
                            print(f"{key}: {value}")
                else:
                    print(f"\n📊 班级统计：{stats}")
            
            elif choice == "7":
                manager.save_data()
            
            elif choice == "8":
                # 自动保存并退出
                manager.save_data()
                print("👋 感谢使用学生成绩管理系统！")
                break
            
            else:
                print("❌ 无效选择，请输入1-8之间的数字！")
                
        except KeyboardInterrupt:
            print("\n\n👋 程序被用户中断，正在保存数据...")
            manager.save_data()
            print("数据已保存，再见！")
            break
        except Exception as e:
            print(f"❌ 程序错误：{e}")
            print("请检查输入是否正确")

def demo_mode():
    """演示模式：自动创建示例数据"""
    print("🎬 演示模式：创建示例学生数据")
    
    manager = StudentManager("demo_students.json")
    
    # 添加示例学生
    demo_students = [
        ("2024001", "张三", "高三", 18),
        ("2024002", "李四", "高三", 17),
        ("2024003", "王五", "高三", 18),
        ("2024004", "赵六", "高三", 17)
    ]
    
    print("\n添加示例学生：")
    for student_id, name, grade, age in demo_students:
        manager.add_student(student_id, name, grade, age)
    
    # 添加示例成绩
    demo_scores = [
        ("2024001", [("数学", 85), ("语文", 90), ("英语", 88)]),
        ("2024002", [("数学", 78), ("语文", 85), ("英语", 82)]),
        ("2024003", [("数学", 92), ("语文", 88), ("英语", 95)]),
        ("2024004", [("数学", 88), ("语文", 92), ("英语", 85)])
    ]
    
    print("\n添加示例成绩：")
    for student_id, subjects in demo_scores:
        for subject, score in subjects:
            manager.add_student_score(student_id, subject, score)
    
    # 显示结果
    print("\n" + "="*50)
    print("演示数据创建完成！")
    print("="*50)
    manager.show_all_students()
    
    # 显示统计信息
    stats = manager.get_class_statistics()
    if isinstance(stats, dict):
        print("\n📊 班级统计信息：")
        for key, value in stats.items():
            if key == "等级分布":
                print(f"{key}:")
                for grade, count in value.items():
                    print(f"  {grade}: {count}人")
            else:
                print(f"{key}: {value}")
    
    # 保存演示数据
    manager.save_data()
    print("\n💾 演示数据已保存到 demo_students.json")

if __name__ == "__main__":
    print("🎓 学生成绩管理系统")
    print("这是一个综合项目示例，展示了Python的各种特性：")
    print("- 面向对象编程（类和对象）")
    print("- 文件操作（JSON数据持久化）")
    print("- 错误处理（异常捕获）")
    print("- 数据结构（列表、字典）")
    print("- 函数（各种类型的方法）")
    print("- 用户交互（输入输出）")
    
    print("\n请选择模式：")
    print("1. 交互模式（手动操作）")
    print("2. 演示模式（自动创建示例数据）")
    
    try:
        mode = input("请选择 (1/2): ").strip()
        
        if mode == "1":
            main_menu()
        elif mode == "2":
            demo_mode()
        else:
            print("❌ 无效选择")
            
    except KeyboardInterrupt:
        print("\n👋 程序被中断，再见！") 