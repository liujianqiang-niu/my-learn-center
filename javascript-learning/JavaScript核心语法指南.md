# JavaScript核心语法指南 ⚡

## 📖 目录
1. [基础语法](#1-基础语法)
2. [函数详解](#2-函数详解)
3. [对象和数组](#3-对象和数组)
4. [ES6+现代特性](#4-es6现代特性)
5. [异步编程](#5-异步编程)
6. [DOM操作](#6-dom操作)
7. [Node.js后端](#7-nodejs后端)
8. [实战项目](#8-实战项目)

---

## 1. 基础语法

### 变量声明
```javascript
// ES6+推荐方式
let name = "张三";           // 可变变量
const PI = 3.14159;          // 常量
const age = 25;              // 推荐用const

// 老式声明（不推荐）
var oldStyle = "避免使用";

// 数据类型
let str = "字符串";
let num = 42;
let bool = true;
let arr = [1, 2, 3];
let obj = {name: "张三", age: 25};
let nothing = null;
let undefined_var = undefined;

console.log(typeof name);    // "string"
console.log(typeof age);     // "number"
```

### 模板字符串
```javascript
const name = "李四";
const age = 30;

// 模板字符串（推荐）
const message = `我叫${name}，今年${age}岁`;
const multiLine = `
这是一个
多行字符串
当前时间：${new Date()}
`;

console.log(message);
console.log(multiLine);
```

### 条件和循环
```javascript
// 条件语句
const score = 85;
if (score >= 90) {
    console.log("优秀");
} else if (score >= 60) {
    console.log("及格");
} else {
    console.log("不及格");
}

// 三元操作符
const result = score >= 60 ? "通过" : "未通过";

// 循环
for (let i = 0; i < 5; i++) {
    console.log(`计数: ${i}`);
}

const fruits = ["苹果", "香蕉", "橘子"];
for (const fruit of fruits) {
    console.log(`水果: ${fruit}`);
}

fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});
```

---

## 2. 函数详解

### 函数定义
```javascript
// 函数声明
function greet(name) {
    return `Hello, ${name}!`;
}

// 函数表达式
const add = function(a, b) {
    return a + b;
};

// 箭头函数（推荐）
const multiply = (a, b) => a * b;
const square = x => x * x;           // 单参数可省略括号
const sayHello = () => "Hello!";     // 无参数

console.log(greet("张三"));
console.log(add(10, 20));
console.log(multiply(5, 6));
```

### 高级函数特性
```javascript
// 默认参数
const createUser = (name, age = 18, city = "北京") => {
    return {name, age, city};
};

// 剩余参数
const sum = (...numbers) => {
    return numbers.reduce((total, num) => total + num, 0);
};

console.log(sum(1, 2, 3, 4, 5));  // 15

// 解构参数
const printUser = ({name, age, city}) => {
    console.log(`${name}, ${age}岁, 来自${city}`);
};

const user = createUser("王五", 28, "上海");
printUser(user);
```

---

## 3. 对象和数组

### 对象操作
```javascript
const person = {
    name: "张三",
    age: 25,
    hobbies: ["编程", "读书"],
    
    // 方法
    introduce() {
        return `我叫${this.name}，今年${this.age}岁`;
    }
};

// 属性访问
console.log(person.name);         // 点号访问
console.log(person["age"]);       // 方括号访问

// 动态属性
const prop = "hobbies";
console.log(person[prop]);

// 对象方法
console.log(Object.keys(person));     // 获取所有键
console.log(Object.values(person));   // 获取所有值
console.log(Object.entries(person));  // 获取键值对数组
```

### 数组方法
```javascript
const numbers = [1, 2, 3, 4, 5];

// 基础方法
numbers.push(6);           // 添加到末尾
numbers.unshift(0);        // 添加到开头
const last = numbers.pop(); // 删除最后一个
const first = numbers.shift(); // 删除第一个

// 高级方法
const doubled = numbers.map(x => x * 2);        // 映射
const evens = numbers.filter(x => x % 2 === 0); // 过滤
const sum = numbers.reduce((acc, curr) => acc + curr, 0); // 累积
const hasLarge = numbers.some(x => x > 10);     // 某个满足
const allPositive = numbers.every(x => x > 0);  // 全部满足

console.log("原数组:", numbers);
console.log("翻倍:", doubled);
console.log("偶数:", evens);
console.log("总和:", sum);
```

---

## 4. ES6+现代特性

### 解构赋值
```javascript
// 数组解构
const [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log(first, second, rest); // 1 2 [3, 4, 5]

// 对象解构
const person = {name: "张三", age: 25, city: "北京"};
const {name, age, city = "上海"} = person;
console.log(name, age, city);

// 函数参数解构
const printCoordinates = ({x, y}) => {
    console.log(`坐标: (${x}, ${y})`);
};
printCoordinates({x: 10, y: 20});
```

### 展开运算符
```javascript
// 数组展开
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];  // [1, 2, 3, 4, 5, 6]

// 对象展开
const obj1 = {a: 1, b: 2};
const obj2 = {c: 3, d: 4};
const merged = {...obj1, ...obj2, e: 5}; // {a:1, b:2, c:3, d:4, e:5}

// 函数调用展开
const numbers = [1, 2, 3, 4, 5];
console.log(Math.max(...numbers));  // 5
```

### 类语法
```javascript
class Vehicle {
    constructor(brand, model) {
        this.brand = brand;
        this.model = model;
    }
    
    start() {
        console.log(`${this.brand} ${this.model} 启动了`);
    }
    
    // 静态方法
    static compare(v1, v2) {
        return v1.brand === v2.brand;
    }
}

class Car extends Vehicle {
    constructor(brand, model, doors) {
        super(brand, model);
        this.doors = doors;
    }
    
    honk() {
        console.log("嘀嘀！");
    }
}

const car = new Car("丰田", "凯美瑞", 4);
car.start();
car.honk();
```

---

## 5. 异步编程

### Promise基础
```javascript
// 创建Promise
const fetchData = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = Math.random() > 0.3;
            if (success) {
                resolve({data: "获取成功", time: new Date()});
            } else {
                reject(new Error("获取失败"));
            }
        }, 1000);
    });
};

// 使用Promise
fetchData()
    .then(result => {
        console.log("成功:", result);
        return result.data;
    })
    .then(data => {
        console.log("数据处理:", data);
    })
    .catch(error => {
        console.error("错误:", error.message);
    })
    .finally(() => {
        console.log("请求完成");
    });
```

### Async/Await
```javascript
// 异步函数
const getUserData = async (userId) => {
    try {
        const response = await fetch(`/api/users/${userId}`);
        const userData = await response.json();
        return userData;
    } catch (error) {
        console.error("获取用户数据失败:", error);
        throw error;
    }
};

// 并行处理
const getMultipleUsers = async (userIds) => {
    try {
        const promises = userIds.map(id => getUserData(id));
        const users = await Promise.all(promises);
        return users;
    } catch (error) {
        console.error("批量获取用户失败:", error);
    }
};

// 使用
(async () => {
    const users = await getMultipleUsers([1, 2, 3]);
    console.log("用户列表:", users);
})();
```

---

## 6. DOM操作

### 基础DOM操作
```javascript
// 选择元素
const button = document.getElementById("myButton");
const items = document.querySelectorAll(".item");
const first = document.querySelector(".item");

// 修改内容
button.textContent = "点击我";
button.innerHTML = "<strong>点击我</strong>";

// 修改样式
button.style.backgroundColor = "blue";
button.style.color = "white";

// 添加/删除类
button.classList.add("active");
button.classList.remove("inactive");
button.classList.toggle("highlighted");

// 事件处理
button.addEventListener("click", (event) => {
    console.log("按钮被点击了！");
    event.preventDefault(); // 阻止默认行为
});
```

### 动态内容创建
```javascript
// 创建元素
const createUserCard = (user) => {
    const card = document.createElement("div");
    card.className = "user-card";
    
    card.innerHTML = `
        <h3>${user.name}</h3>
        <p>年龄: ${user.age}</p>
        <p>邮箱: ${user.email}</p>
        <button onclick="deleteUser(${user.id})">删除</button>
    `;
    
    return card;
};

// 添加到DOM
const userList = document.getElementById("userList");
const users = [
    {id: 1, name: "张三", age: 25, email: "zhang@email.com"},
    {id: 2, name: "李四", age: 30, email: "li@email.com"}
];

users.forEach(user => {
    const card = createUserCard(user);
    userList.appendChild(card);
});
```

---

## 7. Node.js后端

### HTTP服务器
```javascript
// 使用Express框架
const express = require('express');
const app = express();
const PORT = 3000;

// 中间件
app.use(express.json()); // 解析JSON请求体

// 路由
app.get('/', (req, res) => {
    res.send('Hello Node.js!');
});

app.get('/api/users', (req, res) => {
    const users = [
        {id: 1, name: "张三", email: "zhang@email.com"},
        {id: 2, name: "李四", email: "li@email.com"}
    ];
    res.json(users);
});

app.post('/api/users', (req, res) => {
    const {name, email} = req.body;
    const newUser = {
        id: Date.now(),
        name,
        email,
        createdAt: new Date()
    };
    res.status(201).json(newUser);
});

app.listen(PORT, () => {
    console.log(`服务器运行在 http://localhost:${PORT}`);
});
```

### 文件系统操作
```javascript
const fs = require('fs').promises;
const path = require('path');

// 文件操作工具类
class FileUtils {
    static async readJson(filePath) {
        try {
            const data = await fs.readFile(filePath, 'utf8');
            return JSON.parse(data);
        } catch (error) {
            console.error('读取JSON文件失败:', error);
            return null;
        }
    }
    
    static async writeJson(filePath, data) {
        try {
            const jsonStr = JSON.stringify(data, null, 2);
            await fs.writeFile(filePath, jsonStr);
            console.log('JSON文件写入成功:', filePath);
        } catch (error) {
            console.error('写入JSON文件失败:', error);
        }
    }
    
    static async listFiles(dirPath) {
        try {
            const files = await fs.readdir(dirPath);
            return files.filter(file => !file.startsWith('.'));
        } catch (error) {
            console.error('读取目录失败:', error);
            return [];
        }
    }
}

// 使用示例
(async () => {
    const userData = {name: "王五", age: 35, city: "深圳"};
    await FileUtils.writeJson('user.json', userData);
    
    const loadedData = await FileUtils.readJson('user.json');
    console.log('加载的数据:', loadedData);
    
    const files = await FileUtils.listFiles('.');
    console.log('当前目录文件:', files);
})();
```

---

## 8. 实战项目

### 项目1：待办事项应用
```javascript
// 待办事项管理器
class TodoManager {
    constructor() {
        this.todos = JSON.parse(localStorage.getItem('todos') || '[]');
        this.nextId = Math.max(...this.todos.map(t => t.id), 0) + 1;
    }
    
    add(text) {
        const todo = {
            id: this.nextId++,
            text,
            completed: false,
            createdAt: new Date()
        };
        this.todos.push(todo);
        this.save();
        return todo;
    }
    
    toggle(id) {
        const todo = this.todos.find(t => t.id === id);
        if (todo) {
            todo.completed = !todo.completed;
            this.save();
        }
        return todo;
    }
    
    remove(id) {
        this.todos = this.todos.filter(t => t.id !== id);
        this.save();
    }
    
    getAll() {
        return this.todos;
    }
    
    getActive() {
        return this.todos.filter(t => !t.completed);
    }
    
    getCompleted() {
        return this.todos.filter(t => t.completed);
    }
    
    save() {
        localStorage.setItem('todos', JSON.stringify(this.todos));
    }
}

// DOM操作
class TodoApp {
    constructor() {
        this.manager = new TodoManager();
        this.init();
    }
    
    init() {
        this.render();
        this.bindEvents();
    }
    
    bindEvents() {
        const form = document.getElementById('todoForm');
        const input = document.getElementById('todoInput');
        
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const text = input.value.trim();
            if (text) {
                this.manager.add(text);
                input.value = '';
                this.render();
            }
        });
    }
    
    render() {
        const container = document.getElementById('todoList');
        const todos = this.manager.getAll();
        
        container.innerHTML = todos.map(todo => `
            <div class="todo-item ${todo.completed ? 'completed' : ''}">
                <span>${todo.text}</span>
                <div>
                    <button onclick="app.toggle(${todo.id})">
                        ${todo.completed ? '取消' : '完成'}
                    </button>
                    <button onclick="app.remove(${todo.id})">删除</button>
                </div>
            </div>
        `).join('');
        
        // 更新统计
        this.updateStats();
    }
    
    toggle(id) {
        this.manager.toggle(id);
        this.render();
    }
    
    remove(id) {
        this.manager.remove(id);
        this.render();
    }
    
    updateStats() {
        const total = this.manager.getAll().length;
        const active = this.manager.getActive().length;
        const completed = this.manager.getCompleted().length;
        
        document.getElementById('stats').textContent = 
            `总计: ${total}, 待完成: ${active}, 已完成: ${completed}`;
    }
}

// HTML页面
const todoHTML = `
<!DOCTYPE html>
<html>
<head>
    <title>待办事项应用</title>
    <style>
        .todo-item { 
            display: flex; 
            justify-content: space-between; 
            padding: 10px; 
            border: 1px solid #ddd; 
            margin: 5px 0; 
        }
        .completed { opacity: 0.6; text-decoration: line-through; }
    </style>
</head>
<body>
    <h1>我的待办事项</h1>
    <form id="todoForm">
        <input type="text" id="todoInput" placeholder="输入待办事项...">
        <button type="submit">添加</button>
    </form>
    <div id="stats"></div>
    <div id="todoList"></div>
    <script>
        // TodoManager和TodoApp类代码...
        const app = new TodoApp();
    </script>
</body>
</html>
`;
```

### 项目2：天气查询应用
```javascript
// 天气API服务
class WeatherService {
    constructor(apiKey) {
        this.apiKey = apiKey;
        this.baseUrl = 'https://api.openweathermap.org/data/2.5';
    }
    
    async getCurrentWeather(city) {
        try {
            const url = `${this.baseUrl}/weather?q=${city}&appid=${this.apiKey}&units=metric&lang=zh_cn`;
            const response = await fetch(url);
            
            if (!response.ok) {
                throw new Error(`HTTP错误: ${response.status}`);
            }
            
            const data = await response.json();
            return this.formatWeatherData(data);
        } catch (error) {
            console.error('获取天气失败:', error);
            throw error;
        }
    }
    
    formatWeatherData(data) {
        return {
            city: data.name,
            country: data.sys.country,
            temperature: Math.round(data.main.temp),
            description: data.weather[0].description,
            humidity: data.main.humidity,
            windSpeed: data.wind.speed,
            icon: data.weather[0].icon
        };
    }
}

// 天气应用界面
class WeatherApp {
    constructor(apiKey) {
        this.service = new WeatherService(apiKey);
        this.init();
    }
    
    init() {
        this.bindEvents();
        this.loadDefaultCity();
    }
    
    bindEvents() {
        const form = document.getElementById('searchForm');
        const input = document.getElementById('cityInput');
        
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const city = input.value.trim();
            if (city) {
                await this.searchWeather(city);
            }
        });
    }
    
    async searchWeather(city) {
        try {
            this.showLoading(true);
            const weather = await this.service.getCurrentWeather(city);
            this.displayWeather(weather);
        } catch (error) {
            this.showError('获取天气信息失败，请检查城市名称');
        } finally {
            this.showLoading(false);
        }
    }
    
    displayWeather(weather) {
        const container = document.getElementById('weatherInfo');
        container.innerHTML = `
            <div class="weather-card">
                <h2>${weather.city}, ${weather.country}</h2>
                <div class="temperature">${weather.temperature}°C</div>
                <div class="description">${weather.description}</div>
                <div class="details">
                    <p>湿度: ${weather.humidity}%</p>
                    <p>风速: ${weather.windSpeed} m/s</p>
                </div>
            </div>
        `;
    }
    
    showLoading(loading) {
        const loader = document.getElementById('loading');
        loader.style.display = loading ? 'block' : 'none';
    }
    
    showError(message) {
        const container = document.getElementById('weatherInfo');
        container.innerHTML = `<div class="error">${message}</div>`;
    }
    
    async loadDefaultCity() {
        await this.searchWeather('北京');
    }
}

// 使用
// const app = new WeatherApp('your-api-key-here');
```

---

## 🎯 学习路径规划

### 第1周：JavaScript基础
- ✅ 变量、数据类型、操作符
- ✅ 函数定义和调用
- ✅ 条件语句和循环
- **练习**: 编写计算器程序

### 第2周：数组和对象
- ✅ 数组方法掌握（map, filter, reduce）
- ✅ 对象操作和方法
- ✅ 解构赋值和展开运算符
- **练习**: 数据处理小程序

### 第3周：异步编程
- ✅ Promise理解和使用
- ✅ async/await语法
- ✅ 错误处理机制
- **练习**: 网络请求应用

### 第4周：DOM和浏览器
- ✅ DOM选择和操作
- ✅ 事件处理
- ✅ 本地存储使用
- **练习**: 交互式Web应用

### 第5-6周：Node.js后端
- ✅ Express框架
- ✅ 文件系统操作
- ✅ API开发
- **练习**: RESTful服务

### 第7-8周：前端框架
- ✅ React或Vue基础
- ✅ 组件化开发
- ✅ 状态管理
- **练习**: 单页应用

### 第9周+：项目实战
- ✅ 全栈项目开发
- ✅ 部署和测试
- ✅ 性能优化
- **目标**: 独立开发完整应用

---

## 💡 学习建议

1. **每天编码**: 坚持每天写JavaScript代码
2. **项目驱动**: 通过实际项目学习新特性
3. **阅读源码**: 学习优秀开源项目
4. **关注生态**: 了解npm包和工具链
5. **社区参与**: 加入JavaScript开发者社区

**准备好成为JavaScript全栈开发专家了吗？开始编码吧！** ⚡ 