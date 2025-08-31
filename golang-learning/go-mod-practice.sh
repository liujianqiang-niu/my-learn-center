#!/bin/bash

echo "🚀 Go Modules 实践教程"
echo "这个脚本会带您一步步练习 go mod 的使用"
echo ""

# 创建练习目录
PRACTICE_DIR="go-mod-practice"
if [ -d "$PRACTICE_DIR" ]; then
    echo "清理之前的练习目录..."
    rm -rf "$PRACTICE_DIR"
fi

echo "📁 创建练习目录: $PRACTICE_DIR"
mkdir "$PRACTICE_DIR"
cd "$PRACTICE_DIR"

echo ""
echo "🎯 练习1: 初始化模块"
echo "运行: go mod init example.com/hello-world"
go mod init example.com/hello-world

echo ""
echo "📋 查看生成的 go.mod 文件:"
cat go.mod

echo ""
echo "🎯 练习2: 创建简单的Go程序"
cat > main.go << 'EOF'
package main

import (
    "fmt"
    "github.com/fatih/color"
)

func main() {
    color.Red("Hello, ")
    color.Blue("Go Modules!")
    fmt.Println()
    
    color.Yellow("这个程序演示了如何使用第三方依赖")
}
EOF

echo "📄 创建了 main.go 文件"

echo ""
echo "🎯 练习3: 自动下载依赖"
echo "运行: go mod tidy"
go mod tidy

echo ""
echo "📋 查看更新后的 go.mod 文件:"
cat go.mod

echo ""
echo "📋 查看生成的 go.sum 文件:"
if [ -f "go.sum" ]; then
    echo "go.sum 文件内容 (前5行):"
    head -5 go.sum
else
    echo "go.sum 文件尚未生成"
fi

echo ""
echo "🎯 练习4: 运行程序"
echo "运行: go run main.go"
go run main.go

echo ""
echo "🎯 练习5: 查看依赖信息"
echo "所有依赖模块:"
go list -m all

echo ""
echo "依赖关系图:"
go mod graph

echo ""
echo "🎯 练习6: 添加特定版本依赖"
echo "添加 logrus 日志库:"
go get github.com/sirupsen/logrus@v1.9.0

echo ""
echo "📋 查看再次更新的 go.mod:"
cat go.mod

echo ""
echo "🎯 练习7: 创建带版本管理的程序"
cat > version_demo.go << 'EOF'
package main

import (
    "github.com/fatih/color"
    "github.com/sirupsen/logrus"
)

func main() {
    logrus.SetLevel(logrus.InfoLevel)
    
    logrus.Info("程序启动")
    
    color.Green("✅ Go Modules 依赖管理成功!")
    color.Cyan("📦 使用的依赖:")
    color.White("  - github.com/fatih/color (彩色输出)")
    color.White("  - github.com/sirupsen/logrus (结构化日志)")
    
    logrus.Info("程序结束")
}
EOF

echo ""
echo "🎯 练习8: 运行新程序"
go run version_demo.go

echo ""
echo "🎯 练习9: 升级依赖"
echo "升级 logrus 到最新版本:"
go get github.com/sirupsen/logrus@latest

echo ""
echo "📋 查看最终的 go.mod:"
cat go.mod

echo ""
echo "🎯 练习10: 构建可执行文件"
echo "构建程序:"
go build -o hello-modules main.go

if [ -f "hello-modules" ]; then
    echo "✅ 构建成功! 运行 ./hello-modules:"
    ./hello-modules
else
    echo "❌ 构建失败"
fi

echo ""
echo "🎯 练习11: 清理和验证"
echo "验证依赖完整性:"
go mod verify

echo ""
echo "清理未使用的依赖:"
go mod tidy

echo ""
echo "🔗 接下来请阅读 go-modules-guide.md 了解更多高级用法"

cd ..
echo ""
echo "💡 提示: 练习文件保存在 $PRACTICE_DIR/ 目录中，您可以继续实验" 