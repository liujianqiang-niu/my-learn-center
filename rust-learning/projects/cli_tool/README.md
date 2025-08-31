# Rust命令行工具实战项目 🛠️

这是一个综合性的Rust项目，旨在帮助初学者将理论知识应用到实践中，体验真实的Rust项目开发流程。

## 🎯 项目目标
通过构建一个功能完整的命令行工具，学习和应用：
- Rust项目结构和Cargo管理
- 外部crate的使用（clap、serde等）
- 文件I/O和数据处理
- 错误处理的最佳实践
- 命令行应用程序设计

## 🚀 功能特性

### 1. 文件统计 (`count-words`)
- 统计文件的字符数、单词数、行数
- 详细模式：显示字节数、高频词汇等
- 支持任意文本文件格式

### 2. JSON格式化 (`json-format`)
- 美化JSON文件格式
- 支持控制台输出或保存到文件
- 验证JSON语法的正确性

### 3. 文本查找替换 (`find-replace`)
- 在文件中查找指定文本并替换
- 自动创建备份文件
- 统计替换操作的次数

## 🏗️ 项目结构
```
cli_tool/
├── Cargo.toml              # 项目配置和依赖管理
├── README.md               # 项目说明（本文件）
├── src/
│   └── main.rs             # 主程序入口
├── test_files/             # 测试文件
│   ├── sample.txt
│   ├── data.json
│   └── README.md
└── target/                 # 编译输出目录（自动生成）
```

## 🛠️ 环境要求
- Rust 1.70.0 或更新版本
- Cargo（随Rust安装）
- 支持Unicode的终端

## 🚀 快速开始

### 1. 进入项目目录
```bash
cd rust-learning/projects/cli_tool
```

### 2. 构建项目
```bash
# 检查代码（推荐，快速验证）
cargo check

# 编译项目
cargo build

# 构建发布版本（优化性能）
cargo build --release
```

### 3. 运行项目
```bash
# 查看帮助信息
cargo run -- --help

# 文件统计示例
cargo run -- count-words ../../README.md

# 详细统计
cargo run -- count-words ../../README.md --verbose

# JSON格式化
cargo run -- json-format test_files/data.json

# JSON格式化并保存
cargo run -- json-format test_files/data.json --output formatted.json

# 文本替换
cargo run -- find-replace test_files/sample.txt "旧文本" "新文本"
```

## 📋 使用示例

### 示例1：统计Rust代码文件
```bash
# 基础统计
cargo run -- count-words src/main.rs

# 详细统计，包括高频词汇分析
cargo run -- count-words src/main.rs --verbose
```

期望输出：
```
🦀 Rust CLI工具 v1.0
====================
📊 文件统计: src/main.rs
  字符数: 1500
  单词数: 200
  行数: 50

📋 详细统计:
  字节数: 1500
  非空白字符: 1200
  平均单词长度: 6.00

🏆 最常见的单词:
  1. 'fn' 出现 15 次
  2. 'let' 出现 12 次
  3. 'string' 出现 8 次
```

### 示例2：格式化JSON配置文件
```bash
cargo run -- json-format Cargo.toml --output formatted_cargo.json
```

### 示例3：批处理文本替换
```bash
# 替换注释中的占位符
cargo run -- find-replace src/main.rs "TODO" "DONE"
```

## 🎓 学习要点

### 1. Cargo项目管理
学习如何：
- 配置`Cargo.toml`文件
- 管理外部依赖
- 使用不同的构建配置
- 理解Rust的项目结构约定

### 2. 外部Crate的使用
体验如何：
- 查找和选择合适的crate
- 阅读crate文档
- 集成第三方库到项目中
- 管理版本兼容性

### 3. 错误处理模式
掌握：
- `Result<T, E>`类型的使用
- `?`运算符简化错误传播
- 自定义错误类型
- 用户友好的错误消息

### 4. 系统编程实践
学习：
- 文件系统操作
- 命令行参数解析
- 标准输入输出处理
- 跨平台兼容性考虑

## 🧪 测试和调试

### 运行单元测试
```bash
cargo test
```

### 代码质量检查
```bash
# 代码风格检查
cargo fmt --check

# 代码质量建议
cargo clippy

# 安全审计
cargo audit
```

### 性能分析
```bash
# 发布构建（优化性能）
cargo build --release

# 运行发布版本
./target/release/rust_cli_tool --help

# 比较debug和release版本的性能
time cargo run -- count-words large_file.txt
time ./target/release/rust_cli_tool count-words large_file.txt
```

## 🔧 扩展练习

### 初级扩展
1. **添加新的统计功能**：
   - 统计特定字符的出现次数
   - 计算文件的MD5哈希值
   - 分析编程语言的关键字频率

2. **改进用户体验**：
   - 添加进度条（对大文件）
   - 支持通配符文件匹配
   - 添加彩色输出

### 中级扩展
1. **增强JSON处理**：
   - JSON验证功能
   - JSON查询（类似jq）
   - JSON转换为其他格式

2. **文本处理增强**：
   - 正则表达式支持
   - 多文件批处理
   - 差异比较功能

### 高级扩展
1. **性能优化**：
   - 并行文件处理
   - 流式处理大文件
   - 内存映射文件

2. **系统集成**：
   - 配置文件支持
   - 日志系统集成
   - 插件系统设计

## 🐛 常见问题解决

### 问题1：依赖下载失败
```bash
# 清理并重新构建
cargo clean
cargo build

# 使用国内镜像（如果需要）
# 编辑 ~/.cargo/config.toml
```

### 问题2：编译错误
```bash
# 检查Rust版本
rustc --version

# 更新工具链
rustup update

# 查看详细错误信息
cargo build --verbose
```

### 问题3：运行时错误
```bash
# 启用调试信息
RUST_BACKTRACE=1 cargo run -- command args

# 使用调试器
cargo build
gdb target/debug/rust_cli_tool
```

## 📚 相关学习资源

### Rust官方文档
- [The Rust Programming Language Book](https://doc.rust-lang.org/book/)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Cargo Book](https://doc.rust-lang.org/cargo/)

### 使用的Crates文档
- [clap](https://docs.rs/clap/) - 命令行参数解析
- [serde](https://docs.rs/serde/) - 序列化框架
- [chrono](https://docs.rs/chrono/) - 日期时间处理

## 🏆 完成标准

完成这个项目后，你应该能够：
- ✅ 独立创建和配置Rust项目
- ✅ 集成和使用外部依赖
- ✅ 处理文件I/O和错误情况
- ✅ 设计用户友好的命令行界面
- ✅ 编写模块化、可测试的代码
- ✅ 使用Cargo进行项目管理
- ✅ 理解Rust在系统编程中的优势

恭喜！这个项目将让你体验到Rust在实际开发中的强大能力。完成后，你就具备了开发实用工具的基础技能！🚀 