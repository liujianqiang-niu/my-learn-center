#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3 面向对象编程示例：类、对象、继承、多态
"""

def basic_class_demo():
    """基础类演示"""
    print("=" * 50)
    print("基础类和对象演示")
    print("=" * 50)
    
    # 定义一个简单的类
    class Dog:
        """狗类 - 演示基本的类定义"""
        
        # 类属性（所有实例共享）
        species = "犬科动物"
        
        def __init__(self, name, age, breed="混血"):
            """初始化方法（构造函数）"""
            self.name = name        # 实例属性
            self.age = age
            self.breed = breed
            self.energy = 100       # 狗的精力值
        
        def bark(self):
            """狗叫方法"""
            if self.energy > 0:
                self.energy -= 10
                return f"{self.name}正在汪汪叫！剩余精力：{self.energy}"
            else:
                return f"{self.name}太累了，不想叫了..."
        
        def sleep(self):
            """睡觉恢复精力"""
            self.energy = 100
            return f"{self.name}睡了一觉，精力恢复到{self.energy}！"
        
        def introduce(self):
            """自我介绍"""
            return f"大家好！我是{self.name}，{self.age}岁的{self.breed}，我是{self.species}。"
        
        def __str__(self):
            """字符串表示（当print对象时调用）"""
            return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"
    
    # 创建对象
    dog1 = Dog("旺财", 3, "金毛")
    dog2 = Dog("小黑", 2)  # 使用默认品种
    
    print("创建的狗狗们:")
    print(dog1)
    print(dog2)
    
    # 调用方法
    print(f"\n{dog1.introduce()}")
    print(dog1.bark())
    print(dog1.bark())
    print(dog1.sleep())
    
    print(f"\n{dog2.introduce()}")

def inheritance_demo():
    """继承演示"""
    print("\n" + "=" * 50)
    print("继承演示")
    print("=" * 50)
    
    # 父类（基类）
    class Animal:
        """动物基类"""
        
        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.health = 100
        
        def eat(self, food):
            """吃东西"""
            self.health = min(100, self.health + 10)
            return f"{self.name}吃了{food}，健康值：{self.health}"
        
        def sleep(self):
            """睡觉"""
            self.health = 100
            return f"{self.name}睡了一觉，完全恢复了！"
        
        def speak(self):
            """抽象方法，子类需要重写"""
            return f"{self.name}发出了声音"
        
        def __str__(self):
            return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"
    
    # 子类1：狗
    class Dog(Animal):
        """狗类，继承自Animal"""
        
        def __init__(self, name, age, breed="混血"):
            super().__init__(name, age)  # 调用父类构造函数
            self.breed = breed
            self.loyalty = 100
        
        def speak(self):
            """重写父类方法"""
            return f"{self.name}说：汪汪汪！"
        
        def fetch(self, item):
            """狗特有的方法"""
            self.loyalty = min(100, self.loyalty + 5)
            return f"{self.name}把{item}捡回来了！忠诚度：{self.loyalty}"
    
    # 子类2：猫
    class Cat(Animal):
        """猫类，继承自Animal"""
        
        def __init__(self, name, age, color="橘色"):
            super().__init__(name, age)
            self.color = color
            self.independence = 80
        
        def speak(self):
            """重写父类方法"""
            return f"{self.name}说：喵喵喵~"
        
        def hunt(self, prey):
            """猫特有的方法"""
            self.independence += 10
            return f"{self.name}抓到了{prey}！独立性：{self.independence}"
    
    # 创建对象
    dog = Dog("旺财", 3, "拉布拉多")
    cat = Cat("咪咪", 2, "橘猫")
    
    print("创建的动物们:")
    print(dog)
    print(cat)
    
    # 调用方法
    print(f"\n{dog.speak()}")
    print(dog.eat("狗粮"))
    print(dog.fetch("球"))
    
    print(f"\n{cat.speak()}")
    print(cat.eat("猫粮"))
    print(cat.hunt("老鼠"))

def polymorphism_demo():
    """多态演示"""
    print("\n" + "=" * 50)
    print("多态演示")
    print("=" * 50)
    
    # 使用上面定义的Animal、Dog、Cat类
    class Animal:
        def __init__(self, name):
            self.name = name
        
        def speak(self):
            return f"{self.name}发出声音"
    
    class Dog(Animal):
        def speak(self):
            return f"{self.name}说：汪汪！"
    
    class Cat(Animal):
        def speak(self):
            return f"{self.name}说：喵喵！"
    
    class Bird(Animal):
        def speak(self):
            return f"{self.name}说：叽叽喳喳！"
    
    # 多态的体现：相同的方法调用，不同的行为
    def make_animal_speak(animal):
        """让动物说话 - 体现多态"""
        return animal.speak()
    
    # 创建不同类型的动物
    animals = [
        Dog("旺财"),
        Cat("咪咪"),
        Bird("小鸟"),
        Animal("神秘动物")
    ]
    
    print("让所有动物说话:")
    for animal in animals:
        print(f"  {make_animal_speak(animal)}")

def encapsulation_demo():
    """封装演示"""
    print("\n" + "=" * 50)
    print("封装演示（私有属性和方法）")
    print("=" * 50)
    
    class BankAccount:
        """银行账户类 - 演示封装"""
        
        def __init__(self, account_number, initial_balance=0):
            self.account_number = account_number    # 公开属性
            self._balance = initial_balance         # 受保护属性（约定私有）
            self.__pin = "1234"                    # 私有属性
            self.__transaction_count = 0           # 私有属性
        
        def deposit(self, amount):
            """存款"""
            if amount > 0:
                self._balance += amount
                self.__record_transaction("存款", amount)
                return f"存款成功！当前余额：{self._balance}元"
            else:
                return "存款金额必须大于0"
        
        def withdraw(self, amount, pin):
            """取款"""
            if not self.__validate_pin(pin):
                return "密码错误！"
            
            if amount <= 0:
                return "取款金额必须大于0"
            
            if amount > self._balance:
                return "余额不足！"
            
            self._balance -= amount
            self.__record_transaction("取款", amount)
            return f"取款成功！当前余额：{self._balance}元"
        
        def get_balance(self, pin):
            """查询余额"""
            if self.__validate_pin(pin):
                return f"当前余额：{self._balance}元"
            else:
                return "密码错误！"
        
        def __validate_pin(self, pin):
            """私有方法：验证密码"""
            return pin == self.__pin
        
        def __record_transaction(self, transaction_type, amount):
            """私有方法：记录交易"""
            self.__transaction_count += 1
            print(f"  交易记录：{transaction_type} {amount}元 (第{self.__transaction_count}次交易)")
        
        def change_pin(self, old_pin, new_pin):
            """修改密码"""
            if self.__validate_pin(old_pin):
                self.__pin = new_pin
                return "密码修改成功！"
            else:
                return "原密码错误！"
    
    # 使用银行账户
    account = BankAccount("123456789", 1000)
    
    print("银行账户操作:")
    print(account.deposit(500))
    print(account.withdraw(200, "1234"))
    print(account.get_balance("1234"))
    
    # 尝试错误操作
    print(account.withdraw(100, "0000"))  # 错误密码
    print(account.withdraw(2000, "1234"))  # 余额不足
    
    # 无法直接访问私有属性
    print(f"账户号码: {account.account_number}")  # 可以访问
    print(f"余额（受保护）: {account._balance}")    # 可以访问但不推荐
    # print(account.__pin)  # 错误！无法访问私有属性

def practical_oop_example():
    """面向对象实际应用示例"""
    print("\n" + "=" * 50)
    print("实际应用示例：学生管理系统")
    print("=" * 50)
    
    class Student:
        """学生类"""
        
        def __init__(self, student_id, name, grade):
            self.student_id = student_id
            self.name = name
            self.grade = grade
            self.subjects = {}  # 学科成绩
        
        def add_score(self, subject, score):
            """添加学科成绩"""
            if 0 <= score <= 100:
                self.subjects[subject] = score
                return f"{self.name}的{subject}成绩已记录：{score}分"
            else:
                return "成绩必须在0-100之间！"
        
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
        
        def __str__(self):
            return f"Student(ID:{self.student_id}, 姓名:{self.name}, 年级:{self.grade})"
    
    class Classroom:
        """教室类"""
        
        def __init__(self, class_name):
            self.class_name = class_name
            self.students = []
        
        def add_student(self, student):
            """添加学生"""
            self.students.append(student)
            return f"学生{student.name}已加入{self.class_name}"
        
        def get_class_average(self):
            """计算班级平均分"""
            if not self.students:
                return 0
            
            total_avg = sum(student.get_average() for student in self.students)
            return round(total_avg / len(self.students), 2)
        
        def get_top_students(self, n=3):
            """获取前n名学生"""
            sorted_students = sorted(self.students, 
                                   key=lambda s: s.get_average(), 
                                   reverse=True)
            return sorted_students[:n]
        
        def display_class_info(self):
            """显示班级信息"""
            print(f"\n{self.class_name} 班级信息:")
            print(f"学生人数: {len(self.students)}")
            print(f"班级平均分: {self.get_class_average()}")
            
            print("\n学生详情:")
            for student in self.students:
                avg = student.get_average()
                level = student.get_grade_level()
                print(f"  {student.name}: 平均分{avg}, 等级{level}")
    
    # 使用示例
    # 创建教室
    classroom = Classroom("三年一班")
    
    # 创建学生
    students_data = [
        ("001", "张三", "三年级"),
        ("002", "李四", "三年级"),
        ("003", "王五", "三年级"),
        ("004", "赵六", "三年级")
    ]
    
    students = []
    for student_id, name, grade in students_data:
        student = Student(student_id, name, grade)
        students.append(student)
        classroom.add_student(student)
    
    # 添加成绩
    scores_data = [
        (0, [("数学", 85), ("语文", 90), ("英语", 88)]),  # 张三
        (1, [("数学", 78), ("语文", 85), ("英语", 82)]),  # 李四
        (2, [("数学", 92), ("语文", 88), ("英语", 95)]),  # 王五
        (3, [("数学", 88), ("语文", 92), ("英语", 85)])   # 赵六
    ]
    
    for student_idx, subjects in scores_data:
        for subject, score in subjects:
            result = students[student_idx].add_score(subject, score)
            print(result)
    
    # 显示班级信息
    classroom.display_class_info()
    
    # 显示前三名
    top_students = classroom.get_top_students(3)
    print(f"\n前三名学生:")
    for i, student in enumerate(top_students, 1):
        print(f"  第{i}名: {student.name} (平均分: {student.get_average()})")

def inheritance_advanced_demo():
    """高级继承演示"""
    print("\n" + "=" * 50)
    print("高级继承：方法重写和super()使用")
    print("=" * 50)
    
    class Vehicle:
        """交通工具基类"""
        
        def __init__(self, brand, model, year):
            self.brand = brand
            self.model = model
            self.year = year
            self.fuel = 0
        
        def start(self):
            """启动"""
            return f"{self.brand} {self.model} 启动了！"
        
        def stop(self):
            """停止"""
            return f"{self.brand} {self.model} 停止了！"
        
        def refuel(self, amount):
            """加油"""
            self.fuel += amount
            return f"加油{amount}升，当前油量：{self.fuel}升"
    
    class Car(Vehicle):
        """汽车类"""
        
        def __init__(self, brand, model, year, doors=4):
            super().__init__(brand, model, year)  # 调用父类构造函数
            self.doors = doors
            self.trunk_open = False
        
        def start(self):
            """重写启动方法"""
            base_message = super().start()  # 调用父类方法
            return base_message + " 请系好安全带！"
        
        def open_trunk(self):
            """汽车特有方法"""
            self.trunk_open = True
            return f"{self.brand} {self.model} 的后备箱已打开"
    
    class Motorcycle(Vehicle):
        """摩托车类"""
        
        def __init__(self, brand, model, year, engine_size):
            super().__init__(brand, model, year)
            self.engine_size = engine_size
            self.helmet_on = False
        
        def start(self):
            """重写启动方法"""
            if not self.helmet_on:
                return "请先戴好头盔！"
            return super().start() + " 享受风的感觉吧！"
        
        def wear_helmet(self):
            """戴头盔"""
            self.helmet_on = True
            return "头盔已戴好，安全第一！"
    
    # 使用示例
    car = Car("丰田", "卡罗拉", 2023, doors=4)
    motorcycle = Motorcycle("本田", "CBR600", 2022, 600)
    
    print("交通工具操作:")
    print(car.start())
    print(car.refuel(50))
    print(car.open_trunk())
    
    print(f"\n{motorcycle.start()}")  # 没戴头盔
    print(motorcycle.wear_helmet())
    print(motorcycle.start())  # 戴好头盔后

def composition_demo():
    """组合演示（更灵活的代码复用方式）"""
    print("\n" + "=" * 50)
    print("组合演示：用组合代替继承")
    print("=" * 50)
    
    class Engine:
        """引擎类"""
        
        def __init__(self, horsepower, fuel_type="汽油"):
            self.horsepower = horsepower
            self.fuel_type = fuel_type
            self.running = False
        
        def start(self):
            self.running = True
            return f"{self.horsepower}马力{self.fuel_type}引擎启动！"
        
        def stop(self):
            self.running = False
            return "引擎已停止"
    
    class GPS:
        """GPS导航类"""
        
        def __init__(self):
            self.destination = None
        
        def set_destination(self, address):
            self.destination = address
            return f"目的地设置为：{address}"
        
        def navigate(self):
            if self.destination:
                return f"正在导航到：{self.destination}"
            else:
                return "请先设置目的地"
    
    class Car:
        """汽车类 - 使用组合"""
        
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model
            self.engine = Engine(150)      # 组合：汽车"有一个"引擎
            self.gps = GPS()               # 组合：汽车"有一个"GPS
        
        def start(self):
            """启动汽车"""
            engine_msg = self.engine.start()
            return f"{self.brand} {self.model} 启动！{engine_msg}"
        
        def navigate_to(self, destination):
            """导航到目的地"""
            gps_msg = self.gps.set_destination(destination)
            nav_msg = self.gps.navigate()
            return f"{gps_msg}\n{nav_msg}"
    
    # 使用示例
    my_car = Car("宝马", "X5")
    print(my_car.start())
    print(my_car.navigate_to("北京大学"))

if __name__ == "__main__":
    basic_class_demo()
    inheritance_demo()
    polymorphism_demo()
    encapsulation_demo()
    composition_demo() 