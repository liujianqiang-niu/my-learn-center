# 第1章：Rust环境搭建和工具链 🛠️

## 学习目标
- 理解Rust工具链的组成
- 成功安装和配置Rust开发环境
- 熟悉Cargo包管理器的基本使用
- 配置开发工具和编辑器
- 编写并运行第一个Rust程序

## 1. Rust语言简介

### 什么是Rust？
Rust是一门系统编程语言，由Mozilla在2010年开发。它的设计目标是：
- **内存安全**: 编译时防止内存泄漏、缓冲区溢出等问题
- **并发安全**: 类型系统防止数据竞争
- **零成本抽象**: 高级特性不会影响运行时性能
- **跨平台**: 支持多种操作系统和硬件架构

### Rust的应用领域
- **系统编程**: 操作系统、驱动程序、嵌入式系统
- **Web后端**: 高性能Web服务器和API
- **区块链**: 智能合约、加密货币系统
- **游戏开发**: 游戏引擎、图形处理
- **命令行工具**: 系统管理工具、开发工具

## 2. 安装Rust工具链

### 方法一：使用rustup (推荐)
rustup是Rust官方的工具链管理器，可以轻松管理Rust版本。

```bash
# Linux/macOS安装命令
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Windows用户可以下载rustup-init.exe
# 从 https://rustup.rs/ 下载
```

安装过程中的选择：
1. 选择默认安装 (推荐)
2. 自动添加到PATH环境变量
3. 安装默认的stable工具链

### 方法二：包管理器安装
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install rustc cargo

# Fedora
sudo dnf install rust cargo

# macOS (使用Homebrew)
brew install rust

# Arch Linux
sudo pacman -S rust
```

### 验证安装
```bash
# 检查Rust编译器版本
rustc --version

# 检查Cargo包管理器版本  
cargo --version

# 检查rustup版本
rustup --version
```

期望输出：
```
rustc 1.75.0 (82e1608df 2023-12-21)
cargo 1.75.0 (1d8b05cdd 2023-11-20)  
rustup 1.26.0 (5af9b9484 2023-04-05)
```

## 3. Rust工具链组成

### 核心组件
- **rustc**: Rust编译器，将.rs文件编译为可执行文件
- **cargo**: 包管理器和构建工具
- **rustup**: 工具链管理器，管理Rust版本和组件
- **rustfmt**: 代码格式化工具
- **clippy**: 代码检查工具，提供lint建议

### 安装附加组件
```bash
# 安装rustfmt (代码格式化)
rustup component add rustfmt

# 安装clippy (代码检查)
rustup component add clippy

# 安装rust-src (源码，用于IDE补全)
rustup component add rust-src

# 安装llvm-tools (性能分析工具)
rustup component add llvm-tools-preview
```

### 管理Rust版本
```bash
# 更新工具链
rustup update

# 安装特定版本
rustup install 1.74.0

# 设置默认版本
rustup default stable

# 查看已安装的工具链
rustup toolchain list

# 切换到特定版本
rustup default 1.74.0
```

## 4. 配置开发环境

### VS Code配置 (推荐)
1. 安装VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. 安装Rust扩展：
   - **rust-analyzer**: 提供智能补全、错误检查、代码导航
   - **Even Better TOML**: 处理Cargo.toml配置文件
   - **CodeLLDB**: 调试支持

VS Code配置文件 (`.vscode/settings.json`):
```json
{
    "rust-analyzer.check.command": "clippy",
    "rust-analyzer.rustfmt.rangeFormatting.enable": true,
    "editor.formatOnSave": true,
    "[rust]": {
        "editor.defaultFormatter": "rust-lang.rust-analyzer"
    }
}
```

### 其他IDE配置
```bash
# IntelliJ IDEA
# 安装Rust插件即可

# Vim/Neovim
# 安装rust.vim插件
git clone https://github.com/rust-lang/rust.vim ~/.vim/pack/plugins/start/rust.vim

# Emacs
# 在配置文件中添加
(use-package rust-mode
  :ensure t)
```

## 5. 第一个Rust程序

### 创建hello world程序
创建文件 `hello.rs`:
```rust
fn main() {
    println!("Hello, World!");
    println!("欢迎来到Rust世界！🦀");
}
```

### 编译并运行
```bash
# 编译
rustc hello.rs

# 运行 (Linux/macOS)
./hello

# 运行 (Windows)
hello.exe
```

### 程序解析
- `fn main()`: main函数是程序入口点
- `println!`: 宏(macro)，用于输出文本到控制台
- `!`: 表示这是一个宏调用，不是函数调用
- 分号 `;`: Rust语句必须以分号结尾

## 6. 使用Cargo管理项目

### 创建新项目
```bash
# 创建可执行程序项目
cargo new hello_cargo
cd hello_cargo

# 创建库项目
cargo new my_library --lib
```

### 项目结构
```
hello_cargo/
├── Cargo.toml          # 项目配置文件
├── src/
│   └── main.rs         # 源代码文件
└── .gitignore          # Git忽略文件
```

### Cargo.toml文件解析
```toml
[package]
name = "hello_cargo"      # 项目名称
version = "0.1.0"         # 版本号
edition = "2021"          # Rust版本

[dependencies]            # 依赖包
# 在这里添加外部依赖
```

### Cargo常用命令
```bash
# 检查代码是否能编译（不生成可执行文件）
cargo check

# 编译项目
cargo build

# 编译并运行
cargo run

# 运行测试
cargo test

# 构建文档
cargo doc --open

# 清理构建文件
cargo clean

# 更新依赖
cargo update

# 发布构建（优化版本）
cargo build --release
```

### 添加依赖包
在 `Cargo.toml` 中添加：
```toml
[dependencies]
rand = "0.8"              # 随机数生成器
serde = "1.0"             # 序列化/反序列化
tokio = "1.0"             # 异步运行时
```

安装依赖：
```bash
cargo build  # 自动下载并编译依赖
```

## 7. 实践练习

### 练习1：环境验证
创建并运行一个程序，输出Rust版本信息：

```rust
fn main() {
    println!("Rust版本信息:");
    println!("编译器版本: {}", env!("RUSTC_VERSION"));
    println!("目标架构: {}", env!("TARGET"));
}
```

### 练习2：使用Cargo创建项目
```bash
# 1. 创建新项目
cargo new my_first_project

# 2. 进入项目目录
cd my_first_project

# 3. 修改src/main.rs，添加个人信息输出

# 4. 运行项目
cargo run
```

### 练习3：添加外部依赖
修改 `Cargo.toml`，添加 `chrono` 依赖：
```toml
[dependencies]
chrono = "0.4"
```

在 `main.rs` 中使用：
```rust
use chrono::Local;

fn main() {
    let now = Local::now();
    println!("当前时间: {}", now.format("%Y-%m-%d %H:%M:%S"));
}
```

## 8. 常用工具安装

### 安装有用的Cargo子命令
```bash
# cargo-edit: 命令行编辑依赖
cargo install cargo-edit

# cargo-watch: 监控文件变化自动重新构建
cargo install cargo-watch

# cargo-expand: 查看宏展开结果
cargo install cargo-expand

# cargo-audit: 安全审计
cargo install cargo-audit

# cargo-outdated: 检查过期依赖
cargo install cargo-outdated
```

### 使用示例
```bash
# 添加依赖（需要cargo-edit）
cargo add serde

# 监控文件变化（需要cargo-watch）
cargo watch -x run

# 检查安全漏洞（需要cargo-audit）
cargo audit

# 检查过期依赖（需要cargo-outdated）
cargo outdated
```

## 9. 故障排除

### 常见问题及解决方案

**问题1：rustc: command not found**
```bash
# 解决方案：检查PATH环境变量
echo $PATH
source ~/.bashrc    # 或 ~/.zshrc
```

**问题2：cargo build失败**
```bash
# 解决方案：清理并重新构建
cargo clean
cargo build
```

**问题3：网络问题导致依赖下载失败**
```bash
# 解决方案：配置国内镜像
# 创建 ~/.cargo/config.toml
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml << EOF
[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = 'tuna'

[source.tuna]
registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"
EOF
```

**问题4：IDE没有智能提示**
```bash
# 解决方案：安装rust-src组件
rustup component add rust-src
```

## 10. 本章小结

✅ **已完成的学习目标**:
- 成功安装Rust工具链和开发环境
- 理解Rust工具链的组成和作用
- 掌握Cargo项目管理的基本使用
- 编写并运行第一个Rust程序
- 配置开发工具获得更好的开发体验

🎯 **下一步学习**:
- 学习Rust基础语法
- 理解变量、数据类型和函数
- 掌握Rust的基本编程概念

📝 **学习检查点**:
- [ ] 能够成功编译并运行Rust程序
- [ ] 能够使用cargo创建和管理项目
- [ ] 能够添加和使用外部依赖包
- [ ] 开发工具配置完成，有代码补全和错误提示

恭喜您完成了Rust学习的第一步！环境搭建是编程学习的基础，现在您已经具备了学习Rust的所有工具。让我们继续学习Rust的基础语法吧！🚀 