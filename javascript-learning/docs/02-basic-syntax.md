# JavaScript基础语法详解

## 🎯 学习目标
- 掌握JavaScript的变量定义和数据类型
- 理解动态类型和类型转换
- 掌握运算符和表达式的使用
- 学会基本的控制流语句

## 🔤 变量和数据类型

### 变量声明
```javascript
// ES6+推荐语法
const name = "JavaScript学习者";  // 常量，不可重新赋值
let age = 25;                     // 可变变量，块作用域
var height = 1.75;                // 函数作用域（不推荐使用）

// const的特点
const person = { name: "张三", age: 30 };
// person = {};  // 错误！不能重新赋值
person.age = 31;  // 正确！可以修改对象属性

console.log("姓名:", name);
console.log("年龄:", age);
console.log("身高:", height);
console.log("个人信息:", person);
```

### 基础数据类型
```javascript
// 1. 字符串 (String)
const str1 = "双引号字符串";
const str2 = '单引号字符串';
const str3 = `模板字符串可以插值: ${name}`;

console.log("字符串类型:", typeof str1);
console.log("模板字符串:", str3);

// 2. 数字 (Number)
const integer = 42;
const float = 3.14159;
const scientific = 1.5e10;  // 科学计数法
const infinity = Infinity;
const notANumber = NaN;

console.log("整数:", integer);
console.log("浮点数:", float);
console.log("科学计数:", scientific);
console.log("是数字吗:", isNaN(notANumber));

// 3. 布尔值 (Boolean)
const isTrue = true;
const isFalse = false;

console.log("布尔类型:", typeof isTrue);

// 4. undefined 和 null
let undefinedVar;          // 声明但未赋值
const nullVar = null;      // 明确的空值

console.log("undefined:", undefinedVar);
console.log("null:", nullVar);
console.log("undefined类型:", typeof undefinedVar);
console.log("null类型:", typeof nullVar);  // 注意：返回"object"

// 5. Symbol (ES6新增)
const sym1 = Symbol('id');
const sym2 = Symbol('id');
console.log("Symbol相等吗:", sym1 === sym2);  // false，每个Symbol都是唯一的

// 6. BigInt (ES2020新增)
const bigNumber = 123456789012345678901234567890n;
console.log("BigInt:", bigNumber);
console.log("BigInt类型:", typeof bigNumber);
```

### 类型检查和转换
```javascript
// typeof操作符
console.log("\n🔍 类型检查:");
console.log("typeof 42:", typeof 42);
console.log("typeof 'hello':", typeof "hello");
console.log("typeof true:", typeof true);
console.log("typeof {}:", typeof {});
console.log("typeof []:", typeof []);
console.log("typeof function(){}:", typeof function(){});

// 类型转换
console.log("\n🔄 类型转换:");

// 转为字符串
console.log("数字转字符串:", String(123));
console.log("布尔转字符串:", String(true));
console.log("使用toString:", (42).toString());

// 转为数字
console.log("字符串转数字:", Number("123"));
console.log("parseInt:", parseInt("123.45"));
console.log("parseFloat:", parseFloat("123.45"));
console.log("一元+操作符:", +"123");

// 转为布尔值
console.log("Boolean(1):", Boolean(1));
console.log("Boolean(0):", Boolean(0));
console.log("Boolean(''):", Boolean(""));
console.log("Boolean('hello'):", Boolean("hello"));

// 隐式类型转换
console.log("字符串+数字:", "5" + 3);      // "53"
console.log("字符串-数字:", "5" - 3);      // 2
console.log("布尔值计算:", true + 1);       // 2
```

## 📝 字符串操作

### 字符串方法
```javascript
const text = "  JavaScript Programming  ";

console.log("\n🔤 字符串方法:");
console.log("原始:", `'${text}'`);
console.log("长度:", text.length);
console.log("去空格:", `'${text.trim()}'`);
console.log("大写:", text.toUpperCase());
console.log("小写:", text.toLowerCase());

// 查找和提取
const sentence = "JavaScript is awesome, JavaScript is powerful";
console.log("查找位置:", sentence.indexOf("JavaScript"));
console.log("最后位置:", sentence.lastIndexOf("JavaScript"));
console.log("包含awesome:", sentence.includes("awesome"));
console.log("以Java开头:", sentence.startsWith("Java"));
console.log("以ful结尾:", sentence.endsWith("ful"));

// 切片和分割
console.log("切片[0,10]:", sentence.slice(0, 10));
console.log("子字符串:", sentence.substring(0, 10));
console.log("分割:", sentence.split(" "));

// 替换
console.log("替换第一个:", sentence.replace("JavaScript", "Python"));
console.log("替换全部:", sentence.replaceAll("JavaScript", "Python"));
```

### 模板字符串
```javascript
const user = {
    name: "张三",
    age: 30,
    skills: ["JavaScript", "React", "Node.js"]
};

// 多行模板字符串
const profile = `
🧑‍💻 用户档案
==================
姓名: ${user.name}
年龄: ${user.age} 岁
技能: ${user.skills.join(" | ")}
注册时间: ${new Date().toLocaleDateString()}
总技能数: ${user.skills.length}
是否成年: ${user.age >= 18 ? "是" : "否"}
`;

console.log(profile);

// 标签模板字符串（高级用法）
function highlight(strings, ...values) {
    let result = '';
    strings.forEach((string, i) => {
        result += string;
        if (i < values.length) {
            result += `**${values[i]}**`;  // 高亮显示
        }
    });
    return result;
}

const highlighted = highlight`用户 ${user.name} 年龄 ${user.age} 岁`;
console.log("高亮字符串:", highlighted);
```

## 📊 数组操作

### 数组创建和基本操作
```javascript
// 创建数组
const fruits = ["apple", "banana", "cherry"];
const numbers = [1, 2, 3, 4, 5];
const mixed = ["text", 42, true, null, { key: "value" }];

console.log("\n📊 数组基本操作:");
console.log("水果:", fruits);
console.log("数字:", numbers);
console.log("混合:", mixed);

// 访问元素
console.log("第一个水果:", fruits[0]);
console.log("最后一个水果:", fruits[fruits.length - 1]);
console.log("数组长度:", fruits.length);

// 修改数组
fruits.push("orange");        // 末尾添加
fruits.unshift("grape");      // 开头添加
const removed = fruits.pop(); // 末尾移除
console.log("移除的元素:", removed);
console.log("修改后:", fruits);
```

### 数组高级方法
```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log("\n🎯 数组高级方法:");

// 遍历方法
console.log("forEach遍历:");
numbers.forEach((num, index) => {
    if (index < 3) console.log(`  索引${index}: ${num}`);
});

// 转换方法
const doubled = numbers.map(num => num * 2);
console.log("翻倍:", doubled);

const squared = numbers.map(num => ({ original: num, squared: num ** 2 }));
console.log("平方对象:", squared);

// 过滤方法
const evenNumbers = numbers.filter(num => num % 2 === 0);
const oddNumbers = numbers.filter(num => num % 2 !== 0);
console.log("偶数:", evenNumbers);
console.log("奇数:", oddNumbers);

// 查找方法
const found = numbers.find(num => num > 5);
const foundIndex = numbers.findIndex(num => num > 5);
console.log("第一个大于5的数:", found);
console.log("其索引:", foundIndex);

// 归约方法
const sum = numbers.reduce((acc, num) => acc + num, 0);
const product = numbers.reduce((acc, num) => acc * num, 1);
console.log("求和:", sum);
console.log("求积:", product);

// 测试方法
const allPositive = numbers.every(num => num > 0);
const hasEven = numbers.some(num => num % 2 === 0);
console.log("全为正数:", allPositive);
console.log("包含偶数:", hasEven);
```

## 📦 对象操作

### 对象创建和属性访问
```javascript
console.log("\n👤 对象操作:");

// 对象字面量
const student = {
    name: "李四",
    age: 22,
    courses: ["JavaScript", "React", "Node.js"],
    
    // 方法
    introduce() {
        return `我是${this.name}，正在学习${this.courses.join("、")}`;
    },
    
    // 计算属性名
    [`total_courses`]: function() {
        return this.courses.length;
    }
};

// 属性访问
console.log("点号访问:", student.name);
console.log("方括号访问:", student['age']);
console.log("方法调用:", student.introduce());

// 动态属性
const prop = "courses";
console.log("动态属性:", student[prop]);
```

### 对象方法和操作
```javascript
// 添加和删除属性
student.email = "lisi@example.com";  // 添加
student['phone'] = "13800138000";    // 添加
delete student.phone;                // 删除

console.log("修改后的学生:", student);

// Object静态方法
console.log("\n🔧 Object方法:");
console.log("所有键:", Object.keys(student));
console.log("所有值:", Object.values(student));
console.log("键值对:", Object.entries(student));

// 对象合并
const defaults = { theme: "light", language: "zh-CN" };
const userSettings = { theme: "dark", fontSize: 14 };
const finalSettings = Object.assign({}, defaults, userSettings);
// 或使用扩展语法
const finalSettings2 = { ...defaults, ...userSettings };

console.log("合并结果:", finalSettings);
console.log("扩展语法:", finalSettings2);

// 对象冻结和密封
const immutableObj = Object.freeze({ value: 42 });
// immutableObj.value = 100;  // 严格模式下会报错
console.log("冻结对象:", immutableObj);
```

## 🔧 运算符

### 算术运算符
```javascript
console.log("\n➕ 算术运算符:");

const a = 15, b = 4;
console.log(`${a} + ${b} =`, a + b);    // 加法
console.log(`${a} - ${b} =`, a - b);    // 减法  
console.log(`${a} * ${b} =`, a * b);    // 乘法
console.log(`${a} / ${b} =`, a / b);    // 除法
console.log(`${a} % ${b} =`, a % b);    // 求余
console.log(`${a} ** ${b} =`, a ** b);  // 幂运算（ES2016）

// 自增自减
let counter = 10;
console.log("前置自增:", ++counter);  // 11
console.log("后置自增:", counter++);  // 11，然后变成12
console.log("最终值:", counter);     // 12
```

### 比较运算符
```javascript
console.log("\n⚖️ 比较运算符:");

const x = 5, y = "5";

// 相等性比较
console.log("== (相等):", x == y);     // true，类型转换
console.log("=== (严格相等):", x === y); // false，不转换类型
console.log("!= (不等):", x != y);     // false
console.log("!== (严格不等):", x !== y); // true

// 大小比较
console.log("5 > 3:", 5 > 3);
console.log("5 < 3:", 5 < 3);
console.log("5 >= 5:", 5 >= 5);
console.log("5 <= 4:", 5 <= 4);

// 特殊值比较
console.log("null == undefined:", null == undefined);   // true
console.log("null === undefined:", null === undefined); // false
console.log("NaN === NaN:", NaN === NaN);              // false
console.log("Object.is(NaN, NaN):", Object.is(NaN, NaN)); // true
```

### 逻辑运算符
```javascript
console.log("\n🧠 逻辑运算符:");

const isAdult = true;
const hasLicense = false;

console.log("&& (与):", isAdult && hasLicense);  // false
console.log("|| (或):", isAdult || hasLicense);  // true  
console.log("! (非):", !isAdult);               // false

// 短路求值
console.log("短路与:", false && console.log("不会执行"));
console.log("短路或:", true || console.log("不会执行"));

// 空值合并操作符 (ES2020)
const userInput = null;
const defaultValue = userInput ?? "默认值";
console.log("空值合并:", defaultValue);

// 可选链操作符 (ES2020)
const user = { profile: { name: "张三" } };
console.log("可选链:", user?.profile?.name);      // "张三"
console.log("可选链null:", user?.settings?.theme); // undefined
```

## 🏗️ 函数基础

### 函数定义方式
```javascript
console.log("\n🎯 函数定义:");

// 1. 函数声明（会被提升）
function add(a, b) {
    return a + b;
}

// 2. 函数表达式
const subtract = function(a, b) {
    return a - b;
};

// 3. 箭头函数 (ES6)
const multiply = (a, b) => a * b;

// 4. 简化的箭头函数
const square = x => x * x;
const greet = () => "Hello!";

console.log("函数声明:", add(10, 5));
console.log("函数表达式:", subtract(10, 5));
console.log("箭头函数:", multiply(10, 5));
console.log("简化箭头函数:", square(5));
console.log("无参箭头函数:", greet());
```

### 函数参数
```javascript
console.log("\n📋 函数参数:");

// 默认参数 (ES6)
function createUser(name, age = 18, city = "北京") {
    return { name, age, city };
}

// 剩余参数 (ES6)
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

// 解构参数
function displayPerson({ name, age, city = "未知" }) {
    return `${name}，${age}岁，来自${city}`;
}

console.log("默认参数:", createUser("张三"));
console.log("部分参数:", createUser("李四", 25));
console.log("全部参数:", createUser("王五", 30, "上海"));

console.log("剩余参数:", sum(1, 2, 3, 4, 5));
console.log("解构参数:", displayPerson({ name: "赵六", age: 28 }));
```

## 🎛️ 控制流语句

### 条件语句
```javascript
console.log("\n🔀 条件语句:");

const score = 85;

// if-else语句
if (score >= 90) {
    console.log("成绩等级: 优秀");
} else if (score >= 80) {
    console.log("成绩等级: 良好");
} else if (score >= 60) {
    console.log("成绩等级: 及格");
} else {
    console.log("成绩等级: 不及格");
}

// 三元运算符
const result = score >= 60 ? "及格" : "不及格";
console.log("三元运算符:", result);

// switch语句
const grade = "B";
switch (grade) {
    case "A":
        console.log("优秀");
        break;
    case "B":
    case "C":
        console.log("良好");
        break;
    case "D":
        console.log("及格");
        break;
    default:
        console.log("不及格");
}
```

### 循环语句
```javascript
console.log("\n🔄 循环语句:");

// for循环
console.log("传统for循环:");
for (let i = 0; i < 5; i++) {
    process.stdout.write(`${i} `);
}
console.log();

// for...of循环（遍历值）
const colors = ["red", "green", "blue"];
console.log("for...of遍历值:");
for (const color of colors) {
    process.stdout.write(`${color} `);
}
console.log();

// for...in循环（遍历键/索引）
console.log("for...in遍历索引:");
for (const index in colors) {
    console.log(`  索引${index}: ${colors[index]}`);
}

// while循环
console.log("while循环:");
let count = 0;
while (count < 3) {
    process.stdout.write(`第${count + 1}次 `);
    count++;
}
console.log();

// do-while循环
console.log("do-while循环:");
let num = 0;
do {
    process.stdout.write(`${num} `);
    num++;
} while (num < 3);
console.log();
```

### 循环控制
```javascript
console.log("\n🎮 循环控制:");

// break和continue
for (let i = 1; i <= 10; i++) {
    if (i === 3) continue;  // 跳过3
    if (i === 8) break;     // 在8处停止
    process.stdout.write(`${i} `);
}
console.log("\n循环结束");

// 标签和嵌套循环控制
outer: for (let i = 1; i <= 3; i++) {
    inner: for (let j = 1; j <= 3; j++) {
        if (i === 2 && j === 2) {
            console.log(`跳出外层循环在 i=${i}, j=${j}`);
            break outer;
        }
        console.log(`i=${i}, j=${j}`);
    }
}
```

## 🎨 现代JavaScript语法

### 解构赋值
```javascript
console.log("\n🎁 解构赋值:");

// 数组解构
const [first, second, third] = ["a", "b", "c"];
console.log("数组解构:", { first, second, third });

// 跳过元素和剩余语法
const [head, , ...tail] = [1, 2, 3, 4, 5];
console.log("头部:", head);
console.log("尾部:", tail);

// 对象解构
const person = { name: "张三", age: 30, city: "北京" };
const { name, age, city } = person;
console.log("对象解构:", { name, age, city });

// 重命名和默认值
const { name: personName, age: personAge, email = "未提供" } = person;
console.log("重命名解构:", { personName, personAge, email });

// 嵌套解构
const company = {
    name: "科技公司",
    address: {
        street: "中关村大街",
        city: "北京"
    }
};

const { address: { street, city: companyCity } } = company;
console.log("嵌套解构:", { street, companyCity });
```

### 扩展语法
```javascript
console.log("\n🎈 扩展语法:");

// 数组扩展
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];
console.log("数组合并:", combined);

// 对象扩展
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const combinedObj = { ...obj1, ...obj2, e: 5 };
console.log("对象合并:", combinedObj);

// 函数调用中的扩展
function showArgs(a, b, c) {
    console.log("参数:", { a, b, c });
}
showArgs(...arr1);

// 数组复制
const originalArray = [1, 2, 3];
const copiedArray = [...originalArray];
copiedArray.push(4);
console.log("原数组:", originalArray);
console.log("复制数组:", copiedArray);
```

## 📋 练习题

### 练习1：变量和类型
```javascript
// 声明不同类型的变量并检查其类型
// 练习类型转换

// 你的答案：

```

### 练习2：字符串处理
```javascript
// 给定一个句子，编写程序：
// 1. 统计单词数量
// 2. 找出最长的单词
// 3. 将每个单词首字母大写

const sentence = "javascript is a powerful programming language";

// 你的答案：

```

### 练习3：数组操作
```javascript
// 给定一个数字数组，编写程序：
// 1. 找出所有偶数
// 2. 计算所有数字的平均值
// 3. 找出最大值和最小值

const numbers = [23, 45, 12, 67, 34, 89, 56, 78, 90, 11];

// 你的答案：

```

### 练习4：对象操作
```javascript
// 创建一个学生管理系统：
// 1. 定义学生对象结构
// 2. 创建添加课程的方法
// 3. 计算平均成绩的方法

// 你的答案：

```

## 💡 最佳实践

### 1. 变量命名规范
```javascript
// 好的命名
const userName = "张三";
const userAge = 25;
const isActive = true;

// 避免的命名
const a = "张三";          // 太简短
const user_name = "张三";   // 不使用下划线
const UserName = "张三";    // 不使用PascalCase（除了构造函数）
```

### 2. 使用const vs let
```javascript
// 优先使用const
const PI = 3.14159;
const users = [];  // 数组内容可以改变，但引用不变

// 需要重新赋值时使用let
let counter = 0;
for (let i = 0; i < 5; i++) {
    counter += i;
}

// 避免使用var
// var有函数作用域，容易造成问题
```

### 3. 函数定义选择
```javascript
// 需要提升时使用函数声明
function utilityFunction() {
    return "可以在定义前调用";
}

// 作为值传递时使用函数表达式
const handlers = {
    click: function() { console.log("点击"); },
    hover: () => console.log("悬停")
};

// 简短函数使用箭头函数
const double = x => x * 2;
const isEven = num => num % 2 === 0;
```

## 🎯 小结

本章我们学习了JavaScript的基础语法：

✅ **变量声明**：const、let、var的区别和使用  
✅ **数据类型**：7种基础类型和类型检查  
✅ **字符串操作**：模板字符串、字符串方法  
✅ **数组操作**：创建、访问、高级方法  
✅ **对象操作**：对象字面量、属性访问、Object方法  
✅ **运算符**：算术、比较、逻辑、现代运算符  
✅ **控制流**：条件语句、循环语句、循环控制  
✅ **现代语法**：解构赋值、扩展语法  

### 下一步
学习**03-functions.md**，深入掌握JavaScript函数的高级用法和作用域概念。

### 记住要点
- 优先使用`const`，需要时使用`let`
- 使用`===`进行严格比较
- 善用现代JavaScript特性提高代码可读性
- 多练习数组和对象的操作方法 