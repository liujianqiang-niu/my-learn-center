# Go语言最佳实践

## 1. 代码规范

### 1.1 命名规范

```go
// ✅ 好的命名
type UserManager struct {
    users []User
}

func (um *UserManager) GetUserByID(id int) (*User, error) {
    // 实现逻辑
}

// ❌ 不好的命名
type usrmgr struct {
    u []User
}

func (um *usrmgr) get(i int) (*User, error) {
    // 实现逻辑
}
```

**命名原则**:
- 使用驼峰命名法 (camelCase)
- 导出的标识符首字母大写 (如 `UserManager`)
- 私有标识符首字母小写 (如 `userManager`)
- 包名使用小写字母，简短有意义
- 常量使用大写字母和下划线

### 1.2 包组织

```go
// 好的包结构
myproject/
├── cmd/           // 可执行程序
│   └── myapp/
│       └── main.go
├── internal/      // 私有代码
│   ├── config/
│   ├── service/
│   └── database/
├── pkg/           // 可被外部导入的代码
│   ├── api/
│   └── utils/
├── configs/       // 配置文件
├── docs/          // 文档
└── go.mod
```

### 1.3 错误处理规范

```go
// ✅ 好的错误处理
func LoadConfig(filename string) (*Config, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, fmt.Errorf("读取配置文件失败: %w", err)
    }
    
    var config Config
    if err := yaml.Unmarshal(data, &config); err != nil {
        return nil, fmt.Errorf("解析配置文件失败: %w", err)
    }
    
    return &config, nil
}

// ❌ 不好的错误处理
func LoadConfig(filename string) *Config {
    data, _ := os.ReadFile(filename)  // 忽略错误
    var config Config
    yaml.Unmarshal(data, &config)     // 忽略错误
    return &config
}
```

## 2. 设计模式

### 2.1 接口设计

```go
// 定义小而专注的接口
type Reader interface {
    Read([]byte) (int, error)
}

type Writer interface {
    Write([]byte) (int, error)
}

// 组合接口
type ReadWriter interface {
    Reader
    Writer
}

// 实现接口
type FileHandler struct {
    filename string
}

func (f *FileHandler) Read(data []byte) (int, error) {
    // 实现读取逻辑
    return 0, nil
}

func (f *FileHandler) Write(data []byte) (int, error) {
    // 实现写入逻辑
    return 0, nil
}
```

### 2.2 工厂模式

```go
type Database interface {
    Connect() error
    Query(sql string) ([]Row, error)
}

type MySQLDB struct {
    host string
    port int
}

func (m *MySQLDB) Connect() error {
    fmt.Printf("连接到MySQL: %s:%d\n", m.host, m.port)
    return nil
}

func (m *MySQLDB) Query(sql string) ([]Row, error) {
    fmt.Printf("执行MySQL查询: %s\n", sql)
    return nil, nil
}

// 工厂函数
func NewDatabase(dbType, host string, port int) Database {
    switch dbType {
    case "mysql":
        return &MySQLDB{host: host, port: port}
    default:
        return nil
    }
}
```

### 2.3 装饰器模式

```go
type Handler interface {
    Handle(request string) string
}

type BasicHandler struct{}

func (h *BasicHandler) Handle(request string) string {
    return "处理: " + request
}

// 日志装饰器
type LoggingHandler struct {
    handler Handler
}

func (l *LoggingHandler) Handle(request string) string {
    fmt.Printf("开始处理请求: %s\n", request)
    result := l.handler.Handle(request)
    fmt.Printf("处理完成: %s\n", result)
    return result
}

// 使用装饰器
func main() {
    basic := &BasicHandler{}
    logged := &LoggingHandler{handler: basic}
    
    result := logged.Handle("测试请求")
    fmt.Println(result)
}
```

## 3. 并发最佳实践

### 3.1 Goroutine管理

```go
import (
    "context"
    "sync"
    "time"
)

// 使用WaitGroup等待goroutine完成
func goodConcurrency() {
    var wg sync.WaitGroup
    
    for i := 0; i < 3; i++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            fmt.Printf("Worker %d 完成\n", id)
        }(i)
    }
    
    wg.Wait()
    fmt.Println("所有任务完成")
}

// 使用Context控制goroutine
func withContext() {
    ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
    defer cancel()
    
    go func() {
        select {
        case <-time.After(3 * time.Second):
            fmt.Println("任务完成")
        case <-ctx.Done():
            fmt.Println("任务被取消:", ctx.Err())
        }
    }()
    
    time.Sleep(1 * time.Second)
    cancel()  // 主动取消
}
```

### 3.2 Channel模式

```go
// 生产者-消费者模式
func producerConsumer() {
    jobs := make(chan int, 10)
    results := make(chan int, 10)
    
    // 生产者
    go func() {
        defer close(jobs)
        for i := 1; i <= 5; i++ {
            jobs <- i
        }
    }()
    
    // 消费者
    go func() {
        defer close(results)
        for job := range jobs {
            results <- job * job
        }
    }()
    
    // 收集结果
    for result := range results {
        fmt.Printf("结果: %d\n", result)
    }
}

// Fan-out/Fan-in模式
func fanOutFanIn() {
    input := make(chan int)
    
    // Fan-out: 启动多个worker
    workers := make([]<-chan int, 3)
    for i := 0; i < 3; i++ {
        worker := make(chan int)
        workers[i] = worker
        
        go func(ch chan int) {
            defer close(ch)
            for num := range input {
                ch <- num * num
            }
        }(worker)
    }
    
    // 发送数据
    go func() {
        defer close(input)
        for i := 1; i <= 10; i++ {
            input <- i
        }
    }()
    
    // Fan-in: 合并结果
    for result := range merge(workers...) {
        fmt.Printf("结果: %d\n", result)
    }
}

func merge(channels ...<-chan int) <-chan int {
    out := make(chan int)
    var wg sync.WaitGroup
    
    for _, ch := range channels {
        wg.Add(1)
        go func(c <-chan int) {
            defer wg.Done()
            for value := range c {
                out <- value
            }
        }(ch)
    }
    
    go func() {
        wg.Wait()
        close(out)
    }()
    
    return out
}
```

## 4. 性能优化

### 4.1 内存优化

```go
// ✅ 预分配切片容量
func goodSliceUsage() []string {
    // 如果知道大概大小，预分配容量
    result := make([]string, 0, 100)
    for i := 0; i < 100; i++ {
        result = append(result, fmt.Sprintf("item-%d", i))
    }
    return result
}

// ❌ 频繁扩容
func badSliceUsage() []string {
    var result []string  // 初始容量为0
    for i := 0; i < 100; i++ {
        result = append(result, fmt.Sprintf("item-%d", i))
    }
    return result
}

// 字符串拼接优化
func goodStringConcat(items []string) string {
    var builder strings.Builder
    builder.Grow(len(items) * 10)  // 预分配容量
    
    for _, item := range items {
        builder.WriteString(item)
        builder.WriteString(" ")
    }
    return builder.String()
}
```

### 4.2 避免常见陷阱

```go
// ✅ 正确的循环变量使用
func goodLoop() {
    for i := 0; i < 3; i++ {
        go func(num int) {  // 传递副本
            fmt.Printf("Number: %d\n", num)
        }(i)
    }
}

// ❌ 错误的循环变量使用
func badLoop() {
    for i := 0; i < 3; i++ {
        go func() {
            fmt.Printf("Number: %d\n", i)  // 所有goroutine共享变量i
        }()
    }
}

// ✅ 正确的切片传递
func goodSlicePass(data []int) []int {
    result := make([]int, len(data))
    copy(result, data)  // 创建副本
    // 修改result不会影响原切片
    return result
}
```

## 5. 测试

### 5.1 单元测试

```go
// math.go
package math

func Add(a, b int) int {
    return a + b
}

func Divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("除数不能为零")
    }
    return a / b, nil
}

// math_test.go
package math

import "testing"

func TestAdd(t *testing.T) {
    result := Add(2, 3)
    expected := 5
    
    if result != expected {
        t.Errorf("Add(2, 3) = %d; 期望 %d", result, expected)
    }
}

func TestDivide(t *testing.T) {
    // 测试正常情况
    result, err := Divide(10, 2)
    if err != nil {
        t.Errorf("不应该有错误: %v", err)
    }
    if result != 5.0 {
        t.Errorf("Divide(10, 2) = %.2f; 期望 5.00", result)
    }
    
    // 测试除零错误
    _, err = Divide(10, 0)
    if err == nil {
        t.Error("应该返回除零错误")
    }
}

// 运行测试: go test
```

### 5.2 基准测试

```go
func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(100, 200)
    }
}

// 运行基准测试: go test -bench=.
```

## 6. 日志和调试

### 6.1 结构化日志

```go
import "github.com/sirupsen/logrus"

func setupLogging() {
    logrus.SetFormatter(&logrus.JSONFormatter{})
    logrus.SetLevel(logrus.InfoLevel)
}

func processUser(userID int) error {
    logger := logrus.WithFields(logrus.Fields{
        "userID": userID,
        "action": "processUser",
    })
    
    logger.Info("开始处理用户")
    
    // 处理逻辑...
    if userID < 0 {
        logger.Error("无效的用户ID")
        return errors.New("无效的用户ID")
    }
    
    logger.Info("用户处理完成")
    return nil
}
```

### 6.2 错误包装

```go
import "fmt"

func readUserData(filename string) (*UserData, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, fmt.Errorf("读取用户数据文件 %s 失败: %w", filename, err)
    }
    
    var userData UserData
    if err := json.Unmarshal(data, &userData); err != nil {
        return nil, fmt.Errorf("解析用户数据失败: %w", err)
    }
    
    return &userData, nil
}
```

## 7. 实际项目模式

### 7.1 配置管理

```go
type Config struct {
    Server ServerConfig `yaml:"server"`
    DB     DBConfig     `yaml:"database"`
    Log    LogConfig    `yaml:"logging"`
}

type ServerConfig struct {
    Host string `yaml:"host"`
    Port int    `yaml:"port"`
}

func LoadConfig(filename string) (*Config, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, fmt.Errorf("读取配置文件失败: %w", err)
    }
    
    var config Config
    if err := yaml.Unmarshal(data, &config); err != nil {
        return nil, fmt.Errorf("解析配置失败: %w", err)
    }
    
    return &config, nil
}
```

### 7.2 依赖注入

```go
type UserService struct {
    db     Database
    logger Logger
}

func NewUserService(db Database, logger Logger) *UserService {
    return &UserService{
        db:     db,
        logger: logger,
    }
}

func (us *UserService) CreateUser(user *User) error {
    us.logger.Info("创建用户", "username", user.Username)
    
    if err := us.db.Save(user); err != nil {
        us.logger.Error("保存用户失败", "error", err)
        return fmt.Errorf("创建用户失败: %w", err)
    }
    
    return nil
}
```

### 7.3 中间件模式

```go
type Handler func(request string) string

type Middleware func(Handler) Handler

// 日志中间件
func LoggingMiddleware(next Handler) Handler {
    return func(request string) string {
        fmt.Printf("处理请求: %s\n", request)
        result := next(request)
        fmt.Printf("请求完成: %s\n", result)
        return result
    }
}

// 认证中间件
func AuthMiddleware(next Handler) Handler {
    return func(request string) string {
        if request == "" {
            return "认证失败"
        }
        return next(request)
    }
}

// 应用中间件
func applyMiddleware(handler Handler, middlewares ...Middleware) Handler {
    for i := len(middlewares) - 1; i >= 0; i-- {
        handler = middlewares[i](handler)
    }
    return handler
}
```

## 8. 性能监控

### 8.1 性能分析

```go
import (
    _ "net/http/pprof"
    "net/http"
)

func main() {
    // 启动pprof服务器
    go func() {
        http.ListenAndServe("localhost:6060", nil)
    }()
    
    // 你的应用逻辑
    runApplication()
}

// 使用方法:
// go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30
```

### 8.2 基准测试

```go
func BenchmarkStringConcat(b *testing.B) {
    items := make([]string, 100)
    for i := range items {
        items[i] = fmt.Sprintf("item-%d", i)
    }
    
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        result := strings.Join(items, " ")
        _ = result
    }
}
```

## 9. 项目实践技巧

### 9.1 资源清理

```go
func processFile(filename string) error {
    file, err := os.Open(filename)
    if err != nil {
        return err
    }
    defer file.Close()  // 确保文件被关闭
    
    // 处理文件内容
    return nil
}

// 使用sync.Pool复用对象
var bufferPool = sync.Pool{
    New: func() interface{} {
        return make([]byte, 1024)
    },
}

func processData() {
    buffer := bufferPool.Get().([]byte)
    defer bufferPool.Put(buffer)
    
    // 使用buffer处理数据
}
```

### 9.2 优雅关闭

```go
func gracefulShutdown() {
    server := &http.Server{Addr: ":8080"}
    
    // 监听关闭信号
    sigChan := make(chan os.Signal, 1)
    signal.Notify(sigChan, os.Interrupt, syscall.SIGTERM)
    
    go func() {
        <-sigChan
        fmt.Println("收到关闭信号，开始优雅关闭...")
        
        ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
        defer cancel()
        
        if err := server.Shutdown(ctx); err != nil {
            fmt.Printf("服务器关闭错误: %v\n", err)
        }
    }()
    
    if err := server.ListenAndServe(); err != http.ErrServerClosed {
        fmt.Printf("服务器启动错误: %v\n", err)
    }
}
```

## 10. 常见反模式

### 避免这些做法：

```go
// ❌ 忽略错误
data, _ := os.ReadFile("config.yaml")

// ❌ 空接口滥用
func process(data interface{}) {
    // 类型断言过多
}

// ❌ 不必要的goroutine
for _, item := range items {
    go processItem(item)  // 没有控制并发数量
}

// ❌ 内存泄漏
func badChannelUsage() {
    ch := make(chan int)
    go func() {
        ch <- 42  // 永远阻塞，goroutine泄漏
    }()
    // 没有读取channel
}
```

## 学习检查点

完成本章学习后，您应该能够：

- ✅ 编写符合Go规范的代码
- ✅ 使用Go的惯用法解决问题
- ✅ 设计合理的包结构和接口
- ✅ 安全地使用并发编程
- ✅ 编写高性能的Go代码
- ✅ 避免常见的编程陷阱

继续学习：[04-examples.md](./04-examples.md) 