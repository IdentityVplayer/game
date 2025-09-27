#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
继续生成剩余游戏文件
"""

import os
import sys
sys.path.append('/workspace')
from generate_games import GameGenerator

def continue_generation():
    """继续生成剩余的游戏"""
    # 检查当前已生成的文件数量
    games_dir = "games"
    existing_files = len([f for f in os.listdir(games_dir) if f.endswith('.html')])
    
    print(f"当前已有 {existing_files} 个游戏文件")
    
    if existing_files >= 10000:
        print("✅ 已完成所有10000个游戏的生成！")
        return
    
    remaining = 10000 - existing_files
    print(f"还需要生成 {remaining} 个游戏文件")
    
    # 创建生成器实例
    generator = GameGenerator()
    
    # 从当前数量+1开始生成
    start_id = existing_files + 1
    batch_size = 10
    
    for i in range(start_id, 10001, batch_size):
        batch_start = i
        batch_end = min(i + batch_size - 1, 10000)
        
        print(f"生成第 {batch_start}-{batch_end} 个游戏...")
        
        # 生成这批游戏
        for game_id in range(batch_start, batch_end + 1):
            import random
            template_func = random.choice(generator.game_templates)
            game_html = template_func(game_id)
            
            file_path = os.path.join(games_dir, f"{game_id}.html")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(game_html)
        
        # 每10个文件提交一次
        if generator.commit_changes(batch_start, batch_end):
            print(f"✅ 已完成并提交第 {batch_start}-{batch_end} 个游戏")
        else:
            print(f"❌ 提交第 {batch_start}-{batch_end} 个游戏时出错")
        
        # 显示进度
        progress = (batch_end / 10000) * 100
        print(f"总进度: {progress:.1f}% ({batch_end}/10000)")
    
    print(f"🎉 所有 10000 个游戏生成完成！")

if __name__ == "__main__":
    continue_generation()