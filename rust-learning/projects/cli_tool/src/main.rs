// Rust命令行工具项目
// 这是一个综合实战项目，应用了前面学到的Rust知识
//
// 功能：
// 1. 文件操作：读取、写入、统计
// 2. 数据处理：JSON解析、文本分析
// 3. 命令行界面：参数解析、用户交互
//
// 运行方式：
// cargo run -- --help
// cargo run -- count-words input.txt
// cargo run -- json-format data.json

use clap::{Parser, Subcommand};
use std::fs;
use std::path::Path;
use serde_json::Value;

#[derive(Parser)]
#[command(name = "rust-cli-tool")]
#[command(about = "一个用于学习Rust的命令行工具")]
#[command(version = "1.0")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// 统计文件中的单词数量
    CountWords {
        /// 要分析的文件路径
        file_path: String,
        
        /// 是否显示详细统计
        #[arg(short, long)]
        verbose: bool,
    },
    /// 格式化JSON文件
    JsonFormat {
        /// JSON文件路径
        file_path: String,
        
        /// 输出文件路径（可选）
        #[arg(short, long)]
        output: Option<String>,
    },
    /// 文本查找和替换
    FindReplace {
        /// 要搜索的文件
        file_path: String,
        
        /// 搜索的文本
        #[arg(short, long)]
        find: String,
        
        /// 替换的文本
        #[arg(short, long)]
        replace: String,
    },
}

fn main() {
    let cli = Cli::parse();
    
    println!("🦀 Rust CLI工具 v1.0");
    println!("====================");
    
    match cli.command {
        Commands::CountWords { file_path, verbose } => {
            if let Err(e) = count_words(&file_path, verbose) {
                eprintln!("❌ 错误: {}", e);
                std::process::exit(1);
            }
        }
        Commands::JsonFormat { file_path, output } => {
            if let Err(e) = format_json(&file_path, output.as_deref()) {
                eprintln!("❌ 错误: {}", e);
                std::process::exit(1);
            }
        }
        Commands::FindReplace { file_path, find, replace } => {
            if let Err(e) = find_and_replace(&file_path, &find, &replace) {
                eprintln!("❌ 错误: {}", e);
                std::process::exit(1);
            }
        }
    }
}

// 功能1：统计单词数量
fn count_words(file_path: &str, verbose: bool) -> Result<(), Box<dyn std::error::Error>> {
    // 检查文件是否存在
    if !Path::new(file_path).exists() {
        return Err(format!("文件不存在: {}", file_path).into());
    }
    
    // 读取文件内容
    let content = fs::read_to_string(file_path)?;
    
    // 基础统计
    let char_count = content.chars().count();
    let word_count = content.split_whitespace().count();
    let line_count = content.lines().count();
    
    println!("📊 文件统计: {}", file_path);
    println!("  字符数: {}", char_count);
    println!("  单词数: {}", word_count);
    println!("  行数: {}", line_count);
    
    if verbose {
        // 详细统计
        let bytes = content.len();
        let non_whitespace_chars = content.chars().filter(|c| !c.is_whitespace()).count();
        
        println!("\n📋 详细统计:");
        println!("  字节数: {}", bytes);
        println!("  非空白字符: {}", non_whitespace_chars);
        println!("  平均单词长度: {:.2}", 
                non_whitespace_chars as f64 / word_count as f64);
        
        // 最常见的单词
        let mut word_freq = std::collections::HashMap::new();
        for word in content.split_whitespace() {
            let word = word.to_lowercase().trim_matches(|c: char| c.is_ascii_punctuation());
            if !word.is_empty() {
                *word_freq.entry(word.to_string()).or_insert(0) += 1;
            }
        }
        
        // 找出最常见的5个单词
        let mut sorted_words: Vec<_> = word_freq.iter().collect();
        sorted_words.sort_by(|a, b| b.1.cmp(a.1));
        
        println!("\n🏆 最常见的单词:");
        for (i, (word, count)) in sorted_words.iter().take(5).enumerate() {
            println!("  {}. '{}' 出现 {} 次", i + 1, word, count);
        }
    }
    
    Ok(())
}

// 功能2：格式化JSON
fn format_json(file_path: &str, output_path: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
    // 检查文件是否存在
    if !Path::new(file_path).exists() {
        return Err(format!("文件不存在: {}", file_path).into());
    }
    
    // 读取并解析JSON
    let content = fs::read_to_string(file_path)?;
    let json: Value = serde_json::from_str(&content)?;
    
    // 格式化JSON
    let formatted = serde_json::to_string_pretty(&json)?;
    
    match output_path {
        Some(output) => {
            // 写入到指定文件
            fs::write(output, formatted)?;
            println!("✅ JSON已格式化并保存到: {}", output);
        }
        None => {
            // 输出到控制台
            println!("📄 格式化的JSON:");
            println!("{}", formatted);
        }
    }
    
    Ok(())
}

// 功能3：查找和替换
fn find_and_replace(file_path: &str, find: &str, replace: &str) -> Result<(), Box<dyn std::error::Error>> {
    // 检查文件是否存在
    if !Path::new(file_path).exists() {
        return Err(format!("文件不存在: {}", file_path).into());
    }
    
    // 读取文件内容
    let content = fs::read_to_string(file_path)?;
    
    // 统计替换次数
    let occurrences = content.matches(find).count();
    
    if occurrences == 0 {
        println!("⚠️ 未找到要替换的文本: '{}'", find);
        return Ok(());
    }
    
    // 执行替换
    let new_content = content.replace(find, replace);
    
    // 创建备份文件
    let backup_path = format!("{}.backup", file_path);
    fs::write(&backup_path, &content)?;
    
    // 写入新内容
    fs::write(file_path, new_content)?;
    
    println!("✅ 替换完成:");
    println!("  文件: {}", file_path);
    println!("  查找: '{}'", find);
    println!("  替换: '{}'", replace);
    println!("  替换次数: {}", occurrences);
    println!("  备份文件: {}", backup_path);
    
    Ok(())
}

// 这个CLI工具项目演示了：
//
// 1. **项目结构**:
//    - Cargo.toml配置文件管理依赖
//    - 模块化的代码组织
//    - 错误处理和用户友好的输出
//
// 2. **Rust核心概念应用**:
//    - 所有权系统（字符串操作）
//    - 模式匹配（命令行解析）
//    - 错误处理（Result类型）
//    - 集合操作（HashMap、Vec）
//
// 3. **实用功能**:
//    - 文件I/O操作
//    - JSON数据处理
//    - 文本分析和处理
//    - 命令行界面设计
//
// 学习价值：
// - 理解真实Rust项目的结构
// - 学习外部crate的使用
// - 掌握错误处理的最佳实践
// - 体验Rust在系统工具开发中的优势
//
// 使用方法：
// 1. cd projects/cli_tool
// 2. cargo run -- count-words ../../README.md
// 3. cargo run -- json-format test.json
// 4. cargo run -- find-replace test.txt old new 