# Java核心语法指南 ☕

## 📖 目录
1. [基础语法](#1-基础语法)
2. [面向对象](#2-面向对象)
3. [集合框架](#3-集合框架)
4. [异常处理](#4-异常处理)
5. [多线程编程](#5-多线程编程)
6. [IO操作](#6-io操作)
7. [Spring框架](#7-spring框架)
8. [实战项目](#8-实战项目)

---

## 1. 基础语法

### 变量和数据类型
```java
public class BasicSyntax {
    public static void main(String[] args) {
        // 基本数据类型
        int age = 25;
        double height = 175.5;
        boolean isStudent = true;
        char grade = 'A';
        
        // 引用数据类型
        String name = "张三";
        String[] subjects = {"数学", "编程", "英语"};
        
        // 常量
        final double PI = 3.14159;
        final String APP_NAME = "我的应用";
        
        // 类型转换
        String ageStr = String.valueOf(age);
        int parsed = Integer.parseInt("123");
        
        // 输出
        System.out.println("姓名：" + name);
        System.out.printf("年龄：%d，身高：%.1f%n", age, height);
    }
}
```

### 控制结构
```java
// 条件语句
public void checkGrade(int score) {
    if (score >= 90) {
        System.out.println("优秀");
    } else if (score >= 80) {
        System.out.println("良好");
    } else if (score >= 60) {
        System.out.println("及格");
    } else {
        System.out.println("不及格");
    }
    
    // switch语句
    switch (score / 10) {
        case 10:
        case 9:
            System.out.println("A级");
            break;
        case 8:
            System.out.println("B级");
            break;
        default:
            System.out.println("C级");
    }
}

// 循环
public void loopExamples() {
    // for循环
    for (int i = 0; i < 5; i++) {
        System.out.println("计数: " + i);
    }
    
    // 增强for循环
    String[] fruits = {"苹果", "香蕉", "橘子"};
    for (String fruit : fruits) {
        System.out.println("水果: " + fruit);
    }
    
    // while循环
    int count = 0;
    while (count < 3) {
        System.out.println("循环: " + count);
        count++;
    }
}
```

---

## 2. 面向对象

### 类和对象
```java
// 学生类
public class Student {
    private String name;
    private int age;
    private List<String> subjects;
    
    // 构造函数
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
        this.subjects = new ArrayList<>();
    }
    
    // Getter和Setter
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        }
    }
    
    // 业务方法
    public void addSubject(String subject) {
        if (!subjects.contains(subject)) {
            subjects.add(subject);
        }
    }
    
    public void introduce() {
        System.out.println("我是" + name + "，今年" + age + "岁");
        System.out.println("学习科目：" + String.join("、", subjects));
    }
    
    @Override
    public String toString() {
        return "Student{name='" + name + "', age=" + age + "}";
    }
}
```

### 继承和多态
```java
// 抽象父类
abstract class Animal {
    protected String name;
    
    public Animal(String name) {
        this.name = name;
    }
    
    public abstract void makeSound();
    
    public void sleep() {
        System.out.println(name + "在睡觉");
    }
}

// 具体子类
class Dog extends Animal {
    private String breed;
    
    public Dog(String name, String breed) {
        super(name);
        this.breed = breed;
    }
    
    @Override
    public void makeSound() {
        System.out.println(name + "（" + breed + "）在汪汪叫");
    }
    
    public void fetch() {
        System.out.println(name + "在捡球");
    }
}

class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }
    
    @Override
    public void makeSound() {
        System.out.println(name + "在喵喵叫");
    }
}

// 接口
interface Flyable {
    void fly();
}

class Bird extends Animal implements Flyable {
    public Bird(String name) {
        super(name);
    }
    
    @Override
    public void makeSound() {
        System.out.println(name + "在唧唧叫");
    }
    
    @Override
    public void fly() {
        System.out.println(name + "在飞行");
    }
}

// 多态演示
public void demonstratePolymorphism() {
    List<Animal> animals = Arrays.asList(
        new Dog("旺财", "金毛"),
        new Cat("小咪"),
        new Bird("小鸟")
    );
    
    for (Animal animal : animals) {
        animal.makeSound();  // 多态调用
        animal.sleep();
        
        // 类型检查和转换
        if (animal instanceof Flyable) {
            ((Flyable) animal).fly();
        }
    }
}
```

---

## 3. 集合框架

### List集合
```java
import java.util.*;

public class CollectionExamples {
    public void listExamples() {
        // ArrayList - 可变大小数组
        List<String> names = new ArrayList<>();
        names.add("张三");
        names.add("李四");
        names.add("王五");
        
        // 访问元素
        System.out.println("第一个：" + names.get(0));
        System.out.println("大小：" + names.size());
        
        // 遍历
        for (String name : names) {
            System.out.println("姓名：" + name);
        }
        
        // Lambda表达式遍历
        names.forEach(name -> System.out.println("Hello, " + name));
        
        // Stream操作
        List<String> upperNames = names.stream()
            .map(String::toUpperCase)
            .collect(Collectors.toList());
        
        List<String> filtered = names.stream()
            .filter(name -> name.startsWith("张"))
            .collect(Collectors.toList());
    }
}
```

### Map集合
```java
public void mapExamples() {
    // HashMap
    Map<String, Object> person = new HashMap<>();
    person.put("name", "张三");
    person.put("age", 25);
    person.put("city", "北京");
    
    // 访问
    String name = (String) person.get("name");
    Integer age = (Integer) person.get("age");
    
    // 遍历
    for (Map.Entry<String, Object> entry : person.entrySet()) {
        System.out.println(entry.getKey() + ": " + entry.getValue());
    }
    
    // Lambda遍历
    person.forEach((key, value) -> 
        System.out.println(key + " -> " + value));
    
    // 实用方法
    Object defaultValue = person.getOrDefault("job", "未知");
    person.putIfAbsent("hobby", "编程");
}
```

### Set集合
```java
public void setExamples() {
    Set<String> uniqueNames = new HashSet<>();
    uniqueNames.add("张三");
    uniqueNames.add("李四");
    uniqueNames.add("张三");  // 重复元素会被忽略
    
    System.out.println("唯一姓名数量：" + uniqueNames.size());
    
    // TreeSet - 自动排序
    Set<Integer> sortedNumbers = new TreeSet<>();
    sortedNumbers.addAll(Arrays.asList(3, 1, 4, 1, 5, 9));
    System.out.println("排序后的数字：" + sortedNumbers);
}
```

---

## 4. 异常处理

### 基础异常处理
```java
public class ExceptionDemo {
    
    public void basicExceptionHandling() {
        try {
            int result = divideNumbers(10, 0);
            System.out.println("结果：" + result);
        } catch (ArithmeticException e) {
            System.err.println("数学错误：" + e.getMessage());
        } catch (Exception e) {
            System.err.println("未知错误：" + e.getMessage());
        } finally {
            System.out.println("清理资源");
        }
    }
    
    public int divideNumbers(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("不能除以零");
        }
        return a / b;
    }
}
```

### 自定义异常
```java
// 自定义异常类
class UserNotFoundException extends Exception {
    public UserNotFoundException(String message) {
        super(message);
    }
}

class UserService {
    private Map<Integer, String> users = Map.of(
        1, "张三",
        2, "李四"
    );
    
    public String findUser(int id) throws UserNotFoundException {
        String user = users.get(id);
        if (user == null) {
            throw new UserNotFoundException("用户ID " + id + " 不存在");
        }
        return user;
    }
    
    public void demonstrateUsage() {
        try {
            String user = findUser(999);
            System.out.println("找到用户：" + user);
        } catch (UserNotFoundException e) {
            System.err.println("错误：" + e.getMessage());
        }
    }
}
```

---

## 5. 多线程编程

### 基础线程
```java
// 继承Thread类
class CounterThread extends Thread {
    private String name;
    
    public CounterThread(String name) {
        this.name = name;
    }
    
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(name + "：计数 " + i);
            try {
                Thread.sleep(1000);  // 暂停1秒
            } catch (InterruptedException e) {
                System.out.println(name + " 被中断");
                break;
            }
        }
    }
}

// 实现Runnable接口（推荐）
class TaskRunner implements Runnable {
    private String taskName;
    
    public TaskRunner(String taskName) {
        this.taskName = taskName;
    }
    
    @Override
    public void run() {
        System.out.println("开始执行任务：" + taskName);
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("任务完成：" + taskName);
    }
}

// 使用线程
public void threadDemo() {
    // 方法1
    CounterThread t1 = new CounterThread("线程1");
    t1.start();
    
    // 方法2
    Thread t2 = new Thread(new TaskRunner("数据处理"));
    t2.start();
    
    // Lambda表达式
    Thread t3 = new Thread(() -> {
        System.out.println("Lambda线程执行");
    });
    t3.start();
}
```

### 线程池
```java
import java.util.concurrent.*;

public class ThreadPoolDemo {
    
    public void executorDemo() {
        // 创建线程池
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        // 提交任务
        for (int i = 1; i <= 5; i++) {
            final int taskId = i;
            executor.submit(() -> {
                System.out.println("执行任务 " + taskId + 
                    " by " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }
        
        // 关闭线程池
        executor.shutdown();
        try {
            if (!executor.awaitTermination(5, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
        }
    }
}
```

---

## 6. IO操作

### 文件读写
```java
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class FileOperations {
    
    // 读取文件
    public void readFile() {
        try {
            // 读取整个文件
            String content = Files.readString(Paths.get("test.txt"));
            System.out.println(content);
            
            // 按行读取
            List<String> lines = Files.readAllLines(Paths.get("test.txt"));
            for (int i = 0; i < lines.size(); i++) {
                System.out.println((i + 1) + ": " + lines.get(i));
            }
            
        } catch (IOException e) {
            System.err.println("读取文件失败：" + e.getMessage());
        }
    }
    
    // 写入文件
    public void writeFile() {
        try {
            // 写入字符串
            Files.writeString(Paths.get("output.txt"), "Hello Java!");
            
            // 写入行列表
            List<String> data = Arrays.asList("第一行", "第二行", "第三行");
            Files.write(Paths.get("lines.txt"), data);
            
            // 追加内容
            Files.write(Paths.get("output.txt"), 
                "\n新的内容".getBytes(), 
                StandardOpenOption.APPEND);
                
        } catch (IOException e) {
            System.err.println("写入文件失败：" + e.getMessage());
        }
    }
}
```

### 目录操作
```java
public void directoryOperations() {
    try {
        Path dir = Paths.get("myDirectory");
        
        // 创建目录
        Files.createDirectories(dir);
        
        // 遍历目录
        Files.list(dir).forEach(path -> {
            System.out.println("文件：" + path.getFileName());
        });
        
        // 递归遍历
        Files.walk(dir)
            .filter(Files::isRegularFile)
            .filter(path -> path.toString().endsWith(".txt"))
            .forEach(System.out::println);
            
    } catch (IOException e) {
        System.err.println("目录操作失败：" + e.getMessage());
    }
}
```

---

## 7. Spring框架

### Spring Boot基础
```java
// 主启动类
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

// 控制器
@RestController
@RequestMapping("/api")
public class UserController {
    
    private final UserService userService;
    
    // 构造器注入
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @GetMapping("/users")
    public List<User> getAllUsers() {
        return userService.findAll();
    }
    
    @GetMapping("/users/{id}")
    public User getUser(@PathVariable Long id) {
        return userService.findById(id);
    }
    
    @PostMapping("/users")
    public User createUser(@RequestBody User user) {
        return userService.save(user);
    }
    
    @PutMapping("/users/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User user) {
        user.setId(id);
        return userService.save(user);
    }
    
    @DeleteMapping("/users/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteById(id);
    }
}
```

### 依赖注入和配置
```java
// 服务层
@Service
public class UserService {
    
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public List<User> findAll() {
        return userRepository.findAll();
    }
    
    public User findById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException("用户不存在: " + id));
    }
    
    public User save(User user) {
        // 业务逻辑验证
        if (user.getName() == null || user.getName().trim().isEmpty()) {
            throw new IllegalArgumentException("用户名不能为空");
        }
        return userRepository.save(user);
    }
    
    public void deleteById(Long id) {
        if (!userRepository.existsById(id)) {
            throw new UserNotFoundException("要删除的用户不存在: " + id);
        }
        userRepository.deleteById(id);
    }
}

// 数据访问层
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByNameContaining(String name);
    List<User> findByAgeGreaterThan(int age);
}
```

### 实体类和配置
```java
// 实体类
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, length = 100)
    private String name;
    
    @Column(nullable = false)
    private String email;
    
    private Integer age;
    
    @CreationTimestamp
    private LocalDateTime createdAt;
    
    // 构造函数
    public User() {}
    
    public User(String name, String email, Integer age) {
        this.name = name;
        this.email = email;
        this.age = age;
    }
    
    // Getter和Setter（省略）
}

// 配置类
@Configuration
public class AppConfig {
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    
    @Bean
    @Primary
    public ObjectMapper objectMapper() {
        ObjectMapper mapper = new ObjectMapper();
        mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
        return mapper;
    }
}
```

---

## 8. 实战项目

### 项目1：图书管理系统
```java
// 图书实体
@Entity
public class Book {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String title;
    private String author;
    private String isbn;
    private BigDecimal price;
    private LocalDate publishDate;
    
    // 构造函数和getter/setter省略
}

// 图书服务
@Service
@Transactional
public class BookService {
    
    @Autowired
    private BookRepository bookRepository;
    
    public List<Book> searchBooks(String keyword) {
        return bookRepository.findByTitleContainingOrAuthorContaining(keyword, keyword);
    }
    
    public Book borrowBook(Long bookId) {
        Book book = bookRepository.findById(bookId)
            .orElseThrow(() -> new BookNotFoundException("图书不存在"));
            
        if (book.isAvailable()) {
            book.setStatus("BORROWED");
            book.setBorrowDate(LocalDate.now());
            return bookRepository.save(book);
        } else {
            throw new BookNotAvailableException("图书已被借出");
        }
    }
    
    public Book returnBook(Long bookId) {
        Book book = bookRepository.findById(bookId)
            .orElseThrow(() -> new BookNotFoundException("图书不存在"));
            
        book.setStatus("AVAILABLE");
        book.setBorrowDate(null);
        book.setReturnDate(LocalDate.now());
        return bookRepository.save(book);
    }
}

// 图书控制器
@RestController
@RequestMapping("/api/books")
public class BookController {
    
    @Autowired
    private BookService bookService;
    
    @GetMapping("/search")
    public ResponseEntity<List<Book>> searchBooks(@RequestParam String keyword) {
        List<Book> books = bookService.searchBooks(keyword);
        return ResponseEntity.ok(books);
    }
    
    @PostMapping("/{id}/borrow")
    public ResponseEntity<Book> borrowBook(@PathVariable Long id) {
        try {
            Book book = bookService.borrowBook(id);
            return ResponseEntity.ok(book);
        } catch (BookNotFoundException e) {
            return ResponseEntity.notFound().build();
        } catch (BookNotAvailableException e) {
            return ResponseEntity.badRequest().build();
        }
    }
    
    @PostMapping("/{id}/return")
    public ResponseEntity<Book> returnBook(@PathVariable Long id) {
        try {
            Book book = bookService.returnBook(id);
            return ResponseEntity.ok(book);
        } catch (BookNotFoundException e) {
            return ResponseEntity.notFound().build();
        }
    }
}
```

### 项目2：用户认证系统
```java
// 用户实体
@Entity
public class AppUser {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(unique = true)
    private String username;
    
    private String password;
    private String email;
    
    @Enumerated(EnumType.STRING)
    private UserRole role;
    
    private boolean enabled = true;
    
    // 构造函数和getter/setter省略
}

// 认证服务
@Service
public class AuthService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private PasswordEncoder passwordEncoder;
    
    @Autowired
    private JwtTokenUtil jwtTokenUtil;
    
    public String authenticate(String username, String password) {
        AppUser user = userRepository.findByUsername(username)
            .orElseThrow(() -> new UsernameNotFoundException("用户不存在"));
        
        if (!passwordEncoder.matches(password, user.getPassword())) {
            throw new BadCredentialsException("密码错误");
        }
        
        if (!user.isEnabled()) {
            throw new DisabledException("用户账户已禁用");
        }
        
        return jwtTokenUtil.generateToken(user);
    }
    
    public AppUser registerUser(UserRegistrationDto dto) {
        if (userRepository.findByUsername(dto.getUsername()).isPresent()) {
            throw new IllegalArgumentException("用户名已存在");
        }
        
        AppUser user = new AppUser();
        user.setUsername(dto.getUsername());
        user.setPassword(passwordEncoder.encode(dto.getPassword()));
        user.setEmail(dto.getEmail());
        user.setRole(UserRole.USER);
        
        return userRepository.save(user);
    }
}

// 认证控制器
@RestController
@RequestMapping("/auth")
public class AuthController {
    
    @Autowired
    private AuthService authService;
    
    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@RequestBody LoginRequest request) {
        try {
            String token = authService.authenticate(request.getUsername(), request.getPassword());
            AuthResponse response = new AuthResponse(token, "登录成功");
            return ResponseEntity.ok(response);
        } catch (AuthenticationException e) {
            AuthResponse response = new AuthResponse(null, "认证失败：" + e.getMessage());
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(response);
        }
    }
    
    @PostMapping("/register")
    public ResponseEntity<AuthResponse> register(@RequestBody UserRegistrationDto dto) {
        try {
            AppUser user = authService.registerUser(dto);
            AuthResponse response = new AuthResponse(null, "注册成功");
            return ResponseEntity.status(HttpStatus.CREATED).body(response);
        } catch (IllegalArgumentException e) {
            AuthResponse response = new AuthResponse(null, e.getMessage());
            return ResponseEntity.badRequest().body(response);
        }
    }
}
```

---

## 🎯 Java学习路径

### 第1-2周：基础语法
- ✅ 变量类型、运算符、控制结构
- ✅ 数组操作和字符串处理
- ✅ 方法定义和调用
- **练习**: 控制台计算器

### 第3-4周：面向对象
- ✅ 类、对象、继承、多态
- ✅ 接口和抽象类
- ✅ 包和访问控制
- **练习**: 学生管理系统

### 第5-6周：集合和异常
- ✅ List、Set、Map使用
- ✅ Stream API和Lambda
- ✅ 异常处理机制
- **练习**: 数据处理程序

### 第7-8周：多线程和IO
- ✅ 线程创建和同步
- ✅ 线程池使用
- ✅ 文件IO操作
- **练习**: 并发下载器

### 第9-12周：Spring框架
- ✅ 依赖注入和Bean管理
- ✅ Spring Boot快速开发
- ✅ JPA数据库操作
- **练习**: RESTful API服务

### 第13周+：企业级开发
- ✅ 微服务架构
- ✅ 性能优化
- ✅ 部署和监控
- **目标**: 企业级应用开发

---

## 💡 实用开发技巧

### 1. 代码规范
```java
// 命名规范
public class UserService {           // 类名：大驼峰
    private static final String API_KEY = "abc123";  // 常量：大写下划线
    private UserRepository userRepository;           // 变量：小驼峰
    
    public User findUserById(Long id) {             // 方法：小驼峰
        return userRepository.findById(id).orElse(null);
    }
}
```

### 2. 异常处理最佳实践
```java
// 全局异常处理器
@ControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException e) {
        ErrorResponse error = new ErrorResponse("USER_NOT_FOUND", e.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(ValidationException.class)
    public ResponseEntity<ErrorResponse> handleValidation(ValidationException e) {
        ErrorResponse error = new ErrorResponse("VALIDATION_ERROR", e.getMessage());
        return ResponseEntity.badRequest().body(error);
    }
}
```

### 3. 单元测试
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void testFindUserById() {
        // Given
        Long userId = 1L;
        User expectedUser = new User("张三", "zhang@email.com", 25);
        when(userRepository.findById(userId)).thenReturn(Optional.of(expectedUser));
        
        // When
        User actualUser = userService.findById(userId);
        
        // Then
        assertEquals(expectedUser.getName(), actualUser.getName());
        assertEquals(expectedUser.getEmail(), actualUser.getEmail());
        verify(userRepository).findById(userId);
    }
    
    @Test
    void testUserNotFound() {
        // Given
        Long userId = 999L;
        when(userRepository.findById(userId)).thenReturn(Optional.empty());
        
        // When & Then
        assertThrows(UserNotFoundException.class, () -> {
            userService.findById(userId);
        });
    }
}
```

---

## 📚 学习资源推荐

1. **官方文档**: [Oracle Java Documentation](https://docs.oracle.com/javase/)
2. **Spring官网**: [Spring.io](https://spring.io/guides)
3. **经典书籍**:
   - 《Java核心技术》
   - 《Effective Java》
   - 《Spring实战》
4. **在线资源**:
   - Baeldung Java教程
   - Spring Boot官方指南

---

## 🎉 成为Java专家的关键

### 核心技能
- ✅ **扎实基础**: 深入理解OOP、集合、多线程
- ✅ **Spring生态**: 熟练使用Spring全家桶
- ✅ **数据库技术**: JPA/MyBatis + MySQL/PostgreSQL
- ✅ **测试能力**: JUnit + Mockito单元测试
- ✅ **工具掌握**: Maven/Gradle + Git + IDE

### 项目经验
- ✅ **Web应用**: Spring Boot + RESTful API
- ✅ **微服务**: Spring Cloud分布式架构
- ✅ **数据处理**: 并发编程 + 性能优化
- ✅ **企业应用**: 完整的业务系统开发

### 持续学习
- 🔄 跟进Java新版本特性
- 📖 学习设计模式和架构设计
- 🛠️ 掌握DevOps和云原生技术
- 👥 参与开源项目和技术社区

**开始您的Java专家之旅！编码改变世界！** ☕ 