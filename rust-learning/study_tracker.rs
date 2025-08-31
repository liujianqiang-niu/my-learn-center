// Rust学习进度跟踪器
// 运行方式: rustc study_tracker.rs && ./study_tracker

use std::collections::HashMap;
use std::io;

fn main() {
    println!("🦀 Rust学习进度跟踪器");
    println!("=============================");
    
    let mut tracker = StudyTracker::new();
    
    loop {
        print_menu();
        let choice = get_user_input();
        
        match choice.trim() {
            "1" => tracker.show_progress(),
            "2" => tracker.mark_chapter_complete(),
            "3" => tracker.add_note(),
            "4" => tracker.show_notes(),
            "5" => tracker.show_statistics(),
            "6" => tracker.show_learning_tips(),
            "7" => {
                println!("👋 继续加油学习Rust！祝你早日成为Rust专家！");
                break;
            }
            _ => println!("❌ 无效选择，请输入1-7"),
        }
        
        println!(); // 空行分隔
    }
}

struct StudyTracker {
    chapters: HashMap<String, ChapterInfo>,
    notes: Vec<String>,
}

struct ChapterInfo {
    title: String,
    completed: bool,
    difficulty: u8, // 1-5 难度等级
}

impl StudyTracker {
    fn new() -> Self {
        let mut chapters = HashMap::new();
        
        // 初始化所有章节
        let chapter_list = vec![
            ("01", "环境搭建和工具链", 1),
            ("02", "基础语法", 2),
            ("03", "控制流", 2),
            ("04", "所有权系统基础", 4),
            ("05", "深入理解所有权、借用、引用", 5),
            ("06", "结构体和枚举", 3),
            ("07", "模式匹配和match表达式", 3),
            ("08", "错误处理机制", 4),
            ("09", "泛型编程和特质系统", 5),
            ("10", "生命周期详解", 5),
            ("11", "闭包和迭代器", 4),
            ("12", "智能指针详解", 5),
            ("13", "模块系统和包管理", 3),
            ("14", "集合类型详解", 3),
            ("15", "并发编程", 5),
            ("16", "异步编程基础", 4),
            ("17", "Unsafe Rust和底层编程", 5),
            ("18", "宏编程系统", 5),
            ("19", "高级特质和类型系统", 5),
            ("20", "性能优化技巧", 4),
            ("21", "大型项目架构设计", 4),
            ("22", "测试和调试最佳实践", 3),
            ("23", "部署和分发", 2),
        ];
        
        for (id, title, difficulty) in chapter_list {
            chapters.insert(
                id.to_string(),
                ChapterInfo {
                    title: title.to_string(),
                    completed: false,
                    difficulty,
                }
            );
        }
        
        StudyTracker {
            chapters,
            notes: Vec::new(),
        }
    }
    
    fn show_progress(&self) {
        println!("📊 Rust学习进度报告");
        println!("====================");
        
        let total_chapters = self.chapters.len();
        let completed_chapters = self.chapters.values()
            .filter(|ch| ch.completed)
            .count();
        
        let progress_percentage = (completed_chapters as f64 / total_chapters as f64 * 100.0) as u32;
        
        println!("总体进度: {}/{} ({}%)", completed_chapters, total_chapters, progress_percentage);
        self.print_progress_bar(progress_percentage);
        
        println!("\n📚 章节详情:");
        for i in 1..=23 {
            let id = format!("{:02}", i);
            if let Some(chapter) = self.chapters.get(&id) {
                let status = if chapter.completed { "✅" } else { "⏳" };
                let stars = "★".repeat(chapter.difficulty as usize);
                println!("  {:<3} {} {} (难度: {})",
                         id, status, chapter.title, stars);
            }
        }
        
        // 学习建议
        self.show_current_stage_advice(completed_chapters);
    }
    
    fn print_progress_bar(&self, percentage: u32) {
        let filled = percentage / 5; // 每个块代表5%
        let empty = 20 - filled;
        
        print!("进度: [");
        print!("{}", "█".repeat(filled as usize));
        print!("{}", "░".repeat(empty as usize));
        println!("] {}%", percentage);
    }
    
    fn show_current_stage_advice(&self, completed: usize) {
        println!("\n💡 当前阶段学习建议:");
        
        match completed {
            0..=4 => {
                println!("  🌱 第一阶段：基础语法学习");
                println!("  📖 重点：理解Rust基本概念和所有权系统");
                println!("  ⏰ 建议：每天1-2小时，重点理解不要急于求成");
                println!("  🎯 目标：能够编写简单的Rust程序");
            }
            5..=8 => {
                println!("  🚀 第二阶段：核心概念掌握");
                println!("  📖 重点：深入理解借用、生命周期、错误处理");
                println!("  ⏰ 建议：多做练习，理论结合实践");
                println!("  🎯 目标：能够设计和实现自定义数据结构");
            }
            9..=12 => {
                println!("  ⚡ 第三阶段：高级特性学习");
                println!("  📖 重点：泛型、特质、智能指针");
                println!("  ⏰ 建议：注重概念理解，多看优秀代码");
                println!("  🎯 目标：编写类型安全、高效的抽象代码");
            }
            13..=16 => {
                println!("  🛠️ 第四阶段：实用技能培养");
                println!("  📖 重点：模块化、集合、并发、异步");
                println!("  ⏰ 建议：开始做实际项目，应用所学知识");
                println!("  🎯 目标：能够开发实用的Rust应用程序");
            }
            17..=20 => {
                println!("  🚀 第五阶段：专家进阶");
                println!("  📖 重点：unsafe、宏、高级优化");
                println!("  ⏰ 建议：深入源码，参与开源项目");
                println!("  🎯 目标：成为Rust高级开发者");
            }
            _ => {
                println!("  🏆 恭喜！你已经完成了Rust专家学习！");
                println!("  📖 建议：持续学习新特性，贡献社区");
                println!("  ⏰ 目标：成为Rust专家，帮助他人学习");
            }
        }
    }
    
    fn mark_chapter_complete(&mut self) {
        println!("✅ 标记章节为已完成");
        println!("请输入章节编号 (01-23):");
        
        let input = get_user_input();
        let chapter_id = input.trim();
        
        if let Some(chapter) = self.chapters.get_mut(chapter_id) {
            if chapter.completed {
                println!("⚠️ 章节 '{} - {}' 已经标记为完成", chapter_id, chapter.title);
            } else {
                chapter.completed = true;
                println!("🎉 恭喜！章节 '{} - {}' 已标记为完成！", chapter_id, chapter.title);
                
                // 给出鼓励和建议
                self.give_completion_feedback(chapter_id);
            }
        } else {
            println!("❌ 未找到章节编号: {}，请输入01-23之间的数字", chapter_id);
        }
    }
    
    fn give_completion_feedback(&self, chapter_id: &str) {
        let feedback = match chapter_id {
            "01" => "🎉 环境搭建完成！现在你可以开始编写Rust代码了！",
            "02" => "📚 基础语法掌握！变量、类型、函数是编程的基石！",
            "03" => "🔄 控制流学会！你的程序现在可以做决策和重复操作了！", 
            "04" => "🔒 所有权基础完成！这是Rust最重要的概念，干得好！",
            "05" => "🎯 所有权进阶！你现在理解了Rust安全性的核心机制！",
            "08" => "🛡️ 错误处理掌握！你的程序现在更加健壮了！",
            "09" => "🧬 泛型和特质！你已经可以写出灵活且类型安全的代码了！",
            "15" => "⚡ 并发编程！你掌握了Rust的杀手锏功能！",
            "18" => "🪄 宏编程！你已经理解了Rust元编程的强大能力！",
            "23" => "🏆 恭喜完成所有章节！你现在是真正的Rust专家了！",
            _ => "🌟 又完成一章！继续保持这个节奏！",
        };
        
        println!("{}", feedback);
        
        // 给出下一步学习建议
        if let Ok(next_num) = chapter_id.parse::<u32>() {
            if next_num < 23 {
                let next_chapter = format!("{:02}", next_num + 1);
                if let Some(next) = self.chapters.get(&next_chapter) {
                    println!("📖 下一章：{} - {}", next_chapter, next.title);
                }
            }
        }
    }
    
    fn add_note(&mut self) {
        println!("📓 添加学习笔记");
        println!("请输入你的笔记内容（回车结束）:");
        
        let note = get_user_input();
        if !note.trim().is_empty() {
            // 简单的时间戳
            let timestamp = std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .unwrap()
                .as_secs() % 86400; // 取一天内的秒数
            
            let hours = timestamp / 3600;
            let minutes = (timestamp % 3600) / 60;
            
            let formatted_note = format!("[{:02}:{:02}] {}", hours, minutes, note.trim());
            
            self.notes.push(formatted_note);
            println!("✅ 笔记已添加！");
        } else {
            println!("❌ 笔记内容不能为空");
        }
    }
    
    fn show_notes(&self) {
        println!("📖 学习笔记");
        println!("============");
        
        if self.notes.is_empty() {
            println!("📝 还没有任何笔记。");
            println!("开始记录你的学习心得、疑问和解决方案吧！");
            println!("好的学习笔记包括：");
            println!("  - 重要概念的理解");
            println!("  - 遇到的问题和解决方案");
            println!("  - 代码示例和技巧");
            println!("  - 学习心得和感悟");
            return;
        }
        
        println!("📝 你的学习笔记 ({} 条):", self.notes.len());
        for (index, note) in self.notes.iter().enumerate() {
            println!("{}. {}", index + 1, note);
        }
    }
    
    fn show_statistics(&self) {
        println!("📈 Rust学习统计报告");
        println!("=====================");
        
        let total_chapters = self.chapters.len();
        let completed_chapters = self.chapters.values()
            .filter(|ch| ch.completed)
            .count();
        let remaining_chapters = total_chapters - completed_chapters;
        
        // 按难度分组统计
        let mut difficulty_stats = HashMap::new();
        for chapter in self.chapters.values() {
            let counter = difficulty_stats.entry(chapter.difficulty).or_insert((0, 0));
            if chapter.completed {
                counter.0 += 1;
            } else {
                counter.1 += 1;
            }
        }
        
        println!("📊 学习进度总览:");
        println!("  ✅ 已完成: {} 章", completed_chapters);
        println!("  ⏳ 待学习: {} 章", remaining_chapters);
        println!("  📈 完成度: {:.1}%", 
                completed_chapters as f64 / total_chapters as f64 * 100.0);
        
        println!("\n📊 各难度等级进度:");
        for difficulty in 1..=5 {
            if let Some((completed, remaining)) = difficulty_stats.get(&difficulty) {
                let total = completed + remaining;
                let stars = "★".repeat(difficulty as usize);
                let percentage = if total > 0 { *completed as f64 / total as f64 * 100.0 } else { 0.0 };
                println!("  {} 难度: {}/{} ({:.1}%)", stars, completed, total, percentage);
            }
        }
        
        println!("\n📝 其他统计:");
        println!("  学习笔记: {} 条", self.notes.len());
        
        // 预估剩余学习时间
        if remaining_chapters > 0 {
            println!("\n⏰ 预估剩余学习时间:");
            println!("  按每周3章速度: {:.1} 周", remaining_chapters as f64 / 3.0);
            println!("  按每周2章速度: {:.1} 周", remaining_chapters as f64 / 2.0);
            println!("  按每周1章速度: {} 周", remaining_chapters);
            
            // 给出具体的学习建议
            match remaining_chapters {
                1..=5 => println!("  🎯 你即将完成学习！坚持到底！"),
                6..=10 => println!("  🚀 已经过半！继续保持这个节奏！"),
                11..=15 => println!("  📚 还有一段路要走，但你已经有了好基础！"),
                _ => println!("  🌱 学习之路刚开始，每一步都很重要！"),
            }
        } else {
            println!("\n🏆 恭喜！你已经完成了所有章节！");
            println!("  🚀 现在可以开始挑战更复杂的项目了！");
        }
    }
    
    fn show_learning_tips(&self) {
        println!("💡 Rust学习技巧和建议");
        println!("======================");
        
        println!("🎯 高效学习方法:");
        println!("  1. 📖 先理解概念，再看代码");
        println!("  2. ✍️ 手写所有示例代码，不要复制粘贴");
        println!("  3. 🔧 修改示例代码，观察编译器反应");
        println!("  4. 📝 记录学习笔记和疑问");
        println!("  5. 🔄 定期回顾之前学过的内容");
        
        println!("\n🚫 避免的学习误区:");
        println!("  1. ❌ 不要跳过章节，Rust概念相互依赖");
        println!("  2. ❌ 不要害怕编译错误，它们是学习的好伙伴");
        println!("  3. ❌ 不要只看不练，理论必须结合实践");
        println!("  4. ❌ 不要急于求成，理解比速度更重要");
        
        println!("\n🔥 突破学习瓶颈:");
        println!("  💪 所有权概念难？多画内存图，多做练习");
        println!("  💪 生命周期复杂？先理解概念，后掌握语法");
        println!("  💪 错误信息看不懂？仔细阅读，编译器很友好");
        println!("  💪 代码写不出来？从简单示例开始修改");
        
        println!("\n📚 推荐学习资源:");
        println!("  🌐 官方文档: https://doc.rust-lang.org/book/");
        println!("  💡 Rust by Example: https://doc.rust-lang.org/rust-by-example/");
        println!("  🎮 Rustlings练习: https://github.com/rust-lang/rustlings");
        println!("  🎥 视频教程: YouTube搜索'Rust programming'");
        
        println!("\n🤝 获得帮助的方法:");
        println!("  1. 🔍 仔细阅读编译器错误信息");
        println!("  2. 📖 查看官方文档和示例");
        println!("  3. 🌐 在Rust官方论坛提问");
        println!("  4. 💬 参加Rust学习群组讨论");
    }
}

fn print_menu() {
    println!("🦀 请选择操作:");
    println!("1. 📊 查看学习进度");
    println!("2. ✅ 标记章节完成");
    println!("3. 📓 添加学习笔记");
    println!("4. 📖 查看学习笔记");
    println!("5. 📈 查看详细统计");
    println!("6. 💡 学习技巧建议");
    println!("7. 👋 退出程序");
    print!("请输入选项 (1-7): ");
}

fn get_user_input() -> String {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("❌ 读取输入失败");
    input
}

// 这个学习跟踪器的特色：
// 
// 1. **进度可视化**：
//    - 进度条显示整体学习情况
//    - 章节列表显示详细状态
//    - 难度等级帮助规划学习强度
//
// 2. **学习指导**：  
//    - 根据进度给出个性化建议
//    - 提供学习方法和技巧
//    - 推荐学习资源
//
// 3. **记录功能**：
//    - 学习笔记记录
//    - 详细统计分析
//    - 时间估算和规划
//
// 使用建议：
// - 每完成一章就来标记一下
// - 遇到问题时记录笔记
// - 定期查看统计了解进度
// - 参考学习建议优化方法 