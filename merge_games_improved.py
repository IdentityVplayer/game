#!/usr/bin/env python3
"""
改进版：将所有游戏文件整合到一个index.html文件中
基于原始games数组中的file字段来查找游戏文件
"""
import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

def extract_games_array_from_original():
    """从原始的index.original.html中提取games数组"""
    with open('/workspace/index.original.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到games数组
    start_pattern = r'const games = \['
    end_pattern = r'\];'
    
    start_match = re.search(start_pattern, content)
    if not start_match:
        print("未找到games数组")
        return []
    
    start_pos = start_match.start()
    
    # 从开始位置向后查找结束位置
    brace_count = 0
    end_pos = start_pos
    in_games_array = False
    
    for i, char in enumerate(content[start_pos:]):
        if char == '[':
            in_games_array = True
            brace_count += 1
        elif char == ']' and in_games_array:
            brace_count -= 1
            if brace_count == 0:
                end_pos = start_pos + i + 1
                break
    
    games_text = content[start_pos:end_pos]
    
    # 解析games数组
    games = []
    lines = games_text.split('\n')
    current_game = {}
    
    for line in lines:
        line = line.strip()
        if line.startswith('{id:'):
            current_game = {}
            # 解析整行游戏定义
            # 使用正则表达式提取字段
            id_match = re.search(r'id: (\d+)', line)
            title_match = re.search(r'title: "([^"]*)"', line)
            file_match = re.search(r'file: "([^"]*)"', line)
            
            if id_match and title_match and file_match:
                current_game = {
                    'id': int(id_match.group(1)),
                    'title': title_match.group(1),
                    'file': file_match.group(1)
                }
                games.append(current_game)
    
    print(f"解析到 {len(games)} 个游戏")
    return games

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

def create_merged_html_improved():
    """创建改进的合并HTML文件"""
    print("开始创建改进的合并HTML文件...")
    
    # 从原始文件中提取games数组
    games_array = extract_games_array_from_original()
    
    # 读取原始index.html的内容作为基础
    with open('/workspace/index.original.html', 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    soup = BeautifulSoup(original_content, 'html.parser')
    
    # 收集所有游戏内容
    all_games_data = {}
    games_dir = Path('/workspace/games')
    
    print("正在读取游戏文件...")
    for game in games_array:
        game_id = game['id']
        game_file = game['file']
        game_title = game['title']
        
        # 查找游戏文件
        game_path = games_dir / game_file
        if game_path.exists():
            print(f"处理游戏 {game_id}: {game_file} ({game_title})")
            try:
                with open(game_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                all_games_data[game_id] = extract_game_content(content, game_id)
                all_games_data[game_id]['title'] = game_title  # 使用数组中的标题
            except Exception as e:
                print(f"处理游戏 {game_id} 时出错: {e}")
                all_games_data[game_id] = {
                    'title': game_title,
                    'css': "",
                    'html': f"<p>游戏 {game_id} ({game_title}) 加载失败</p>",
                    'js': ""
                }
        else:
            print(f"未找到游戏文件: {game_file} (游戏 {game_id}: {game_title})")
            all_games_data[game_id] = {
                'title': game_title,
                'css': "",
                'html': f"<p>游戏 {game_id} ({game_title}) 文件不存在</p>",
                'js': ""
            }
    
    # 创建新的HTML结构
    new_html = create_unified_html_structure_improved(soup, all_games_data)
    
    return new_html

def create_unified_html_structure_improved(original_soup, games_data):
    """创建改进的统一HTML结构"""
    
    # 获取原始样式和脚本
    original_styles = get_original_styles(original_soup)
    original_scripts = get_original_scripts(original_soup)
    original_body = get_original_body_content(original_soup)
    
    html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>7X7X-H5小游戏合集 - 完整单文件版</title>
    <style>
        /* === 原始样式 === */
        {original_styles}
        
        /* === 游戏容器样式 === */
        .game-overlay {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            z-index: 10000;
            backdrop-filter: blur(5px);
        }}
        
        .game-overlay.active {{
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .game-window {{
            width: 95%;
            height: 95%;
            max-width: 1200px;
            max-height: 900px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}
        
        .game-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 25px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px 15px 0 0;
        }}
        
        .game-title {{
            font-size: 1.5rem;
            font-weight: bold;
            margin: 0;
        }}
        
        .game-controls {{
            display: flex;
            gap: 10px;
        }}
        
        .game-btn {{
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s ease;
        }}
        
        .game-btn:hover {{
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }}
        
        .close-btn {{
            background: #e74c3c !important;
            border-color: #c0392b !important;
        }}
        
        .close-btn:hover {{
            background: #c0392b !important;
        }}
        
        .game-content {{
            flex: 1;
            overflow: auto;
            background: #f8f9fa;
        }}
        
        .game-iframe {{
            width: 100%;
            height: 100%;
            border: none;
            background: white;
        }}
        
        /* 响应式设计 */
        @media (max-width: 768px) {{
            .game-window {{
                width: 100%;
                height: 100%;
                max-width: none;
                max-height: none;
                border-radius: 0;
            }}
            
            .game-header {{
                padding: 10px 15px;
                border-radius: 0;
            }}
            
            .game-title {{
                font-size: 1.2rem;
            }}
            
            .game-btn {{
                padding: 6px 12px;
                font-size: 12px;
            }}
        }}
        
        /* === 游戏特定样式 === */
        {get_all_game_styles(games_data)}
    </style>
</head>
<body>
    <!-- === 原始主页面内容 === -->
    {original_body}
    
    <!-- === 游戏覆盖层 === -->
    <div id="game-overlay" class="game-overlay">
        <div class="game-window">
            <div class="game-header">
                <h2 id="current-game-title" class="game-title">游戏</h2>
                <div class="game-controls">
                    <button class="game-btn" onclick="restartCurrentGame()">重新开始</button>
                    <button class="game-btn" onclick="toggleFullscreen()">全屏</button>
                    <button class="game-btn close-btn" onclick="closeGame()">关闭</button>
                </div>
            </div>
            <div class="game-content" id="game-content">
                <!-- 游戏内容将在这里动态加载 -->
            </div>
        </div>
    </div>
    
    <script>
        /* === 原始JavaScript === */
        {original_scripts}
        
        /* === 游戏管理系统 === */
        let currentGameId = null;
        let currentGameData = null;
        
        // 游戏数据存储
        const gameContents = {{
            {generate_game_data_object(games_data)}
        }};
        
        function openGame(gameId) {{
            if (!gameContents[gameId]) {{
                alert('游戏 ' + gameId + ' 暂不可用');
                return;
            }}
            
            currentGameId = gameId;
            currentGameData = gameContents[gameId];
            
            // 更新游戏标题
            document.getElementById('current-game-title').textContent = currentGameData.title;
            
            // 加载游戏内容
            const gameContent = document.getElementById('game-content');
            gameContent.innerHTML = `
                <div id="game-container-${{gameId}}" style="width: 100%; height: 100%; position: relative;">
                    ${{currentGameData.html}}
                </div>
            `;
            
            // 显示游戏覆盖层
            document.getElementById('game-overlay').classList.add('active');
            document.body.style.overflow = 'hidden';
            
            // 执行游戏初始化
            setTimeout(() => {{
                initializeGame(gameId);
            }}, 100);
        }}
        
        function initializeGame(gameId) {{
            try {{
                // 执行游戏的JavaScript代码
                if (currentGameData && currentGameData.js) {{
                    // 创建一个函数来执行游戏代码
                    const gameFunction = new Function(currentGameData.js);
                    gameFunction();
                }}
            }} catch (e) {{
                console.error('游戏初始化错误:', e);
            }}
        }}
        
        function closeGame() {{
            if (currentGameId) {{
                // 清理当前游戏
                const gameContent = document.getElementById('game-content');
                gameContent.innerHTML = '';
                
                // 隐藏游戏覆盖层
                document.getElementById('game-overlay').classList.remove('active');
                document.body.style.overflow = '';
                
                currentGameId = null;
                currentGameData = null;
            }}
        }}
        
        function restartCurrentGame() {{
            if (currentGameId) {{
                const gameId = currentGameId;
                closeGame();
                setTimeout(() => {{
                    openGame(gameId);
                }}, 100);
            }}
        }}
        
        function toggleFullscreen() {{
            const gameOverlay = document.getElementById('game-overlay');
            if (!document.fullscreenElement) {{
                gameOverlay.requestFullscreen().catch(err => {{
                    console.log('无法进入全屏模式:', err);
                }});
            }} else {{
                document.exitFullscreen();
            }}
        }}
        
        // 修改原始的openGameInNewTab函数以使用新的游戏系统
        function openGameInNewTab(gameId) {{
            openGame(gameId);
        }}
        
        // ESC键关闭游戏
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape' && currentGameId) {{
                closeGame();
            }}
        }});
        
        // 防止游戏内容溢出
        document.addEventListener('click', function(e) {{
            if (e.target.id === 'game-overlay') {{
                // 点击覆盖层背景关闭游戏
                closeGame();
            }}
        }});
        
        console.log('🎮 游戏系统已加载，包含', Object.keys(gameContents).length, '个游戏');
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
        # 创建一个新的soup对象来处理body内容
        body_soup = BeautifulSoup(str(body), 'html.parser')
        
        # 移除所有script标签
        for script in body_soup.find_all('script'):
            script.decompose()
        
        # 返回body内容（不包括body标签本身）
        body_content = body_soup.find('body')
        if body_content:
            return body_content.decode_contents()
    return ""

def get_original_scripts(soup):
    """提取原始JavaScript"""
    scripts = ""
    script_tags = soup.find_all('script')
    for script in script_tags:
        content = script.get_text().strip()
        if content:
            scripts += content + "\n"
    return scripts

def get_all_game_styles(games_data):
    """获取所有游戏的CSS样式"""
    all_styles = ""
    for game_id, data in games_data.items():
        if data['css']:
            # 为游戏样式添加作用域前缀
            scoped_css = scope_css_for_game(data['css'], game_id)
            all_styles += f"\n/* === Game {game_id} ({data['title']}) Styles === */\n"
            all_styles += scoped_css + "\n"
    return all_styles

def scope_css_for_game(css, game_id):
    """为游戏CSS添加作用域"""
    lines = css.split('\n')
    scoped_lines = []
    
    for line in lines:
        line = line.strip()
        if line and not line.startswith('/*') and not line.startswith('*/') and '{' in line and not line.startswith('@'):
            # 这是一个CSS选择器
            selector_part = line.split('{')[0].strip()
            rest_part = '{' + line.split('{', 1)[1] if '{' in line else ''
            
            # 为每个选择器添加作用域
            selectors = [s.strip() for s in selector_part.split(',')]
            scoped_selectors = []
            for sel in selectors:
                if sel and not sel.startswith('@'):
                    scoped_selectors.append(f"#game-container-{game_id} {sel}")
                else:
                    scoped_selectors.append(sel)
            
            scoped_line = ', '.join(scoped_selectors) + rest_part
            scoped_lines.append(scoped_line)
        else:
            scoped_lines.append(line)
    
    return '\n'.join(scoped_lines)

def generate_game_data_object(games_data):
    """生成游戏数据JavaScript对象"""
    game_entries = []
    
    for game_id, data in games_data.items():
        # 转义JavaScript字符串
        title = data['title'].replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        html = data['html'].replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
        js = data['js'].replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
        
        entry = f"""    {game_id}: {{
        title: "{title}",
        html: `{html}`,
        js: `{js}`
    }}"""
        game_entries.append(entry)
    
    return ',\n'.join(game_entries)

def main():
    """主函数"""
    print("开始创建完整的单文件游戏平台...")
    
    try:
        # 确保备份文件存在
        if not os.path.exists('/workspace/index.original.html'):
            print("❌ 未找到原始备份文件 index.original.html")
            return
        
        merged_html = create_merged_html_improved()
        
        # 写入新的合并文件
        print("写入完整的合并HTML文件...")
        with open('/workspace/index.html', 'w', encoding='utf-8') as f:
            f.write(merged_html)
        
        print("✅ 完整合并完成！所有游戏已整合到单个index.html文件中。")
        print("原始文件已保存为 index.original.html")
        
        # 显示文件大小
        file_size = os.path.getsize('/workspace/index.html')
        print(f"📊 新文件大小: {file_size:,} 字节 ({file_size / 1024 / 1024:.2f} MB)")
        
    except Exception as e:
        print(f"❌ 合并过程中出现错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()