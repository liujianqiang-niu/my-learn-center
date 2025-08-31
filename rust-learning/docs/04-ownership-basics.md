# 第4章：所有权系统基础 🔒

## 学习目标
- 理解Rust所有权系统的核心概念
- 掌握移动(Move)语义
- 理解栈和堆的内存分配
- 学会克隆(Clone)数据
- 理解函数中的所有权转移

## 1. 什么是所有权？

所有权(Ownership)是Rust最独特的特性，它使Rust无需垃圾回收器就能保证内存安全。

### 所有权规则
1. Rust中的每一个值都有一个被称为其**所有者**(owner)的变量
2. 值在任意时刻有且只有一个所有者
3. 当所有者离开作用域时，这个值将被丢弃

### 作用域
```rust
fn main() {
    {                      // s 在这里无效, 它尚未声明
        let s = "hello";   // 从此处起，s 是有效的
        
        // 使用 s
        println!("{}", s);
    }                      // 此作用域已结束，s 不再有效
}
```

## 2. String类型介绍

为了演示所有权规则，我们需要一个比基本数据类型更复杂的数据类型。String类型分配在堆上，是一个很好的例子。

```rust
fn main() {
    // 字符串字面值：不可变，分配在栈上
    let s1 = "hello";
    
    // String类型：可变，分配在堆上
    let mut s2 = String::from("hello");
    s2.push_str(", world!"); // 可以修改String
    
    println!("s1: {}", s1);
    println!("s2: {}", s2);
}
```

## 3. 内存分配：栈与堆

### 栈(Stack)
- 后进先出的数据结构
- 存储已知固定大小的数据
- 分配和释放速度很快
- 例如：整数、布尔值、字符等基本类型

### 堆(Heap)
- 用于存储大小在编译时未知的数据
- 分配时需要请求特定大小的空间
- 通过指针访问数据
- 例如：String、Vec等

```rust
fn main() {
    // 栈上分配
    let x = 5;          // 存储在栈上
    let y = x;          // 复制值到y，x和y都有效
    
    println!("x: {}, y: {}", x, y); // 都可以使用
    
    // 堆上分配
    let s1 = String::from("hello");  // s1指向堆上的数据
    let s2 = s1;                     // 移动s1到s2，s1不再有效
    
    // println!("{}", s1);           // 错误！s1已经无效
    println!("{}", s2);              // 只能使用s2
}
```

## 4. 移动(Move)语义

### 变量与数据交互的方式：移动
```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1; // s1被移动到s2
    
    // 此时s1不再有效，只有s2有效
    println!("{}", s2);
    // println!("{}", s1); // 编译错误！
}
```

### 为什么要有移动语义？
如果Rust允许两个变量同时拥有同一块堆内存，当它们离开作用域时，都会尝试释放相同的内存，这会导致**二次释放**(double free)错误。

```
堆内存        栈内存
┌─────────────┐
│ hello       │  ← s1 ┌──────────┐
└─────────────┘       │ ptr      │
                      │ len: 5   │
                      │ cap: 5   │
                      └──────────┘
                        s2 ┌──────────┐
                           │ ptr  ────┤ (指向同一个位置)
                           │ len: 5   │
                           │ cap: 5   │
                           └──────────┘
```

移动后，s1变为无效：
```
堆内存        栈内存
┌─────────────┐
│ hello       │  ← s2 ┌──────────┐
└─────────────┘       │ ptr      │
                      │ len: 5   │
                      │ cap: 5   │
              s1      └──────────┘
           (invalid)  ┌──────────┐
                      │ ✗ ✗ ✗ ✗ │
                      │ ✗ ✗ ✗ ✗ │
                      │ ✗ ✗ ✗ ✗ │
                      └──────────┘
```

## 5. 克隆(Clone)数据

如果确实需要深度复制String的堆上数据，可以使用clone方法：

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1.clone(); // 深度复制
    
    // 现在s1和s2都有效
    println!("s1 = {}, s2 = {}", s1, s2);
}
```

### Clone vs Copy
```rust
fn main() {
    // 实现了Copy trait的类型（如整数）
    let x = 5;
    let y = x; // 实际上是复制，不是移动
    println!("x: {}, y: {}", x, y); // 都有效
    
    // 没有实现Copy trait的类型（如String）
    let s1 = String::from("hello");
    let s2 = s1; // 移动，不是复制
    // println!("{}", s1); // 错误！
    println!("{}", s2);
}
```

## 6. 函数与所有权

### 传递值给函数
```rust
fn main() {
    let s = String::from("hello");  // s进入作用域
    
    takes_ownership(s);             // s的值移动到函数里...
                                    // ... 所以到这里不再有效
    
    let x = 5;                      // x进入作用域
    
    makes_copy(x);                  // x应该移动函数里，
                                    // 但i32是Copy的，
                                    // 所以在后面可继续使用x
    
    println!("x is still valid: {}", x);
    // println!("{}", s);           // 错误！s已经无效
} // 这里, x先移出了作用域，然后是s。但因为s的值已经被移动了，
  // 所以不会有特殊操作

fn takes_ownership(some_string: String) { // some_string进入作用域
    println!("{}", some_string);
} // 这里，some_string移出作用域并调用drop方法。占用的内存被释放

fn makes_copy(some_integer: i32) { // some_integer进入作用域
    println!("{}", some_integer);
} // 这里，some_integer移出作用域。不会有特殊操作
```

### 返回值与作用域
```rust
fn main() {
    let s1 = gives_ownership();         // gives_ownership将返回值
                                        // 移给s1
    
    let s2 = String::from("hello");     // s2进入作用域
    
    let s3 = takes_and_gives_back(s2);  // s2被移动到
                                        // takes_and_gives_back中,
                                        // 它也将返回值移给s3
    
    println!("s1: {}, s3: {}", s1, s3);
    // println!("{}", s2);              // 错误！s2已经无效
} // 这里, s3移出作用域并被丢弃。s2也移出作用域，但已被移动，
  // 所以什么也不会发生。s1移出作用域并被丢弃

fn gives_ownership() -> String {             // gives_ownership将返回值移动给
                                             // 调用它的函数
    let some_string = String::from("hello"); // some_string进入作用域.
    
    some_string                              // 返回some_string并移出给调用的函数
}

// takes_and_gives_back将传入字符串并返回该值
fn takes_and_gives_back(a_string: String) -> String { // a_string进入作用域
    a_string  // 返回a_string并移出给调用的函数
}
```

## 7. 实际应用示例

### 计算字符串长度
```rust
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(s1);
    
    // println!("{}", s1); // 错误！s1已经被移动
    println!("长度是: {}", len);
}

fn calculate_length(s: String) -> usize {
    s.len()
} // 这里，s移出作用域并被丢弃
```

### 同时返回值和所有权
```rust
fn main() {
    let s1 = String::from("hello");
    let (s2, len) = calculate_length(s1);
    
    println!("'{}'的长度是 {}", s2, len);
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len()返回字符串的长度
    
    (s, length)
}
```

## 8. 实践练习

### 练习1：理解移动语义
```rust
fn main() {
    let s1 = String::from("Rust");
    let s2 = s1;
    
    // TODO: 下面哪些代码会编译错误？为什么？
    // println!("s1: {}", s1);    // 这行会出错吗？
    println!("s2: {}", s2);       // 这行会出错吗？
    
    let x = 42;
    let y = x;
    println!("x: {}, y: {}", x, y); // 这行会出错吗？为什么？
}
```

### 练习2：函数和所有权
```rust
fn main() {
    let s = String::from("programming");
    
    // TODO: 修改下面的代码，使其能够同时打印s和长度
    let length = string_length(s);
    // println!("'{}'的长度是{}", s, length); // 如何让这行代码工作？
    println!("长度是{}", length);
}

fn string_length(s: String) -> usize {
    s.len()
}

// TODO: 写一个函数，接受String参数并返回第一个字符
// 提示：需要同时返回原字符串和字符
fn first_char(s: String) -> (String, Option<char>) {
    let first = s.chars().next();
    (s, first)
}
```

### 练习3：克隆的使用
```rust
fn main() {
    let original = String::from("Hello, World!");
    
    // TODO: 创建original的克隆
    let cloned = original.clone();
    
    // TODO: 验证两个字符串都可以使用
    println!("Original: {}", original);
    println!("Cloned: {}", cloned);
    
    // TODO: 修改cloned（提示：需要让它可变）
    // cloned.push_str(" - Modified");
    // println!("Modified: {}", cloned);
    // println!("Original: {}", original);
}
```

## 9. 常见错误和解决方案

### 错误1：使用已移动的值
```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1; // s1移动到s2
    
    // println!("{}", s1); // 错误：borrow of moved value
}

// 解决方案1：使用克隆
fn solution1() {
    let s1 = String::from("hello");
    let s2 = s1.clone(); // 克隆而不是移动
    
    println!("s1: {}, s2: {}", s1, s2); // 都可以使用
}

// 解决方案2：重新设计逻辑（稍后学习引用）
```

### 错误2：函数调用后无法使用原变量
```rust
fn print_string(s: String) {
    println!("{}", s);
}

fn main() {
    let my_string = String::from("hello");
    print_string(my_string); // my_string被移动
    
    // println!("{}", my_string); // 错误：已被移动
}

// 解决方案：返回所有权
fn print_and_return(s: String) -> String {
    println!("{}", s);
    s
}
```

## 10. 性能考虑

### 避免不必要的克隆
```rust
fn main() {
    let s = String::from("hello world");
    
    // 低效：不必要的克隆
    let len1 = calculate_length_inefficient(s.clone());
    let len2 = calculate_length_inefficient(s.clone());
    
    println!("原字符串: {}", s);
    println!("长度: {}, {}", len1, len2);
}

fn calculate_length_inefficient(s: String) -> usize {
    s.len()
}

// 更好的方式将在下一章介绍（使用引用）
```

### 理解Copy类型的性能
```rust
fn main() {
    let numbers = [1, 2, 3, 4, 5];
    
    // Copy类型的"移动"实际上是复制，开销小
    let sum1 = sum_array(numbers);
    let sum2 = sum_array(numbers); // numbers仍然有效
    
    println!("两次求和结果: {}, {}", sum1, sum2);
}

fn sum_array(arr: [i32; 5]) -> i32 {
    arr.iter().sum()
}
```

## 11. 本章小结

✅ **已掌握的核心概念**:
- 所有权的三条基本规则
- 栈和堆内存的区别及使用场景
- 移动语义和为什么需要它
- Clone trait的作用和使用时机
- 函数调用中的所有权转移规则

🎯 **下一步学习**:
- 学习引用和借用
- 理解如何在不获取所有权的情况下使用值
- 掌握可变引用和不可变引用

📝 **学习检查点**:
- [ ] 理解什么情况下会发生移动
- [ ] 知道何时使用clone()方法
- [ ] 能够预测函数调用后变量的有效性
- [ ] 理解Copy trait和Clone trait的区别
- [ ] 掌握所有权在函数参数和返回值中的转移

💡 **重要理解**:
所有权系统是Rust内存安全的基石。虽然一开始可能感觉限制很多，但这些限制在编译时就能发现内存相关的错误，避免了运行时的崩溃。理解所有权需要时间，但一旦掌握，你就能写出既安全又高效的代码！

接下来我们将学习引用和借用，这将大大提高所有权系统的实用性！🚀 