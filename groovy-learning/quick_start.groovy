#!/usr/bin/env groovy

/**
 * Groovy语言快速开始指南
 * 这个文件演示了Groovy的基本语法和特性，让你快速上手Groovy编程
 * 
 * 运行方式：groovy quick_start.groovy
 */

// ================================
// 1. 基础语法演示
// ================================
println "=" * 50
println "🚀 欢迎来到Groovy学习世界！"
println "=" * 50

// 变量定义 - 动态类型
def name = "Groovy学习者"
def age = 25
def height = 1.75

println "\n📝 变量定义："
println "姓名: $name"
println "年龄: $age 岁"
println "身高: ${height}米"

// ================================
// 2. 字符串处理
// ================================
println "\n🔤 字符串处理："

// 字符串插值
String greeting = "你好，$name！今年${age}岁了"
println greeting

// 多行字符串
def multilineText = """
这是一个多行字符串，
可以包含换行符，
非常方便！
"""
println multilineText

// 字符串方法
def text = "  Groovy很棒！  "
println "原始: '$text'"
println "去空格: '${text.trim()}'"
println "大写: '${text.toUpperCase()}'"
println "反转: '${text.reverse()}'"

// ================================
// 3. 集合操作
// ================================
println "\n📊 集合操作："

// 列表（List）
def languages = ["Java", "Groovy", "Kotlin", "Scala"]
println "编程语言: $languages"
println "第一个语言: ${languages[0]}"
println "最后一个语言: ${languages[-1]}"

// 添加元素
languages << "Clojure"
languages.add("Frege")
println "添加后: $languages"

// 列表操作
def longNames = languages.findAll { it.length() > 4 }
println "长度>4的语言: $longNames"

// 映射（Map）
def person = [
    name: "张三",
    age: 30,
    city: "北京",
    skills: ["Java", "Groovy", "Spring"]
]

println "\n👤 个人信息:"
person.each { key, value ->
    println "  $key: $value"
}

// ================================
// 4. 闭包（Closures）
// ================================
println "\n🎯 闭包演示："

// 简单闭包
def greet = { msg -> println "Hello, $msg!" }
greet("World")

// 遍历闭包
def numbers = [1, 2, 3, 4, 5]
println "数字列表: $numbers"

// 使用闭包进行函数式编程
def doubled = numbers.collect { it * 2 }
println "翻倍后: $doubled"

def evenNumbers = numbers.findAll { it % 2 == 0 }
println "偶数: $evenNumbers"

def sum = numbers.inject(0) { acc, val -> acc + val }
println "总和: $sum"

// ================================
// 5. 面向对象编程
// ================================
println "\n🏗️ 面向对象编程："

// 简单的类定义
class Student {
    String name
    int age
    List<String> courses = []
    
    // 构造器
    Student(String name, int age) {
        this.name = name
        this.age = age
    }
    
    // 方法
    void addCourse(String course) {
        courses << course
    }
    
    void study() {
        println "$name 正在学习: ${courses.join(', ')}"
    }
    
    // toString方法
    String toString() {
        return "学生[姓名=$name, 年龄=$age, 课程=${courses.size()}门]"
    }
}

// 创建和使用对象
def student = new Student("李四", 22)
student.addCourse("Java编程")
student.addCourse("Groovy开发")
student.addCourse("数据库设计")

println student
student.study()

// ================================
// 6. 文件操作
// ================================
println "\n📁 文件操作："

// 写文件
def tempFile = new File("temp_example.txt")
tempFile.text = """这是一个临时文件
用来演示Groovy的文件操作
创建时间: ${new Date()}
"""

println "文件已创建: ${tempFile.name}"
println "文件大小: ${tempFile.size()} 字节"

// 读文件
println "文件内容："
tempFile.eachLine { line, number ->
    println "  第${number}行: $line"
}

// 清理临时文件
tempFile.delete()
println "临时文件已删除"

// ================================
// 7. JSON处理
// ================================
println "\n🌐 JSON处理："

import groovy.json.JsonBuilder
import groovy.json.JsonSlurper

// 创建JSON
def jsonBuilder = new JsonBuilder()
jsonBuilder {
    name "Groovy学习"
    version "1.0"
    features([
        "动态类型",
        "闭包支持",
        "Java集成",
        "DSL构建"
    ])
    author {
        name "开发者"
        email "developer@example.com"
    }
}

def jsonText = jsonBuilder.toPrettyString()
println "生成的JSON:"
println jsonText

// 解析JSON
def jsonSlurper = new JsonSlurper()
def parsedJson = jsonSlurper.parseText(jsonText)
println "\n解析后的数据:"
println "项目名称: ${parsedJson.name}"
println "版本: ${parsedJson.version}"
println "作者: ${parsedJson.author.name}"
println "特性: ${parsedJson.features.join(', ')}"

// ================================
// 8. 脚本特性
// ================================
println "\n⚡ 脚本特性演示："

// 命令执行
if (System.getProperty("os.name").toLowerCase().contains("linux")) {
    def result = "ls -la".execute()
    result.waitFor()
    if (result.exitValue() == 0) {
        println "当前目录文件列表："
        result.text.split('\n')[0..5].each { line ->
            if (line.trim()) println "  $line"
        }
        println "  ..."
    }
}

// 日期处理
Date now = new Date()
println "当前时间: ${now.format('yyyy-MM-dd HH:mm:ss')}"

// 随机数生成
Random random = new Random()
def luckyNumbers = (1..5).collect { random.nextInt(100) }
println "幸运数字: $luckyNumbers"

// ================================
// 9. 动态特性演示
// ================================
println "\n🎭 动态特性："

// 动态方法调用
class Calculator {
    def add(a, b) { a + b }
    def subtract(a, b) { a - b }
    def multiply(a, b) { a * b }
    def divide(a, b) { b != 0 ? a / b : "除数不能为0" }
}

def calc = new Calculator()
def operations = ["add", "subtract", "multiply", "divide"]
def a = 10, b = 3

operations.each { operation ->
    def result = calc."$operation"(a, b)
    println "$operation($a, $b) = $result"
}

// ================================
// 10. 构建器模式演示
// ================================
println "\n🏗️ 构建器模式："

// 简单的构建器
class EmailBuilder {
    String to
    String subject  
    String body
    List<String> attachments = []
    
    EmailBuilder to(String to) {
        this.to = to
        return this
    }
    
    EmailBuilder subject(String subject) {
        this.subject = subject
        return this
    }
    
    EmailBuilder body(String body) {
        this.body = body
        return this
    }
    
    EmailBuilder attach(String file) {
        attachments << file
        return this
    }
    
    void send() {
        println "📧 邮件发送:"
        println "  收件人: $to"
        println "  主题: $subject"
        println "  正文: $body"
        if (attachments) {
            println "  附件: ${attachments.join(', ')}"
        }
        println "  ✅ 邮件发送成功！"
    }
}

// 使用构建器
new EmailBuilder()
    .to("student@example.com")
    .subject("Groovy学习资料")
    .body("这里是你的Groovy学习资料，请查收！")
    .attach("groovy_guide.pdf")
    .attach("examples.zip")
    .send()

// ================================
// 结束语
// ================================
println "\n" + "=" * 50
println "🎉 恭喜！你已经体验了Groovy的主要特性"
println "🚀 现在可以开始系统学习docs/目录中的文档了"
println "💪 记住：多练习，多实践，你会很快成为Groovy专家！"
println "=" * 50 