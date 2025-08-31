# Go语言实例代码和练习

## 1. 基础练习

### 练习1: 计算器

```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

type Calculator struct{}

func (c Calculator) Add(a, b float64) float64 {
    return a + b
}

func (c Calculator) Subtract(a, b float64) float64 {
    return a - b
}

func (c Calculator) Multiply(a, b float64) float64 {
    return a * b
}

func (c Calculator) Divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("除数不能为零")
    }
    return a / b, nil
}

func main() {
    calc := Calculator{}
    
    fmt.Printf("10 + 5 = %.2f\n", calc.Add(10, 5))
    fmt.Printf("10 - 5 = %.2f\n", calc.Subtract(10, 5))
    fmt.Printf("10 * 5 = %.2f\n", calc.Multiply(10, 5))
    
    if result, err := calc.Divide(10, 5); err != nil {
        fmt.Printf("错误: %v\n", err)
    } else {
        fmt.Printf("10 / 5 = %.2f\n", result)
    }
}
```

### 练习2: 学生成绩管理

```go
type Student struct {
    ID     int
    Name   string
    Scores []float64
}

func (s *Student) AddScore(score float64) {
    s.Scores = append(s.Scores, score)
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

func (s Student) Grade() string {
    avg := s.Average()
    switch {
    case avg >= 90:
        return "A"
    case avg >= 80:
        return "B"
    case avg >= 70:
        return "C"
    case avg >= 60:
        return "D"
    default:
        return "F"
    }
}

type ClassRoom struct {
    Students []Student
}

func (c *ClassRoom) AddStudent(student Student) {
    c.Students = append(c.Students, student)
}

func (c ClassRoom) GetTopStudent() *Student {
    if len(c.Students) == 0 {
        return nil
    }
    
    topStudent := &c.Students[0]
    for i := 1; i < len(c.Students); i++ {
        if c.Students[i].Average() > topStudent.Average() {
            topStudent = &c.Students[i]
        }
    }
    return topStudent
}

func main() {
    classroom := ClassRoom{}
    
    // 添加学生
    student1 := Student{ID: 1, Name: "张三"}
    student1.AddScore(85)
    student1.AddScore(92)
    student1.AddScore(78)
    
    student2 := Student{ID: 2, Name: "李四"}
    student2.AddScore(90)
    student2.AddScore(88)
    student2.AddScore(95)
    
    classroom.AddStudent(student1)
    classroom.AddStudent(student2)
    
    // 显示结果
    for _, student := range classroom.Students {
        fmt.Printf("学生: %s, 平均分: %.2f, 等级: %s\n",
            student.Name, student.Average(), student.Grade())
    }
    
    if top := classroom.GetTopStudent(); top != nil {
        fmt.Printf("最优学生: %s (%.2f分)\n", top.Name, top.Average())
    }
}
```

## 2. 高级练习

### 练习3: HTTP服务器

```go
package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
    "strconv"
    "time"
)

type User struct {
    ID       int       `json:"id"`
    Name     string    `json:"name"`
    Email    string    `json:"email"`
    Created  time.Time `json:"created"`
}

type UserService struct {
    users map[int]*User
    nextID int
}

func NewUserService() *UserService {
    return &UserService{
        users: make(map[int]*User),
        nextID: 1,
    }
}

func (us *UserService) CreateUser(name, email string) *User {
    user := &User{
        ID:      us.nextID,
        Name:    name,
        Email:   email,
        Created: time.Now(),
    }
    us.users[us.nextID] = user
    us.nextID++
    return user
}

func (us *UserService) GetUser(id int) *User {
    return us.users[id]
}

func (us *UserService) ListUsers() []*User {
    users := make([]*User, 0, len(us.users))
    for _, user := range us.users {
        users = append(users, user)
    }
    return users
}

func main() {
    userService := NewUserService()
    
    // 创建一些测试数据
    userService.CreateUser("张三", "zhangsan@example.com")
    userService.CreateUser("李四", "lisi@example.com")
    
    // API处理器
    http.HandleFunc("/users", func(w http.ResponseWriter, r *http.Request) {
        switch r.Method {
        case "GET":
            users := userService.ListUsers()
            w.Header().Set("Content-Type", "application/json")
            json.NewEncoder(w).Encode(users)
        case "POST":
            var req struct {
                Name  string `json:"name"`
                Email string `json:"email"`
            }
            if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
                http.Error(w, "无效的JSON", http.StatusBadRequest)
                return
            }
            
            user := userService.CreateUser(req.Name, req.Email)
            w.Header().Set("Content-Type", "application/json")
            json.NewEncoder(w).Encode(user)
        default:
            http.Error(w, "方法不支持", http.StatusMethodNotAllowed)
        }
    })
    
    http.HandleFunc("/users/", func(w http.ResponseWriter, r *http.Request) {
        if r.Method != "GET" {
            http.Error(w, "方法不支持", http.StatusMethodNotAllowed)
            return
        }
        
        idStr := strings.TrimPrefix(r.URL.Path, "/users/")
        id, err := strconv.Atoi(idStr)
        if err != nil {
            http.Error(w, "无效的用户ID", http.StatusBadRequest)
            return
        }
        
        user := userService.GetUser(id)
        if user == nil {
            http.Error(w, "用户不存在", http.StatusNotFound)
            return
        }
        
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(user)
    })
    
    fmt.Println("服务器启动在 :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

### 练习4: 并发下载器

```go
package main

import (
    "fmt"
    "io"
    "net/http"
    "os"
    "path/filepath"
    "sync"
    "time"
)

type DownloadTask struct {
    URL      string
    Filename string
}

type Downloader struct {
    maxWorkers int
    client     *http.Client
}

func NewDownloader(maxWorkers int) *Downloader {
    return &Downloader{
        maxWorkers: maxWorkers,
        client: &http.Client{
            Timeout: 30 * time.Second,
        },
    }
}

func (d *Downloader) Download(tasks []DownloadTask) error {
    taskChan := make(chan DownloadTask, len(tasks))
    errorChan := make(chan error, len(tasks))
    
    // 启动worker goroutines
    var wg sync.WaitGroup
    for i := 0; i < d.maxWorkers; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for task := range taskChan {
                if err := d.downloadFile(task); err != nil {
                    errorChan <- fmt.Errorf("下载 %s 失败: %w", task.URL, err)
                } else {
                    fmt.Printf("✅ 下载完成: %s\n", task.Filename)
                }
            }
        }()
    }
    
    // 发送任务
    go func() {
        for _, task := range tasks {
            taskChan <- task
        }
        close(taskChan)
    }()
    
    // 等待完成
    go func() {
        wg.Wait()
        close(errorChan)
    }()
    
    // 收集错误
    for err := range errorChan {
        if err != nil {
            fmt.Printf("❌ %v\n", err)
        }
    }
    
    return nil
}

func (d *Downloader) downloadFile(task DownloadTask) error {
    resp, err := d.client.Get(task.URL)
    if err != nil {
        return err
    }
    defer resp.Body.Close()
    
    if resp.StatusCode != http.StatusOK {
        return fmt.Errorf("HTTP错误: %d", resp.StatusCode)
    }
    
    file, err := os.Create(task.Filename)
    if err != nil {
        return err
    }
    defer file.Close()
    
    _, err = io.Copy(file, resp.Body)
    return err
}

func main() {
    downloader := NewDownloader(3)
    
    tasks := []DownloadTask{
        {"https://golang.org/robots.txt", "golang-robots.txt"},
        {"https://github.com/robots.txt", "github-robots.txt"},
    }
    
    fmt.Println("开始并发下载...")
    if err := downloader.Download(tasks); err != nil {
        fmt.Printf("下载过程中出现错误: %v\n", err)
    }
    fmt.Println("下载完成!")
}
```

## 3. 深入项目代码

### 分析deepin-compatible-ctl项目

现在您可以尝试阅读和理解deepin-compatible-ctl项目的代码：

#### 3.1 从main.go开始
1. 理解CLI框架的初始化
2. 学习配置管理模式
3. 分析命令行参数处理

#### 3.2 学习AppManager
1. 理解业务逻辑封装
2. 学习装饰器模式的应用
3. 分析错误处理策略

#### 3.3 研究容器接口
1. 理解接口设计原则
2. 学习多态的实际应用
3. 分析依赖注入模式

#### 3.4 深入并发处理
1. 学习goroutine的实际使用
2. 理解channel在项目中的作用
3. 分析资源管理和清理

## 4. 动手练习任务

### 任务1: 为项目添加新功能
尝试为deepin-compatible-ctl添加一个新的命令，比如`app backup`，用于备份应用数据。

### 任务2: 优化现有代码
找到项目中可以优化的地方，比如：
- 添加更好的错误处理
- 改进日志输出
- 优化性能

### 任务3: 编写测试
为现有的函数编写单元测试，确保代码质量。

### 任务4: 重构代码
尝试重构某个模块，使其更加清晰和可维护。

## 学习资源

### 官方资源
- [Go官方文档](https://golang.org/doc/)
- [Go语言规范](https://golang.org/ref/spec)
- [Go官方教程](https://tour.golang.org/)

### 推荐书籍
- 《Go语言圣经》- Alan Donovan & Brian Kernighan
- 《Go语言实战》- William Kennedy
- 《Go并发编程实战》

### 在线资源
- [Go Playground](https://play.golang.org/) - 在线编程环境
- [Go by Example](https://gobyexample.com/) - 通过例子学习
- [Effective Go](https://golang.org/doc/effective_go.html) - 官方最佳实践

恭喜您完成了Go语言学习指南！现在您已经具备了阅读和开发Go项目的基础能力。 