// 基础语法示例：变量和数据类型演示
// 运行方式: rustc variables_demo.rs && ./variables_demo

fn main() {
    println!("🔢 Rust变量和数据类型演示");
    println!("=============================");
    
    // 1. 变量声明和可变性
    variables_and_mutability();
    
    // 2. 数据类型演示
    data_types_demo();
    
    // 3. 常量演示
    constants_demo();
    
    // 4. 遮蔽演示
    shadowing_demo();
    
    // 5. 类型推断和注解
    type_inference_demo();
}

fn variables_and_mutability() {
    println!("\n📝 1. 变量和可变性");
    println!("-------------------");
    
    // 不可变变量（默认）
    let x = 5;
    println!("不可变变量 x: {}", x);
    
    // x = 6; // 这会编译错误！
    
    // 可变变量
    let mut y = 5;
    println!("可变变量 y 初始值: {}", y);
    y = 6;
    println!("可变变量 y 修改后: {}", y);
    
    // 可以改变可变变量的类型吗？不可以！
    // y = "hello"; // 编译错误：类型不匹配
}

fn data_types_demo() {
    println!("\n🔢 2. 数据类型演示");
    println!("------------------");
    
    // 整数类型
    println!("整数类型:");
    let small: i8 = 127;
    let medium: i32 = 2_147_483_647;
    let large: i64 = 9_223_372_036_854_775_807;
    let unsigned: u32 = 4_294_967_295;
    
    println!("  i8最大值: {}", small);
    println!("  i32最大值: {}", medium);
    println!("  i64最大值: {}", large);
    println!("  u32最大值: {}", unsigned);
    
    // 浮点类型
    println!("\n浮点类型:");
    let x = 2.0;        // f64
    let y: f32 = 3.0;   // f32
    println!("  f64: {}, f32: {}", x, y);
    
    // 布尔类型
    println!("\n布尔类型:");
    let t = true;
    let f: bool = false;
    println!("  真: {}, 假: {}", t, f);
    
    // 字符类型 (4字节，支持Unicode)
    println!("\n字符类型:");
    let c = 'z';
    let z = 'ℤ';
    let cat = '😻';
    println!("  英文: {}, 数学符号: {}, 表情: {}", c, z, cat);
    
    // 复合类型：元组
    println!("\n元组类型:");
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = tup; // 解构
    println!("  元组: {:?}", tup);
    println!("  解构后: x={}, y={}, z={}", x, y, z);
    println!("  通过索引访问: tup.0={}, tup.1={}", tup.0, tup.1);
    
    // 复合类型：数组
    println!("\n数组类型:");
    let a = [1, 2, 3, 4, 5];
    let months = ["一月", "二月", "三月"];
    let same_value = [3; 5]; // [3, 3, 3, 3, 3]
    
    println!("  数组a: {:?}", a);
    println!("  月份: {:?}", months);
    println!("  相同值数组: {:?}", same_value);
    println!("  数组长度: {}", a.len());
    println!("  第一个元素: {}", a[0]);
}

fn constants_demo() {
    println!("\n📌 3. 常量演示");
    println!("---------------");
    
    const MAX_POINTS: u32 = 100_000;
    const PI: f64 = 3.14159265359;
    const PROGRAM_NAME: &str = "Rust学习演示";
    
    println!("  最大分数: {}", MAX_POINTS);
    println!("  圆周率: {}", PI);
    println!("  程序名称: {}", PROGRAM_NAME);
    
    // 常量在整个程序运行期间都有效
    // 必须指定类型，必须是编译时常量表达式
}

fn shadowing_demo() {
    println!("\n👥 4. 变量遮蔽演示");
    println!("-------------------");
    
    let x = 5;
    println!("  第一个x: {}", x);
    
    let x = x + 1; // 遮蔽前一个x
    println!("  第二个x: {}", x);
    
    {
        let x = x * 2; // 在内部作用域遮蔽
        println!("  内部作用域的x: {}", x);
    }
    
    println!("  外部作用域的x: {}", x);
    
    // 遮蔽允许改变类型
    let spaces = "   ";
    println!("  spaces字符串: '{}'", spaces);
    let spaces = spaces.len();
    println!("  spaces数字: {}", spaces);
}

fn type_inference_demo() {
    println!("\n🤖 5. 类型推断和注解");
    println!("---------------------");
    
    // Rust可以推断大多数类型
    let inferred_int = 42;              // 推断为i32
    let inferred_float = 3.14;          // 推断为f64
    let inferred_string = "hello";      // 推断为&str
    let inferred_bool = true;           // 推断为bool
    
    println!("  推断的整数: {} (类型: i32)", inferred_int);
    println!("  推断的浮点数: {} (类型: f64)", inferred_float);
    println!("  推断的字符串: {} (类型: &str)", inferred_string);
    println!("  推断的布尔值: {} (类型: bool)", inferred_bool);
    
    // 有时需要显式指定类型
    let explicit_int: i64 = 42;
    let explicit_float: f32 = 3.14;
    let parsed_number: u32 = "42".parse().expect("解析失败");
    
    println!("  显式i64: {}", explicit_int);
    println!("  显式f32: {}", explicit_float);
    println!("  解析的数字: {}", parsed_number);
    
    // 数组类型注解
    let array: [i32; 5] = [1, 2, 3, 4, 5];
    let vector: Vec<i32> = vec![1, 2, 3, 4, 5];
    
    println!("  固定数组: {:?}", array);
    println!("  动态向量: {:?}", vector);
}

// 演示数值运算
fn arithmetic_operations() {
    println!("\n🧮 数值运算演示");
    println!("----------------");
    
    let a = 10;
    let b = 3;
    
    println!("  {} + {} = {}", a, b, a + b);
    println!("  {} - {} = {}", a, b, a - b);
    println!("  {} * {} = {}", a, b, a * b);
    println!("  {} / {} = {}", a, b, a / b);
    println!("  {} % {} = {}", a, b, a % b);
    
    // 浮点运算
    let x = 10.5;
    let y = 3.2;
    
    println!("  {:.1} + {:.1} = {:.1}", x, y, x + y);
    println!("  {:.1} / {:.1} = {:.2}", x, y, x / y);
}

// 字符串类型比较
fn string_types_demo() {
    println!("\n📝 字符串类型演示");
    println!("------------------");
    
    // 字符串字面值 (&str)
    let string_literal = "这是字符串字面值";
    println!("  字符串字面值: {}", string_literal);
    
    // String类型
    let mut string_object = String::from("这是String对象");
    println!("  String对象: {}", string_object);
    
    // String可以修改
    string_object.push_str(" - 已修改");
    println!("  修改后的String: {}", string_object);
    
    // 字符串方法
    println!("  字符串长度: {}", string_object.len());
    println!("  是否包含'Rust': {}", string_object.contains("String"));
    println!("  转为大写: {}", string_object.to_uppercase());
}

// 这个文件演示了：
// 1. 变量声明和可变性
// 2. 所有基本数据类型的使用
// 3. 复合数据类型（元组、数组）
// 4. 常量声明
// 5. 变量遮蔽
// 6. 类型推断和显式类型注解
// 7. 基本的数值和字符串操作
//
// 学习建议：
// - 运行这个程序，观察输出
// - 尝试修改变量值，理解可变性
// - 实验不同的数据类型
// - 尝试触发编译错误，理解限制的原因 