package main

import (
	"fmt"
	"math"
	"time"
)

// 基础练习：变量和函数
func basicPractice() {
	fmt.Println("=== 基础练习 ===")

	// 变量声明和初始化
	var name string = "Go学习者"
	age := 25
	isLearning := true

	fmt.Printf("姓名: %s, 年龄: %d, 正在学习: %t\n", name, age, isLearning)

	// 函数调用
	sum := add(10, 20)
	fmt.Printf("10 + 20 = %d\n", sum)

	// 多返回值
	quotient, remainder := divmod(17, 5)
	fmt.Printf("17 ÷ 5 = %d 余 %d\n", quotient, remainder)
}

// 简单的加法函数
func add(a, b int) int {
	return a + b
}

// 返回商和余数
func divmod(a, b int) (int, int) {
	return a / b, a % b
}

// 切片和映射练习
func collectionPractice() {
	fmt.Println("\n=== 集合练习 ===")

	// 切片操作
	numbers := []int{1, 2, 3, 4, 5}
	fmt.Printf("原切片: %v\n", numbers)

	// 追加元素
	numbers = append(numbers, 6, 7, 8)
	fmt.Printf("追加后: %v\n", numbers)

	// 切片截取
	fmt.Printf("numbers[2:5]: %v\n", numbers[2:5])

	// 映射操作
	grades := map[string]int{
		"张三": 85,
		"李四": 92,
		"王五": 78,
	}

	fmt.Println("学生成绩:")
	for name, grade := range grades {
		fmt.Printf("  %s: %d分\n", name, grade)
	}

	// 添加新学生
	grades["赵六"] = 88
	fmt.Printf("新增学生后的成绩: %v\n", grades)
}

// 结构体和方法练习
type Circle struct {
	Radius float64
}

func (c Circle) Area() float64 {
	return math.Pi * c.Radius * c.Radius
}

func (c Circle) Circumference() float64 {
	return 2 * math.Pi * c.Radius
}

func (c Circle) Perimeter() float64 {
	return c.Circumference()
}

func (c *Circle) Scale(factor float64) {
	c.Radius *= factor
}

func structPractice() {
	fmt.Println("\n=== 结构体练习 ===")

	circle := Circle{Radius: 5.0}
	fmt.Printf("圆的半径: %.1f\n", circle.Radius)
	fmt.Printf("圆的面积: %.2f\n", circle.Area())
	fmt.Printf("圆的周长: %.2f\n", circle.Circumference())

	// 修改半径
	circle.Scale(2.0)
	fmt.Printf("缩放后半径: %.1f, 面积: %.2f\n", circle.Radius, circle.Area())
}

// 接口练习
type Shape interface {
	Area() float64
	Perimeter() float64
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

func printShapeInfo(s Shape) {
	fmt.Printf("面积: %.2f, 周长: %.2f\n", s.Area(), s.Perimeter())
}

func interfacePractice() {
	fmt.Println("\n=== 接口练习 ===")

	circle := Circle{Radius: 3.0}
	rectangle := Rectangle{Width: 4.0, Height: 5.0}

	fmt.Print("圆形 - ")
	printShapeInfo(circle)

	fmt.Print("矩形 - ")
	printShapeInfo(rectangle)
}

// 错误处理练习
func divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, fmt.Errorf("除数不能为零")
	}
	return a / b, nil
}

func errorPractice() {
	fmt.Println("\n=== 错误处理练习 ===")

	// 正常情况
	if result, err := divide(10, 2); err != nil {
		fmt.Printf("错误: %v\n", err)
	} else {
		fmt.Printf("10 ÷ 2 = %.2f\n", result)
	}

	// 错误情况
	if result, err := divide(10, 0); err != nil {
		fmt.Printf("错误: %v\n", err)
	} else {
		fmt.Printf("10 ÷ 0 = %.2f\n", result)
	}
}

// 并发练习
func worker(id int, jobs <-chan int, results chan<- int) {
	for job := range jobs {
		fmt.Printf("Worker %d 处理任务 %d\n", id, job)
		time.Sleep(100 * time.Millisecond)
		results <- job * job
	}
}

func concurrencyPractice() {
	fmt.Println("\n=== 并发练习 ===")

	jobs := make(chan int, 10)
	results := make(chan int, 10)

	// 启动3个worker
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// 发送5个任务
	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)

	// 收集结果
	for r := 1; r <= 5; r++ {
		result := <-results
		fmt.Printf("任务结果: %d\n", result)
	}
}

// 主函数：运行所有练习
func main() {
	fmt.Println("🎯 Go语言练习程序")
	fmt.Println("运行各种练习来验证您的学习成果！")

	basicPractice()
	collectionPractice()
	structPractice()
	interfacePractice()
	errorPractice()
	concurrencyPractice()

	fmt.Println("\n🎉 所有练习完成！您已经掌握了Go语言的基础知识。")
	fmt.Println("📚 继续阅读deepin-compatible-ctl项目代码，加深理解！")
}
