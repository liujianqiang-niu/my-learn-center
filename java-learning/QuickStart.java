import java.util.*;
import java.util.stream.Collectors;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.io.*;
import java.nio.file.*;

/**
 * Java语言快速开始指南
 * 这个文件演示了Java的基本语法和特性，让你快速上手Java编程
 * 
 * 编译运行方式：
 * javac QuickStart.java
 * java QuickStart
 */
public class QuickStart {
    
    public static void main(String[] args) {
        System.out.println("=".repeat(50));
        System.out.println("☕ 欢迎来到Java学习世界！");
        System.out.println("=".repeat(50));
        
        // 调用各个演示方法
        demonstrateBasicSyntax();
        demonstrateCollections();
        demonstrateOOP();
        demonstrateStreamAPI();
        demonstrateExceptionHandling();
        demonstrateFileOperations();
        demonstrateGenics();
        demonstrateLambdas();
        demonstrateDateTime();
        
        System.out.println("\n" + "=".repeat(50));
        System.out.println("🎉 恭喜！你已经体验了Java的主要特性");
        System.out.println("🚀 现在可以开始系统学习docs/目录中的文档了");
        System.out.println("💪 记住：多练习，多实践，你会很快成为Java专家！");
        System.out.println("=".repeat(50));
    }
    
    // ================================
    // 1. 基础语法演示
    // ================================
    public static void demonstrateBasicSyntax() {
        System.out.println("\n📝 基础语法演示：");
        
        // 变量定义
        String name = "Java学习者";
        int age = 25;
        double height = 1.75;
        boolean isStudent = true;
        
        // 字符串格式化
        System.out.printf("姓名: %s%n", name);
        System.out.printf("年龄: %d 岁%n", age);
        System.out.printf("身高: %.2f米%n", height);
        System.out.printf("是学生: %b%n", isStudent);
        
        // 运算符
        int a = 10, b = 3;
        System.out.printf("运算结果: %d + %d = %d%n", a, b, a + b);
        System.out.printf("运算结果: %d %% %d = %d%n", a, b, a % b);
    }
    
    // ================================
    // 2. 集合框架演示
    // ================================
    public static void demonstrateCollections() {
        System.out.println("\n📊 集合框架：");
        
        // ArrayList
        List<String> languages = new ArrayList<>();
        languages.add("Java");
        languages.add("Kotlin");
        languages.add("Scala");
        languages.add("Groovy");
        
        System.out.println("编程语言: " + languages);
        
        // HashMap
        Map<String, Integer> scores = new HashMap<>();
        scores.put("张三", 95);
        scores.put("李四", 87);
        scores.put("王五", 92);
        
        System.out.println("\n📊 成绩统计:");
        scores.forEach((name, score) -> {
            System.out.printf("  %s: %d分%n", name, score);
        });
        
        // Set去重
        Set<String> uniqueSkills = new HashSet<>(Arrays.asList(
            "Java", "Spring", "MySQL", "Java", "Redis", "Spring"
        ));
        System.out.println("技能栈（去重）: " + uniqueSkills);
    }
    
    // ================================
    // 3. 面向对象编程
    // ================================
    public static void demonstrateOOP() {
        System.out.println("\n🏗️ 面向对象编程：");
        
        // 创建学生对象
        Student student = new Student("李四", 22);
        student.addCourse("Java编程");
        student.addCourse("Spring框架");
        student.addCourse("数据库设计");
        
        System.out.println(student);
        student.study();
        
        // 继承演示
        GraduateStudent gradStudent = new GraduateStudent("王五", 24, "计算机科学");
        gradStudent.addCourse("高级算法");
        gradStudent.addCourse("分布式系统");
        gradStudent.conductResearch();
        
        System.out.println(gradStudent);
    }
    
    // ================================
    // 4. Stream API演示
    // ================================
    public static void demonstrateStreamAPI() {
        System.out.println("\n🌊 Stream API：");
        
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        System.out.println("原始数字: " + numbers);
        
        // 过滤偶数
        List<Integer> evenNumbers = numbers.stream()
            .filter(n -> n % 2 == 0)
            .collect(Collectors.toList());
        System.out.println("偶数: " + evenNumbers);
        
        // 映射操作
        List<Integer> squared = numbers.stream()
            .map(n -> n * n)
            .collect(Collectors.toList());
        System.out.println("平方: " + squared);
        
        // 聚合操作
        int sum = numbers.stream()
            .mapToInt(Integer::intValue)
            .sum();
        System.out.println("总和: " + sum);
        
        OptionalDouble average = numbers.stream()
            .mapToDouble(Integer::doubleValue)
            .average();
        System.out.println("平均值: " + average.orElse(0.0));
    }
    
    // ================================
    // 5. 异常处理
    // ================================
    public static void demonstrateExceptionHandling() {
        System.out.println("\n🛡️ 异常处理：");
        
        try {
            int result = divide(10, 2);
            System.out.println("10 ÷ 2 = " + result);
            
            int errorResult = divide(10, 0); // 这里会抛出异常
            System.out.println("10 ÷ 0 = " + errorResult);
        } catch (ArithmeticException e) {
            System.err.println("❌ 算术异常: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("❌ 未知异常: " + e.getMessage());
        } finally {
            System.out.println("✅ 异常处理演示完成");
        }
    }
    
    // ================================
    // 6. 文件操作
    // ================================
    public static void demonstrateFileOperations() {
        System.out.println("\n📁 文件操作：");
        
        String fileName = "temp_example.txt";
        String content = String.format("这是一个临时文件\n用来演示Java的文件操作\n创建时间: %s\n",
            LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));
        
        try {
            // 写文件
            Files.write(Paths.get(fileName), content.getBytes());
            System.out.println("文件已创建: " + fileName);
            
            // 读文件
            List<String> lines = Files.readAllLines(Paths.get(fileName));
            System.out.println("文件内容:");
            for (int i = 0; i < lines.size(); i++) {
                System.out.printf("  第%d行: %s%n", i + 1, lines.get(i));
            }
            
            // 文件信息
            Path path = Paths.get(fileName);
            System.out.println("文件大小: " + Files.size(path) + " 字节");
            
            // 删除文件
            Files.deleteIfExists(path);
            System.out.println("临时文件已删除");
            
        } catch (IOException e) {
            System.err.println("❌ 文件操作失败: " + e.getMessage());
        }
    }
    
    // ================================
    // 7. 泛型演示
    // ================================
    public static void demonstrateGenics() {
        System.out.println("\n🔧 泛型编程：");
        
        // 泛型类使用
        Container<String> stringContainer = new Container<>("Hello, Generics!");
        Container<Integer> numberContainer = new Container<>(42);
        
        System.out.println("字符串容器: " + stringContainer.getValue());
        System.out.println("数字容器: " + numberContainer.getValue());
        
        // 泛型方法
        String[] names = {"张三", "李四", "王五"};
        Integer[] numbers = {1, 2, 3, 4, 5};
        
        System.out.println("交换前姓名: " + Arrays.toString(names));
        swap(names, 0, 2);
        System.out.println("交换后姓名: " + Arrays.toString(names));
        
        System.out.println("交换前数字: " + Arrays.toString(numbers));
        swap(numbers, 1, 3);
        System.out.println("交换后数字: " + Arrays.toString(numbers));
    }
    
    // ================================
    // 8. Lambda表达式和函数式编程
    // ================================
    public static void demonstrateLambdas() {
        System.out.println("\n🎯 Lambda表达式：");
        
        List<String> words = Arrays.asList("Java", "Lambda", "Stream", "Optional", "Functional");
        
        // Lambda表达式
        words.stream()
            .filter(word -> word.length() > 4)
            .map(String::toUpperCase)
            .sorted()
            .forEach(word -> System.out.println("  处理后: " + word));
        
        // 方法引用
        List<Integer> lengths = words.stream()
            .map(String::length)
            .collect(Collectors.toList());
        System.out.println("单词长度: " + lengths);
        
        // 函数式接口
        Calculator calc = (x, y) -> x + y;
        System.out.println("Lambda计算: 5 + 3 = " + calc.calculate(5, 3));
    }
    
    // ================================
    // 9. 日期时间处理
    // ================================
    public static void demonstrateDateTime() {
        System.out.println("\n⏰ 日期时间处理：");
        
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        
        System.out.println("当前时间: " + now.format(formatter));
        System.out.println("今年是: " + now.getYear());
        System.out.println("这个月是: " + now.getMonth());
        System.out.println("今天是周: " + now.getDayOfWeek());
        
        // 时间计算
        LocalDateTime future = now.plusDays(30);
        System.out.println("30天后: " + future.format(formatter));
    }
    
    // ================================
    // 工具方法
    // ================================
    public static int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("除数不能为零");
        }
        return a / b;
    }
    
    public static <T> void swap(T[] array, int i, int j) {
        if (i >= 0 && i < array.length && j >= 0 && j < array.length) {
            T temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
}

// ================================
// 学生类定义
// ================================
class Student {
    private String name;
    private int age;
    private List<String> courses;
    
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
        this.courses = new ArrayList<>();
    }
    
    public void addCourse(String course) {
        courses.add(course);
        System.out.printf("%s 添加了课程: %s%n", name, course);
    }
    
    public void study() {
        if (!courses.isEmpty()) {
            System.out.printf("%s 正在学习: %s%n", name, String.join("、", courses));
        } else {
            System.out.printf("%s 还没有选择课程%n", name);
        }
    }
    
    // Getters
    public String getName() { return name; }
    public int getAge() { return age; }
    public List<String> getCourses() { return new ArrayList<>(courses); }
    
    @Override
    public String toString() {
        return String.format("学生[姓名=%s, 年龄=%d, 课程=%d门]", name, age, courses.size());
    }
}

// ================================
// 研究生类 - 继承演示
// ================================
class GraduateStudent extends Student {
    private String major;
    
    public GraduateStudent(String name, int age, String major) {
        super(name, age);
        this.major = major;
    }
    
    public void conductResearch() {
        System.out.printf("%s 正在进行 %s 领域的研究%n", getName(), major);
    }
    
    @Override
    public String toString() {
        return String.format("研究生[姓名=%s, 年龄=%d, 专业=%s, 课程=%d门]", 
            getName(), getAge(), major, getCourses().size());
    }
}

// ================================
// 泛型容器类
// ================================
class Container<T> {
    private T value;
    
    public Container(T value) {
        this.value = value;
    }
    
    public T getValue() {
        return value;
    }
    
    public void setValue(T value) {
        this.value = value;
    }
    
    @Override
    public String toString() {
        return "Container{value=" + value + ", type=" + value.getClass().getSimpleName() + "}";
    }
}

// ================================
// 函数式接口
// ================================
@FunctionalInterface
interface Calculator {
    int calculate(int a, int b);
} 