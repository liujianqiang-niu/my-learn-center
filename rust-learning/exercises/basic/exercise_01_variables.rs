// 练习1：变量和数据类型
// 
// 说明：完成下面的练习，填写TODO部分
// 运行方式: rustc exercise_01_variables.rs && ./exercise_01_variables

fn main() {
    println!("🎯 练习1：变量和数据类型");
    println!("=========================");
    
    // 练习1.1：变量声明和可变性
    exercise_1_variables();
    
    // 练习1.2：数据类型操作
    exercise_2_data_types();
    
    // 练习1.3：函数编写
    exercise_3_functions();
    
    // 练习1.4：控制流基础
    exercise_4_control_flow();
    
    println!("\n🎉 练习完成！检查你的答案是否正确。");
}

fn exercise_1_variables() {
    println!("\n📝 练习1.1：变量声明");
    println!("--------------------");
    
    // TODO: 声明一个不可变变量x，值为10
    // let x = ?;
    
    // TODO: 声明一个可变变量y，初始值为5，然后将其修改为15
    // let mut y = ?;
    // y = ?;
    
    // TODO: 使用变量遮蔽，将x的类型从数字改为字符串
    // let x = ?;
    
    // 取消注释下面的代码来测试你的答案
    // println!("x: {}", x);
    // println!("y: {}", y);
    
    // 正确答案应该输出:
    // x: hello (或其他字符串)
    // y: 15
    
    println!("  ✍️ 请完成TODO部分，然后取消注释测试代码");
}

fn exercise_2_data_types() {
    println!("\n🔢 练习1.2：数据类型");
    println!("--------------------");
    
    // TODO: 创建以下类型的变量
    // 1. 一个i64类型的大整数
    // let big_int: ? = ?;
    
    // 2. 一个f32类型的浮点数
    // let float_num: ? = ?;
    
    // 3. 一个包含姓名和年龄的元组
    // let person: (?, ?) = (?, ?);
    
    // 4. 一个包含5个数字的数组
    // let numbers: [?; ?] = [?, ?, ?, ?, ?];
    
    // 5. 一个布尔值表示是否为Rust初学者
    // let is_beginner: ? = ?;
    
    // TODO: 解构元组，获取姓名和年龄
    // let (?, ?) = person;
    
    // TODO: 获取数组的第一个和最后一个元素
    // let first = ?;
    // let last = ?;
    
    // 取消注释下面的代码来测试
    /*
    println!("  大整数: {}", big_int);
    println!("  浮点数: {}", float_num);
    println!("  姓名: {}, 年龄: {}", name, age);
    println!("  第一个数字: {}, 最后一个数字: {}", first, last);
    println!("  是初学者: {}", is_beginner);
    */
    
    println!("  ✍️ 请完成TODO部分并测试");
}

fn exercise_3_functions() {
    println!("\n🔧 练习1.3：函数编写");
    println!("--------------------");
    
    // TODO: 实现以下函数
    
    // 函数1：计算两个数的平均值
    fn average(a: f64, b: f64) -> f64 {
        // TODO: 实现这个函数
        0.0 // 临时返回值，请替换
    }
    
    // 函数2：检查数字是否为偶数
    fn is_even(n: i32) -> bool {
        // TODO: 实现这个函数
        false // 临时返回值，请替换
    }
    
    // 函数3：返回较大的数字
    fn max_of_two(a: i32, b: i32) -> i32 {
        // TODO: 实现这个函数
        0 // 临时返回值，请替换
    }
    
    // 函数4：计算字符串长度（接受String参数）
    fn string_length(s: String) -> usize {
        // TODO: 实现这个函数
        0 // 临时返回值，请替换
    }
    
    // 测试你的函数实现
    println!("  测试函数实现:");
    
    // 取消注释下面的测试代码
    /*
    let avg = average(10.0, 20.0);
    println!("    10.0和20.0的平均值: {}", avg);
    
    let even = is_even(4);
    let odd = is_even(7);
    println!("    4是偶数: {}, 7是偶数: {}", even, odd);
    
    let larger = max_of_two(15, 25);
    println!("    15和25中较大的: {}", larger);
    
    let test_string = String::from("Hello, Rust!");
    let len = string_length(test_string);
    println!("    字符串长度: {}", len);
    // 注意：test_string在这里不能再使用了，为什么？
    */
    
    println!("  ✍️ 实现函数并取消注释测试代码");
}

fn exercise_4_control_flow() {
    println!("\n🔄 练习1.4：控制流基础");
    println!("----------------------");
    
    // TODO: 完成以下控制流练习
    
    // 练习4.1：分类数字
    let number = 42;
    
    // TODO: 使用if表达式，根据数字大小分类：
    // - 大于50: "大数字"
    // - 20-50: "中等数字"  
    // - 小于20: "小数字"
    // let category = ?;
    
    // 练习4.2：循环求和
    // TODO: 计算1到10的和
    // let mut sum = 0;
    // for i in ? {
    //     sum += i;
    // }
    
    // 练习4.3：match表达式
    let grade = 85;
    
    // TODO: 使用match表达式转换分数到等级
    // 90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
    // let letter_grade = match grade {
    //     ? => ?,
    //     ? => ?,
    //     ? => ?,
    //     ? => ?,
    //     _ => ?,
    // };
    
    // 练习4.4：遍历数组
    let fruits = ["苹果", "香蕉", "橙子", "葡萄"];
    
    // TODO: 遍历水果数组，打印编号和水果名称
    // 期望输出: "1. 苹果", "2. 香蕉" ...
    // for (?, ?) in ?.?().?() {
    //     println!("{}. {}", ?, ?);
    // }
    
    // 取消注释测试代码
    /*
    println!("  数字{}属于: {}", number, category);
    println!("  1到10的和: {}", sum);
    println!("  分数{}对应等级: {}", grade, letter_grade);
    */
    
    println!("  ✍️ 完成控制流练习");
}

// 挑战题：综合练习
fn bonus_challenge() {
    println!("\n🏆 挑战题：综合练习");
    println!("--------------------");
    
    // TODO: 编写一个函数，接收一个整数数组，返回：
    // - 数组的和
    // - 最大值
    // - 最小值
    // - 平均值
    
    fn analyze_array(arr: [i32; 5]) -> (i32, i32, i32, f64) {
        // TODO: 实现这个函数
        (0, 0, 0, 0.0) // 临时返回值
    }
    
    // TODO: 编写一个函数，判断字符串是否为回文
    fn is_palindrome(s: String) -> bool {
        // 提示：可以使用 s.chars().rev().collect::<String>() 来反转字符串
        // TODO: 实现这个函数
        false // 临时返回值
    }
    
    // 测试你的实现
    let test_array = [1, 5, 3, 9, 2];
    // let (sum, max, min, avg) = analyze_array(test_array);
    
    let test_word = String::from("level");
    // let is_palindrom = is_palindrome(test_word);
    
    println!("  🏁 挑战题已准备就绪，开始实现吧！");
}

// 答案提示（不要偷看！自己先尝试实现）
//
// 练习1.1 答案：
// let x = 10;
// let mut y = 5;
// y = 15;
// let x = "hello";
//
// 练习1.2 答案：
// let big_int: i64 = 1_000_000_000;
// let float_num: f32 = 3.14;
// let person: (&str, u32) = ("张三", 25);
// let numbers: [i32; 5] = [1, 2, 3, 4, 5];
// let is_beginner: bool = true;
// let (name, age) = person;
// let first = numbers[0];
// let last = numbers[4];
//
// 练习1.3 答案：
// fn average(a: f64, b: f64) -> f64 { (a + b) / 2.0 }
// fn is_even(n: i32) -> bool { n % 2 == 0 }
// fn max_of_two(a: i32, b: i32) -> i32 { if a > b { a } else { b } }
// fn string_length(s: String) -> usize { s.len() }
//
// 学习重点：
// 1. 理解变量的可变性和遮蔽
// 2. 熟悉各种数据类型的使用
// 3. 掌握函数的定义和调用
// 4. 注意所有权在函数调用中的转移 