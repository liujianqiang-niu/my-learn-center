# Java基础语法详解

## 🎯 学习目标
- 掌握Java的变量定义和数据类型
- 理解强类型系统和类型安全
- 掌握运算符和表达式的使用
- 学会基本的控制流语句

## 🔤 变量和数据类型

### 变量声明
```java
public class VariableExample {
    public static void main(String[] args) {
        // 基础变量声明（必须声明类型）
        String name = "Java学习者";
        int age = 25;
        double height = 1.75;
        boolean isStudent = true;
        
        System.out.println("姓名: " + name);
        System.out.println("年龄: " + age);
        System.out.println("身高: " + height);
        System.out.println("是学生: " + isStudent);
        
        // final变量（常量）
        final double PI = 3.14159;
        final String COMPANY_NAME = "我的公司";
        
        // PI = 3.14;  // 编译错误！final变量不能修改
        
        System.out.println("圆周率: " + PI);
        System.out.println("公司名: " + COMPANY_NAME);
    }
}
```

### 基础数据类型
```java
public class DataTypes {
    public static void main(String[] args) {
        // 整型
        byte byteValue = 127;                    // 8位，-128到127
        short shortValue = 32767;                // 16位
        int intValue = 2147483647;              // 32位
        long longValue = 9223372036854775807L;  // 64位，注意L后缀
        
        // 浮点型
        float floatValue = 3.14f;               // 32位，注意f后缀
        double doubleValue = 3.141592653589793; // 64位
        
        // 字符型
        char charValue = 'A';                   // 16位Unicode字符
        char unicodeChar = '\u4e2d';           // Unicode中文字符'中'
        
        // 布尔型
        boolean isTrue = true;
        boolean isFalse = false;
        
        // 打印所有类型
        System.out.println("=== 基础数据类型 ===");
        System.out.println("byte: " + byteValue);
        System.out.println("short: " + shortValue);
        System.out.println("int: " + intValue);
        System.out.println("long: " + longValue);
        System.out.println("float: " + floatValue);
        System.out.println("double: " + doubleValue);
        System.out.println("char: " + charValue);
        System.out.println("unicode: " + unicodeChar);
        System.out.println("boolean: " + isTrue);
        
        // 类型范围
        System.out.println("\n=== 数据类型范围 ===");
        System.out.println("int最小值: " + Integer.MIN_VALUE);
        System.out.println("int最大值: " + Integer.MAX_VALUE);
        System.out.println("double最小值: " + Double.MIN_VALUE);
        System.out.println("double最大值: " + Double.MAX_VALUE);
    }
}
```

### 引用数据类型
```java
import java.math.BigDecimal;
import java.math.BigInteger;

public class ReferenceTypes {
    public static void main(String[] args) {
        // 字符串（引用类型）
        String str1 = "Hello";
        String str2 = new String("Hello");
        String str3 = "Hello";
        
        System.out.println("str1 == str2: " + (str1 == str2));      // false
        System.out.println("str1.equals(str2): " + str1.equals(str2)); // true
        System.out.println("str1 == str3: " + (str1 == str3));      // true（字符串池）
        
        // 数组（引用类型）
        int[] numbers = {1, 2, 3, 4, 5};
        String[] names = new String[3];
        names[0] = "张三";
        names[1] = "李四";
        names[2] = "王五";
        
        System.out.println("数组长度: " + numbers.length);
        System.out.println("姓名数组: " + java.util.Arrays.toString(names));
        
        // 包装类型（自动装箱/拆箱）
        Integer intObj = 42;           // 自动装箱
        int intPrim = intObj;          // 自动拆箱
        
        Double doubleObj = 3.14;
        Boolean boolObj = true;
        
        System.out.println("包装类型: " + intObj);
        System.out.println("是否为null: " + (intObj != null));
        
        // 大数类型
        BigInteger bigInt = new BigInteger("12345678901234567890");
        BigDecimal bigDec = new BigDecimal("123.456789012345678901234567890");
        
        System.out.println("BigInteger: " + bigInt);
        System.out.println("BigDecimal: " + bigDec);
        
        // null值
        String nullString = null;
        System.out.println("null字符串: " + nullString);
        // System.out.println(nullString.length()); // 会抛出NullPointerException
    }
}
```

## 📝 字符串操作

### 字符串创建和基本方法
```java
public class StringOperations {
    public static void main(String[] args) {
        String text = "  Java Programming  ";
        
        System.out.println("=== 字符串基本操作 ===");
        System.out.println("原始: '" + text + "'");
        System.out.println("长度: " + text.length());
        System.out.println("去空格: '" + text.trim() + "'");
        System.out.println("大写: " + text.toUpperCase());
        System.out.println("小写: " + text.toLowerCase());
        
        // 查找和判断
        String sentence = "Java is awesome, Java is powerful";
        System.out.println("\n=== 查找和判断 ===");
        System.out.println("包含awesome: " + sentence.contains("awesome"));
        System.out.println("查找Java位置: " + sentence.indexOf("Java"));
        System.out.println("最后出现Java: " + sentence.lastIndexOf("Java"));
        System.out.println("以Java开头: " + sentence.startsWith("Java"));
        System.out.println("以ful结尾: " + sentence.endsWith("ful"));
        
        // 切片和分割
        System.out.println("\n=== 切片和分割 ===");
        System.out.println("子字符串[0,4]: " + sentence.substring(0, 4));
        System.out.println("子字符串[5开始]: " + sentence.substring(5));
        
        String[] words = sentence.split(" ");
        System.out.println("分割后单词数: " + words.length);
        for (String word : words) {
            System.out.println("  " + word);
        }
        
        // 替换
        System.out.println("\n=== 替换操作 ===");
        System.out.println("替换第一个: " + sentence.replace("Java", "Python"));
        System.out.println("替换所有: " + sentence.replaceAll("Java", "Kotlin"));
        System.out.println("正则替换: " + sentence.replaceAll("\\w+", "***"));
    }
}
```

### StringBuilder使用
```java
public class StringBuilderExample {
    public static void main(String[] args) {
        // 为什么使用StringBuilder
        System.out.println("=== 字符串性能对比 ===");
        
        // 效率低下的方式
        long startTime = System.currentTimeMillis();
        String result1 = "";
        for (int i = 0; i < 1000; i++) {
            result1 += "Java ";  // 每次都创建新的String对象
        }
        long endTime = System.currentTimeMillis();
        System.out.println("String拼接耗时: " + (endTime - startTime) + "ms");
        
        // 高效的方式
        startTime = System.currentTimeMillis();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 1000; i++) {
            sb.append("Java ");
        }
        String result2 = sb.toString();
        endTime = System.currentTimeMillis();
        System.out.println("StringBuilder耗时: " + (endTime - startTime) + "ms");
        
        // StringBuilder方法
        StringBuilder builder = new StringBuilder();
        builder.append("Hello");
        builder.append(" ");
        builder.append("World");
        builder.insert(5, " Beautiful");  // 在位置5插入
        builder.delete(5, 15);            // 删除位置5-15的字符
        builder.reverse();                // 反转
        
        System.out.println("StringBuilder结果: " + builder.toString());
    }
}
```

## 📊 数组操作

### 数组创建和基本操作
```java
import java.util.Arrays;

public class ArrayOperations {
    public static void main(String[] args) {
        // 数组创建方式
        int[] numbers1 = {1, 2, 3, 4, 5};                    // 直接初始化
        int[] numbers2 = new int[]{6, 7, 8, 9, 10};         // new方式
        int[] numbers3 = new int[5];                          // 指定大小
        
        // 二维数组
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        System.out.println("=== 数组基本操作 ===");
        System.out.println("数组1: " + Arrays.toString(numbers1));
        System.out.println("数组长度: " + numbers1.length);
        System.out.println("第一个元素: " + numbers1[0]);
        System.out.println("最后一个元素: " + numbers1[numbers1.length - 1]);
        
        // 数组赋值
        numbers3[0] = 100;
        numbers3[1] = 200;
        System.out.println("赋值后的数组3: " + Arrays.toString(numbers3));
        
        // 二维数组访问
        System.out.println("矩阵[1][2]: " + matrix[1][2]);
        System.out.println("矩阵: " + Arrays.deepToString(matrix));
        
        // 数组遍历
        System.out.println("\n=== 数组遍历 ===");
        
        // 传统for循环
        System.out.print("传统for: ");
        for (int i = 0; i < numbers1.length; i++) {
            System.out.print(numbers1[i] + " ");
        }
        System.out.println();
        
        // 增强for循环（for-each）
        System.out.print("增强for: ");
        for (int num : numbers1) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
```

### Arrays工具类
```java
import java.util.Arrays;

public class ArraysUtility {
    public static void main(String[] args) {
        int[] original = {5, 2, 8, 1, 9, 3};
        
        System.out.println("原数组: " + Arrays.toString(original));
        
        // 数组排序
        int[] sorted = original.clone();  // 复制数组
        Arrays.sort(sorted);
        System.out.println("排序后: " + Arrays.toString(sorted));
        
        // 二分查找（需要排序后的数组）
        int index = Arrays.binarySearch(sorted, 5);
        System.out.println("数字5的位置: " + index);
        
        // 数组比较
        int[] copy = Arrays.copyOf(original, original.length);
        System.out.println("数组相等: " + Arrays.equals(original, copy));
        
        // 数组填充
        int[] filled = new int[5];
        Arrays.fill(filled, 42);
        System.out.println("填充数组: " + Arrays.toString(filled));
        
        // 数组复制
        int[] partial = Arrays.copyOfRange(original, 1, 4);  // 复制索引1-3
        System.out.println("部分复制: " + Arrays.toString(partial));
    }
}
```

## 🔧 运算符

### 算术运算符
```java
public class ArithmeticOperators {
    public static void main(String[] args) {
        int a = 15, b = 4;
        
        System.out.println("=== 算术运算符 ===");
        System.out.println(a + " + " + b + " = " + (a + b));    // 加法
        System.out.println(a + " - " + b + " = " + (a - b));    // 减法
        System.out.println(a + " * " + b + " = " + (a * b));    // 乘法
        System.out.println(a + " / " + b + " = " + (a / b));    // 整数除法
        System.out.println(a + " % " + b + " = " + (a % b));    // 取余
        
        // 浮点数除法
        double result = (double) a / b;
        System.out.println("浮点除法: " + a + " / " + b + " = " + result);
        
        // 自增自减
        int x = 10;
        System.out.println("\n=== 自增自减 ===");
        System.out.println("x的初始值: " + x);
        System.out.println("前置自增 ++x: " + (++x));  // 11
        System.out.println("后置自增 x++: " + (x++));  // 11，然后变成12
        System.out.println("x的最终值: " + x);          // 12
        
        // 复合赋值运算符
        int y = 10;
        y += 5;   // 等同于 y = y + 5
        System.out.println("复合赋值 y += 5: " + y);
        
        y *= 2;   // y = y * 2
        System.out.println("复合赋值 y *= 2: " + y);
    }
}
```

### 比较运算符
```java
public class ComparisonOperators {
    public static void main(String[] args) {
        int x = 10, y = 20;
        String str1 = "Hello";
        String str2 = "Hello";
        String str3 = new String("Hello");
        
        System.out.println("=== 数值比较 ===");
        System.out.println(x + " == " + y + ": " + (x == y));
        System.out.println(x + " != " + y + ": " + (x != y));
        System.out.println(x + " < " + y + ": " + (x < y));
        System.out.println(x + " > " + y + ": " + (x > y));
        System.out.println(x + " <= " + y + ": " + (x <= y));
        System.out.println(x + " >= " + y + ": " + (x >= y));
        
        System.out.println("\n=== 字符串比较 ===");
        System.out.println("str1 == str2: " + (str1 == str2));        // true（字符串池）
        System.out.println("str1 == str3: " + (str1 == str3));        // false（不同对象）
        System.out.println("str1.equals(str3): " + str1.equals(str3)); // true（内容相同）
        
        // 字符串比较最佳实践
        System.out.println("字符串比较（推荐）:");
        System.out.println("  内容比较: " + str1.equals(str3));
        System.out.println("  忽略大小写: " + str1.equalsIgnoreCase("HELLO"));
        
        // 处理null值的安全比较
        String nullStr = null;
        System.out.println("安全比较: " + java.util.Objects.equals(str1, nullStr));
    }
}
```

### 逻辑运算符
```java
public class LogicalOperators {
    public static void main(String[] args) {
        boolean isAdult = true;
        boolean hasLicense = false;
        int age = 25;
        int income = 5000;
        
        System.out.println("=== 逻辑运算符 ===");
        System.out.println("与运算 &&: " + (isAdult && hasLicense));
        System.out.println("或运算 ||: " + (isAdult || hasLicense));
        System.out.println("非运算 !: " + (!isAdult));
        
        // 短路求值
        System.out.println("\n=== 短路求值 ===");
        System.out.println("短路与: " + (false && (age++ > 0)));
        System.out.println("age值: " + age);  // 25，没有被自增
        
        System.out.println("短路或: " + (true || (age++ > 0)));
        System.out.println("age值: " + age);  // 25，没有被自增
        
        // 复杂逻辑表达式
        boolean canDrive = isAdult && hasLicense;
        boolean canLoan = isAdult && (income > 3000);
        
        System.out.println("可以开车: " + canDrive);
        System.out.println("可以贷款: " + canLoan);
    }
}
```

## 🎛️ 控制流语句

### 条件语句
```java
public class ConditionalStatements {
    public static void main(String[] args) {
        int score = 85;
        char grade;
        
        // if-else语句
        if (score >= 90) {
            grade = 'A';
            System.out.println("优秀");
        } else if (score >= 80) {
            grade = 'B';
            System.out.println("良好");
        } else if (score >= 70) {
            grade = 'C';
            System.out.println("中等");
        } else if (score >= 60) {
            grade = 'D';
            System.out.println("及格");
        } else {
            grade = 'F';
            System.out.println("不及格");
        }
        
        // 三元运算符
        String result = score >= 60 ? "及格" : "不及格";
        System.out.println("三元运算符结果: " + result);
        
        // switch语句
        switch (grade) {
            case 'A':
                System.out.println("奖学金: 5000元");
                break;
            case 'B':
                System.out.println("奖学金: 3000元");
                break;
            case 'C':
                System.out.println("奖学金: 1000元");
                break;
            case 'D':
                System.out.println("无奖学金，需要努力");
                break;
            default:
                System.out.println("需要重修");
                break;
        }
        
        // 新式switch表达式（Java 14+）
        String scholarship = switch (grade) {
            case 'A' -> "5000元";
            case 'B' -> "3000元";
            case 'C' -> "1000元";
            case 'D' -> "0元";
            default -> "重修";
        };
        System.out.println("switch表达式结果: " + scholarship);
    }
}
```

### 循环语句
```java
public class LoopStatements {
    public static void main(String[] args) {
        System.out.println("=== 循环语句演示 ===");
        
        // for循环
        System.out.print("传统for循环: ");
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        // 增强for循环（for-each）
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.print("增强for循环: ");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
        
        // while循环
        System.out.print("while循环: ");
        int count = 1;
        while (count <= 5) {
            System.out.print(count + " ");
            count++;
        }
        System.out.println();
        
        // do-while循环
        System.out.print("do-while循环: ");
        int num = 1;
        do {
            System.out.print(num + " ");
            num++;
        } while (num <= 5);
        System.out.println();
        
        // 嵌套循环
        System.out.println("\n=== 嵌套循环 - 乘法表 ===");
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                System.out.printf("%d × %d = %d  ", i, j, i * j);
            }
            System.out.println();
        }
    }
}
```

### 循环控制
```java
public class LoopControl {
    public static void main(String[] args) {
        System.out.println("=== 循环控制演示 ===");
        
        // break和continue
        System.out.print("break和continue: ");
        for (int i = 1; i <= 10; i++) {
            if (i == 3) continue;  // 跳过3
            if (i == 8) break;     // 在8处停止
            System.out.print(i + " ");
        }
        System.out.println();
        
        // 标签控制嵌套循环
        System.out.println("\n标签控制嵌套循环:");
        outer: for (int i = 1; i <= 3; i++) {
            inner: for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) {
                    System.out.println("在 i=" + i + ", j=" + j + " 处跳出外层循环");
                    break outer;
                }
                System.out.println("i=" + i + ", j=" + j);
            }
        }
        
        // 在实际项目中查找元素的例子
        int[][] data = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int target = 5;
        boolean found = false;
        
        search: for (int i = 0; i < data.length; i++) {
            for (int j = 0; j < data[i].length; j++) {
                if (data[i][j] == target) {
                    System.out.println("找到 " + target + " 在位置 [" + i + "][" + j + "]");
                    found = true;
                    break search;
                }
            }
        }
        
        if (!found) {
            System.out.println("未找到 " + target);
        }
    }
}
```

## 🎯 方法基础

### 方法定义和调用
```java
public class MethodBasics {
    
    // 无参数无返回值
    public static void sayHello() {
        System.out.println("Hello, World!");
    }
    
    // 有参数有返回值
    public static int add(int a, int b) {
        return a + b;
    }
    
    // 多个参数
    public static String createFullName(String firstName, String lastName) {
        return lastName + ", " + firstName;
    }
    
    // 可变参数
    public static int sum(int... numbers) {
        int total = 0;
        for (int num : numbers) {
            total += num;
        }
        return total;
    }
    
    // 方法重载
    public static double calculateArea(double radius) {
        return Math.PI * radius * radius;  // 圆的面积
    }
    
    public static double calculateArea(double length, double width) {
        return length * width;  // 矩形面积
    }
    
    public static void main(String[] args) {
        System.out.println("=== 方法调用演示 ===");
        
        sayHello();
        
        int result = add(10, 20);
        System.out.println("加法结果: " + result);
        
        String fullName = createFullName("三", "张");
        System.out.println("全名: " + fullName);
        
        int total = sum(1, 2, 3, 4, 5);
        System.out.println("可变参数求和: " + total);
        
        // 方法重载调用
        double circleArea = calculateArea(5.0);
        double rectangleArea = calculateArea(4.0, 6.0);
        System.out.println("圆形面积: " + circleArea);
        System.out.println("矩形面积: " + rectangleArea);
    }
}
```

## 💾 变量作用域

### 作用域演示
```java
public class VariableScope {
    // 类变量（静态）
    static int classVariable = 100;
    
    // 实例变量
    int instanceVariable = 200;
    
    public static void main(String[] args) {
        // 局部变量
        int localVariable = 300;
        
        System.out.println("=== 变量作用域 ===");
        System.out.println("类变量: " + classVariable);
        System.out.println("局部变量: " + localVariable);
        
        // 块作用域
        if (true) {
            int blockVariable = 400;  // 只在这个块中有效
            System.out.println("块变量: " + blockVariable);
        }
        // System.out.println(blockVariable);  // 编译错误！变量不在作用域内
        
        // 方法调用
        demonstrateScope(localVariable);
        
        // 创建实例访问实例变量
        VariableScope instance = new VariableScope();
        System.out.println("实例变量: " + instance.instanceVariable);
    }
    
    public static void demonstrateScope(int parameter) {
        // 参数也是局部变量
        int methodLocal = 500;
        System.out.println("方法内参数: " + parameter);
        System.out.println("方法内局部变量: " + methodLocal);
        System.out.println("访问类变量: " + classVariable);
    }
}
```

## 📋 练习题

### 练习1：基础语法
```java
public class Exercise1 {
    public static void main(String[] args) {
        // 任务：
        // 1. 声明不同类型的变量
        // 2. 进行基本运算
        // 3. 打印结果
        
        // 你的代码：
        
    }
}
```

### 练习2：数组操作
```java
import java.util.Arrays;

public class Exercise2 {
    public static void main(String[] args) {
        // 任务：
        // 1. 创建一个包含10个随机数的数组
        // 2. 找出最大值和最小值
        // 3. 计算平均值
        // 4. 排序数组
        
        // 你的代码：
        
    }
}
```

### 练习3：方法定义
```java
public class Exercise3 {
    
    // 任务：
    // 1. 编写一个计算阶乘的方法
    // 2. 编写一个判断是否为质数的方法
    // 3. 编写一个反转字符串的方法
    
    // 你的代码：
    
    public static void main(String[] args) {
        // 测试你的方法
        
    }
}
```

## 💡 最佳实践

### 1. 命名规范
```java
// 变量和方法：驼峰命名法
int studentAge = 20;
String userName = "张三";

// 常量：大写字母+下划线
final int MAX_SIZE = 100;
final String CONFIG_FILE_NAME = "config.properties";

// 类名：帕斯卡命名法
public class StudentManager {
    // 类内容
}
```

### 2. 类型选择
```java
// 整数类型选择
byte smallNumber = 100;     // -128到127
short mediumNumber = 1000;  // 较小整数
int normalNumber = 100000;  // 最常用
long bigNumber = 1000000L;  // 大整数

// 浮点数类型选择
float precision = 3.14f;    // 单精度，内存敏感时使用
double highPrecision = 3.141592653589793;  // 双精度，推荐使用
```

### 3. 字符串处理
```java
// 频繁字符串操作使用StringBuilder
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append("item").append(i).append(" ");
}
String result = sb.toString();

// 简单拼接使用+
String message = "Hello, " + userName + "!";
```

### 4. 数组vs集合选择
```java
// 固定大小，性能要求高
int[] fixedArray = new int[100];

// 动态大小，功能丰富
java.util.List<Integer> dynamicList = new java.util.ArrayList<>();
```

## 🎯 小结

本章我们学习了Java的基础语法：

✅ **变量声明**：类型声明、final常量、作用域规则  
✅ **数据类型**：基础类型、引用类型、包装类、类型转换  
✅ **字符串操作**：String类方法、StringBuilder性能优化  
✅ **数组操作**：创建、访问、遍历、Arrays工具类  
✅ **运算符**：算术、比较、逻辑、赋值运算符  
✅ **控制流**：if-else、switch、for、while、循环控制  
✅ **方法定义**：参数、返回值、重载、作用域  

### 下一步
学习**03-control-flow.md**，深入掌握Java的程序控制结构和异常处理。

### 记住要点
- Java是强类型语言，变量必须声明类型
- 使用equals()比较字符串内容
- 优先使用增强for循环遍历数组
- 频繁字符串操作使用StringBuilder 