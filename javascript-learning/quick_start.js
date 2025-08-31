#!/usr/bin/env node

/**
 * JavaScript语言快速开始指南
 * 这个文件演示了JavaScript的基本语法和特性，让你快速上手JavaScript编程
 * 
 * 运行方式：
 * - 浏览器：直接在HTML中引入或开发者工具中运行
 * - Node.js：node quick_start.js
 */

// ================================
// 1. 基础语法演示
// ================================
console.log("=".repeat(50));
console.log("⚡ 欢迎来到JavaScript学习世界！");
console.log("=".repeat(50));

// 变量定义 - ES6语法
const name = "JavaScript学习者";  // 常量
let age = 25;                      // 可变变量
var height = 1.75;                 // 函数作用域变量（不推荐）

console.log("\n📝 变量定义：");
console.log(`姓名: ${name}`);
console.log(`年龄: ${age} 岁`);
console.log(`身高: ${height}米`);

// ================================
// 2. 数据类型
// ================================
console.log("\n🎭 数据类型：");

// 基础数据类型
const types = {
    string: "文本",
    number: 42,
    boolean: true,
    undefined: undefined,
    null: null,
    symbol: Symbol("唯一标识"),
    bigint: 123n
};

Object.entries(types).forEach(([type, value]) => {
    console.log(`${type}: ${value} (${typeof value})`);
});

// ================================
// 3. 数组操作
// ================================
console.log("\n📊 数组操作：");

// 创建数组
const languages = ["JavaScript", "TypeScript", "Node.js", "React"];
console.log("编程技术:", languages);

// 数组方法
console.log("第一个技术:", languages[0]);
console.log("最后一个技术:", languages[languages.length - 1]);

// 添加元素
languages.push("Vue.js");
languages.unshift("HTML");
console.log("添加后:", languages);

// 函数式编程方法
const longNames = languages.filter(lang => lang.length > 4);
console.log("长度>4的技术:", longNames);

const upperCased = languages.map(lang => lang.toUpperCase());
console.log("大写:", upperCased);

// ================================
// 4. 对象操作
// ================================
console.log("\n👤 对象操作：");

// 创建对象
const person = {
    name: "张三",
    age: 30,
    city: "北京",
    skills: ["JavaScript", "React", "Node.js"],
    
    // 方法
    introduce() {
        return `我是${this.name}，来自${this.city}，擅长${this.skills.join("、")}`;
    },
    
    // 箭头函数属性
    getAge: () => age // 注意：箭头函数中this指向不同
};

console.log("个人信息:");
console.log(person.introduce());

// 对象解构
const { name: personName, city, skills } = person;
console.log(`解构结果: ${personName} 来自 ${city}`);

// ================================
// 5. 函数定义和使用
// ================================
console.log("\n🎯 函数定义：");

// 函数声明
function calculateSum(a, b) {
    return a + b;
}

// 函数表达式
const calculateProduct = function(a, b) {
    return a * b;
};

// 箭头函数
const calculateDivision = (a, b) => b !== 0 ? a / b : "除数不能为0";

// 默认参数
const greet = (name = "朋友", greeting = "你好") => `${greeting}，${name}！`;

console.log("加法:", calculateSum(10, 5));
console.log("乘法:", calculateProduct(10, 5));
console.log("除法:", calculateDivision(10, 5));
console.log("问候:", greet());
console.log("自定义问候:", greet("小明", "早上好"));

// ================================
// 6. 异步编程演示
// ================================
console.log("\n⏰ 异步编程：");

// Promise
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// 使用async/await
async function asyncExample() {
    console.log("异步操作开始...");
    
    try {
        await delay(1000); // 等待1秒
        console.log("✅ 异步操作完成！");
        
        // 并行异步操作
        const results = await Promise.all([
            Promise.resolve("任务1完成"),
            Promise.resolve("任务2完成"),
            Promise.resolve("任务3完成")
        ]);
        
        console.log("并行结果:", results);
    } catch (error) {
        console.error("❌ 异步操作失败:", error);
    }
}

// 运行异步示例
asyncExample();

// ================================
// 7. 类和面向对象
// ================================
console.log("\n🏗️ 面向对象编程：");

// ES6类
class Student {
    constructor(name, age) {
        this.name = name;
        this.age = age;
        this.courses = [];
    }
    
    // 方法
    addCourse(course) {
        this.courses.push(course);
        console.log(`${this.name} 添加了课程: ${course}`);
    }
    
    study() {
        if (this.courses.length > 0) {
            console.log(`${this.name} 正在学习: ${this.courses.join("、")}`);
        } else {
            console.log(`${this.name} 还没有选择课程`);
        }
    }
    
    // Getter
    get info() {
        return `学生[姓名=${this.name}, 年龄=${this.age}, 课程=${this.courses.length}门]`;
    }
    
    // 静态方法
    static createStudent(name, age) {
        return new Student(name, age);
    }
}

// 使用类
const student = Student.createStudent("李四", 22);
student.addCourse("JavaScript编程");
student.addCourse("React开发");
student.addCourse("Node.js后端");

console.log(student.info);
student.study();

// ================================
// 8. 错误处理
// ================================
console.log("\n🛡️ 错误处理：");

function divide(a, b) {
    if (b === 0) {
        throw new Error("除数不能为零");
    }
    return a / b;
}

try {
    console.log("10 ÷ 2 =", divide(10, 2));
    console.log("10 ÷ 0 =", divide(10, 0)); // 这里会抛出错误
} catch (error) {
    console.error("❌ 捕获到错误:", error.message);
} finally {
    console.log("✅ 错误处理演示完成");
}

// ================================
// 9. 模块化（Node.js环境）
// ================================
if (typeof module !== 'undefined' && module.exports) {
    console.log("\n📦 模块化演示（Node.js）：");
    
    // 导出工具函数
    const utils = {
        formatDate(date) {
            return date.toLocaleDateString('zh-CN');
        },
        
        formatTime(date) {
            return date.toLocaleTimeString('zh-CN');
        },
        
        isWeekend(date) {
            const day = date.getDay();
            return day === 0 || day === 6;
        }
    };
    
    const now = new Date();
    console.log("当前日期:", utils.formatDate(now));
    console.log("当前时间:", utils.formatTime(now));
    console.log("是否周末:", utils.isWeekend(now) ? "是" : "否");
    
    // 导出模块
    module.exports = { Student, utils };
}

// ================================
// 10. 现代JavaScript特性
// ================================
console.log("\n🆕 现代JavaScript特性：");

// 解构赋值
const [first, second, ...rest] = languages;
console.log("第一个技术:", first);
console.log("第二个技术:", second);
console.log("其余技术:", rest);

// 扩展运算符
const newLanguages = [...languages, "Angular", "Express"];
console.log("扩展后的技术栈:", newLanguages);

// 模板字符串
const template = `
🌟 学习总结：
   技术栈: ${newLanguages.join(" | ")}
   总数量: ${newLanguages.length} 项技术
   学习进度: 刚刚开始！
`;
console.log(template);

// Optional Chaining (可选链)
const config = {
    app: {
        name: "我的应用",
        version: "1.0.0",
        database: {
            host: "localhost",
            port: 3306
        }
    }
};

console.log("应用名称:", config?.app?.name);
console.log("数据库端口:", config?.app?.database?.port);
console.log("缓存配置:", config?.app?.cache?.enabled ?? "未配置");

// ================================
// 结束语
// ================================
setTimeout(() => {
    console.log("\n" + "=".repeat(50));
    console.log("🎉 恭喜！你已经体验了JavaScript的主要特性");
    console.log("🚀 现在可以开始系统学习docs/目录中的文档了");
    console.log("💪 记住：多练习，多实践，你会很快成为JavaScript专家！");
    console.log("=".repeat(50));
}, 2000); 