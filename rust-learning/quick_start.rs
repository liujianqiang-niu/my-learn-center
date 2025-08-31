// Rust学习快速开始示例
// 运行方式：rustc quick_start.rs && ./quick_start
// 或者：在Cargo项目中运行：cargo run --bin quick_start

fn main() {
    println!("🦀 欢迎来到Rust学习世界！");
    println!("==========================================");
    
    // 1. 基础语法演示
    basic_syntax_demo();
    
    // 2. 控制流演示
    control_flow_demo();
    
    // 3. 所有权系统演示
    ownership_demo();
    
    // 4. 实用功能演示
    practical_demo();
    
    println!("\n🎉 快速开始演示完成！");
    println!("现在你已经看到了Rust的基本特性。");
    println!("建议接下来按顺序学习docs/目录下的文档：");
    println!("1. 01-environment-setup.md");
    println!("2. 02-basic-syntax.md");
    println!("3. 03-control-flow.md");
    println!("4. 04-ownership-basics.md");
    println!("...");
    println!("\n开始你的Rust专家之路吧！🚀");
}

fn basic_syntax_demo() {
    println!("\n📝 1. 基础语法演示");
    println!("-------------------");
    
    // 变量和可变性
    let name = "Rust学习者";
    let mut count = 0;
    count += 1;
    
    println!("👋 你好，{}！这是你的第{}次Rust体验", name, count);
    
    // 数据类型
    let integer: i32 = 42;
    let float: f64 = 3.14159;
    let boolean: bool = true;
    let character: char = '🦀';
    
    println!("🔢 整数: {}, 浮点数: {:.2}, 布尔值: {}, 字符: {}", 
             integer, float, boolean, character);
    
    // 元组和数组
    let tuple: (i32, f64, &str) = (42, 3.14, "Rust");
    let array: [i32; 3] = [1, 2, 3];
    
    println!("📦 元组: {:?}, 数组: {:?}", tuple, array);
    
    // 函数调用
    let result = add_numbers(5, 7);
    println!("➕ 5 + 7 = {}", result);
}

fn control_flow_demo() {
    println!("\n🔄 2. 控制流演示");
    println!("------------------");
    
    // if表达式
    let number = 42;
    let description = if number > 50 {
        "大数字"
    } else if number > 20 {
        "中等数字"
    } else {
        "小数字"
    };
    
    println!("🔍 数字{}是一个{}", number, description);
    
    // 循环
    println!("🔁 for循环演示:");
    for i in 1..=5 {
        print!("{} ", i);
    }
    println!();
    
    // match表达式
    let grade = 85;
    let level = match grade {
        90..=100 => "优秀",
        80..=89 => "良好", 
        70..=79 => "中等",
        60..=69 => "及格",
        _ => "不及格",
    };
    
    println!("📊 分数{}对应等级: {}", grade, level);
    
    // 集合遍历
    let fruits = vec!["苹果", "香蕉", "橙子"];
    println!("🍎 水果列表:");
    for (index, fruit) in fruits.iter().enumerate() {
        println!("  {}. {}", index + 1, fruit);
    }
}

fn ownership_demo() {
    println!("\n🔒 3. 所有权系统演示");
    println!("----------------------");
    
    // 基本类型的复制
    let x = 5;
    let y = x; // 复制，不是移动
    println!("📋 复制行为 - x: {}, y: {}", x, y);
    
    // String类型的移动
    let s1 = String::from("Hello");
    let s2 = s1; // 移动，s1不再有效
    println!("📦 移动行为 - s2: {}", s2);
    // println!("{}", s1); // 这行会编译错误
    
    // 克隆
    let s3 = String::from("World");
    let s4 = s3.clone(); // 深度复制
    println!("📑 克隆行为 - s3: {}, s4: {}", s3, s4);
    
    // 函数中的所有权
    let message = String::from("Rust很棒！");
    let length = calculate_length_take_ownership(message);
    println!("📏 字符串长度: {}", length);
    // println!("{}", message); // message已经被移动，不能再使用
    
    // 演示如何返回所有权
    let (returned_string, len) = calculate_length_and_return(String::from("所有权演示"));
    println!("🔄 返回的字符串: '{}', 长度: {}", returned_string, len);
}

fn practical_demo() {
    println!("\n🛠️ 4. 实用功能演示");
    println!("-------------------");
    
    // 错误处理预览
    let numbers = vec![1, 2, 3, 4, 5];
    match get_element(&numbers, 2) {
        Some(value) => println!("🎯 索引2的值是: {}", value),
        None => println!("❌ 索引超出范围"),
    }
    
    match get_element(&numbers, 10) {
        Some(value) => println!("🎯 索引10的值是: {}", value),
        None => println!("❌ 索引10超出范围"),
    }
    
    // 字符串操作
    let mut greeting = String::from("Hello");
    greeting.push_str(", Rust!");
    println!("📝 字符串操作结果: {}", greeting);
    
    // 集合操作
    let mut numbers = vec![1, 2, 3];
    numbers.push(4);
    numbers.push(5);
    println!("📊 动态数组: {:?}", numbers);
    
    let sum: i32 = numbers.iter().sum();
    println!("➕ 数组元素之和: {}", sum);
    
    // 高阶函数预览
    let doubled: Vec<i32> = numbers.iter().map(|x| x * 2).collect();
    println!("✖️ 每个元素乘以2: {:?}", doubled);
    
    let even_numbers: Vec<&i32> = numbers.iter().filter(|&&x| x % 2 == 0).collect();
    println!("🔢 偶数: {:?}", even_numbers);
}

// 辅助函数

fn add_numbers(a: i32, b: i32) -> i32 {
    a + b // Rust中最后一个表达式自动返回，不需要return关键字
}

fn calculate_length_take_ownership(s: String) -> usize {
    s.len()
    // s在这里离开作用域，内存被释放
}

fn calculate_length_and_return(s: String) -> (String, usize) {
    let length = s.len();
    (s, length) // 返回字符串的所有权和长度
}

fn get_element(vec: &Vec<i32>, index: usize) -> Option<&i32> {
    vec.get(index)
}

// 这个文件展示了Rust的核心概念，包括：
// - 变量和数据类型
// - 控制流（if、循环、match）
// - 所有权系统（移动、复制、克隆）
// - 基础的错误处理（Option类型）
// - 集合操作和函数式编程预览
//
// 运行这个文件后，建议：
// 1. 阅读docs/目录下的详细文档
// 2. 查看examples/目录下的示例代码
// 3. 完成exercises/目录下的练习题
// 4. 尝试projects/目录下的实战项目 