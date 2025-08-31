# Go语言学习资料

欢迎来到Go语言学习专区！这里包含了专为初学者设计的Go语言学习资料。

## 文档列表

1. **01-basic-syntax.md** - Go语言基础语法
2. **02-advanced-features.md** - Go语言高级特性  
3. **03-best-practices.md** - Go语言最佳实践
4. **04-examples.md** - 实例代码和练习
5. **go-modules-guide.md** - Go Modules依赖管理完整指南

## 快速开始

### 安装Go环境
```bash
# 检查是否已安装
go version

# 如果未安装，下载并安装Go 1.20+
wget https://golang.org/dl/go1.20.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.20.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
```

### 第一个程序
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
```

保存为hello.go，然后运行：
```bash
go run hello.go
```

## 学习建议

1. 按文档顺序学习，不要跳跃
2. 每学一个概念都要写代码验证
3. 特别重视go-modules-guide.md，这是现代Go开发必备技能
4. 结合deepin-compatible-ctl项目代码实践
5. 遇到问题多查官方文档

开始您的Go语言学习之旅吧！ 