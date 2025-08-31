#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3 示例代码运行器
让用户可以快速体验所有示例代码
"""

import os
import sys
from pathlib import Path

def show_menu():
    """显示菜单"""
    print("\n" + "🚀" * 20)
    print("    Python3 示例代码运行器")
    print("🚀" * 20)
    print()
    print("📚 可运行的示例代码：")
    print("1. 快速开始指南 (quick_start.py)")
    print("2. 基础语法示例 (examples/basic_syntax/variables_and_types.py)")
    print("3. 数据结构示例 (examples/data_structures/collections_demo.py)")
    print("4. 函数示例 (examples/functions/function_examples.py)")
    print("5. 面向对象示例 (examples/oop/class_examples.py)")
    print("6. 综合项目示例 (examples/project_example.py)")
    print("7. 学习进度跟踪器 (study_tracker.py)")
    print("8. 基础练习题 (exercises/basic/exercise_01_variables.py)")
    print("9. 查看所有文件")
    print("0. 退出")

def run_file(file_path):
    """运行指定的Python文件"""
    if not Path(file_path).exists():
        print(f"❌ 文件不存在：{file_path}")
        return False
    
    print(f"\n🔄 正在运行：{file_path}")
    print("=" * 60)
    
    try:
        # 执行Python文件
        os.system(f"python3 {file_path}")
        print("=" * 60)
        print("✅ 程序运行完成")
        return True
    except Exception as e:
        print(f"❌ 运行出错：{e}")
        return False

def show_file_content(file_path):
    """显示文件内容（前50行）"""
    if not Path(file_path).exists():
        print(f"❌ 文件不存在：{file_path}")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        print(f"\n📄 {file_path} 的内容预览（前50行）：")
        print("=" * 60)
        
        for i, line in enumerate(lines[:50], 1):
            print(f"{i:3d}| {line.rstrip()}")
        
        if len(lines) > 50:
            print(f"... (省略了 {len(lines) - 50} 行)")
        
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ 读取文件出错：{e}")

def list_all_files():
    """列出所有Python文件"""
    print("\n📁 项目中的所有Python文件：")
    print("=" * 50)
    
    # 获取所有Python文件
    python_files = []
    
    # 根目录的Python文件
    for file in Path(".").glob("*.py"):
        python_files.append(str(file))
    
    # examples目录的Python文件
    examples_dir = Path("examples")
    if examples_dir.exists():
        for file in examples_dir.rglob("*.py"):
            python_files.append(str(file))
    
    # exercises目录的Python文件
    exercises_dir = Path("exercises")
    if exercises_dir.exists():
        for file in exercises_dir.rglob("*.py"):
            python_files.append(str(file))
    
    # 按目录分组显示
    root_files = [f for f in python_files if "/" not in f]
    example_files = [f for f in python_files if f.startswith("examples/")]
    exercise_files = [f for f in python_files if f.startswith("exercises/")]
    
    if root_files:
        print("📄 根目录文件：")
        for file in sorted(root_files):
            print(f"  - {file}")
    
    if example_files:
        print("\n📚 示例代码文件：")
        for file in sorted(example_files):
            print(f"  - {file}")
    
    if exercise_files:
        print("\n✏️  练习题文件：")
        for file in sorted(exercise_files):
            print(f"  - {file}")
    
    print(f"\n📊 总计：{len(python_files)} 个Python文件")

def check_python_installation():
    """检查Python安装"""
    print("🔍 检查Python环境...")
    
    try:
        import sys
        print(f"✅ Python版本：{sys.version}")
        print(f"✅ Python路径：{sys.executable}")
        
        # 检查常用模块
        modules_to_check = ['json', 'datetime', 'pathlib', 'os']
        print("\n📦 检查常用模块：")
        
        for module_name in modules_to_check:
            try:
                __import__(module_name)
                print(f"  ✅ {module_name}")
            except ImportError:
                print(f"  ❌ {module_name} (未安装)")
        
        print("\n🎉 Python环境检查完成！")
        return True
        
    except Exception as e:
        print(f"❌ Python环境检查失败：{e}")
        return False

def main():
    """主程序"""
    print("🐍 Python3 学习环境")
    print("=" * 40)
    
    # 检查Python环境
    if not check_python_installation():
        print("⚠️  请确保Python3已正确安装")
        return
    
    # 文件映射
    file_map = {
        "1": "quick_start.py",
        "2": "examples/basic_syntax/variables_and_types.py",
        "3": "examples/data_structures/collections_demo.py", 
        "4": "examples/functions/function_examples.py",
        "5": "examples/oop/class_examples.py",
        "6": "examples/project_example.py",
        "7": "study_tracker.py",
        "8": "exercises/basic/exercise_01_variables.py"
    }
    
    while True:
        show_menu()
        
        try:
            choice = input("\n请选择要运行的代码 (0-9): ").strip()
            
            if choice == "0":
                print("👋 感谢使用Python3学习环境！")
                print("💪 继续加油学习Python！")
                break
            
            elif choice == "9":
                list_all_files()
                
                # 询问是否要查看某个文件
                show_file = input("\n是否要查看某个文件的内容？输入文件路径（或按回车跳过）: ").strip()
                if show_file:
                    show_file_content(show_file)
            
            elif choice in file_map:
                file_path = file_map[choice]
                
                # 询问是运行还是查看
                action = input(f"\n对于文件 {file_path}，您想要:\n1. 运行代码\n2. 查看代码\n请选择 (1/2): ").strip()
                
                if action == "1":
                    run_file(file_path)
                elif action == "2":
                    show_file_content(file_path)
                else:
                    print("❌ 无效选择")
            
            else:
                print("❌ 无效选择，请输入0-9之间的数字")
                
            # 询问是否继续
            if choice != "0":
                input("\n按回车键继续...")
                
        except KeyboardInterrupt:
            print("\n\n👋 程序被中断，再见！")
            break
        except Exception as e:
            print(f"❌ 程序错误：{e}")

if __name__ == "__main__":
    main() 