# Go语言高级特性

## 1. 数组、切片和映射

### 1.1 数组 (Array)

```go
// 数组声明
var arr1 [5]int                    // 零值初始化
var arr2 = [5]int{1, 2, 3, 4, 5}  // 完整初始化
arr3 := [...]int{10, 20, 30}      // 自动计算长度

// 数组操作
fmt.Printf("长度: %d\n", len(arr2))
arr2[0] = 100  // 修改元素
```

### 1.2 切片 (Slice)

```go
// 切片创建
var slice1 []int               // nil切片
slice2 := []int{1, 2, 3}      // 初始化切片
slice3 := make([]int, 5)      // 长度为5
slice4 := make([]int, 3, 10)  // 长度3，容量10

// 切片操作
slice1 = append(slice1, 10, 20)  // 追加元素
fmt.Printf("长度: %d, 容量: %d\n", len(slice1), cap(slice1))

// 切片截取
numbers := []int{0, 1, 2, 3, 4, 5}
fmt.Printf("numbers[1:4]: %v\n", numbers[1:4])  // [1 2 3]
fmt.Printf("numbers[:3]: %v\n", numbers[:3])    // [0 1 2]
fmt.Printf("numbers[2:]: %v\n", numbers[2:])    // [2 3 4 5]
```

### 1.3 映射 (Map)

```go
// map创建
var map1 map[string]int
map2 := make(map[string]int)
map3 := map[string]int{
    "apple":  5,
    "banana": 3,
}

// map操作
map2["go"] = 2009
value, exists := map2["go"]  // 检查键是否存在
if exists {
    fmt.Printf("Go发布于%d年\n", value)
}

delete(map2, "go")  // 删除键值对

// 遍历map
for key, value := range map3 {
    fmt.Printf("%s: %d\n", key, value)
}
```

## 2. 结构体和方法

### 2.1 结构体定义

```go
type Person struct {
    Name  string
    Age   int
    Email string
}

// 结构体初始化
p1 := Person{
    Name:  "张三",
    Age:   25,
    Email: "zhangsan@example.com",
}

// 匿名字段
type Employee struct {
    Person    // 嵌入Person结构体
    JobTitle  string
    Salary    int
}

emp := Employee{
    Person:   Person{"李四", 30, "lisi@example.com"},
    JobTitle: "工程师",
    Salary:   8000,
}

// 可以直接访问嵌入结构体的字段
fmt.Println(emp.Name)  // 等价于 emp.Person.Name
```

### 2.2 方法

```go
type Rectangle struct {
    Width, Height float64
}

// 值接收者方法
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

// 指针接收者方法
func (r *Rectangle) Scale(factor float64) {
    r.Width *= factor
    r.Height *= factor
}

func main() {
    rect := Rectangle{Width: 3, Height: 4}
    
    // 调用方法
    fmt.Printf("面积: %.2f\n", rect.Area())
    
    rect.Scale(2)  // Go自动取地址
    fmt.Printf("缩放后: %+v\n", rect)
}
```

## 3. 接口 (Interface)

### 3.1 接口定义

```go
// 定义接口
type Shape interface {
    Area() float64
    Perimeter() float64
}

// 实现接口（隐式实现）
type Circle struct {
    Radius float64
}

func (c Circle) Area() float64 {
    return 3.14159 * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
    return 2 * 3.14159 * c.Radius
}

type Rectangle struct {
    Width, Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
    return 2 * (r.Width + r.Height)
}
```

### 3.2 接口使用

```go
func printShapeInfo(s Shape) {
    fmt.Printf("面积: %.2f, 周长: %.2f\n", s.Area(), s.Perimeter())
}

func main() {
    circle := Circle{Radius: 5}
    rect := Rectangle{Width: 3, Height: 4}
    
    // 接口多态
    printShapeInfo(circle)
    printShapeInfo(rect)
    
    // 接口切片
    shapes := []Shape{circle, rect}
    for i, shape := range shapes {
        fmt.Printf("形状%d - ", i+1)
        printShapeInfo(shape)
    }
}
```

### 3.3 空接口和类型断言

```go
func main() {
    // 空接口可以保存任意类型的值
    var value interface{}
    
    value = 42
    fmt.Printf("值: %v, 类型: %T\n", value, value)
    
    value = "Hello"
    fmt.Printf("值: %v, 类型: %T\n", value, value)
    
    // 类型断言
    if str, ok := value.(string); ok {
        fmt.Printf("这是字符串: %s\n", str)
    }
    
    // 类型switch
    switch v := value.(type) {
    case string:
        fmt.Printf("字符串: %s\n", v)
    case int:
        fmt.Printf("整数: %d\n", v)
    default:
        fmt.Printf("其他类型: %T\n", v)
    }
}
```

## 4. 错误处理

### 4.1 基本错误处理

```go
import (
    "errors"
    "fmt"
)

func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("除数不能为零")
    }
    return a / b, nil
}

func main() {
    result, err := divide(10, 2)
    if err != nil {
        fmt.Printf("错误: %v\n", err)
        return
    }
    fmt.Printf("结果: %.2f\n", result)
}
```

### 4.2 自定义错误

```go
type MyError struct {
    Code    int
    Message string
}

func (e MyError) Error() string {
    return fmt.Sprintf("错误码%d: %s", e.Code, e.Message)
}

func someFunction() error {
    return MyError{
        Code:    404,
        Message: "资源未找到",
    }
}
```

## 5. 并发编程基础

### 5.1 Goroutine

```go
import (
    "fmt"
    "time"
)

func sayHello(name string) {
    for i := 0; i < 3; i++ {
        fmt.Printf("Hello, %s! (%d)\n", name, i+1)
        time.Sleep(100 * time.Millisecond)
    }
}

func main() {
    // 启动goroutine
    go sayHello("Alice")
    go sayHello("Bob")
    
    // 主goroutine等待
    time.Sleep(1 * time.Second)
    fmt.Println("程序结束")
}
```

### 5.2 Channel (通道)

```go
func main() {
    // 创建channel
    ch := make(chan string)
    
    // 在goroutine中发送数据
    go func() {
        ch <- "Hello from goroutine!"
    }()
    
    // 接收数据
    message := <-ch
    fmt.Println(message)
    
    // 带缓冲的channel
    bufferedCh := make(chan int, 3)
    bufferedCh <- 1
    bufferedCh <- 2
    bufferedCh <- 3
    
    fmt.Println(<-bufferedCh)  // 1
    fmt.Println(<-bufferedCh)  // 2
    fmt.Println(<-bufferedCh)  // 3
}
```

## 6. 包管理

### 6.1 Go Modules

```bash
# 初始化模块
go mod init myproject

# 添加依赖
go get github.com/sirupsen/logrus

# 更新依赖
go mod tidy

# 查看依赖
go list -m all
```

### 6.2 包的导入和使用

```go
import (
    "fmt"                           // 标准库
    "github.com/sirupsen/logrus"   // 第三方库
    "./mypackage"                  // 本地包
)
```

## 7. 实践练习

### 练习1: 学生管理系统

```go
type Student struct {
    ID     int
    Name   string
    Scores []float64
}

func (s Student) Average() float64 {
    if len(s.Scores) == 0 {
        return 0
    }
    total := 0.0
    for _, score := range s.Scores {
        total += score
    }
    return total / float64(len(s.Scores))
}

func main() {
    student := Student{
        ID:     1,
        Name:   "小明",
        Scores: []float64{85, 92, 78, 96},
    }
    
    fmt.Printf("学生: %s, 平均分: %.2f\n", 
        student.Name, student.Average())
}
```

### 练习2: 简单的并发程序

```go
func worker(id int, jobs <-chan int, results chan<- int) {
    for job := range jobs {
        fmt.Printf("Worker %d 处理任务 %d\n", id, job)
        time.Sleep(time.Second)
        results <- job * 2
    }
}

func main() {
    jobs := make(chan int, 100)
    results := make(chan int, 100)
    
    // 启动3个worker
    for w := 1; w <= 3; w++ {
        go worker(w, jobs, results)
    }
    
    // 发送任务
    for j := 1; j <= 5; j++ {
        jobs <- j
    }
    close(jobs)
    
    // 收集结果
    for r := 1; r <= 5; r++ {
        result := <-results
        fmt.Printf("结果: %d\n", result)
    }
}
```

## 学习检查点

完成本章学习后，您应该能够：

- ✅ 熟练使用切片和map进行数据操作
- ✅ 定义结构体和方法
- ✅ 理解接口的概念和使用
- ✅ 掌握基本的错误处理模式
- ✅ 编写简单的并发程序
- ✅ 使用Go modules管理依赖

继续学习：[03-best-practices.md](./03-best-practices.md) 