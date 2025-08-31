# Groovy开发环境搭建指南

## 🎯 学习目标
- 了解Groovy语言的特点和用途
- 正确安装和配置Groovy开发环境
- 掌握基本的开发工具使用
- 验证环境搭建成功

## 🚀 Groovy简介

### 什么是Groovy？
Groovy是一种基于JVM的动态编程语言，具有以下特点：
- **Java兼容**：可以无缝调用Java类库和框架
- **动态特性**：支持动态类型、元编程、运行时修改
- **简洁语法**：比Java更简洁，减少样板代码
- **脚本能力**：既可以编写脚本，也可以开发大型应用
- **DSL友好**：非常适合构建领域特定语言

### 主要应用场景
- **构建脚本**：Gradle构建工具使用Groovy
- **测试自动化**：Spock测试框架
- **快速原型开发**：快速验证想法
- **配置和部署脚本**：简化运维工作
- **企业应用开发**：Grails Web框架

## 💻 环境安装

### 前提条件
确保已安装Java 8或更高版本：
```bash
# 检查Java版本
java -version
javac -version

# 如果未安装，Ubuntu/Debian系统安装：
sudo apt update
sudo apt install openjdk-17-jdk

# 设置JAVA_HOME（如果需要）
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin
```

### 方法1：使用SDKMAN安装（推荐）
```bash
# 1. 安装SDKMAN
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# 2. 安装Groovy
sdk install groovy

# 3. 验证安装
groovy -version

# 4. 可选：安装特定版本
sdk list groovy          # 查看可用版本
sdk install groovy 4.0.15  # 安装特定版本
sdk use groovy 4.0.15     # 使用特定版本
```

### 方法2：手动安装
```bash
# 1. 下载Groovy二进制包
cd /tmp
wget https://archive.apache.org/dist/groovy/4.0.15/distribution/apache-groovy-binary-4.0.15.zip

# 2. 解压到指定目录
sudo unzip apache-groovy-binary-4.0.15.zip -d /opt/
sudo mv /opt/groovy-4.0.15 /opt/groovy

# 3. 设置环境变量
echo 'export GROOVY_HOME=/opt/groovy' >> ~/.bashrc
echo 'export PATH=$PATH:$GROOVY_HOME/bin' >> ~/.bashrc
source ~/.bashrc

# 4. 验证安装
groovy -version
```

### 方法3：包管理器安装
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install groovy

# macOS
brew install groovy

# 验证安装
groovy -version
```

## 🛠️ 开发工具配置

### IntelliJ IDEA（推荐）
1. **下载安装**
   ```bash
   # 下载Community版本（免费）
   wget https://download.jetbrains.com/idea/ideaIC-2023.2.tar.gz
   
   # 或直接访问：https://www.jetbrains.com/idea/download/
   ```

2. **安装Groovy插件**
   - 打开IntelliJ IDEA
   - File → Settings → Plugins
   - 搜索"Groovy"并安装
   - 重启IDE

3. **创建Groovy项目**
   - File → New → Project
   - 选择"Groovy"
   - 配置Project SDK为你的JDK路径
   - 配置Groovy SDK为Groovy安装路径

### VS Code配置
1. **安装VS Code**
   ```bash
   # Ubuntu/Debian
   wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
   sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
   sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
   sudo apt update
   sudo apt install code
   ```

2. **安装Groovy扩展**
   - 打开VS Code
   - 按Ctrl+Shift+X打开扩展面板
   - 搜索并安装"Groovy"扩展

### Gradle配置
```bash
# 使用SDKMAN安装Gradle（推荐）
sdk install gradle

# 验证安装
gradle --version

# 创建Groovy项目
gradle init --type groovy-library
```

## 🧪 环境验证

### 1. 验证Groovy安装
```bash
# 检查版本
groovy -version

# 应该输出类似：
# Groovy Version: 4.0.15 JVM: 17.0.7 Vendor: Eclipse Adoptium OS: Linux
```

### 2. 运行简单脚本
```bash
# 创建测试文件
cat > test.groovy << 'EOF'
#!/usr/bin/env groovy

println "Hello, Groovy!"
println "Java版本: ${System.getProperty('java.version')}"
println "Groovy版本: ${GroovySystem.getVersion()}"

// 测试Java集成
import java.util.Date
println "当前时间: ${new Date()}"

// 测试动态特性
def list = [1, 2, 3]
println "列表: $list"
println "翻倍: ${list.collect { it * 2 }}"
EOF

# 运行测试
groovy test.groovy

# 清理
rm test.groovy
```

### 3. 交互式Groovy Shell测试
```bash
# 启动Groovy Shell
groovysh

# 在Shell中执行以下命令：
groovy:000> println "Hello from Groovy Shell!"
groovy:000> def name = "Groovy"
groovy:000> "Hello, $name!"
groovy:000> [1,2,3].collect { it * it }
groovy:000> :exit
```

### 4. Groovy控制台测试
```bash
# 启动图形化控制台（需要GUI环境）
groovyConsole &

# 在控制台中输入：
println "Hello from Groovy Console!"
def factorial = { n -> n <= 1 ? 1 : n * factorial(n-1) }
println "5! = ${factorial(5)}"
```

## 📦 项目管理工具

### 使用Gradle管理Groovy项目
```bash
# 创建新的Groovy库项目
gradle init --type groovy-library

# 项目结构
# ├── build.gradle
# ├── gradle/
# ├── gradlew*
# ├── gradlew.bat
# ├── settings.gradle
# └── src/
#     ├── main/groovy/
#     └── test/groovy/
```

### build.gradle配置示例
```gradle
plugins {
    id 'groovy'
    id 'application'
}

repositories {
    mavenCentral()
}

dependencies {
    // Groovy核心库
    implementation 'org.codehaus.groovy:groovy-all:4.0.15'
    
    // 测试框架
    testImplementation 'org.spockframework:spock-core:2.3-groovy-4.0'
    testImplementation 'org.spockframework:spock-junit4:2.3-groovy-4.0'
    
    // 可选：JSON处理
    implementation 'org.codehaus.groovy:groovy-json:4.0.15'
    
    // 可选：XML处理
    implementation 'org.codehaus.groovy:groovy-xml:4.0.15'
}

application {
    mainClass = 'Main'
}
```

## 🔧 常用命令总结

```bash
# 编译Groovy文件
groovyc MyClass.groovy

# 运行Groovy脚本
groovy script.groovy

# 运行编译后的类
java -cp ".:$GROOVY_HOME/lib/*" MyClass

# 启动交互式Shell
groovysh

# 启动图形控制台
groovyConsole

# 查看帮助
groovy --help

# 使用Gradle运行
gradle run

# 使用Gradle构建
gradle build

# 使用Gradle测试
gradle test
```

## ❗ 常见问题

### Q: 提示"groovy: command not found"
A: 检查环境变量配置：
```bash
echo $PATH | grep groovy
echo $GROOVY_HOME
```

### Q: 编码问题
A: 设置正确的编码：
```bash
export JAVA_OPTS="-Dfile.encoding=UTF-8"
groovy -Dfile.encoding=UTF-8 script.groovy
```

### Q: 类路径问题
A: 确保Groovy库在类路径中：
```bash
java -cp ".:$GROOVY_HOME/lib/*" YourClass
```

### Q: IDE不识别Groovy语法
A: 确保安装了正确的插件并配置了Groovy SDK路径。

## 🎉 环境验证成功！

如果上述测试都通过了，恭喜你！Groovy开发环境搭建成功。

### 下一步
1. 📚 学习**02-basic-syntax.md** - 掌握基础语法
2. 🏃‍♂️ 运行**quick_start.groovy** - 快速体验
3. 💪 开始系统性学习Groovy语言特性

### 学习建议
- 多使用`groovysh`进行交互式学习
- 经常查看Groovy官方文档
- 对比Java和Groovy的差异
- 重点理解动态语言特性

开始你的Groovy学习之旅吧！🚀 