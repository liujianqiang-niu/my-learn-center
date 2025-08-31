# 第2章：Rust基础语法 📝

## 学习目标
- 掌握Rust的变量声明和可变性
- 理解Rust的基本数据类型
- 学会函数的定义和调用
- 掌握注释的使用方法
- 理解Rust的表达式和语句概念

## 1. 变量和可变性

### 变量声明
Rust中的变量默认是不可变的(immutable)，这是Rust安全性的重要特性。

```rust
fn main() {
    // 声明不可变变量
    let x = 5;
    println!("x的值是: {}", x);
    
    // x = 6; // 这行代码会编译错误！
    
    // 声明可变变量
    let mut y = 5;
    println!("y的值是: {}", y);
    y = 6; // 这是允许的
    println!("y的新值是: {}", y);
}
```

### 变量遮蔽(Shadowing)
可以重新声明同名变量，新变量会"遮蔽"前一个变量。

```rust
fn main() {
    let x = 5;
    
    // 遮蔽前一个x
    let x = x + 1;
    
    {
        // 在内部作用域遮蔽
        let x = x * 2;
        println!("内部作用域的x: {}", x); // 输出: 12
    }
    
    println!("外部作用域的x: {}", x); // 输出: 6
}
```

### 常量声明
常量必须在编译时确定值，并且必须指定类型。

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;

fn main() {
    println!("三小时等于{}秒", THREE_HOURS_IN_SECONDS);
}
```

## 2. 数据类型

### 标量类型

#### 整数类型
| 长度 | 有符号 | 无符号 |
|------|--------|--------|
| 8位  | i8     | u8     |
| 16位 | i16    | u16    |
| 32位 | i32    | u32    |
| 64位 | i64    | u64    |
| 128位| i128   | u128   |
| arch | isize  | usize  |

```rust
fn main() {
    // 整数类型示例
    let decimal = 98_222;       // 十进制
    let hex = 0xff;             // 十六进制
    let octal = 0o77;           // 八进制
    let binary = 0b1111_0000;   // 二进制
    let byte = b'A';            // 字节(仅限u8)
    
    println!("十进制: {}", decimal);
    println!("十六进制: {}", hex);
    println!("八进制: {}", octal);
    println!("二进制: {}", binary);
    println!("字节: {}", byte);
}
```

#### 浮点类型
```rust
fn main() {
    let x = 2.0;        // f64 (默认)
    let y: f32 = 3.0;   // f32
    
    println!("x: {}, y: {}", x, y);
}
```

#### 布尔类型
```rust
fn main() {
    let t = true;
    let f: bool = false;
    
    println!("真: {}, 假: {}", t, f);
}
```

#### 字符类型
```rust
fn main() {
    let c = 'z';
    let z = 'ℤ';
    let heart_eyed_cat = '😻';
    
    println!("字符: {}, {}, {}", c, z, heart_eyed_cat);
}
```

### 复合类型

#### 元组(Tuple)
```rust
fn main() {
    // 创建元组
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    
    // 解构元组
    let (x, y, z) = tup;
    println!("x: {}, y: {}, z: {}", x, y, z);
    
    // 通过索引访问
    let five_hundred = tup.0;
    let six_point_four = tup.1;
    let one = tup.2;
    
    println!("索引访问: {}, {}, {}", five_hundred, six_point_four, one);
}
```

#### 数组(Array)
```rust
fn main() {
    // 创建数组
    let a = [1, 2, 3, 4, 5];
    let months = ["一月", "二月", "三月", "四月", "五月", "六月",
                 "七月", "八月", "九月", "十月", "十一月", "十二月"];
    
    // 指定类型和长度
    let a: [i32; 5] = [1, 2, 3, 4, 5];
    
    // 相同值初始化
    let a = [3; 5]; // 等价于 [3, 3, 3, 3, 3]
    
    // 访问数组元素
    let first = a[0];
    let second = a[1];
    
    println!("第一个元素: {}", first);
    println!("第二个元素: {}", second);
    
    // 数组长度
    println!("数组长度: {}", a.len());
}
```

## 3. 函数

### 函数定义
```rust
fn main() {
    println!("Hello, world!");
    
    another_function();
    function_with_parameter(5);
    function_with_multiple_parameters(5, 6);
    
    let x = five();
    println!("five()的返回值: {}", x);
    
    let x = plus_one(5);
    println!("plus_one(5)的返回值: {}", x);
}

// 无参数函数
fn another_function() {
    println!("这是另一个函数！");
}

// 带参数的函数
fn function_with_parameter(x: i32) {
    println!("参数x的值是: {}", x);
}

// 多个参数的函数
fn function_with_multiple_parameters(x: i32, y: i32) {
    println!("x: {}, y: {}", x, y);
}

// 有返回值的函数
fn five() -> i32 {
    5  // 注意：没有分号，这是一个表达式
}

fn plus_one(x: i32) -> i32 {
    x + 1  // 返回表达式
}
```

### 语句和表达式
```rust
fn main() {
    // 语句(statement): 执行一些操作但不返回值
    let y = 6;  // 这是一个语句
    
    // 表达式(expression): 计算并返回一个值
    let x = {
        let y = 3;
        y + 1  // 表达式，注意没有分号
    };
    
    println!("x的值是: {}", x); // 输出: 4
}
```

## 4. 注释

### 行注释
```rust
fn main() {
    // 这是行注释
    // 可以写多行
    let x = 5; // 也可以在代码后面注释
}
```

### 文档注释
```rust
/// 这是文档注释
/// 用于生成API文档
/// 
/// # 示例
/// ```
/// let result = add_two(2);
/// assert_eq!(result, 4);
/// ```
fn add_two(x: i32) -> i32 {
    x + 2
}

fn main() {
    let result = add_two(3);
    println!("结果: {}", result);
}
```

## 5. 打印和格式化

### println!宏的使用
```rust
fn main() {
    // 基本打印
    println!("Hello world!");
    
    // 位置参数
    println!("{} days", 31);
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");
    
    // 命名参数
    println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over");
    
    // 数字格式化
    println!("十进制: {}", 42);
    println!("二进制: {:b}", 42);
    println!("八进制: {:o}", 42);
    println!("十六进制: {:x}", 42);
    println!("十六进制(大写): {:X}", 42);
    
    // 浮点数格式化
    let pi = 3.141592653;
    println!("π约等于 {:.3}", pi);  // 保留3位小数
    
    // 对齐和填充
    println!("{:>10}", "右对齐");     // 右对齐，宽度10
    println!("{:<10}", "左对齐");     // 左对齐，宽度10
    println!("{:^10}", "居中");       // 居中，宽度10
    println!("{:0>4}", 42);          // 用0填充到宽度4
}
```

### debug打印
```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect = Rectangle {
        width: 30,
        height: 50,
    };
    
    // Debug格式打印
    println!("rect is {:?}", rect);
    
    // 美化的Debug格式
    println!("rect is {:#?}", rect);
}
```

## 6. 类型推断和类型注解

### 类型推断
```rust
fn main() {
    // Rust可以推断类型
    let x = 42;          // 推断为i32
    let y = 3.14;        // 推断为f64
    let z = true;        // 推断为bool
    let s = "hello";     // 推断为&str
    
    println!("x: {}, y: {}, z: {}, s: {}", x, y, z, s);
}
```

### 类型注解
```rust
fn main() {
    // 显式指定类型
    let x: i64 = 42;
    let y: f32 = 3.14;
    let z: char = 'A';
    
    // 在需要时必须指定类型
    let guess: u32 = "42".parse().expect("不是一个数字！");
    
    println!("guess: {}", guess);
}
```

## 7. 实践练习

### 练习1：变量操作
```rust
fn main() {
    // TODO: 声明一个不可变变量并赋值
    
    // TODO: 声明一个可变变量并修改它的值
    
    // TODO: 使用变量遮蔽改变变量类型
    let spaces = "   ";
    let spaces = spaces.len();
    
    println!("spaces: {}", spaces);
}
```

### 练习2：数据类型练习
```rust
fn main() {
    // TODO: 创建不同类型的整数
    
    // TODO: 创建浮点数并进行运算
    
    // TODO: 创建元组并解构
    
    // TODO: 创建数组并访问元素
}
```

### 练习3：函数练习
```rust
// TODO: 编写一个函数，接收两个i32参数，返回它们的和
fn add(a: i32, b: i32) -> i32 {
    // 实现这里
}

// TODO: 编写一个函数，接收一个数字，返回它的平方
fn square(x: i32) -> i32 {
    // 实现这里
}

// TODO: 编写一个函数，不接收参数，返回一个问候字符串
fn greet() -> String {
    // 实现这里
    String::from("Hello, Rust!")
}

fn main() {
    let result = add(5, 3);
    println!("5 + 3 = {}", result);
    
    let square_result = square(4);
    println!("4的平方 = {}", square_result);
    
    let greeting = greet();
    println!("{}", greeting);
}
```

## 8. 常见错误和解决方案

### 错误1：尝试修改不可变变量
```rust
fn main() {
    let x = 5;
    x = 6; // 错误：cannot assign twice to immutable variable
}

// 解决方案：使用mut关键字
fn main() {
    let mut x = 5;
    x = 6; // 正确
}
```

### 错误2：数组越界访问
```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
    let element = a[10]; // 运行时会panic
}

// 解决方案：使用get方法安全访问
fn main() {
    let a = [1, 2, 3, 4, 5];
    match a.get(10) {
        Some(value) => println!("值是: {}", value),
        None => println!("索引超出范围"),
    }
}
```

### 错误3：函数返回类型不匹配
```rust
fn bad_function() -> i32 {
    "hello" // 错误：expected i32, found &str
}

// 解决方案：确保返回正确的类型
fn good_function() -> i32 {
    42
}
```

## 9. 性能提示

### 选择合适的整数类型
```rust
fn main() {
    // 对于一般用途，i32通常是最好的选择
    let count: i32 = 42;
    
    // 只有在需要特定大小时才使用其他类型
    let big_number: i64 = 1_000_000_000_000;
    let small_number: i8 = 127;
}
```

### 数组vs Vec的选择
```rust
fn main() {
    // 编译时已知大小，使用数组
    let fixed_list = [1, 2, 3, 4, 5];
    
    // 运行时可变大小，使用Vec（后续章节会详细讲解）
    // let dynamic_list = vec![1, 2, 3, 4, 5];
}
```

## 10. 本章小结

✅ **已掌握的概念**:
- Rust变量的不可变性默认特性
- 基本数据类型和复合数据类型
- 函数定义、参数传递和返回值
- 语句和表达式的区别
- 基本的打印和格式化操作

🎯 **下一步学习**:
- 学习控制流语句
- 理解if表达式和循环
- 掌握模式匹配基础

📝 **学习检查点**:
- [ ] 能够正确声明可变和不可变变量
- [ ] 理解各种基本数据类型的使用场景
- [ ] 能够定义和调用函数
- [ ] 掌握基本的格式化打印
- [ ] 理解语句和表达式的区别

💡 **重要提示**:
Rust的变量默认不可变这一特性是其安全性的基础。在编程时，尽量使用不可变变量，只有在必要时才使用`mut`关键字。这样可以避免很多潜在的错误，让代码更加安全可靠。

继续加油！接下来我们将学习Rust的控制流，让您的程序能够根据条件做出不同的决策。🚀 