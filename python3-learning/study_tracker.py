#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python3 学习进度跟踪器
帮助用户记录和监控Python学习进度
"""

import json
import datetime
from pathlib import Path

class StudyTracker:
    """学习进度跟踪器"""
    
    def __init__(self):
        self.progress_file = "study_progress.json"
        self.topics = [
            "Python基础入门",
            "变量和数据类型", 
            "运算符",
            "控制流程",
            "数据结构",
            "函数",
            "面向对象编程",
            "模块和包",
            "文件操作", 
            "错误处理",
            "高级特性",
            "最佳实践"
        ]
        self.load_progress()
    
    def load_progress(self):
        """加载学习进度"""
        try:
            if Path(self.progress_file).exists():
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    self.progress = json.load(f)
            else:
                self.progress = {topic: {"completed": False, "date": None, "notes": ""} 
                               for topic in self.topics}
        except Exception as e:
            print(f"加载进度失败：{e}")
            self.progress = {topic: {"completed": False, "date": None, "notes": ""} 
                           for topic in self.topics}
    
    def save_progress(self):
        """保存学习进度"""
        try:
            with open(self.progress_file, 'w', encoding='utf-8') as f:
                json.dump(self.progress, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"保存进度失败：{e}")
            return False
    
    def mark_completed(self, topic, notes=""):
        """标记主题为已完成"""
        if topic in self.progress:
            self.progress[topic]["completed"] = True
            self.progress[topic]["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.progress[topic]["notes"] = notes
            
            if self.save_progress():
                print(f"✅ 恭喜！您已完成《{topic}》的学习！")
                if notes:
                    print(f"   学习笔记：{notes}")
                return True
        else:
            print(f"错误：主题'{topic}'不存在")
            return False
    
    def show_progress(self):
        """显示学习进度"""
        print("\n" + "=" * 60)
        print("🎯 Python3 学习进度报告")
        print("=" * 60)
        
        completed_count = sum(1 for data in self.progress.values() if data["completed"])
        total_count = len(self.topics)
        progress_percent = (completed_count / total_count) * 100
        
        print(f"📊 总体进度：{completed_count}/{total_count} ({progress_percent:.1f}%)")
        print("=" * 60)
        
        for i, topic in enumerate(self.topics, 1):
            data = self.progress[topic]
            status = "✅" if data["completed"] else "⏳"
            
            print(f"{status} {i:2d}. {topic}")
            
            if data["completed"]:
                print(f"     完成时间：{data['date']}")
                if data["notes"]:
                    print(f"     学习笔记：{data['notes']}")
            print()
        
        # 学习建议
        if completed_count == 0:
            print("🚀 开始您的Python学习之旅吧！建议从'Python基础入门'开始。")
        elif completed_count < total_count:
            # 找到下一个要学习的主题
            next_topic = None
            for topic in self.topics:
                if not self.progress[topic]["completed"]:
                    next_topic = topic
                    break
            if next_topic:
                print(f"📚 建议接下来学习：《{next_topic}》")
        else:
            print("🎉 恭喜您！已完成所有Python3基础学习内容！")
            print("💡 建议继续学习Python高级特性和实际项目开发。")

def main():
    """主程序"""
    tracker = StudyTracker()
    
    while True:
        print("\n" + "=" * 40)
        print("🐍 Python3 学习进度跟踪器")
        print("=" * 40)
        print("1. 查看学习进度")
        print("2. 标记主题完成")
        print("3. 添加学习笔记")
        print("4. 重置进度")
        print("5. 退出")
        print("=" * 40)
        
        try:
            choice = input("请选择操作 (1-5): ").strip()
            
            if choice == "1":
                tracker.show_progress()
            
            elif choice == "2":
                print("\n可选主题：")
                for i, topic in enumerate(tracker.topics, 1):
                    status = "✅" if tracker.progress[topic]["completed"] else "⏳"
                    print(f"{i:2d}. {status} {topic}")
                
                try:
                    topic_num = int(input("\n请选择要标记完成的主题编号: ")) - 1
                    if 0 <= topic_num < len(tracker.topics):
                        topic = tracker.topics[topic_num]
                        notes = input("请输入学习笔记（可选）: ").strip()
                        tracker.mark_completed(topic, notes)
                    else:
                        print("❌ 无效的主题编号！")
                except ValueError:
                    print("❌ 请输入有效的数字！")
            
            elif choice == "3":
                print("\n可选主题：")
                for i, topic in enumerate(tracker.topics, 1):
                    print(f"{i:2d}. {topic}")
                
                try:
                    topic_num = int(input("\n请选择要添加笔记的主题编号: ")) - 1
                    if 0 <= topic_num < len(tracker.topics):
                        topic = tracker.topics[topic_num]
                        note = input("请输入学习笔记: ").strip()
                        if note:
                            current_notes = tracker.progress[topic]["notes"]
                            if current_notes:
                                tracker.progress[topic]["notes"] = current_notes + "\n" + note
                            else:
                                tracker.progress[topic]["notes"] = note
                            
                            if tracker.save_progress():
                                print(f"📝 已为《{topic}》添加学习笔记")
                        else:
                            print("❌ 笔记不能为空！")
                    else:
                        print("❌ 无效的主题编号！")
                except ValueError:
                    print("❌ 请输入有效的数字！")
            
            elif choice == "4":
                confirm = input("⚠️  确定要重置所有学习进度吗？(输入'yes'确认): ")
                if confirm.lower() == 'yes':
                    tracker.progress = {topic: {"completed": False, "date": None, "notes": ""} 
                                      for topic in tracker.topics}
                    if tracker.save_progress():
                        print("🔄 学习进度已重置！")
                else:
                    print("❌ 取消重置操作")
            
            elif choice == "5":
                print("👋 感谢使用Python3学习进度跟踪器！")
                print("💪 继续加油学习Python吧！")
                break
            
            else:
                print("❌ 无效选择，请输入1-5之间的数字！")
                
        except KeyboardInterrupt:
            print("\n\n👋 程序被用户中断，再见！")
            break
        except Exception as e:
            print(f"❌ 程序错误：{e}")

if __name__ == "__main__":
    print("🎓 欢迎使用Python3学习进度跟踪器！")
    print("📚 这个工具将帮助您跟踪Python学习进度。")
    main() 