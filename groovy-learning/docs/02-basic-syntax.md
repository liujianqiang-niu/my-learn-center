# Groovy基础语法详解

## 🎯 学习目标
- 掌握Groovy的变量定义和数据类型
- 理解Groovy与Java的语法差异
- 掌握字符串处理和集合操作
- 学会使用Groovy的简化语法特性

## 🔤 变量和数据类型

### 变量定义
```groovy
// 动态类型定义 - 使用def关键字
def name = "张三"          // 字符串
def age = 25              // 整数
def height = 1.75         // 浮点数
def isStudent = true      // 布尔值

// 显式类型定义（可选）
String firstName = "李"
int score = 95
double salary = 8500.50
boolean married = false

// 打印变量类型
println "name的类型: ${name.class}"
println "age的类型: ${age.class}"
```

### 基础数据类型
```groovy
// Groovy自动装箱，没有原始类型
byte b = 127
short s = 32767
int i = 2147483647
long l = 9223372036854775807L

float f = 3.14f
double d = 3.141592653589793

char c = 'A'
boolean flag = true

// BigInteger和BigDecimal
def bigInt = 123456789123456789123456789G
def bigDec = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938367586366677661732351024633334462090215142604916007202557374317220143522423444559071939829179162299374430
println "BigInteger: $bigInt"
println "BigDecimal: ${bigDec.setScale(2, BigDecimal.ROUND_HALF_UP)}"

// 类型检查
println "bigInt是BigInteger: ${bigInt instanceof BigInteger}"
```

## 📝 字符串操作

### 字符串定义
```groovy
// 单引号字符串（字面值）
def literal = 'Hello World'

// 双引号字符串（支持插值）
def name = "Groovy"
def interpolated = "Hello, $name!"
def expression = "2 + 3 = ${2 + 3}"

// 三重引号字符串（多行）
def multiline = """
这是一个多行字符串，
可以包含换行符，
非常适合写长文本。
当前用户：$name
"""

// 斜杠字符串（正则表达式友好）
def regex = /\d+\.\d+/  // 匹配小数

println literal
println interpolated
println expression
println multiline
```

### 字符串方法
```groovy
def text = "  Groovy Programming  "

// 基础操作
println "原始: '$text'"
println "长度: ${text.length()}"
println "去空格: '${text.trim()}'"
println "大写: '${text.toUpperCase()}'"
println "小写: '${text.toLowerCase()}'"

// 查找和替换
def sentence = "Groovy is awesome, Groovy is powerful"
println "包含awesome: ${sentence.contains('awesome')}"
println "查找Groovy: ${sentence.indexOf('Groovy')}"
println "替换Groovy: ${sentence.replace('Groovy', 'Java')}"
println "替换所有Groovy: ${sentence.replaceAll('Groovy', 'Python')}"

// 分割和连接
def words = "apple,banana,cherry".split(',')
println "分割结果: $words"
println "连接: ${words.join(' | ')}"

// 字符串构建
def builder = new StringBuilder()
builder << "Hello"
builder << " "
builder << "World"
println "构建结果: $builder"
```

## 📊 集合类型

### List（列表）
```groovy
// 创建列表
def fruits = ["apple", "banana", "cherry"]
def numbers = [1, 2, 3, 4, 5]
def mixed = ["text", 42, true, 3.14]

println "水果: $fruits"
println "数字: $numbers"
println "混合: $mixed"

// 访问元素
println "第一个水果: ${fruits[0]}"
println "最后一个水果: ${fruits[-1]}"
println "第2-3个水果: ${fruits[1..2]}"

// 添加和删除
fruits << "orange"           // 添加到末尾
fruits.add(0, "grape")       // 添加到指定位置
fruits.remove("banana")      // 删除元素
println "操作后: $fruits"

// 列表方法
println "列表大小: ${fruits.size()}"
println "是否为空: ${fruits.isEmpty()}"
println "包含apple: ${fruits.contains('apple')}"
println "排序: ${fruits.sort()}"

// 高级操作
def lengths = fruits.collect { it.length() }  // 映射
def longFruits = fruits.findAll { it.length() > 5 }  // 过滤
println "长度: $lengths"
println "长名字的水果: $longFruits"
```

### Map（映射）
```groovy
// 创建映射
def person = [
    name: "张三",
    age: 30,
    city: "北京"
]

// 另一种创建方式
def scores = [:]
scores["语文"] = 95
scores["数学"] = 87
scores["英语"] = 92

println "个人信息: $person"
println "成绩: $scores"

// 访问元素
println "姓名: ${person.name}"        // 点号访问
println "姓名: ${person['name']}"     // 方括号访问
println "年龄: ${person.age}"

// 添加和修改
person.email = "zhangsan@example.com"  // 添加
person['phone'] = "13800138000"        // 添加
person.age = 31                        // 修改

// 遍历映射
person.each { key, value ->
    println "$key: $value"
}

// 映射方法
println "所有键: ${person.keySet()}"
println "所有值: ${person.values()}"
println "包含email: ${person.containsKey('email')}"
```

### Set（集合）
```groovy
// 创建集合
def uniqueNumbers = [1, 2, 3, 2, 1] as Set
def skills = ["Java", "Groovy", "Spring", "Java"] as HashSet

println "去重数字: $uniqueNumbers"
println "技能集合: $skills"

// 集合操作
skills.add("MySQL")
skills.remove("Java")
println "操作后: $skills"

// 集合运算
def set1 = [1, 2, 3, 4] as Set
def set2 = [3, 4, 5, 6] as Set

println "并集: ${set1.union(set2)}"          // 合并
println "交集: ${set1.intersect(set2)}"      // 交集
println "差集: ${set1.minus(set2)}"          // 差集
```

## 🔧 操作符

### 算术操作符
```groovy
def a = 10, b = 3

println "加法: $a + $b = ${a + b}"
println "减法: $a - $b = ${a - b}"
println "乘法: $a * $b = ${a * b}"
println "除法: $a / $b = ${a / b}"
println "整除: $a.intdiv($b) = ${a.intdiv(b)}"
println "取余: $a % $b = ${a % b}"
println "幂运算: $a ** $b = ${a ** b}"

// 字符串操作符
println "字符串相加: 'Hello' + ' World' = ${'Hello' + ' World'}"
println "字符串重复: 'Ha' * 3 = ${'Ha' * 3}"
```

### 比较操作符
```groovy
def x = 10, y = 20

println "等于: $x == $y = ${x == y}"
println "不等于: $x != $y = ${x != y}"  
println "小于: $x < $y = ${x < y}"
println "大于: $x > $y = ${x > y}"
println "小于等于: $x <= $y = ${x <= y}"
println "大于等于: $x >= $y = ${x >= y}"

// 太空船操作符（三向比较）
println "太空船: $x <=> $y = ${x <=> y}"  // -1, 0, 1

// 字符串比较
def str1 = "apple", str2 = "banana"
println "字符串比较: $str1 <=> $str2 = ${str1 <=> str2}"
```

### 逻辑操作符
```groovy
def flag1 = true, flag2 = false

println "与: $flag1 && $flag2 = ${flag1 && flag2}"
println "或: $flag1 || $flag2 = ${flag1 || flag2}"
println "非: !$flag1 = ${!flag1}"

// Elvis操作符（空值处理）
def nullable = null
def result = nullable ?: "默认值"
println "Elvis操作符: $result"

// 安全调用操作符
def obj = null
def length = obj?.length()  // 如果obj为null，返回null而不是异常
println "安全调用: $length"
```

### 特殊操作符
```groovy
// 扩展操作符
def list = [[1, 2], [3, 4], [5, 6]]
def flattened = list.flatten()
println "展开前: $list"
println "展开后: $flattened"

// 范围操作符
def range1 = 1..5         // 包含结束值
def range2 = 1..<5        // 不包含结束值
def letters = 'a'..'e'    // 字符范围

println "范围1: $range1"
println "范围2: $range2"  
println "字母: $letters"

// 在操作符
println "3在范围内: ${3 in range1}"
println "6在范围内: ${6 in range1}"

// 正则表达式操作符
def pattern = ~/\d+/
def text = "我有123个苹果和456个橙子"
println "匹配: ${text =~ pattern}"      // 找到所有匹配
println "精确匹配: ${text ==~ /.*\d+.*/}"  // 整个字符串匹配
```

## 🔄 控制流

### 条件语句
```groovy
def score = 85

// if-else语句
if (score >= 90) {
    println "优秀"
} else if (score >= 80) {
    println "良好"
} else if (score >= 60) {
    println "及格"
} else {
    println "不及格"
}

// 三元操作符
def result = score >= 60 ? "及格" : "不及格"
println "三元操作符结果: $result"

// switch语句
def grade = 'B'
switch (grade) {
    case 'A':
        println "优秀"
        break
    case 'B':
    case 'C':
        println "良好"
        break
    case 'D':
        println "及格"
        break
    default:
        println "不及格"
}

// Groovy增强的switch
def value = 42
switch (value) {
    case 0..10:
        println "小数"
        break
    case [20, 30, 40]:
        println "特定值"
        break
    case Integer:
        println "整数类型"
        break
    case { it > 50 }:
        println "大于50"
        break
    default:
        println "其他"
}
```

### 循环语句
```groovy
// for循环
println "传统for循环:"
for (int i = 0; i < 5; i++) {
    print "$i "
}
println()

// for-in循环（推荐）
println "for-in循环:"
for (item in [1, 2, 3, 4, 5]) {
    print "$item "
}
println()

// 范围循环
println "范围循环:"
for (i in 1..5) {
    print "$i "
}
println()

// while循环
println "while循环:"
def count = 0
while (count < 3) {
    print "第${count + 1}次 "
    count++
}
println()

// each方法（Groovy风格）
println "each方法:"
[1, 2, 3].each { item ->
    print "$item "
}
println()

// eachWithIndex
println "带索引的each:"
['a', 'b', 'c'].eachWithIndex { item, index ->
    println "索引$index: $item"
}
```

## 🎯 方法定义

### 基础方法
```groovy
// 简单方法定义
def greet(name) {
    return "Hello, $name!"
}

// 无return的方法（最后一行自动返回）
def add(a, b) {
    a + b
}

// 显式类型的方法
String formatName(String firstName, String lastName) {
    "$lastName, $firstName"
}

// 使用方法
println greet("World")
println add(10, 20)
println formatName("三", "张")
```

### 默认参数
```groovy
def createUser(name, age = 18, city = "北京") {
    [name: name, age: age, city: city]
}

// 调用方法
println createUser("张三")                    // 使用默认值
println createUser("李四", 25)               // 部分默认值
println createUser("王五", 30, "上海")        // 全部指定
```

### 可变参数
```groovy
def sum(int... numbers) {
    numbers.inject(0) { acc, val -> acc + val }
}

def concatenate(String separator, String... words) {
    words.join(separator)
}

println "求和: ${sum(1, 2, 3, 4, 5)}"
println "连接: ${concatenate(' | ', 'apple', 'banana', 'cherry')}"
```

### 命名参数
```groovy
def createPerson(Map args) {
    def defaults = [age: 18, city: "未知"]
    def person = defaults + args  // 合并映射
    "姓名: ${person.name}, 年龄: ${person.age}, 城市: ${person.city}"
}

// 使用命名参数
println createPerson(name: "张三")
println createPerson(name: "李四", age: 25)
println createPerson(name: "王五", age: 30, city: "深圳")
```

## 🏗️ 面向对象基础

### 类定义
```groovy
// 简单类定义
class Person {
    // 属性（自动生成getter/setter）
    String name
    int age
    
    // 构造方法
    Person(String name, int age) {
        this.name = name
        this.age = age
    }
    
    // 方法
    def introduce() {
        "我是$name，今年${age}岁"
    }
    
    // toString方法
    String toString() {
        "Person(name: $name, age: $age)"
    }
}

// 使用类
def person = new Person("张三", 25)
println person.introduce()
println person

// 属性访问
println "姓名: ${person.name}"
person.age = 26
println "修改后年龄: ${person.age}"
```

### 构造函数和属性
```groovy
class Book {
    String title
    String author
    double price
    Date publishDate = new Date()  // 默认值
    
    // 默认构造函数（Groovy自动生成）
    
    // 带参数构造函数
    Book(String title, String author, double price) {
        this.title = title
        this.author = author
        this.price = price
    }
    
    // 属性验证
    void setPrice(double price) {
        if (price < 0) {
            throw new IllegalArgumentException("价格不能为负数")
        }
        this.price = price
    }
}

// 使用不同的构造方式
def book1 = new Book()
book1.title = "Groovy教程"
book1.author = "专家"
book1.price = 59.9

def book2 = new Book("Java编程", "大师", 79.9)

println "书籍1: $book1.title - ¥$book1.price"
println "书籍2: $book2.title - ¥$book2.price"
```

## 🎨 Groovy特色语法

### 简化语法
```groovy
// 省略分号（可选）
def x = 10
def y = 20

// 省略方法调用的括号
println "Hello World"  // 等同于 println("Hello World")

// 属性访问语法
def list = [1, 2, 3]
println list.size      // 等同于 list.size()
println list.class     // 等同于 list.getClass()

// return关键字可选
def multiply(a, b) {
    a * b  // 自动返回最后一个表达式
}

// 类型声明可选
def process(data) {  // 参数类型可选
    data.toString().toUpperCase()
}
```

### 安全导航
```groovy
class User {
    String name
    Address address
}

class Address {
    String street
    String city
}

def user = new User(name: "张三")

// 传统方式（可能抛出NullPointerException）
// println user.address.city  // 危险！

// 安全导航操作符
println "城市: ${user.address?.city}"  // 返回null，不抛异常
println "街道: ${user?.address?.street ?: '未知'}"  // 组合Elvis操作符
```

### GString（格式化字符串）
```groovy
def name = "Groovy"
def version = 4.0

// 简单插值
def simple = "语言: $name, 版本: $version"

// 表达式插值
def expression = "计算: ${10 + 20} = ${30}"

// 方法调用插值
def method = "当前时间: ${new Date().format('yyyy-MM-dd HH:mm:ss')}"

println simple
println expression  
println method

// 延迟求值
def lazy = "随机数: ${-> new Random().nextInt(100)}"
println lazy  // 每次打印都会生成新的随机数
println lazy
```

## 📋 练习题

### 练习1：基础操作
```groovy
// 创建一个包含你朋友姓名的列表
// 筛选出姓名长度大于2的朋友
// 将结果转换为大写并排序

// 你的答案：

```

### 练习2：字符串处理
```groovy
// 给定一个句子，统计每个单词的长度
def sentence = "Groovy makes Java development easier"

// 你的答案：

```

### 练习3：映射操作
```groovy
// 创建一个学生成绩映射
// 计算平均分并找出最高分的科目

// 你的答案：

```

## 💡 最佳实践

### 1. 变量命名
```groovy
// 好的命名
def userName = "张三"
def userAge = 25
def isActive = true

// 避免的命名
def a = "张三"        // 太简短
def user_name = "张三" // 不符合驼峰命名
```

### 2. 使用def vs 显式类型
```groovy
// 使用def（推荐用于局部变量）
def count = 0
def message = "Hello"

// 使用显式类型（推荐用于方法参数和返回值）
String processMessage(String input) {
    input.trim().toUpperCase()
}
```

### 3. 集合初始化
```groovy
// 推荐方式
def fruits = ["apple", "banana", "cherry"]
def scores = [math: 90, english: 85]

// 不推荐
def list = new ArrayList()
list.add("apple")
list.add("banana")
```

## 🎯 小结

本章我们学习了：

✅ **变量定义**：def关键字和动态类型  
✅ **数据类型**：基础类型和自动装箱  
✅ **字符串处理**：插值、多行字符串、字符串方法  
✅ **集合操作**：List、Map、Set的使用  
✅ **操作符**：算术、比较、逻辑、特殊操作符  
✅ **控制流**：条件语句、循环语句  
✅ **方法定义**：参数、返回值、命名参数  
✅ **面向对象**：类、对象、属性访问  
✅ **Groovy特色**：简化语法、安全导航、GString  

### 下一步
学习**03-control-flow.md**，深入掌握Groovy的控制结构和程序流程。 