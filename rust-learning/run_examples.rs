// Rust示例代码运行器
// 运行方式: rustc run_examples.rs && ./run_examples

use std::process::Command;
use std::path::Path;

fn main() {
    println!("🦀 Rust示例代码运行器");
    println!("========================");
    println!("这个工具帮助你快速编译和运行所有示例代码");
    
    let examples = vec![
        ("基础语法演示", "examples/basic_syntax/variables_demo.rs"),
        ("所有权系统演示", "examples/ownership/ownership_demo.rs"),
        ("快速开始演示", "quick_start.rs"),
    ];
    
    println!("\n📋 可用的示例：");
    for (index, (name, _)) in examples.iter().enumerate() {
        println!("  {}. {}", index + 1, name);
    }
    
    println!("\n🚀 开始运行示例...");
    
    for (name, path) in examples {
        run_example(name, path);
        println!(); // 空行分隔
    }
    
    println!("🎉 所有示例运行完成！");
    println!("\n💡 学习建议：");
    println!("1. 仔细阅读每个示例的输出");
    println!("2. 查看源代码，理解实现原理"); 
    println!("3. 尝试修改代码，观察效果");
    println!("4. 完成相应的练习题");
}

fn run_example(name: &str, path: &str) {
    println!("▶️ 运行示例：{}", name);
    println!("   文件：{}", path);
    println!("   " + "─".repeat(50).as_str());
    
    // 检查文件是否存在
    if !Path::new(path).exists() {
        println!("   ❌ 文件不存在: {}", path);
        return;
    }
    
    // 编译
    let output = Command::new("rustc")
        .arg(path)
        .arg("-o")
        .arg("/tmp/rust_example")
        .output();
    
    match output {
        Ok(output) => {
            if output.status.success() {
                println!("   ✅ 编译成功");
                
                // 运行
                let run_output = Command::new("/tmp/rust_example").output();
                
                match run_output {
                    Ok(run_output) => {
                        if run_output.status.success() {
                            println!("   📤 程序输出：");
                            let stdout = String::from_utf8_lossy(&run_output.stdout);
                            for line in stdout.lines() {
                                println!("   {}", line);
                            }
                            
                            if !run_output.stderr.is_empty() {
                                let stderr = String::from_utf8_lossy(&run_output.stderr);
                                println!("   ⚠️ 警告信息：");
                                for line in stderr.lines() {
                                    println!("   {}", line);
                                }
                            }
                        } else {
                            println!("   ❌ 运行失败");
                            let stderr = String::from_utf8_lossy(&run_output.stderr);
                            for line in stderr.lines() {
                                println!("   {}", line);
                            }
                        }
                    }
                    Err(e) => {
                        println!("   ❌ 运行出错: {}", e);
                    }
                }
            } else {
                println!("   ❌ 编译失败");
                let stderr = String::from_utf8_lossy(&output.stderr);
                for line in stderr.lines() {
                    println!("   {}", line);
                }
            }
        }
        Err(e) => {
            println!("   ❌ 编译出错: {}", e);
        }
    }
    
    // 清理临时文件
    let _ = std::fs::remove_file("/tmp/rust_example");
}

// 这个运行器的设计思路：
//
// 1. **自动化执行**：
//    - 自动发现示例文件
//    - 编译并运行每个示例
//    - 显示程序输出和错误信息
//
// 2. **用户友好**：
//    - 清晰的输出格式
//    - 错误信息的友好显示
//    - 学习建议和指导
//
// 3. **Rust特性应用**：
//    - 使用std::process进行系统调用
//    - 文件系统操作
//    - 错误处理
//    - 字符串和集合操作
//
// 使用场景：
// - 快速验证示例代码
// - 学习过程中的代码实验
// - 理解Rust程序的编译和运行流程
//
// 学习价值：
// - 理解Rust的编译模型
// - 学习系统编程接口
// - 掌握错误处理模式
// - 体验工具开发思路 