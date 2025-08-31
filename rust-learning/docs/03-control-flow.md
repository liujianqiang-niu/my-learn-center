# 第3章：控制流 🔄

## 学习目标
- 掌握if表达式的使用
- 理解Rust中的循环结构
- 学会使用match表达式进行模式匹配
- 掌握控制流的嵌套和组合
- 理解break和continue的使用

## 1. if表达式

### 基本if表达式
在Rust中，if是表达式而不是语句，这意味着它可以返回值。

```rust
fn main() {
    let number = 3;
    
    if number < 5 {
        println!("条件为真");
    } else {
        println!("条件为假");
    }
    
    // if表达式可以返回值
    let condition = true;
    let number = if condition { 5 } else { 6 };
    println!("number的值是: {}", number);
}
```

### 多重条件
```rust
fn main() {
    let number = 6;
    
    if number % 4 == 0 {
        println!("数字能被4整除");
    } else if number % 3 == 0 {
        println!("数字能被3整除");
    } else if number % 2 == 0 {
        println!("数字能被2整除");
    } else {
        println!("数字不能被4、3、2整除");
    }
}
```

### if表达式的值必须是同一类型
```rust
fn main() {
    let condition = true;
    
    // 正确：两个分支返回相同类型
    let number = if condition { 5 } else { 6 };
    
    // 错误：类型不匹配
    // let number = if condition { 5 } else { "six" };
    
    println!("number: {}", number);
}
```

## 2. 循环

### loop循环
`loop`关键字创建一个无限循环，直到显式地使用`break`退出。

```rust
fn main() {
    let mut counter = 0;
    
    loop {
        counter += 1;
        
        if counter == 10 {
            break;
        }
        
        println!("计数: {}", counter);
    }
    
    println!("循环结束!");
}
```

### 从循环返回值
```rust
fn main() {
    let mut counter = 0;
    
    let result = loop {
        counter += 1;
        
        if counter == 10 {
            break counter * 2; // 返回值
        }
    };
    
    println!("结果是: {}", result); // 输出: 20
}
```

### 循环标签
在嵌套循环中，可以使用标签来指定break或continue作用于哪个循环。

```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {}", count);
        let mut remaining = 10;
        
        loop {
            println!("remaining = {}", remaining);
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up; // 跳出外层循环
            }
            remaining -= 1;
        }
        
        count += 1;
    }
    println!("结束 count = {}", count);
}
```

### while循环
```rust
fn main() {
    let mut number = 3;
    
    while number != 0 {
        println!("{}!", number);
        number -= 1;
    }
    
    println!("升空！！！");
}
```

### for循环
```rust
fn main() {
    // 遍历数组
    let a = [10, 20, 30, 40, 50];
    
    for element in a {
        println!("值是: {}", element);
    }
    
    // 使用范围
    for number in 1..4 {
        println!("{}!", number);
    }
    
    // 包含结束值的范围
    for number in 1..=3 {
        println!("{}!", number);
    }
    
    // 倒序
    for number in (1..4).rev() {
        println!("{}!", number);
    }
    
    println!("升空！！！");
}
```

### 遍历集合的不同方式
```rust
fn main() {
    let names = vec!["张三", "李四", "王五"];
    
    // 方式1：获取所有权
    for name in names {
        println!("姓名: {}", name);
    }
    // println!("{:?}", names); // 错误：names已经被移动
    
    let names = vec!["张三", "李四", "王五"];
    
    // 方式2：借用引用
    for name in &names {
        println!("姓名: {}", name);
    }
    println!("原数组: {:?}", names); // 可以继续使用names
    
    // 方式3：可变借用（如果需要修改）
    let mut names = vec!["张三", "李四", "王五"];
    for name in &mut names {
        name.push_str("先生");
    }
    println!("修改后: {:?}", names);
}
```

## 3. match表达式

### 基本match语法
`match`是Rust中强大的控制流运算符，允许将一个值与一系列模式相比较。

```rust
fn main() {
    let number = 13;
    
    match number {
        1 => println!("一"),
        2 => println!("二"),
        3 => println!("三"),
        4 => println!("四"),
        5 => println!("五"),
        _ => println!("其他数字"),
    }
}
```

### match表达式返回值
```rust
fn main() {
    let number = 1;
    
    let chinese = match number {
        1 => "一",
        2 => "二",
        3 => "三",
        4 => "四",
        5 => "五",
        _ => "未知",
    };
    
    println!("数字{}对应的中文是: {}", number, chinese);
}
```

### 匹配多个值
```rust
fn main() {
    let number = 2;
    
    match number {
        1 | 2 => println!("一或二"),
        3..=5 => println!("三到五之间"),
        6 => println!("六"),
        _ => println!("其他"),
    }
}
```

### 绑定值
```rust
fn main() {
    let number = 5;
    
    match number {
        n @ 1..=5 => println!("数字{}在1到5之间", n),
        n @ 6..=10 => println!("数字{}在6到10之间", n),
        _ => println!("数字不在1到10之间"),
    }
}
```

## 4. if let语法糖
当只关心一个模式匹配时，可以使用`if let`简化代码。

```rust
fn main() {
    let some_value = Some(3);
    
    // 使用match
    match some_value {
        Some(3) => println!("三"),
        _ => (),
    }
    
    // 使用if let（更简洁）
    if let Some(3) = some_value {
        println!("三");
    }
    
    // if let with else
    if let Some(value) = some_value {
        println!("值是: {}", value);
    } else {
        println!("没有值");
    }
}
```

## 5. while let循环
当你想要在某个模式匹配时继续循环，可以使用`while let`。

```rust
fn main() {
    let mut stack = Vec::new();
    
    stack.push(1);
    stack.push(2);
    stack.push(3);
    
    // 当pop()返回Some时继续循环
    while let Some(top) = stack.pop() {
        println!("弹出: {}", top);
    }
}
```

## 6. 实际应用示例

### 简单计算器
```rust
fn main() {
    let operator = '+';
    let x = 5;
    let y = 3;
    
    let result = match operator {
        '+' => x + y,
        '-' => x - y,
        '*' => x * y,
        '/' => {
            if y != 0 {
                x / y
            } else {
                println!("错误：除零!");
                return;
            }
        }
        _ => {
            println!("不支持的操作符: {}", operator);
            return;
        }
    };
    
    println!("{} {} {} = {}", x, operator, y, result);
}
```

### 猜数字游戏
```rust
use std::io;
use std::cmp::Ordering;

fn main() {
    let secret_number = 42; // 简化版本，实际应该是随机数
    
    loop {
        println!("请输入你的猜测:");
        
        let mut guess = String::new();
        io::stdin()
            .read_line(&mut guess)
            .expect("读取输入失败");
        
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("请输入一个有效数字!");
                continue;
            }
        };
        
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("太小了!"),
            Ordering::Greater => println!("太大了!"),
            Ordering::Equal => {
                println!("你赢了!");
                break;
            }
        }
    }
}
```

## 7. 实践练习

### 练习1：条件判断
```rust
fn main() {
    // TODO: 写一个函数判断年份是否为闰年
    // 闰年规则：能被4整除但不能被100整除，或者能被400整除
    
    fn is_leap_year(year: u32) -> bool {
        // 实现这里
        (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)
    }
    
    let years = [2000, 2004, 1900, 2024];
    for year in &years {
        if is_leap_year(*year) {
            println!("{}是闰年", year);
        } else {
            println!("{}不是闰年", year);
        }
    }
}
```

### 练习2：循环应用
```rust
fn main() {
    // TODO: 计算1到100的和
    let mut sum = 0;
    // 实现这里
    
    // TODO: 找出1到20之间的所有素数
    fn is_prime(n: u32) -> bool {
        // 实现这里
        if n < 2 {
            return false;
        }
        for i in 2..n {
            if n % i == 0 {
                return false;
            }
        }
        true
    }
    
    println!("1到20的素数:");
    for i in 1..=20 {
        if is_prime(i) {
            print!("{} ", i);
        }
    }
    println!();
}
```

### 练习3：模式匹配
```rust
fn main() {
    // TODO: 根据分数给出等级
    fn get_grade(score: u32) -> &'static str {
        match score {
            90..=100 => "A",
            80..=89 => "B", 
            70..=79 => "C",
            60..=69 => "D",
            _ => "F"
        }
    }
    
    let scores = [95, 87, 73, 56, 68];
    for score in &scores {
        println!("分数: {}, 等级: {}", score, get_grade(*score));
    }
}
```

## 8. 常见错误和解决方案

### 错误1：if条件必须是bool类型
```rust
fn main() {
    let number = 3;
    
    // 错误：条件必须是bool类型
    // if number {
    //     println!("数字非零");
    // }
    
    // 正确：显式比较
    if number != 0 {
        println!("数字非零");
    }
}
```

### 错误2：match必须覆盖所有可能的值
```rust
fn main() {
    let number = 1;
    
    // 错误：没有覆盖所有可能的值
    // let result = match number {
    //     1 => "one",
    //     2 => "two",
    // };
    
    // 正确：添加默认情况
    let result = match number {
        1 => "one",
        2 => "two",
        _ => "other",
    };
    
    println!("{}", result);
}
```

### 错误3：if表达式各分支类型必须相同
```rust
fn main() {
    let condition = true;
    
    // 错误：类型不匹配
    // let result = if condition { 5 } else { "hello" };
    
    // 正确：确保类型一致
    let result = if condition { 5 } else { 0 };
    println!("{}", result);
}
```

## 9. 性能考虑

### 选择合适的循环类型
```rust
fn main() {
    let data = vec![1, 2, 3, 4, 5];
    
    // for循环（推荐）- 更安全，性能好
    for item in &data {
        println!("{}", item);
    }
    
    // while循环 - 需要手动管理索引
    let mut index = 0;
    while index < data.len() {
        println!("{}", data[index]);
        index += 1;
    }
}
```

### match vs if链
```rust
fn main() {
    let value = 5;
    
    // match更高效（编译器可以优化为跳转表）
    let result = match value {
        1 => "one",
        2 => "two",
        3 => "three",
        4 => "four",
        5 => "five",
        _ => "other",
    };
    
    // if链在复杂情况下可能效率较低
    let result2 = if value == 1 {
        "one"
    } else if value == 2 {
        "two"
    } else if value == 3 {
        "three"
    } else {
        "other"
    };
    
    println!("{}, {}", result, result2);
}
```

## 10. 本章小结

✅ **已掌握的概念**:
- if表达式的基本使用和返回值特性
- 各种循环结构：loop、while、for
- match表达式和模式匹配
- if let和while let语法糖
- 控制流的嵌套和组合使用

🎯 **下一步学习**:
- 学习Rust的所有权系统
- 理解借用和引用的概念
- 掌握内存安全的核心机制

📝 **学习检查点**:
- [ ] 能够正确使用if表达式进行条件判断
- [ ] 掌握各种循环结构的使用场景
- [ ] 理解match表达式的模式匹配机制
- [ ] 能够选择合适的控制流结构
- [ ] 理解表达式和语句在控制流中的区别

💡 **重要提示**:
Rust的控制流特性强调安全性和表达力。match表达式必须穷尽所有可能性，这虽然有时候显得繁琐，但能在编译时发现很多潜在错误。if let和while let提供了在特定场景下简化代码的语法糖。

接下来我们将学习Rust最核心的概念——所有权系统，这是Rust内存安全的基础！🚀 