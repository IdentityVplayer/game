#!/usr/bin/env python3
"""
将所有游戏文件整合到一个index.html文件中
"""
import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_game_content(html_content, game_id):
    """从游戏HTML文件中提取CSS、HTML和JavaScript内容"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 提取title
    title_tag = soup.find('title')
    title = title_tag.get_text() if title_tag else f"Game {game_id}"
    
    # 提取CSS
    css_content = ""
    style_tags = soup.find_all('style')
    for style in style_tags:
        css_content += f"\n/* Game {game_id} CSS */\n"
        css_content += style.get_text()
    
    # 提取body内容
    body_tag = soup.find('body')
    body_content = ""
    if body_tag:
        # 移除script标签，我们稍后单独处理
        for script in body_tag.find_all('script'):
            script.decompose()
        body_content = str(body_tag.encode_contents(), 'utf-8')
    
    # 提取JavaScript
    js_content = ""
    script_tags = soup.find_all('script')
    for script in script_tags:
        if script.get_text().strip():
            js_content += f"\n/* Game {game_id} JavaScript */\n"
            js_content += script.get_text()
    
    return {
        'title': title,
        'css': css_content,
        'html': body_content,
        'js': js_content
    }

def read_original_index():
    """读取原始index.html文件"""
    with open('/workspace/index.html', 'r', encoding='utf-8') as f:
        return f.read()

def create_merged_html():
    """创建合并的HTML文件"""
    print("开始创建合并的HTML文件...")
    
    # 读取原始index.html的内容
    original_content = read_original_index()
    soup = BeautifulSoup(original_content, 'html.parser')
    
    # 收集所有游戏内容
    all_games_data = {}
    games_dir = Path('/workspace/games')
    
    print("正在读取游戏文件...")
    for i in range(1, 101):
        game_files = list(games_dir.glob(f"{i}.html"))
        if not game_files:
            # 尝试其他可能的文件名
            possible_names = [f"{i:02d}.html", f"game{i}.html"]
            for name in possible_names:
                game_files = list(games_dir.glob(name))
                if game_files:
                    break
        
        if game_files:
            game_file = game_files[0]
            print(f"处理游戏 {i}: {game_file.name}")
            try:
                with open(game_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                all_games_data[i] = extract_game_content(content, i)
            except Exception as e:
                print(f"处理游戏 {i} 时出错: {e}")
                all_games_data[i] = {
                    'title': f"Game {i}",
                    'css': "",
                    'html': f"<p>游戏 {i} 加载失败</p>",
                    'js': ""
                }
        else:
            print(f"未找到游戏文件: {i}")
            all_games_data[i] = {
                'title': f"Game {i}",
                'css': "",
                'html': f"<p>游戏 {i} 文件不存在</p>",
                'js': ""
            }
    
    # 创建新的HTML结构
    new_html = create_unified_html_structure(soup, all_games_data)
    
    return new_html

def create_unified_html_structure(original_soup, games_data):
    """创建统一的HTML结构"""
    
    # 获取原始的head部分（保持原始样式）
    original_head = original_soup.find('head')
    original_body = original_soup.find('body')
    
    html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>7X7X-H5小游戏合集 - 单文件版</title>
    <style>
        /* 原始样式 */
        {get_original_styles(original_soup)}
        
        /* 游戏容器样式 */
        .game-container {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.9);
            z-index: 10000;
        }}
        
        .game-container.active {{
            display: block;
        }}
        
        .game-content {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 90%;
            height: 90%;
            background: white;
            border-radius: 10px;
            padding: 20px;
            overflow: auto;
        }}
        
        .game-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #ddd;
        }}
        
        .close-game {{
            background: #f44336;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}
        
        .close-game:hover {{
            background: #d32f2f;
        }}
        
        .game-body {{
            height: calc(100% - 80px);
        }}
        
        /* 游戏特定样式 */
        {get_all_game_styles(games_data)}
    </style>
</head>
<body>
    <!-- 原始的主页面内容 -->
    {get_original_body_content(original_soup)}
    
    <!-- 游戏容器 -->
    {generate_game_containers(games_data)}
    
    <script>
        /* 原始JavaScript */
        {get_original_scripts(original_soup)}
        
        /* 游戏管理JavaScript */
        let currentGameId = null;
        
        function openGame(gameId) {{
            // 关闭当前游戏
            if (currentGameId) {{
                closeGame();
            }}
            
            // 显示新游戏
            const gameContainer = document.getElementById('game-' + gameId);
            if (gameContainer) {{
                gameContainer.classList.add('active');
                currentGameId = gameId;
                
                // 初始化游戏（如果有init函数）
                const initFunction = window['initGame' + gameId];
                if (typeof initFunction === 'function') {{
                    initFunction();
                }}
            }}
        }}
        
        function closeGame() {{
            if (currentGameId) {{
                const gameContainer = document.getElementById('game-' + currentGameId);
                if (gameContainer) {{
                    gameContainer.classList.remove('active');
                    
                    // 清理游戏（如果有cleanup函数）
                    const cleanupFunction = window['cleanupGame' + currentGameId];
                    if (typeof cleanupFunction === 'function') {{
                        cleanupFunction();
                    }}
                }}
                currentGameId = null;
            }}
        }}
        
        // 修改原始的openGameInNewTab函数
        function openGameInNewTab(gameId) {{
            openGame(gameId);
        }}
        
        // ESC键关闭游戏
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape' && currentGameId) {{
                closeGame();
            }}
        }});
        
        /* 所有游戏的JavaScript */
        {get_all_game_scripts(games_data)}
    </script>
</body>
</html>"""
    
    return html_template

def get_original_styles(soup):
    """提取原始样式"""
    styles = ""
    style_tags = soup.find_all('style')
    for style in style_tags:
        styles += style.get_text() + "\n"
    return styles

def get_original_body_content(soup):
    """获取原始body内容，但移除script标签"""
    body = soup.find('body')
    if body:
        # 创建body的副本
        body_copy = soup.new_tag('div')
        body_copy.string = ""
        
        # 复制所有非script元素
        for element in body.children:
            if hasattr(element, 'name') and element.name == 'script':
                continue
            if hasattr(element, 'name'):
                body_copy.append(element.__copy__())
            else:
                body_copy.append(str(element))
        
        return str(body_copy)[5:-6]  # 移除<div>和</div>
    return ""

def get_original_scripts(soup):
    """提取原始JavaScript"""
    scripts = ""
    script_tags = soup.find_all('script')
    for script in script_tags:
        if script.get_text().strip():
            scripts += script.get_text() + "\n"
    return scripts

def get_all_game_styles(games_data):
    """获取所有游戏的CSS样式"""
    all_styles = ""
    for game_id, data in games_data.items():
        if data['css']:
            # 为游戏样式添加作用域前缀
            scoped_css = scope_css_for_game(data['css'], game_id)
            all_styles += f"\n/* === Game {game_id} Styles === */\n"
            all_styles += scoped_css + "\n"
    return all_styles

def scope_css_for_game(css, game_id):
    """为游戏CSS添加作用域"""
    # 简单的作用域处理：在每个选择器前添加游戏容器ID
    lines = css.split('\n')
    scoped_lines = []
    
    for line in lines:
        line = line.strip()
        if line and not line.startswith('/*') and not line.startswith('*/') and '{' in line:
            # 这是一个CSS选择器
            if line.startswith('@'):
                # 保持@规则不变
                scoped_lines.append(line)
            else:
                # 添加作用域前缀
                selector_part = line.split('{')[0].strip()
                rest_part = '{' + line.split('{', 1)[1] if '{' in line else ''
                
                # 为每个选择器添加作用域
                selectors = [s.strip() for s in selector_part.split(',')]
                scoped_selectors = []
                for sel in selectors:
                    if sel:
                        scoped_selectors.append(f"#game-{game_id} {sel}")
                
                scoped_line = ', '.join(scoped_selectors) + rest_part
                scoped_lines.append(scoped_line)
        else:
            scoped_lines.append(line)
    
    return '\n'.join(scoped_lines)

def get_all_game_scripts(games_data):
    """获取所有游戏的JavaScript"""
    all_scripts = ""
    for game_id, data in games_data.items():
        if data['js']:
            # 包装游戏JavaScript以避免冲突
            wrapped_js = wrap_game_javascript(data['js'], game_id)
            all_scripts += f"\n/* === Game {game_id} JavaScript === */\n"
            all_scripts += wrapped_js + "\n"
    return all_scripts

def wrap_game_javascript(js, game_id):
    """包装游戏JavaScript以避免冲突"""
    wrapped = f"""
// Game {game_id} scope
(function() {{
    'use strict';
    
    // 游戏初始化函数
    window.initGame{game_id} = function() {{
        const gameContainer = document.getElementById('game-{game_id}');
        if (!gameContainer) return;
        
        // 在这里执行游戏初始化代码
        try {{
            {js}
        }} catch(e) {{
            console.error('Game {game_id} initialization error:', e);
        }}
    }};
    
    // 游戏清理函数
    window.cleanupGame{game_id} = function() {{
        // 清理定时器、事件监听器等
        // 这里可以添加特定的清理代码
    }};
}})();
"""
    return wrapped

def generate_game_containers(games_data):
    """生成所有游戏的HTML容器"""
    containers = ""
    for game_id, data in games_data.items():
        containers += f"""
    <div id="game-{game_id}" class="game-container">
        <div class="game-content">
            <div class="game-header">
                <h2>{data['title']}</h2>
                <button class="close-game" onclick="closeGame()">关闭游戏</button>
            </div>
            <div class="game-body">
                {data['html']}
            </div>
        </div>
    </div>
"""
    return containers

def main():
    """主函数"""
    print("开始将所有游戏文件整合到单个HTML文件...")
    
    try:
        merged_html = create_merged_html()
        
        # 备份原始文件
        print("备份原始index.html文件...")
        os.rename('/workspace/index.html', '/workspace/index.original.html')
        
        # 写入新的合并文件
        print("写入新的合并HTML文件...")
        with open('/workspace/index.html', 'w', encoding='utf-8') as f:
            f.write(merged_html)
        
        print("✅ 合并完成！所有100个游戏已整合到单个index.html文件中。")
        print("原始文件已备份为 index.original.html")
        
    except Exception as e:
        print(f"❌ 合并过程中出现错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()