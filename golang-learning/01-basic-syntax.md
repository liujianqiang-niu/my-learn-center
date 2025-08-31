# Go语言基础语法

## 1. Hello World程序

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
```

**解释**:
- `package main`: 声明这是main包，程序入口包
- `import "fmt"`: 导入格式化输出包
- `func main()`: 程序的入口函数

## 2. 变量声明

### 基本方式

```go
// 方法1: 声明后赋值
var name string
name = "张三"

// 方法2: 声明时初始化
var age int = 25

// 方法3: 类型推断
var city = "北京"

// 方法4: 短变量声明
country := "中国"
```

### 多变量声明

```go
// 同时声明多个
var a, b, c int = 1, 2, 3

// 短声明
x, y := 10, 20

// 组声明
var (
    username string = "admin"
    password string = "123456"
)
```

## 3. 基本数据类型

```go
// 整数类型
var num1 int8 = 127      // 8位整数
var num2 int = 100       // 平台相关
var num3 uint8 = 255     // 无符号8位

// 浮点数
var pi float32 = 3.14    // 32位浮点
var e float64 = 2.718    // 64位浮点

// 布尔类型
var isTrue bool = true
var isFalse bool = false

// 字符串
var message string = "Hello"
var multiline = `多行
字符串`

// 字符
var char1 byte = 'A'     // ASCII字符
var char2 rune = '中'     // Unicode字符
```

## 4. 函数

### 基本函数

```go
// 无参数无返回值
func sayHello() {
    fmt.Println("Hello!")
}

// 有参数有返回值
func add(a, b int) int {
    return a + b
}

// 多返回值
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("除数不能为0")
    }
    return a / b, nil
}

// 命名返回值
func rectangle(w, h float64) (area, perimeter float64) {
    area = w * h
    perimeter = 2 * (w + h)
    return  // 自动返回命名变量
}
```

## 5. 控制结构

### if条件

```go
score := 85

if score >= 90 {
    fmt.Println("优秀")
} else if score >= 80 {
    fmt.Println("良好")
} else {
    fmt.Println("需要努力")
}

// if中初始化
if grade := score / 10; grade >= 9 {
    fmt.Println("A级")
}
```

### for循环

```go
// 传统for循环
for i := 0; i < 5; i++ {
    fmt.Printf("%d ", i)
}

// while模式
j := 0
for j < 3 {
    fmt.Printf("%d ", j)
    j++
}

// 无限循环
for {
    // 使用break跳出
    break
}

// range遍历
numbers := []int{1, 2, 3, 4, 5}
for index, value := range numbers {
    fmt.Printf("索引%d: 值%d\n", index, value)
}
```

### switch选择

```go
day := 3

switch day {
case 1:
    fmt.Println("星期一")
case 2:
    fmt.Println("星期二")
case 3:
    fmt.Println("星期三")
case 6, 7:  // 多个case
    fmt.Println("周末")
default:
    fmt.Println("其他")
}

// 条件switch
temperature := 25
switch {
case temperature < 0:
    fmt.Println("结冰")
case temperature < 30:
    fmt.Println("温暖")
default:
    fmt.Println("炎热")
}
```

## 6. 练习题

1. 编写一个函数计算两个数的最大值
2. 使用循环计算1到100的和
3. 编写一个函数判断一个数是否为偶数
4. 使用switch语句根据分数给出等级评价

继续学习：[02-advanced-features.md](./02-advanced-features.md) 