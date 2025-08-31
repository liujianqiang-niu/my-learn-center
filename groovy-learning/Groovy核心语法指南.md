# Groovy核心语法指南 🚀

## 📖 目录
1. [基础语法](#1-基础语法)
2. [集合操作](#2-集合操作)
3. [闭包详解](#3-闭包详解)
4. [面向对象](#4-面向对象)
5. [元编程](#5-元编程)
6. [文件操作](#6-文件操作)
7. [Web开发](#7-web开发)
8. [实战项目](#8-实战项目)

---

## 1. 基础语法

### 变量和类型
```groovy
// 动态类型
def name = "张三"
def age = 25
def height = 175.5

// 静态类型
String title = "程序员"
int score = 95
boolean passed = true

// 字符串插值
println "姓名：$name，年龄：$age"
println "详情：${name}今年${age}岁"
```

### 控制结构
```groovy
// 条件语句
if (score >= 90) {
    println "优秀"
} else if (score >= 60) {
    println "及格"
} else {
    println "不及格"
}

// 循环
for (i in 1..5) {
    println "第${i}次"
}

def fruits = ["苹果", "香蕉", "橘子"]
fruits.each { println "水果：$it" }
```

---

## 2. 集合操作

### List列表
```groovy
def numbers = [1, 2, 3, 4, 5]

// 基础操作
numbers << 6              // 添加元素
println numbers[0]        // 获取第一个
println numbers[-1]       // 获取最后一个
println numbers[1..3]     // 获取子列表

// 高级方法
def doubled = numbers.collect { it * 2 }    // [2, 4, 6, 8, 10, 12]
def evens = numbers.findAll { it % 2 == 0 } // [2, 4, 6]
def sum = numbers.sum()                     // 21
```

### Map字典
```groovy
def person = [
    name: "张三",
    age: 25,
    city: "北京"
]

// 访问和修改
println person.name        // 张三
person.job = "程序员"      // 添加新属性

// 遍历
person.each { key, value ->
    println "$key: $value"
}
```

---

## 3. 闭包详解

### 闭包基础
```groovy
// 定义闭包
def greet = { name ->
    println "Hello, $name!"
}

def add = { a, b ->
    a + b
}

// 调用闭包
greet("张三")
println add(10, 20)

// 单参数闭包（使用it）
def square = { it * it }
println square(5)  // 25
```

### 闭包作为参数
```groovy
def processNumbers(list, operation) {
    list.collect(operation)
}

def numbers = [1, 2, 3, 4, 5]
def squares = processNumbers(numbers) { it * it }
def doubled = processNumbers(numbers) { it * 2 }

println squares  // [1, 4, 9, 16, 25]
println doubled  // [2, 4, 6, 8, 10]
```

---

## 4. 面向对象

### 类定义
```groovy
class Student {
    String name
    int age
    List<String> subjects = []
    
    // 构造函数
    Student(name, age) {
        this.name = name
        this.age = age
    }
    
    // 方法
    def addSubject(subject) {
        subjects << subject
    }
    
    def introduce() {
        println "我是$name，学习${subjects.join('、')}"
    }
}

// 使用
def student = new Student("小明", 20)
student.addSubject("数学")
student.addSubject("编程")
student.introduce()
```

### 继承和特征
```groovy
trait Flyable {
    def fly() {
        println "${this.class.simpleName}在飞"
    }
}

class Bird implements Flyable {
    String name
    Bird(name) { this.name = name }
}

def bird = new Bird("小鸟")
bird.fly()  // Bird在飞
```

---

## 5. 元编程

### 动态方法添加
```groovy
// 为String类添加方法
String.metaClass.isPalindrome = {
    delegate.toLowerCase() == delegate.toLowerCase().reverse()
}

println "madam".isPalindrome()  // true

// 为类动态添加属性
class DynamicClass {}
DynamicClass.metaClass.dynamicProperty = "动态值"
def obj = new DynamicClass()
println obj.dynamicProperty
```

### AST转换注解
```groovy
import groovy.transform.*

@ToString
@EqualsAndHashCode
class Product {
    String name
    double price
    String category
}

def product = new Product(name: "手机", price: 2999.0, category: "电子产品")
println product  // 自动生成toString
```

---

## 6. 文件操作

### 文件读写
```groovy
// 读取文件
def content = new File("test.txt").text
println content

// 按行读取
new File("test.txt").eachLine { line, number ->
    println "$number: $line"
}

// 写入文件
new File("output.txt").text = "Hello Groovy!"

// 追加内容
new File("output.txt") << "\n新的一行"

// 安全操作
def file = new File("data.txt")
if (file.exists()) {
    def lines = file.readLines()
    println "文件有${lines.size()}行"
}
```

---

## 7. Web开发

### 简单HTTP服务器
```groovy
@Grab('io.ratpack:ratpack-groovy:1.9.0')
import static ratpack.groovy.Groovy.ratpack

ratpack {
    handlers {
        get {
            render "Hello Groovy Web!"
        }
        
        get("api/user/:name") { ctx ->
            def name = ctx.pathTokens.name
            render([
                message: "Hello, $name!",
                timestamp: new Date()
            ])
        }
        
        post("api/data") { ctx ->
            ctx.parse(Map).then { data ->
                ctx.render("接收到数据: ${data}")
            }
        }
    }
}
```

### JSON API开发
```groovy
import groovy.json.JsonBuilder

class UserAPI {
    static def users = [
        [id: 1, name: "张三", email: "zhang@email.com"],
        [id: 2, name: "李四", email: "li@email.com"]
    ]
    
    static def getAllUsers() {
        def json = new JsonBuilder(users)
        return json.toPrettyString()
    }
    
    static def createUser(userData) {
        def newId = users.size() + 1
        def newUser = [id: newId] + userData
        users << newUser
        
        def json = new JsonBuilder(newUser)
        return json.toPrettyString()
    }
}

// 使用
println UserAPI.getAllUsers()
println UserAPI.createUser([name: "王五", email: "wang@email.com"])
```

---

## 8. 实战项目

### 项目1：文件管理工具
```groovy
class FileManager {
    def sourceDir
    def backupDir
    
    FileManager(sourceDir, backupDir) {
        this.sourceDir = new File(sourceDir)
        this.backupDir = new File(backupDir)
        
        if (!this.backupDir.exists()) {
            this.backupDir.mkdirs()
        }
    }
    
    def backup() {
        sourceDir.eachFile { file ->
            if (file.isFile()) {
                def backupFile = new File(backupDir, file.name)
                backupFile.text = file.text
                println "备份文件: ${file.name}"
            }
        }
    }
    
    def listBackups() {
        println "备份文件列表："
        backupDir.eachFile { file ->
            println "- ${file.name} (${file.length()} bytes)"
        }
    }
}

// 使用文件管理工具
def manager = new FileManager("documents", "backup")
manager.backup()
manager.listBackups()
```

### 项目2：配置管理器
```groovy
class ConfigManager {
    def config = [:]
    
    def load(configFile) {
        if (new File(configFile).exists()) {
            def binding = new Binding()
            def shell = new GroovyShell(binding)
            shell.evaluate(new File(configFile))
            config.putAll(binding.variables)
        }
        return this
    }
    
    def get(key, defaultValue = null) {
        return config.getOrDefault(key, defaultValue)
    }
    
    def set(key, value) {
        config[key] = value
        return this
    }
    
    def save(configFile) {
        def file = new File(configFile)
        file.text = config.collect { key, value ->
            if (value instanceof String) {
                "$key = '$value'"
            } else {
                "$key = $value"
            }
        }.join('\n')
        return this
    }
}

// 使用配置管理器
def configMgr = new ConfigManager()
configMgr.set("appName", "我的应用")
        .set("version", "1.0.0")
        .set("debug", true)
        .save("app.config")

println "应用名称: ${configMgr.get('appName')}"
```

---

## 🎯 从初学者到专家路径

### 阶段1：语法掌握（第1-2周）
- ✅ 掌握变量、类型、字符串插值
- ✅ 理解集合操作和闭包基础
- ✅ 能够编写简单脚本

### 阶段2：进阶应用（第3-4周）
- ✅ 熟练使用面向对象编程
- ✅ 理解元编程和动态特性
- ✅ 掌握文件和数据处理

### 阶段3：实战开发（第5-8周）
- ✅ 开发Web应用和API
- ✅ 使用测试框架保证质量
- ✅ 掌握构建器和DSL设计

### 阶段4：专家级别（第9周+）
- ✅ 设计复杂的DSL和工具
- ✅ 优化性能和架构
- ✅ 指导他人使用Groovy

---

## 💻 练习建议

1. **每日编码**: 每天至少写30分钟Groovy代码
2. **解决问题**: 用Groovy解决日常的文件处理、数据分析任务
3. **读源码**: 学习Gradle、Spock等优秀项目的源码
4. **写工具**: 为自己开发实用的脚本工具
5. **教别人**: 教别人Groovy是最好的学习方法

**开始您的Groovy专家之路吧！编程愉快！** 🎉 