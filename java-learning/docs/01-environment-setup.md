# Java开发环境搭建指南

## 🎯 学习目标
- 了解Java语言的特点和生态系统
- 正确安装和配置Java开发环境
- 掌握JDK、IDE、构建工具的使用
- 验证环境搭建并创建第一个项目

## 🚀 Java简介

### 什么是Java？
Java是一种面向对象的编程语言，具有以下特点：
- **跨平台**：一次编写，到处运行（WORA）
- **强类型**：编译时类型检查，减少运行时错误
- **自动内存管理**：垃圾回收器自动管理内存
- **多线程**：内置并发编程支持
- **安全性**：沙盒模型和安全管理器
- **丰富生态**：庞大的类库和框架生态系统

### 主要应用场景
- **企业级应用**：大型业务系统、ERP、CRM
- **Web开发**：Spring Boot、Spring MVC
- **微服务架构**：Spring Cloud、分布式系统
- **Android开发**：移动应用开发
- **大数据处理**：Hadoop、Spark、Kafka
- **科学计算**：数值计算、算法实现

## ☕ JDK安装配置

### 选择Java版本
- **Java 8（LTS）**：长期支持版本，企业常用
- **Java 11（LTS）**：现代特性，推荐学习
- **Java 17（LTS）**：最新LTS版本，推荐使用
- **Java 21（LTS）**：最新版本，包含最新特性

### 方法1：OpenJDK安装（推荐）
```bash
# Ubuntu/Debian系统
sudo apt update
sudo apt install openjdk-17-jdk

# 验证安装
java -version
javac -version

# 查看安装路径
which java
which javac
```

### 方法2：Oracle JDK安装
```bash
# 1. 下载Oracle JDK
# 访问：https://www.oracle.com/java/technologies/downloads/

# 2. 解压安装
sudo tar -xzf jdk-17_linux-x64_bin.tar.gz -C /opt/
sudo mv /opt/jdk-17.0.8 /opt/java

# 3. 配置环境变量
echo 'export JAVA_HOME=/opt/java' >> ~/.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> ~/.bashrc
source ~/.bashrc
```

### 方法3：使用SDKMAN管理版本
```bash
# 1. 安装SDKMAN
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# 2. 查看可用Java版本
sdk list java

# 3. 安装Java
sdk install java 17.0.8-tem    # Eclipse Temurin
# 或
sdk install java 17.0.8-oracle  # Oracle JDK

# 4. 管理版本
sdk current java        # 查看当前版本
sdk use java 17.0.8-tem  # 切换版本
```

### 环境变量配置
```bash
# 添加到~/.bashrc或~/.profile
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/lib/tools.jar

# 应用配置
source ~/.bashrc

# 验证配置
echo $JAVA_HOME
echo $PATH | grep java
```

## 🛠️ IDE开发环境

### IntelliJ IDEA（强烈推荐）

#### 安装IDEA
```bash
# 方法1：官网下载
# https://www.jetbrains.com/idea/download/

# 方法2：使用snap安装
sudo snap install intellij-idea-community --classic

# 方法3：使用apt安装
sudo apt update
sudo apt install snapd
sudo snap install intellij-idea-community --classic
```

#### 配置IDEA
1. **首次启动配置**
   - 选择UI主题
   - 配置JDK路径
   - 安装推荐插件

2. **创建Java项目**
   - File → New → Project
   - 选择"Java"
   - 配置Project SDK
   - 选择项目模板

3. **推荐插件**
   - **Lombok Plugin** - 减少样板代码
   - **Maven Helper** - Maven依赖管理
   - **Spring Boot Helper** - Spring开发
   - **Database Navigator** - 数据库工具

### Eclipse IDE
```bash
# 安装Eclipse
sudo apt install eclipse

# 或下载最新版本
wget https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-09/R/eclipse-java-2023-09-R-linux-gtk-x86_64.tar.gz

# 解压安装
tar -xzf eclipse-java-2023-09-R-linux-gtk-x86_64.tar.gz
sudo mv eclipse /opt/
sudo ln -s /opt/eclipse/eclipse /usr/local/bin/eclipse
```

### VS Code配置
```bash
# 安装Java扩展包
code --install-extension vscjava.vscode-java-pack

# 包含的扩展：
# - Language Support for Java
# - Debugger for Java
# - Test Runner for Java
# - Maven for Java
# - Project Manager for Java
# - Visual Studio IntelliCode
```

## 🏗️ 构建工具配置

### Maven安装配置
```bash
# 1. 安装Maven
sudo apt update
sudo apt install maven

# 2. 验证安装
mvn -version

# 3. 配置Maven（可选）
mkdir -p ~/.m2
cat > ~/.m2/settings.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<settings>
    <localRepository>${user.home}/.m2/repository</localRepository>
    <mirrors>
        <mirror>
            <id>aliyun</id>
            <name>Aliyun Maven</name>
            <url>https://maven.aliyun.com/repository/public</url>
            <mirrorOf>central</mirrorOf>
        </mirror>
    </mirrors>
</settings>
EOF
```

### Gradle安装配置
```bash
# 使用SDKMAN安装（推荐）
sdk install gradle

# 或手动安装
wget https://gradle.org/releases/
# 按照官网指南安装

# 验证安装
gradle --version
```

## 📁 项目创建

### 使用Maven创建项目
```bash
# 创建标准Java项目
mvn archetype:generate \
  -DgroupId=com.example \
  -DartifactId=my-java-app \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DinteractiveMode=false

cd my-java-app

# 项目结构
# ├── pom.xml
# └── src/
#     ├── main/java/com/example/
#     │   └── App.java
#     └── test/java/com/example/
#         └── AppTest.java

# Maven命令
mvn compile      # 编译
mvn test         # 测试
mvn package      # 打包
mvn clean        # 清理
mvn install      # 安装到本地仓库
```

### 使用Gradle创建项目
```bash
# 创建Gradle项目
gradle init --type java-application

# 项目结构
# ├── build.gradle
# ├── gradle/
# ├── gradlew*
# ├── settings.gradle
# └── src/
#     ├── main/java/
#     └── test/java/

# Gradle命令
./gradlew build      # 构建
./gradlew test       # 测试
./gradlew run        # 运行
./gradlew clean      # 清理
```

### 使用Spring Initializr
```bash
# 1. 使用curl创建Spring Boot项目
curl https://start.spring.io/starter.zip \
  -d dependencies=web,data-jpa,h2,devtools \
  -d name=my-spring-app \
  -d packageName=com.example.app \
  -d javaVersion=17 \
  -o my-spring-app.zip

# 2. 解压项目
unzip my-spring-app.zip
cd my-spring-app

# 3. 运行Spring Boot应用
./mvnw spring-boot:run

# 4. 访问应用
# http://localhost:8080
```

## 🧪 环境验证

### 创建验证程序
```java
// EnvironmentTest.java
import java.util.*;
import java.time.LocalDateTime;

public class EnvironmentTest {
    public static void main(String[] args) {
        System.out.println("=".repeat(50));
        System.out.println("🧪 Java开发环境验证");
        System.out.println("=".repeat(50));
        
        // 1. JVM信息
        System.out.println("\n📋 JVM环境信息:");
        System.out.println("  Java版本: " + System.getProperty("java.version"));
        System.out.println("  JVM版本: " + System.getProperty("java.vm.version"));
        System.out.println("  JVM厂商: " + System.getProperty("java.vm.vendor"));
        System.out.println("  操作系统: " + System.getProperty("os.name"));
        System.out.println("  系统架构: " + System.getProperty("os.arch"));
        
        // 2. 内存信息
        Runtime runtime = Runtime.getRuntime();
        System.out.println("\n💾 内存信息:");
        System.out.println("  最大内存: " + runtime.maxMemory() / 1024 / 1024 + "MB");
        System.out.println("  总内存: " + runtime.totalMemory() / 1024 / 1024 + "MB");
        System.out.println("  可用内存: " + runtime.freeMemory() / 1024 / 1024 + "MB");
        
        // 3. 基础语法测试
        System.out.println("\n🔤 基础语法测试:");
        String message = "Java环境正常";
        System.out.println("  ✅ 字符串操作: " + message.toUpperCase());
        
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        System.out.println("  ✅ 集合操作: " + numbers);
        
        // 4. Lambda表达式测试
        System.out.println("\n🎯 Lambda表达式测试:");
        List<Integer> doubled = numbers.stream()
            .map(x -> x * 2)
            .collect(java.util.stream.Collectors.toList());
        System.out.println("  ✅ Stream API: " + doubled);
        
        // 5. 时间API测试
        System.out.println("\n⏰ 时间API测试:");
        LocalDateTime now = LocalDateTime.now();
        System.out.println("  ✅ 当前时间: " + now);
        
        // 6. 异常处理测试
        System.out.println("\n🛡️ 异常处理测试:");
        try {
            int result = 10 / 2;
            System.out.println("  ✅ 正常计算: " + result);
        } catch (Exception e) {
            System.err.println("  ❌ 计算错误: " + e.getMessage());
        }
        
        System.out.println("\n🎉 环境验证完成！所有功能正常。");
        System.out.println("🚀 现在可以开始Java学习了！");
        System.out.println("=" .repeat(50));
    }
}
```

### 运行验证
```bash
# 编译并运行
javac EnvironmentTest.java
java EnvironmentTest

# 清理
rm EnvironmentTest.class
```

## 🔧 开发工具命令总结

### Java基础命令
```bash
# 编译Java文件
javac HelloWorld.java

# 运行Java程序
java HelloWorld

# 打包JAR文件
jar cf myapp.jar *.class

# 运行JAR文件
java -jar myapp.jar

# 查看类信息
javap -c HelloWorld

# 生成文档
javadoc *.java
```

### Maven命令
```bash
# 项目管理
mvn archetype:generate     # 创建项目
mvn clean                  # 清理
mvn compile               # 编译
mvn test                  # 测试
mvn package               # 打包
mvn install               # 安装到本地仓库
mvn deploy                # 部署到远程仓库

# 依赖管理
mvn dependency:tree       # 查看依赖树
mvn dependency:analyze    # 分析依赖
mvn versions:display-dependency-updates  # 检查更新
```

### Gradle命令
```bash
# 项目管理
gradle init               # 初始化项目
gradle clean             # 清理
gradle build             # 构建
gradle test              # 测试
gradle run               # 运行
gradle bootRun           # 运行Spring Boot应用

# 依赖管理
gradle dependencies      # 查看依赖
gradle dependencyInsight # 依赖洞察
gradle refreshDependencies # 刷新依赖
```

## ❗ 常见问题

### Q: javac命令未找到
A: 检查JDK是否正确安装：
```bash
which javac
echo $JAVA_HOME
ls $JAVA_HOME/bin/javac
```

### Q: JAVA_HOME未设置
A: 配置环境变量：
```bash
# 查找Java安装路径
update-java-alternatives --list

# 设置JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
```

### Q: 编码问题
A: 设置UTF-8编码：
```bash
# 编译时指定编码
javac -encoding UTF-8 HelloWorld.java

# 运行时指定编码
java -Dfile.encoding=UTF-8 HelloWorld

# 在IDE中配置默认编码为UTF-8
```

### Q: 类路径问题
A: 正确设置classpath：
```bash
# 编译时指定类路径
javac -cp ".:lib/*" Main.java

# 运行时指定类路径
java -cp ".:lib/*" Main
```

### Q: 版本冲突
A: 管理多个Java版本：
```bash
# 使用update-alternatives管理
sudo update-alternatives --config java
sudo update-alternatives --config javac

# 或使用SDKMAN
sdk list java
sdk use java 17.0.8-tem
```

## 📋 开发环境检查清单

### ✅ 必备组件
- [ ] JDK 17+安装完成
- [ ] JAVA_HOME环境变量设置
- [ ] java和javac命令可用
- [ ] IDE安装和配置完成
- [ ] 构建工具（Maven或Gradle）安装

### ✅ 可选组件
- [ ] Git版本控制
- [ ] 数据库（MySQL/PostgreSQL）
- [ ] Redis缓存
- [ ] Docker容器平台
- [ ] 代码质量工具（SonarQube）

## 🎯 验证完整性

### 创建测试项目
```bash
# 使用Maven创建测试项目
mvn archetype:generate \
  -DgroupId=com.example.test \
  -DartifactId=environment-test \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DinteractiveMode=false

cd environment-test

# 修改App.java
cat > src/main/java/com/example/test/App.java << 'EOF'
package com.example.test;

import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class App {
    public static void main(String[] args) {
        System.out.println("🧪 Java环境完整性测试");
        
        // 基础语法
        String greeting = "Hello, Java!";
        System.out.println("✅ 字符串: " + greeting);
        
        // 集合框架
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> doubled = numbers.stream()
            .map(x -> x * 2)
            .collect(Collectors.toList());
        System.out.println("✅ Stream API: " + doubled);
        
        // 时间API
        LocalDateTime now = LocalDateTime.now();
        System.out.println("✅ 时间API: " + now);
        
        // Lambda表达式
        Runnable task = () -> System.out.println("✅ Lambda表达式正常");
        task.run();
        
        System.out.println("🎉 所有测试通过！环境配置成功！");
    }
}
EOF

# 构建并运行
mvn clean compile exec:java -Dexec.mainClass="com.example.test.App"
```

## 🌟 高级配置

### JVM参数调优
```bash
# 常用JVM参数
export JAVA_OPTS="-Xms512m -Xmx2g -XX:+UseG1GC"

# 开发时调试参数
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005 YourApp
```

### IDE性能优化
```bash
# IntelliJ IDEA JVM配置
# 编辑 $IDEA_HOME/bin/idea64.vmoptions
-Xms1024m
-Xmx4096m
-XX:ReservedCodeCacheSize=1024m
-XX:+UseConcMarkSweepGC
```

## 🎉 环境搭建完成！

恭喜你完成了Java开发环境的搭建！现在你已经具备了：

✅ **Java运行环境** - JDK 17+  
✅ **集成开发环境** - IntelliJ IDEA或Eclipse  
✅ **项目构建工具** - Maven或Gradle  
✅ **版本控制** - Git  
✅ **基础验证** - 环境测试通过  

### 下一步
1. 📚 学习**02-basic-syntax.md** - 掌握基础语法
2. 🏃‍♂️ 运行**QuickStart.java** - 快速体验
3. 🏗️ 创建你的第一个Java项目
4. 💪 开始系统性学习Java编程

### 学习建议
- 熟悉IDE的调试功能
- 学会使用Maven/Gradle管理依赖
- 经常查看Java官方文档
- 多写代码，多实践

开始你的Java专家之路吧！☕ 