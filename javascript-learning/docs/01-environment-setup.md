# JavaScript开发环境搭建指南

## 🎯 学习目标
- 了解JavaScript语言的特点和应用场景
- 正确安装和配置JavaScript开发环境
- 掌握浏览器和Node.js两种运行环境
- 配置现代JavaScript开发工具链

## 🚀 JavaScript简介

### 什么是JavaScript？
JavaScript是一种多范式的动态编程语言，具有以下特点：
- **解释型语言**：无需编译，直接运行
- **动态类型**：运行时确定变量类型
- **事件驱动**：基于事件和回调的编程模型
- **函数式编程**：支持高阶函数、闭包等
- **原型继承**：基于原型链的面向对象编程

### 主要应用场景
- **前端开发**：网页交互、用户界面
- **后端开发**：Node.js服务器端应用
- **移动应用**：React Native、Ionic
- **桌面应用**：Electron桌面应用
- **游戏开发**：Canvas/WebGL游戏
- **物联网**：IoT设备编程

## 🌐 浏览器环境

### 现代浏览器推荐
所有现代浏览器都内置JavaScript引擎：

- **Chrome**：V8引擎（推荐开发使用）
- **Firefox**：SpiderMonkey引擎
- **Safari**：JavaScriptCore引擎
- **Edge**：Chakra/V8引擎

### 浏览器开发者工具
1. **打开开发者工具**
   - Windows/Linux：`F12` 或 `Ctrl+Shift+I`
   - macOS：`Cmd+Opt+I`

2. **控制台使用**
   ```javascript
   // 在控制台中尝试运行：
   console.log("Hello, JavaScript!");
   alert("这是一个弹窗");
   
   // 变量定义
   let name = "学习者";
   console.log(`你好，${name}！`);
   
   // 简单计算
   let result = 10 + 20;
   console.log("计算结果：", result);
   ```

3. **创建HTML文件测试**
   ```html
   <!DOCTYPE html>
   <html lang="zh-CN">
   <head>
       <meta charset="UTF-8">
       <title>JavaScript测试</title>
   </head>
   <body>
       <h1>JavaScript学习环境测试</h1>
       <button onclick="testFunction()">点击测试</button>
       
       <script>
           function testFunction() {
               alert("JavaScript环境运行正常！");
               console.log("测试成功！");
           }
           
           console.log("页面加载完成，JavaScript正在运行...");
       </script>
   </body>
   </html>
   ```

## 🖥️ Node.js环境

### 安装Node.js
Node.js让JavaScript能在服务器端运行。

#### 方法1：官方安装包（推荐）
```bash
# 1. 访问官网下载LTS版本
# https://nodejs.org/

# 2. Ubuntu/Debian安装
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# 3. 验证安装
node --version
npm --version
```

#### 方法2：使用NVM管理版本
```bash
# 1. 安装NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc

# 2. 安装最新LTS Node.js
nvm install --lts
nvm use --lts

# 3. 验证安装
node --version
npm --version

# 管理多个版本
nvm list              # 查看已安装版本
nvm install 18.17.0   # 安装特定版本
nvm use 18.17.0       # 切换版本
```

### NPM包管理器
```bash
# NPM基本命令
npm --version         # 查看版本
npm init             # 初始化项目
npm init -y          # 快速初始化

# 包管理
npm install <package>           # 安装包
npm install <package> --save    # 保存到dependencies
npm install <package> --save-dev # 保存到devDependencies
npm install -g <package>        # 全局安装

# 常用全局包
npm install -g nodemon          # 文件变化自动重启
npm install -g http-server      # 简单HTTP服务器
npm install -g live-server      # 带热重载的服务器
```

### 替代包管理器
```bash
# Yarn（Facebook开发）
npm install -g yarn
yarn --version
yarn init

# pnpm（高性能）
npm install -g pnpm
pnpm --version
pnpm init
```

## 🛠️ 开发工具配置

### VS Code配置（推荐）
1. **安装VS Code**
   ```bash
   # Ubuntu/Debian
   curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
   sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
   echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
   sudo apt update
   sudo apt install code
   ```

2. **推荐扩展插件**
   ```bash
   # JavaScript相关
   code --install-extension ms-vscode.vscode-javascript
   code --install-extension bradlc.vscode-tailwindcss
   
   # Node.js相关
   code --install-extension christian-kohler.npm-intellisense
   code --install-extension eg2.vscode-npm-script
   
   # 代码质量
   code --install-extension dbaeumer.vscode-eslint
   code --install-extension esbenp.prettier-vscode
   
   # 调试和测试
   code --install-extension ms-vscode.vscode-json
   code --install-extension humao.rest-client
   ```

### WebStorm配置（专业IDE）
```bash
# 下载WebStorm（付费，但功能强大）
# https://www.jetbrains.com/webstorm/

# 学生可免费使用：
# https://www.jetbrains.com/student/
```

## 📁 项目结构创建

### 基础项目结构
```bash
# 创建项目目录
mkdir my-js-project && cd my-js-project

# 初始化项目
npm init -y

# 创建基本目录结构
mkdir -p src/{components,utils,styles} public tests docs

# 创建入口文件
cat > src/index.js << 'EOF'
// 项目入口文件
console.log("🚀 JavaScript项目启动成功！");

// 导入模块示例
import { formatDate } from './utils/date.js';

const now = new Date();
console.log("当前时间:", formatDate(now));
EOF

# 创建工具模块
mkdir -p src/utils
cat > src/utils/date.js << 'EOF'
// 日期工具函数
export function formatDate(date) {
    return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    });
}

export function isToday(date) {
    const today = new Date();
    return date.toDateString() === today.toDateString();
}
EOF
```

### 配置文件
```bash
# package.json配置
cat > package.json << 'EOF'
{
  "name": "my-js-project",
  "version": "1.0.0",
  "description": "JavaScript学习项目",
  "main": "src/index.js",
  "type": "module",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "node tests/test.js",
    "serve": "http-server public -p 8080"
  },
  "keywords": ["javascript", "learning"],
  "author": "JavaScript学习者",
  "license": "MIT"
}
EOF
```

## 🧪 环境验证

### 1. Node.js环境验证
```bash
# 创建测试文件
cat > test-node.js << 'EOF'
#!/usr/bin/env node

console.log("🧪 Node.js环境测试");
console.log("Node.js版本:", process.version);
console.log("NPM版本:", process.env.npm_version || "未知");
console.log("操作系统:", process.platform);
console.log("CPU架构:", process.arch);

// 测试ES6特性
const [a, b, c] = [1, 2, 3];
console.log("解构赋值:", { a, b, c });

// 测试异步操作
setTimeout(() => {
    console.log("✅ 异步操作正常");
}, 100);

// 测试模块系统
const fs = require('fs');
const path = require('path');
console.log("当前目录:", process.cwd());

Promise.resolve("Promise正常")
    .then(result => console.log("✅", result))
    .catch(err => console.error("❌", err));
EOF

# 运行测试
node test-node.js

# 清理
rm test-node.js
```

### 2. 浏览器环境验证
```bash
# 创建HTML测试文件
cat > test-browser.html << 'EOF'
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript浏览器环境测试</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .test-result { margin: 10px 0; padding: 10px; border-radius: 5px; }
        .success { background-color: #d4edda; color: #155724; }
        .info { background-color: #d1ecf1; color: #0c5460; }
    </style>
</head>
<body>
    <h1>🧪 JavaScript浏览器环境测试</h1>
    <div id="results"></div>
    
    <script>
        const results = document.getElementById('results');
        
        function addResult(message, type = 'info') {
            const div = document.createElement('div');
            div.className = `test-result ${type}`;
            div.textContent = message;
            results.appendChild(div);
        }
        
        // 基础语法测试
        addResult("✅ JavaScript基础语法正常", "success");
        
        // ES6特性测试
        const [x, y] = [10, 20];
        addResult(`✅ ES6解构赋值正常: x=${x}, y=${y}`, "success");
        
        // 异步测试
        fetch('data:application/json,{"test":"ok"}')
            .then(response => response.json())
            .then(data => addResult("✅ Fetch API正常: " + JSON.stringify(data), "success"))
            .catch(err => addResult("❌ Fetch API失败: " + err.message, "error"));
        
        // DOM操作测试
        addResult("✅ DOM操作正常", "success");
        
        // 本地存储测试
        try {
            localStorage.setItem('test', 'ok');
            const value = localStorage.getItem('test');
            localStorage.removeItem('test');
            addResult("✅ 本地存储正常: " + value, "success");
        } catch (e) {
            addResult("⚠️ 本地存储不可用", "info");
        }
        
        console.log("🎉 浏览器环境测试完成，查看页面结果");
    </script>
</body>
</html>
EOF

echo "✅ HTML测试文件已创建: test-browser.html"
echo "请在浏览器中打开此文件进行测试"
```

## 🚀 现代开发环境

### 使用Vite快速开始
```bash
# 创建Vite项目（推荐）
npm create vite@latest my-js-app -- --template vanilla
cd my-js-app
npm install
npm run dev

# 或创建React项目
npm create vite@latest my-react-app -- --template react
```

### 使用Create React App
```bash
# 创建React项目
npx create-react-app my-react-app
cd my-react-app
npm start
```

### 使用Express快速API
```bash
# 创建后端项目
mkdir my-api && cd my-api
npm init -y
npm install express

# 创建简单API
cat > server.js << 'EOF'
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {
    res.json({ message: '欢迎使用JavaScript API！' });
});

app.get('/api/hello/:name', (req, res) => {
    const { name } = req.params;
    res.json({ message: `你好，${name}！` });
});

app.listen(port, () => {
    console.log(`🚀 服务器运行在 http://localhost:${port}`);
});
EOF

# 运行服务器
node server.js
```

## 📦 包管理配置

### package.json详解
```json
{
  "name": "my-javascript-project",
  "version": "1.0.0",
  "description": "JavaScript学习项目",
  "main": "src/index.js",
  "type": "module",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "build": "webpack --mode production",
    "serve": "http-server public -p 8080",
    "lint": "eslint src/",
    "format": "prettier --write src/"
  },
  "dependencies": {
    "express": "^4.18.0",
    "lodash": "^4.17.21"
  },
  "devDependencies": {
    "nodemon": "^3.0.0",
    "jest": "^29.0.0",
    "eslint": "^8.0.0",
    "prettier": "^3.0.0",
    "webpack": "^5.0.0"
  },
  "keywords": ["javascript", "learning", "nodejs"],
  "author": "JavaScript学习者",
  "license": "MIT"
}
```

### 代码质量工具
```bash
# ESLint（代码检查）
npm install --save-dev eslint
npx eslint --init

# Prettier（代码格式化）
npm install --save-dev prettier
echo '{"semi": true, "singleQuote": true}' > .prettierrc

# Husky（Git钩子）
npm install --save-dev husky
npx husky install
```

## 🔧 开发工具命令总结

### Node.js命令
```bash
# 运行JavaScript文件
node script.js

# 启动交互式REPL
node

# 查看Node.js信息
node --version
node -p "process.versions"

# 使用nodemon自动重启
npx nodemon script.js

# 检查语法
node --check script.js
```

### NPM命令
```bash
# 项目管理
npm init                    # 初始化项目
npm install                 # 安装依赖
npm update                  # 更新依赖
npm audit                   # 安全检查

# 包管理
npm search <keyword>        # 搜索包
npm info <package>          # 包信息
npm list                    # 查看已安装包
npm outdated               # 查看过期包

# 脚本运行
npm start                  # 运行start脚本
npm test                   # 运行测试
npm run <script>           # 运行自定义脚本
```

### 调试工具
```bash
# Node.js调试
node --inspect script.js          # 启动调试模式
node --inspect-brk script.js      # 断点调试

# Chrome DevTools调试
# 在Chrome中访问：chrome://inspect
```

## 🧪 环境验证

### 完整验证脚本
```bash
# 创建验证脚本
cat > verify-environment.js << 'EOF'
#!/usr/bin/env node

console.log("🧪 JavaScript开发环境验证\n");

// 1. Node.js版本检查
console.log("📋 环境信息:");
console.log("  Node.js版本:", process.version);
console.log("  npm版本:", process.env.npm_version || "使用npm --version查看");
console.log("  操作系统:", process.platform);
console.log("  架构:", process.arch);

// 2. 基础语法测试
console.log("\n🔤 基础语法测试:");
const testString = "JavaScript";
console.log("  ✅ 字符串操作:", testString.toUpperCase());

const testArray = [1, 2, 3, 4, 5];
const doubled = testArray.map(x => x * 2);
console.log("  ✅ 数组操作:", doubled);

// 3. ES6+特性测试
console.log("\n🆕 ES6+特性测试:");
const [first, ...rest] = testArray;
console.log("  ✅ 解构赋值:", { first, rest });

const obj = { name: "测试", value: 42 };
console.log("  ✅ 模板字符串:", `对象: ${JSON.stringify(obj)}`);

// 4. 异步操作测试
console.log("\n⏰ 异步操作测试:");
Promise.resolve("异步操作")
    .then(result => console.log("  ✅ Promise:", result))
    .catch(err => console.error("  ❌ Promise错误:", err));

// 5. 模块系统测试
console.log("\n📦 模块系统测试:");
try {
    const fs = require('fs');
    const os = require('os');
    console.log("  ✅ CommonJS模块正常");
    console.log("  ✅ 系统信息:", os.type(), os.release());
} catch (e) {
    console.error("  ❌ 模块导入失败:", e.message);
}

// 6. 文件操作测试
setTimeout(() => {
    console.log("\n📁 文件操作测试:");
    const testContent = "JavaScript环境测试文件";
    
    try {
        require('fs').writeFileSync('test-file.txt', testContent);
        const content = require('fs').readFileSync('test-file.txt', 'utf8');
        console.log("  ✅ 文件写入读取:", content === testContent);
        
        require('fs').unlinkSync('test-file.txt');
        console.log("  ✅ 文件删除成功");
    } catch (e) {
        console.error("  ❌ 文件操作失败:", e.message);
    }
    
    console.log("\n🎉 环境验证完成！所有功能正常。");
    console.log("🚀 现在可以开始JavaScript学习了！");
}, 1000);
EOF

# 运行验证
node verify-environment.js

# 清理
rm verify-environment.js
```

## ❗ 常见问题

### Q: node命令未找到
A: 检查Node.js是否正确安装和环境变量：
```bash
which node
echo $PATH
```

### Q: npm权限问题
A: 配置npm全局目录：
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Q: 模块导入错误
A: 检查package.json中的type设置：
```json
{
  "type": "module"  // 使用ES6模块
  // 或不设置，使用CommonJS
}
```

### Q: 版本冲突
A: 使用nvm管理多个Node.js版本：
```bash
nvm install 18.17.0
nvm install 20.5.0
nvm use 18.17.0    # 切换版本
```

## 🎉 环境验证成功！

如果上述测试都通过了，恭喜你！JavaScript开发环境搭建成功。

### 下一步
1. 📚 学习**02-basic-syntax.md** - 掌握基础语法
2. 🏃‍♂️ 运行**quick_start.js** - 快速体验
3. 🌐 在浏览器和Node.js中都试试代码
4. 💪 开始系统性学习JavaScript特性

### 学习建议
- 同时熟悉浏览器和Node.js环境
- 多使用开发者工具调试
- 关注JavaScript新特性和最佳实践
- 通过实际项目巩固知识

开始你的JavaScript学习之旅吧！⚡ 