#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
游戏生成器 - 生成10000个HTML5游戏
"""

import os
import random
import subprocess
from typing import List, Dict

class GameGenerator:
    def __init__(self):
        self.games_dir = "games"
        self.game_templates = [
            self.generate_snake_game,
            self.generate_tetris_game,
            self.generate_2048_game,
            self.generate_puzzle_game,
            self.generate_matching_game,
            self.generate_card_game,
            self.generate_number_game,
            self.generate_reaction_game,
            self.generate_strategy_game,
            self.generate_platform_game,
            self.generate_racing_game,
            self.generate_shooting_game,
            self.generate_rpg_game,
            self.generate_quiz_game,
            self.generate_memory_game,
        ]
        
        self.colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD", "#98D8C8", "#F7DC6F", "#BB8FCE", "#85C1E9"]
        self.game_names = [
            "超级", "炫酷", "经典", "神奇", "终极", "无敌", "极速", "梦幻", "魔法", "传奇",
            "王者", "霸王", "英雄", "勇士", "冠军", "大师", "精英", "天才", "明星", "巨星"
        ]
        
    def generate_base_html(self, title: str, body_content: str, style_content: str, script_content: str) -> str:
        """生成基础HTML模板"""
        return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, {random.choice(self.colors)}, {random.choice(self.colors)});
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}
        
        .game-container {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            text-align: center;
            max-width: 800px;
            width: 100%;
        }}
        
        h1 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }}
        
        .btn {{
            background: linear-gradient(45deg, {random.choice(self.colors)}, {random.choice(self.colors)});
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 25px;
            cursor: pointer;
            margin: 10px;
            transition: transform 0.3s;
        }}
        
        .btn:hover {{
            transform: scale(1.05);
        }}
        
        .score {{
            font-size: 24px;
            font-weight: bold;
            margin: 20px 0;
            color: #333;
        }}
        
        {style_content}
    </style>
</head>
<body>
    <div class="game-container">
        <h1>{title}</h1>
        {body_content}
    </div>
    
    <script>
        {script_content}
    </script>
</body>
</html>"""

    def generate_snake_game(self, game_id: int) -> str:
        """生成贪吃蛇游戏"""
        title = f"{random.choice(self.game_names)}贪吃蛇 {game_id}"
        
        body_content = """
        <canvas id="gameCanvas" width="400" height="400"></canvas>
        <div class="score">得分: <span id="score">0</span></div>
        <button class="btn" onclick="startGame()">开始游戏</button>
        <button class="btn" onclick="resetGame()">重新开始</button>
        """
        
        style_content = """
        #gameCanvas {
            border: 3px solid #333;
            background: #000;
            margin: 20px 0;
        }
        """
        
        script_content = f"""
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const gridSize = 20;
        const tileCount = canvas.width / gridSize;
        
        let snake = [{{x: 10, y: 10}}];
        let food = {{x: 15, y: 15}};
        let dx = 0;
        let dy = 0;
        let score = 0;
        let gameRunning = false;
        
        function drawGame() {{
            clearCanvas();
            drawSnake();
            drawFood();
            moveSnake();
            checkCollision();
            updateScore();
        }}
        
        function clearCanvas() {{
            ctx.fillStyle = '{random.choice(self.colors)}';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }}
        
        function drawSnake() {{
            ctx.fillStyle = 'lime';
            for (let segment of snake) {{
                ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize - 2, gridSize - 2);
            }}
        }}
        
        function drawFood() {{
            ctx.fillStyle = 'red';
            ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
        }}
        
        function moveSnake() {{
            const head = {{x: snake[0].x + dx, y: snake[0].y + dy}};
            snake.unshift(head);
            
            if (head.x === food.x && head.y === food.y) {{
                score += 10;
                generateFood();
            }} else {{
                snake.pop();
            }}
        }}
        
        function generateFood() {{
            food = {{
                x: Math.floor(Math.random() * tileCount),
                y: Math.floor(Math.random() * tileCount)
            }};
        }}
        
        function checkCollision() {{
            const head = snake[0];
            
            if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {{
                gameOver();
            }}
            
            for (let i = 1; i < snake.length; i++) {{
                if (head.x === snake[i].x && head.y === snake[i].y) {{
                    gameOver();
                }}
            }}
        }}
        
        function gameOver() {{
            gameRunning = false;
            alert('游戏结束！得分: ' + score);
        }}
        
        function updateScore() {{
            document.getElementById('score').textContent = score;
        }}
        
        function startGame() {{
            if (!gameRunning) {{
                gameRunning = true;
                gameLoop();
            }}
        }}
        
        function resetGame() {{
            snake = [{{x: 10, y: 10}}];
            food = {{x: 15, y: 15}};
            dx = 0;
            dy = 0;
            score = 0;
            gameRunning = false;
            updateScore();
            clearCanvas();
            drawSnake();
            drawFood();
        }}
        
        function gameLoop() {{
            if (gameRunning) {{
                drawGame();
                setTimeout(gameLoop, {random.randint(100, 300)});
            }}
        }}
        
        document.addEventListener('keydown', function(e) {{
            if (!gameRunning) return;
            
            switch(e.code) {{
                case 'ArrowUp':
                    if (dy !== 1) {{ dx = 0; dy = -1; }}
                    break;
                case 'ArrowDown':
                    if (dy !== -1) {{ dx = 0; dy = 1; }}
                    break;
                case 'ArrowLeft':
                    if (dx !== 1) {{ dx = -1; dy = 0; }}
                    break;
                case 'ArrowRight':
                    if (dx !== -1) {{ dx = 1; dy = 0; }}
                    break;
            }}
        }});
        
        resetGame();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_tetris_game(self, game_id: int) -> str:
        """生成俄罗斯方块游戏"""
        title = f"{random.choice(self.game_names)}俄罗斯方块 {game_id}"
        
        body_content = """
        <canvas id="gameCanvas" width="320" height="640"></canvas>
        <div class="score">得分: <span id="score">0</span></div>
        <div class="score">级别: <span id="level">1</span></div>
        <button class="btn" onclick="startGame()">开始游戏</button>
        <button class="btn" onclick="pauseGame()">暂停</button>
        """
        
        style_content = """
        #gameCanvas {
            border: 3px solid #333;
            background: #000;
            margin: 20px 0;
        }
        """
        
        script_content = f"""
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const ROWS = 20;
        const COLS = 10;
        const BLOCK_SIZE = 32;
        
        let board = Array(ROWS).fill().map(() => Array(COLS).fill(0));
        let score = 0;
        let level = 1;
        let gameRunning = false;
        let currentPiece = null;
        
        const PIECES = [
            [[[1,1,1,1]]], // I
            [[[1,1],[1,1]]], // O
            [[[0,1,0],[1,1,1]]], // T
            [[[0,1,1],[1,1,0]]], // S
            [[[1,1,0],[0,1,1]]], // Z
            [[[1,0,0],[1,1,1]]], // J
            [[[0,0,1],[1,1,1]]]  // L
        ];
        
        const COLORS = ['{random.choice(self.colors)}', '{random.choice(self.colors)}', '{random.choice(self.colors)}', '{random.choice(self.colors)}', '{random.choice(self.colors)}', '{random.choice(self.colors)}', '{random.choice(self.colors)}'];
        
        class Piece {{
            constructor() {{
                this.shape = PIECES[Math.floor(Math.random() * PIECES.length)][0];
                this.color = COLORS[Math.floor(Math.random() * COLORS.length)];
                this.x = Math.floor(COLS / 2) - Math.floor(this.shape[0].length / 2);
                this.y = 0;
            }}
            
            draw() {{
                ctx.fillStyle = this.color;
                for (let row = 0; row < this.shape.length; row++) {{
                    for (let col = 0; col < this.shape[row].length; col++) {{
                        if (this.shape[row][col]) {{
                            ctx.fillRect(
                                (this.x + col) * BLOCK_SIZE,
                                (this.y + row) * BLOCK_SIZE,
                                BLOCK_SIZE - 1,
                                BLOCK_SIZE - 1
                            );
                        }}
                    }}
                }}
            }}
            
            canMove(dx, dy) {{
                for (let row = 0; row < this.shape.length; row++) {{
                    for (let col = 0; col < this.shape[row].length; col++) {{
                        if (this.shape[row][col]) {{
                            const newX = this.x + col + dx;
                            const newY = this.y + row + dy;
                            
                            if (newX < 0 || newX >= COLS || newY >= ROWS) {{
                                return false;
                            }}
                            
                            if (newY >= 0 && board[newY][newX]) {{
                                return false;
                            }}
                        }}
                    }}
                }}
                return true;
            }}
            
            move(dx, dy) {{
                if (this.canMove(dx, dy)) {{
                    this.x += dx;
                    this.y += dy;
                    return true;
                }}
                return false;
            }}
            
            place() {{
                for (let row = 0; row < this.shape.length; row++) {{
                    for (let col = 0; col < this.shape[row].length; col++) {{
                        if (this.shape[row][col]) {{
                            board[this.y + row][this.x + col] = this.color;
                        }}
                    }}
                }}
            }}
        }}
        
        function drawBoard() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            for (let row = 0; row < ROWS; row++) {{
                for (let col = 0; col < COLS; col++) {{
                    if (board[row][col]) {{
                        ctx.fillStyle = board[row][col];
                        ctx.fillRect(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1);
                    }}
                }}
            }}
        }}
        
        function clearLines() {{
            let linesCleared = 0;
            for (let row = ROWS - 1; row >= 0; row--) {{
                if (board[row].every(cell => cell !== 0)) {{
                    board.splice(row, 1);
                    board.unshift(Array(COLS).fill(0));
                    linesCleared++;
                    row++; // Check the same row again
                }}
            }}
            
            if (linesCleared > 0) {{
                score += linesCleared * 100 * level;
                level = Math.floor(score / 1000) + 1;
                updateUI();
            }}
        }}
        
        function gameOver() {{
            gameRunning = false;
            alert('游戏结束！得分: ' + score);
        }}
        
        function updateUI() {{
            document.getElementById('score').textContent = score;
            document.getElementById('level').textContent = level;
        }}
        
        function gameLoop() {{
            if (!gameRunning) return;
            
            if (!currentPiece.move(0, 1)) {{
                currentPiece.place();
                clearLines();
                currentPiece = new Piece();
                
                if (!currentPiece.canMove(0, 0)) {{
                    gameOver();
                    return;
                }}
            }}
            
            drawBoard();
            currentPiece.draw();
            
            setTimeout(gameLoop, Math.max(50, 500 - level * 50));
        }}
        
        function startGame() {{
            if (!gameRunning) {{
                gameRunning = true;
                currentPiece = new Piece();
                gameLoop();
            }}
        }}
        
        function pauseGame() {{
            gameRunning = !gameRunning;
            if (gameRunning) {{
                gameLoop();
            }}
        }}
        
        document.addEventListener('keydown', function(e) {{
            if (!gameRunning || !currentPiece) return;
            
            switch(e.code) {{
                case 'ArrowLeft':
                    currentPiece.move(-1, 0);
                    break;
                case 'ArrowRight':
                    currentPiece.move(1, 0);
                    break;
                case 'ArrowDown':
                    currentPiece.move(0, 1);
                    break;
                case 'Space':
                    while (currentPiece.move(0, 1)) {{}}
                    break;
            }}
        }});
        
        updateUI();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_2048_game(self, game_id: int) -> str:
        """生成2048游戏"""
        title = f"{random.choice(self.game_names)}2048 {game_id}"
        
        body_content = """
        <div id="gameBoard"></div>
        <div class="score">得分: <span id="score">0</span></div>
        <button class="btn" onclick="newGame()">新游戏</button>
        """
        
        style_content = """
        #gameBoard {
            display: grid;
            grid-template-columns: repeat(4, 80px);
            grid-template-rows: repeat(4, 80px);
            gap: 10px;
            background-color: #bbada0;
            border-radius: 10px;
            padding: 10px;
            margin: 20px auto;
            width: fit-content;
        }
        
        .tile {
            width: 80px;
            height: 80px;
            background-color: #cdc1b4;
            border-radius: 5px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            font-weight: bold;
            color: #776e65;
        }
        
        .tile-2 { background-color: #eee4da; }
        .tile-4 { background-color: #ede0c8; }
        .tile-8 { background-color: #f2b179; color: white; }
        .tile-16 { background-color: #f59563; color: white; }
        .tile-32 { background-color: #f67c5f; color: white; }
        .tile-64 { background-color: #f65e3b; color: white; }
        .tile-128 { background-color: #edcf72; color: white; font-size: 20px; }
        .tile-256 { background-color: #edcc61; color: white; font-size: 20px; }
        .tile-512 { background-color: #edc850; color: white; font-size: 20px; }
        .tile-1024 { background-color: #edc53f; color: white; font-size: 18px; }
        .tile-2048 { background-color: #edc22e; color: white; font-size: 18px; }
        """
        
        script_content = f"""
        let board = [];
        let score = 0;
        
        function initGame() {{
            board = Array(4).fill().map(() => Array(4).fill(0));
            score = 0;
            addRandomTile();
            addRandomTile();
            updateDisplay();
        }}
        
        function addRandomTile() {{
            const emptyCells = [];
            for (let i = 0; i < 4; i++) {{
                for (let j = 0; j < 4; j++) {{
                    if (board[i][j] === 0) {{
                        emptyCells.push({{x: i, y: j}});
                    }}
                }}
            }}
            
            if (emptyCells.length > 0) {{
                const randomCell = emptyCells[Math.floor(Math.random() * emptyCells.length)];
                board[randomCell.x][randomCell.y] = Math.random() < 0.9 ? 2 : 4;
            }}
        }}
        
        function updateDisplay() {{
            const gameBoard = document.getElementById('gameBoard');
            gameBoard.innerHTML = '';
            
            for (let i = 0; i < 4; i++) {{
                for (let j = 0; j < 4; j++) {{
                    const tile = document.createElement('div');
                    tile.className = 'tile';
                    
                    if (board[i][j] !== 0) {{
                        tile.textContent = board[i][j];
                        tile.classList.add('tile-' + board[i][j]);
                    }}
                    
                    gameBoard.appendChild(tile);
                }}
            }}
            
            document.getElementById('score').textContent = score;
        }}
        
        function moveLeft() {{
            let moved = false;
            for (let i = 0; i < 4; i++) {{
                let row = board[i].filter(val => val !== 0);
                
                for (let j = 0; j < row.length - 1; j++) {{
                    if (row[j] === row[j + 1]) {{
                        row[j] *= 2;
                        score += row[j];
                        row[j + 1] = 0;
                    }}
                }}
                
                row = row.filter(val => val !== 0);
                while (row.length < 4) {{
                    row.push(0);
                }}
                
                for (let j = 0; j < 4; j++) {{
                    if (board[i][j] !== row[j]) {{
                        moved = true;
                    }}
                    board[i][j] = row[j];
                }}
            }}
            return moved;
        }}
        
        function moveRight() {{
            let moved = false;
            for (let i = 0; i < 4; i++) {{
                let row = board[i].filter(val => val !== 0);
                
                for (let j = row.length - 1; j > 0; j--) {{
                    if (row[j] === row[j - 1]) {{
                        row[j] *= 2;
                        score += row[j];
                        row[j - 1] = 0;
                    }}
                }}
                
                row = row.filter(val => val !== 0);
                while (row.length < 4) {{
                    row.unshift(0);
                }}
                
                for (let j = 0; j < 4; j++) {{
                    if (board[i][j] !== row[j]) {{
                        moved = true;
                    }}
                    board[i][j] = row[j];
                }}
            }}
            return moved;
        }}
        
        function moveUp() {{
            let moved = false;
            for (let j = 0; j < 4; j++) {{
                let column = [];
                for (let i = 0; i < 4; i++) {{
                    if (board[i][j] !== 0) {{
                        column.push(board[i][j]);
                    }}
                }}
                
                for (let i = 0; i < column.length - 1; i++) {{
                    if (column[i] === column[i + 1]) {{
                        column[i] *= 2;
                        score += column[i];
                        column[i + 1] = 0;
                    }}
                }}
                
                column = column.filter(val => val !== 0);
                while (column.length < 4) {{
                    column.push(0);
                }}
                
                for (let i = 0; i < 4; i++) {{
                    if (board[i][j] !== column[i]) {{
                        moved = true;
                    }}
                    board[i][j] = column[i];
                }}
            }}
            return moved;
        }}
        
        function moveDown() {{
            let moved = false;
            for (let j = 0; j < 4; j++) {{
                let column = [];
                for (let i = 0; i < 4; i++) {{
                    if (board[i][j] !== 0) {{
                        column.push(board[i][j]);
                    }}
                }}
                
                for (let i = column.length - 1; i > 0; i--) {{
                    if (column[i] === column[i - 1]) {{
                        column[i] *= 2;
                        score += column[i];
                        column[i - 1] = 0;
                    }}
                }}
                
                column = column.filter(val => val !== 0);
                while (column.length < 4) {{
                    column.unshift(0);
                }}
                
                for (let i = 0; i < 4; i++) {{
                    if (board[i][j] !== column[i]) {{
                        moved = true;
                    }}
                    board[i][j] = column[i];
                }}
            }}
            return moved;
        }}
        
        function isGameOver() {{
            // Check for empty cells
            for (let i = 0; i < 4; i++) {{
                for (let j = 0; j < 4; j++) {{
                    if (board[i][j] === 0) return false;
                }}
            }}
            
            // Check for possible merges
            for (let i = 0; i < 4; i++) {{
                for (let j = 0; j < 3; j++) {{
                    if (board[i][j] === board[i][j + 1] || board[j][i] === board[j + 1][i]) {{
                        return false;
                    }}
                }}
            }}
            
            return true;
        }}
        
        function checkWin() {{
            for (let i = 0; i < 4; i++) {{
                for (let j = 0; j < 4; j++) {{
                    if (board[i][j] === 2048) {{
                        alert('恭喜！你达到了2048！');
                        return true;
                    }}
                }}
            }}
            return false;
        }}
        
        function newGame() {{
            initGame();
        }}
        
        document.addEventListener('keydown', function(e) {{
            let moved = false;
            
            switch(e.code) {{
                case 'ArrowLeft':
                    moved = moveLeft();
                    break;
                case 'ArrowRight':
                    moved = moveRight();
                    break;
                case 'ArrowUp':
                    moved = moveUp();
                    break;
                case 'ArrowDown':
                    moved = moveDown();
                    break;
            }}
            
            if (moved) {{
                addRandomTile();
                updateDisplay();
                
                if (checkWin()) {{
                    return;
                }}
                
                if (isGameOver()) {{
                    alert('游戏结束！得分: ' + score);
                }}
            }}
        }});
        
        initGame();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_puzzle_game(self, game_id: int) -> str:
        """生成拼图游戏"""
        title = f"{random.choice(self.game_names)}拼图 {game_id}"
        size = random.choice([3, 4, 5])
        
        body_content = f"""
        <div id="puzzleGrid"></div>
        <div class="score">步数: <span id="moves">0</span></div>
        <button class="btn" onclick="shufflePuzzle()">打乱</button>
        <button class="btn" onclick="solvePuzzle()">解决</button>
        """
        
        style_content = f"""
        #puzzleGrid {{
            display: grid;
            grid-template-columns: repeat({size}, 80px);
            grid-template-rows: repeat({size}, 80px);
            gap: 2px;
            margin: 20px auto;
            width: fit-content;
            background-color: #333;
            padding: 10px;
            border-radius: 10px;
        }}
        
        .puzzle-tile {{
            width: 80px;
            height: 80px;
            background: linear-gradient(45deg, {random.choice(self.colors)}, {random.choice(self.colors)});
            border: none;
            border-radius: 5px;
            font-size: 24px;
            font-weight: bold;
            color: white;
            cursor: pointer;
            transition: all 0.3s;
        }}
        
        .puzzle-tile:hover {{
            transform: scale(1.05);
        }}
        
        .empty {{
            background: transparent !important;
        }}
        """
        
        script_content = f"""
        const SIZE = {size};
        let puzzle = [];
        let emptyPos = {{x: SIZE - 1, y: SIZE - 1}};
        let moves = 0;
        
        function initPuzzle() {{
            puzzle = [];
            for (let i = 0; i < SIZE; i++) {{
                puzzle[i] = [];
                for (let j = 0; j < SIZE; j++) {{
                    puzzle[i][j] = i * SIZE + j + 1;
                }}
            }}
            puzzle[SIZE - 1][SIZE - 1] = 0; // Empty space
            emptyPos = {{x: SIZE - 1, y: SIZE - 1}};
            moves = 0;
            updateDisplay();
        }}
        
        function updateDisplay() {{
            const grid = document.getElementById('puzzleGrid');
            grid.innerHTML = '';
            
            for (let i = 0; i < SIZE; i++) {{
                for (let j = 0; j < SIZE; j++) {{
                    const tile = document.createElement('button');
                    tile.className = 'puzzle-tile';
                    
                    if (puzzle[i][j] === 0) {{
                        tile.classList.add('empty');
                    }} else {{
                        tile.textContent = puzzle[i][j];
                        tile.onclick = () => moveTile(i, j);
                    }}
                    
                    grid.appendChild(tile);
                }}
            }}
            
            document.getElementById('moves').textContent = moves;
        }}
        
        function moveTile(x, y) {{
            const dx = Math.abs(x - emptyPos.x);
            const dy = Math.abs(y - emptyPos.y);
            
            if ((dx === 1 && dy === 0) || (dx === 0 && dy === 1)) {{
                puzzle[emptyPos.x][emptyPos.y] = puzzle[x][y];
                puzzle[x][y] = 0;
                emptyPos = {{x, y}};
                moves++;
                updateDisplay();
                
                if (isSolved()) {{
                    setTimeout(() => alert('恭喜！你完成了拼图！步数: ' + moves), 100);
                }}
            }}
        }}
        
        function isSolved() {{
            for (let i = 0; i < SIZE; i++) {{
                for (let j = 0; j < SIZE; j++) {{
                    const expected = i * SIZE + j + 1;
                    if (i === SIZE - 1 && j === SIZE - 1) {{
                        if (puzzle[i][j] !== 0) return false;
                    }} else {{
                        if (puzzle[i][j] !== expected) return false;
                    }}
                }}
            }}
            return true;
        }}
        
        function shufflePuzzle() {{
            for (let i = 0; i < 1000; i++) {{
                const directions = [];
                if (emptyPos.x > 0) directions.push({{x: -1, y: 0}});
                if (emptyPos.x < SIZE - 1) directions.push({{x: 1, y: 0}});
                if (emptyPos.y > 0) directions.push({{x: 0, y: -1}});
                if (emptyPos.y < SIZE - 1) directions.push({{x: 0, y: 1}});
                
                const dir = directions[Math.floor(Math.random() * directions.length)];
                const newX = emptyPos.x + dir.x;
                const newY = emptyPos.y + dir.y;
                
                puzzle[emptyPos.x][emptyPos.y] = puzzle[newX][newY];
                puzzle[newX][newY] = 0;
                emptyPos = {{x: newX, y: newY}};
            }}
            moves = 0;
            updateDisplay();
        }}
        
        function solvePuzzle() {{
            initPuzzle();
        }}
        
        initPuzzle();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_matching_game(self, game_id: int) -> str:
        """生成消除游戏"""
        title = f"{random.choice(self.game_names)}消除 {game_id}"
        
        body_content = """
        <canvas id="gameCanvas" width="480" height="640"></canvas>
        <div class="score">得分: <span id="score">0</span></div>
        <div class="score">消除: <span id="eliminated">0</span></div>
        <button class="btn" onclick="startGame()">开始游戏</button>
        """
        
        style_content = """
        #gameCanvas {
            border: 3px solid #333;
            margin: 20px 0;
            cursor: pointer;
        }
        """
        
        script_content = f"""
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const ROWS = 10;
        const COLS = 8;
        const CELL_SIZE = 60;
        const COLORS = ['{random.choice(self.colors)}', '{random.choice(self.colors)}', '{random.choice(self.colors)}', '{random.choice(self.colors)}', '{random.choice(self.colors)}', '{random.choice(self.colors)}'];
        
        let board = [];
        let score = 0;
        let eliminated = 0;
        let selectedCell = null;
        
        function initGame() {{
            board = [];
            for (let i = 0; i < ROWS; i++) {{
                board[i] = [];
                for (let j = 0; j < COLS; j++) {{
                    board[i][j] = Math.floor(Math.random() * COLORS.length);
                }}
            }}
            score = 0;
            eliminated = 0;
            selectedCell = null;
            updateDisplay();
        }}
        
        function drawBoard() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            for (let i = 0; i < ROWS; i++) {{
                for (let j = 0; j < COLS; j++) {{
                    const x = j * CELL_SIZE;
                    const y = i * CELL_SIZE;
                    
                    ctx.fillStyle = COLORS[board[i][j]];
                    ctx.fillRect(x, y, CELL_SIZE - 2, CELL_SIZE - 2);
                    
                    if (selectedCell && selectedCell.x === i && selectedCell.y === j) {{
                        ctx.strokeStyle = 'white';
                        ctx.lineWidth = 4;
                        ctx.strokeRect(x, y, CELL_SIZE - 2, CELL_SIZE - 2);
                    }}
                }}
            }}
        }}
        
        function updateDisplay() {{
            drawBoard();
            document.getElementById('score').textContent = score;
            document.getElementById('eliminated').textContent = eliminated;
        }}
        
        function findMatches() {{
            const matches = [];
            
            // Horizontal matches
            for (let i = 0; i < ROWS; i++) {{
                let count = 1;
                let color = board[i][0];
                for (let j = 1; j < COLS; j++) {{
                    if (board[i][j] === color) {{
                        count++;
                    }} else {{
                        if (count >= 3) {{
                            for (let k = j - count; k < j; k++) {{
                                matches.push({{x: i, y: k}});
                            }}
                        }}
                        count = 1;
                        color = board[i][j];
                    }}
                }}
                if (count >= 3) {{
                    for (let k = COLS - count; k < COLS; k++) {{
                        matches.push({{x: i, y: k}});
                    }}
                }}
            }}
            
            // Vertical matches
            for (let j = 0; j < COLS; j++) {{
                let count = 1;
                let color = board[0][j];
                for (let i = 1; i < ROWS; i++) {{
                    if (board[i][j] === color) {{
                        count++;
                    }} else {{
                        if (count >= 3) {{
                            for (let k = i - count; k < i; k++) {{
                                matches.push({{x: k, y: j}});
                            }}
                        }}
                        count = 1;
                        color = board[i][j];
                    }}
                }}
                if (count >= 3) {{
                    for (let k = ROWS - count; k < ROWS; k++) {{
                        matches.push({{x: k, y: j}});
                    }}
                }}
            }}
            
            return matches;
        }}
        
        function removeMatches(matches) {{
            for (let match of matches) {{
                board[match.x][match.y] = -1; // Mark for removal
            }}
            eliminated += matches.length;
            score += matches.length * 10;
        }}
        
        function dropPieces() {{
            for (let j = 0; j < COLS; j++) {{
                let writePos = ROWS - 1;
                for (let i = ROWS - 1; i >= 0; i--) {{
                    if (board[i][j] !== -1) {{
                        board[writePos][j] = board[i][j];
                        if (writePos !== i) {{
                            board[i][j] = -1;
                        }}
                        writePos--;
                    }}
                }}
                
                // Fill empty spaces with new pieces
                for (let i = writePos; i >= 0; i--) {{
                    board[i][j] = Math.floor(Math.random() * COLORS.length);
                }}
            }}
        }}
        
        function isAdjacent(cell1, cell2) {{
            const dx = Math.abs(cell1.x - cell2.x);
            const dy = Math.abs(cell1.y - cell2.y);
            return (dx === 1 && dy === 0) || (dx === 0 && dy === 1);
        }}
        
        function swapCells(cell1, cell2) {{
            const temp = board[cell1.x][cell1.y];
            board[cell1.x][cell1.y] = board[cell2.x][cell2.y];
            board[cell2.x][cell2.y] = temp;
        }}
        
        canvas.addEventListener('click', function(e) {{
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const col = Math.floor(x / CELL_SIZE);
            const row = Math.floor(y / CELL_SIZE);
            
            if (row >= 0 && row < ROWS && col >= 0 && col < COLS) {{
                const clickedCell = {{x: row, y: col}};
                
                if (!selectedCell) {{
                    selectedCell = clickedCell;
                }} else if (selectedCell.x === clickedCell.x && selectedCell.y === clickedCell.y) {{
                    selectedCell = null;
                }} else if (isAdjacent(selectedCell, clickedCell)) {{
                    swapCells(selectedCell, clickedCell);
                    
                    const matches = findMatches();
                    if (matches.length > 0) {{
                        removeMatches(matches);
                        dropPieces();
                        
                        // Continue removing matches until no more
                        let newMatches = findMatches();
                        while (newMatches.length > 0) {{
                            removeMatches(newMatches);
                            dropPieces();
                            newMatches = findMatches();
                        }}
                    }} else {{
                        // Swap back if no matches
                        swapCells(selectedCell, clickedCell);
                    }}
                    
                    selectedCell = null;
                }} else {{
                    selectedCell = clickedCell;
                }}
                
                updateDisplay();
            }}
        }});
        
        function startGame() {{
            initGame();
        }}
        
        initGame();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_card_game(self, game_id: int) -> str:
        """生成卡片游戏"""
        title = f"{random.choice(self.game_names)}纸牌 {game_id}"
        
        body_content = """
        <div id="gameArea">
            <div id="deck">
                <div class="card card-back" onclick="drawCard()">牌堆</div>
            </div>
            <div id="hand"></div>
            <div id="table"></div>
        </div>
        <div class="score">得分: <span id="score">0</span></div>
        <div class="score">剩余: <span id="remaining">52</span></div>
        <button class="btn" onclick="newGame()">新游戏</button>
        """
        
        style_content = """
        #gameArea {
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin: 20px 0;
        }
        
        #deck, #hand, #table {
            display: flex;
            gap: 10px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .card {
            width: 80px;
            height: 120px;
            border: 2px solid #333;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s;
            background: white;
        }
        
        .card:hover {
            transform: translateY(-10px);
        }
        
        .card-back {
            background: linear-gradient(45deg, #1e3c72, #2a5298);
            color: white;
        }
        
        .card-red {
            color: red;
        }
        
        .card-black {
            color: black;
        }
        """
        
        script_content = f"""
        const SUITS = ['♠', '♥', '♦', '♣'];
        const RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
        
        let deck = [];
        let hand = [];
        let table = [];
        let score = 0;
        
        function createDeck() {{
            deck = [];
            for (let suit of SUITS) {{
                for (let rank of RANKS) {{
                    deck.push({{
                        suit: suit,
                        rank: rank,
                        value: getRankValue(rank),
                        color: suit === '♥' || suit === '♦' ? 'red' : 'black'
                    }});
                }}
            }}
            shuffleDeck();
        }}
        
        function getRankValue(rank) {{
            if (rank === 'A') return 1;
            if (rank === 'J') return 11;
            if (rank === 'Q') return 12;
            if (rank === 'K') return 13;
            return parseInt(rank);
        }}
        
        function shuffleDeck() {{
            for (let i = deck.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [deck[i], deck[j]] = [deck[j], deck[i]];
            }}
        }}
        
        function drawCard() {{
            if (deck.length > 0) {{
                const card = deck.pop();
                hand.push(card);
                updateDisplay();
            }}
        }}
        
        function playCard(cardIndex) {{
            if (cardIndex >= 0 && cardIndex < hand.length) {{
                const card = hand.splice(cardIndex, 1)[0];
                table.push(card);
                score += card.value;
                updateDisplay();
                
                if (hand.length === 0 && deck.length === 0) {{
                    alert('游戏结束！最终得分: ' + score);
                }}
            }}
        }}
        
        function createCardElement(card, index, area) {{
            const cardEl = document.createElement('div');
            cardEl.className = `card card-${{card.color}}`;
            cardEl.textContent = card.rank + card.suit;
            
            if (area === 'hand') {{
                cardEl.onclick = () => playCard(index);
            }}
            
            return cardEl;
        }}
        
        function updateDisplay() {{
            // Update deck
            const deckEl = document.getElementById('deck');
            deckEl.innerHTML = '';
            if (deck.length > 0) {{
                const deckCard = document.createElement('div');
                deckCard.className = 'card card-back';
                deckCard.textContent = '牌堆';
                deckCard.onclick = drawCard;
                deckEl.appendChild(deckCard);
            }}
            
            // Update hand
            const handEl = document.getElementById('hand');
            handEl.innerHTML = '';
            hand.forEach((card, index) => {{
                handEl.appendChild(createCardElement(card, index, 'hand'));
            }});
            
            // Update table
            const tableEl = document.getElementById('table');
            tableEl.innerHTML = '';
            table.forEach((card, index) => {{
                tableEl.appendChild(createCardElement(card, index, 'table'));
            }});
            
            // Update stats
            document.getElementById('score').textContent = score;
            document.getElementById('remaining').textContent = deck.length;
        }}
        
        function newGame() {{
            createDeck();
            hand = [];
            table = [];
            score = 0;
            
            // Deal initial hand
            for (let i = 0; i < 5; i++) {{
                if (deck.length > 0) {{
                    hand.push(deck.pop());
                }}
            }}
            
            updateDisplay();
        }}
        
        newGame();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_number_game(self, game_id: int) -> str:
        """生成数字游戏"""
        title = f"{random.choice(self.game_names)}数字 {game_id}"
        
        body_content = """
        <div id="gameBoard"></div>
        <div class="score">目标: <span id="target">0</span></div>
        <div class="score">当前: <span id="current">0</span></div>
        <div class="score">步数: <span id="steps">0</span></div>
        <button class="btn" onclick="newGame()">新游戏</button>
        """
        
        style_content = """
        #gameBoard {
            display: grid;
            grid-template-columns: repeat(5, 80px);
            grid-template-rows: repeat(5, 80px);
            gap: 5px;
            margin: 20px auto;
            width: fit-content;
        }
        
        .number-tile {
            width: 80px;
            height: 80px;
            border: 2px solid #333;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            background: white;
        }
        
        .number-tile:hover {
            transform: scale(1.1);
        }
        
        .selected {
            background: #ffeb3b !important;
        }
        
        .correct {
            background: #4caf50 !important;
            color: white;
        }
        """
        
        script_content = f"""
        let board = [];
        let target = 0;
        let current = 0;
        let steps = 0;
        let selectedTiles = [];
        
        function initGame() {{
            board = [];
            for (let i = 0; i < 25; i++) {{
                board.push(Math.floor(Math.random() * 9) + 1);
            }}
            
            target = Math.floor(Math.random() * 50) + 10;
            current = 0;
            steps = 0;
            selectedTiles = [];
            updateDisplay();
        }}
        
        function updateDisplay() {{
            const gameBoard = document.getElementById('gameBoard');
            gameBoard.innerHTML = '';
            
            board.forEach((number, index) => {{
                const tile = document.createElement('div');
                tile.className = 'number-tile';
                tile.textContent = number;
                tile.onclick = () => selectTile(index);
                
                if (selectedTiles.includes(index)) {{
                    tile.classList.add('selected');
                }}
                
                gameBoard.appendChild(tile);
            }});
            
            document.getElementById('target').textContent = target;
            document.getElementById('current').textContent = current;
            document.getElementById('steps').textContent = steps;
        }}
        
        function selectTile(index) {{
            if (selectedTiles.includes(index)) {{
                // Deselect
                selectedTiles = selectedTiles.filter(i => i !== index);
                current -= board[index];
            }} else {{
                // Select
                selectedTiles.push(index);
                current += board[index];
            }}
            
            steps++;
            updateDisplay();
            
            if (current === target) {{
                setTimeout(() => {{
                    alert('恭喜！你达到了目标数字！步数: ' + steps);
                    markCorrect();
                }}, 100);
            }} else if (current > target) {{
                setTimeout(() => {{
                    alert('超过了目标数字！请重新选择。');
                    resetSelection();
                }}, 100);
            }}
        }}
        
        function markCorrect() {{
            selectedTiles.forEach(index => {{
                const tiles = document.querySelectorAll('.number-tile');
                tiles[index].classList.add('correct');
            }});
        }}
        
        function resetSelection() {{
            selectedTiles = [];
            current = 0;
            updateDisplay();
        }}
        
        function newGame() {{
            initGame();
        }}
        
        initGame();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_reaction_game(self, game_id: int) -> str:
        """生成反应游戏"""
        title = f"{random.choice(self.game_names)}反应 {game_id}"
        
        body_content = """
        <div id="gameArea">
            <div id="circle"></div>
            <div id="instructions">点击开始</div>
        </div>
        <div class="score">反应时间: <span id="reactionTime">-</span>ms</div>
        <div class="score">最佳时间: <span id="bestTime">-</span>ms</div>
        <button class="btn" onclick="startReactionTest()">开始测试</button>
        """
        
        style_content = """
        #gameArea {
            width: 400px;
            height: 400px;
            border: 3px solid #333;
            margin: 20px auto;
            position: relative;
            background: #f0f0f0;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        #circle {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: red;
            position: absolute;
            cursor: pointer;
            transition: all 0.3s;
            display: none;
        }
        
        #circle.green {
            background: #4caf50;
        }
        
        #instructions {
            font-size: 24px;
            font-weight: bold;
            color: #666;
        }
        """
        
        script_content = f"""
        let startTime = 0;
        let endTime = 0;
        let timeout = null;
        let gameActive = false;
        let bestTime = localStorage.getItem('bestReactionTime') || null;
        
        function updateDisplay() {{
            if (bestTime) {{
                document.getElementById('bestTime').textContent = bestTime;
            }}
        }}
        
        function startReactionTest() {{
            const circle = document.getElementById('circle');
            const instructions = document.getElementById('instructions');
            
            if (gameActive) return;
            
            // Reset
            circle.style.display = 'none';
            circle.classList.remove('green');
            instructions.textContent = '等待绿色圆圈...';
            gameActive = true;
            
            // Random delay between 1-5 seconds
            const delay = Math.random() * 4000 + 1000;
            
            timeout = setTimeout(() => {{
                showGreenCircle();
            }}, delay);
        }}
        
        function showGreenCircle() {{
            const circle = document.getElementById('circle');
            const instructions = document.getElementById('instructions');
            
            // Random position
            const gameArea = document.getElementById('gameArea');
            const areaRect = gameArea.getBoundingClientRect();
            const maxX = 300; // 400 - 100 (circle width)
            const maxY = 300; // 400 - 100 (circle height)
            
            const x = Math.random() * maxX;
            const y = Math.random() * maxY;
            
            circle.style.left = x + 'px';
            circle.style.top = y + 'px';
            circle.style.display = 'block';
            circle.classList.add('green');
            
            instructions.textContent = '点击绿色圆圈！';
            startTime = Date.now();
            
            circle.onclick = () => {{
                if (gameActive) {{
                    endTime = Date.now();
                    const reactionTime = endTime - startTime;
                    
                    document.getElementById('reactionTime').textContent = reactionTime;
                    
                    if (!bestTime || reactionTime < parseInt(bestTime)) {{
                        bestTime = reactionTime;
                        localStorage.setItem('bestReactionTime', bestTime);
                        instructions.textContent = '新纪录！反应时间: ' + reactionTime + 'ms';
                    }} else {{
                        instructions.textContent = '反应时间: ' + reactionTime + 'ms';
                    }}
                    
                    updateDisplay();
                    endGame();
                }}
            }};
            
            // Auto end after 3 seconds
            setTimeout(() => {{
                if (gameActive) {{
                    instructions.textContent = '太慢了！';
                    endGame();
                }}
            }}, 3000);
        }}
        
        function endGame() {{
            gameActive = false;
            const circle = document.getElementById('circle');
            circle.style.display = 'none';
            circle.onclick = null;
            
            if (timeout) {{
                clearTimeout(timeout);
                timeout = null;
            }}
        }}
        
        // Prevent early clicks
        document.getElementById('gameArea').addEventListener('click', function(e) {{
            if (gameActive && !e.target.id === 'circle') {{
                const instructions = document.getElementById('instructions');
                instructions.textContent = '太早了！重新开始';
                endGame();
            }}
        }});
        
        updateDisplay();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_strategy_game(self, game_id: int) -> str:
        """生成策略游戏"""
        title = f"{random.choice(self.game_names)}策略 {game_id}"
        
        body_content = """
        <div id="gameBoard"></div>
        <div class="score">玩家: <span id="playerScore">0</span></div>
        <div class="score">电脑: <span id="aiScore">0</span></div>
        <div id="currentPlayer">玩家回合</div>
        <button class="btn" onclick="newGame()">新游戏</button>
        """
        
        style_content = """
        #gameBoard {
            display: grid;
            grid-template-columns: repeat(8, 50px);
            grid-template-rows: repeat(8, 50px);
            gap: 2px;
            margin: 20px auto;
            width: fit-content;
            background: #333;
            padding: 10px;
            border-radius: 10px;
        }
        
        .cell {
            width: 50px;
            height: 50px;
            background: #4caf50;
            border-radius: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .cell:hover {
            background: #66bb6a;
        }
        
        .cell.player {
            background: #2196f3;
            color: white;
        }
        
        .cell.ai {
            background: #f44336;
            color: white;
        }
        
        .cell.possible {
            background: #ffeb3b;
        }
        
        #currentPlayer {
            font-size: 20px;
            font-weight: bold;
            margin: 20px 0;
            color: #333;
        }
        """
        
        script_content = f"""
        const BOARD_SIZE = 8;
        let board = [];
        let currentPlayer = 1; // 1 = player, 2 = AI
        let playerScore = 0;
        let aiScore = 0;
        let gameActive = true;
        
        function initGame() {{
            board = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(0));
            
            // Initial setup
            board[3][3] = 1;
            board[4][4] = 1;
            board[3][4] = 2;
            board[4][3] = 2;
            
            currentPlayer = 1;
            gameActive = true;
            updateScore();
            updateDisplay();
        }}
        
        function updateDisplay() {{
            const gameBoard = document.getElementById('gameBoard');
            gameBoard.innerHTML = '';
            
            for (let i = 0; i < BOARD_SIZE; i++) {{
                for (let j = 0; j < BOARD_SIZE; j++) {{
                    const cell = document.createElement('div');
                    cell.className = 'cell';
                    
                    if (board[i][j] === 1) {{
                        cell.classList.add('player');
                        cell.textContent = '●';
                    }} else if (board[i][j] === 2) {{
                        cell.classList.add('ai');
                        cell.textContent = '●';
                    }} else if (isValidMove(i, j, currentPlayer)) {{
                        cell.classList.add('possible');
                        cell.onclick = () => makeMove(i, j);
                    }}
                    
                    gameBoard.appendChild(cell);
                }}
            }}
            
            document.getElementById('currentPlayer').textContent = 
                currentPlayer === 1 ? '玩家回合' : 'AI回合';
            
            updateScore();
        }}
        
        function isValidMove(row, col, player) {{
            if (board[row][col] !== 0) return false;
            
            const directions = [
                [-1, -1], [-1, 0], [-1, 1],
                [0, -1],           [0, 1],
                [1, -1],  [1, 0],  [1, 1]
            ];
            
            for (let [dx, dy] of directions) {{
                if (canFlip(row, col, dx, dy, player)) {{
                    return true;
                }}
            }}
            
            return false;
        }}
        
        function canFlip(row, col, dx, dy, player) {{
            let x = row + dx;
            let y = col + dy;
            let hasOpponent = false;
            
            while (x >= 0 && x < BOARD_SIZE && y >= 0 && y < BOARD_SIZE) {{
                if (board[x][y] === 0) return false;
                if (board[x][y] === player) {{
                    return hasOpponent;
                }}
                hasOpponent = true;
                x += dx;
                y += dy;
            }}
            
            return false;
        }}
        
        function makeMove(row, col) {{
            if (!gameActive || !isValidMove(row, col, currentPlayer)) return;
            
            board[row][col] = currentPlayer;
            flipPieces(row, col, currentPlayer);
            
            currentPlayer = currentPlayer === 1 ? 2 : 1;
            
            if (!hasValidMoves(currentPlayer)) {{
                currentPlayer = currentPlayer === 1 ? 2 : 1;
                if (!hasValidMoves(currentPlayer)) {{
                    endGame();
                    return;
                }}
            }}
            
            updateDisplay();
            
            if (currentPlayer === 2 && gameActive) {{
                setTimeout(makeAIMove, 1000);
            }}
        }}
        
        function flipPieces(row, col, player) {{
            const directions = [
                [-1, -1], [-1, 0], [-1, 1],
                [0, -1],           [0, 1],
                [1, -1],  [1, 0],  [1, 1]
            ];
            
            for (let [dx, dy] of directions) {{
                if (canFlip(row, col, dx, dy, player)) {{
                    let x = row + dx;
                    let y = col + dy;
                    
                    while (board[x][y] !== player) {{
                        board[x][y] = player;
                        x += dx;
                        y += dy;
                    }}
                }}
            }}
        }}
        
        function hasValidMoves(player) {{
            for (let i = 0; i < BOARD_SIZE; i++) {{
                for (let j = 0; j < BOARD_SIZE; j++) {{
                    if (isValidMove(i, j, player)) {{
                        return true;
                    }}
                }}
            }}
            return false;
        }}
        
        function makeAIMove() {{
            if (!gameActive) return;
            
            const validMoves = [];
            for (let i = 0; i < BOARD_SIZE; i++) {{
                for (let j = 0; j < BOARD_SIZE; j++) {{
                    if (isValidMove(i, j, 2)) {{
                        validMoves.push({{row: i, col: j}});
                    }}
                }}
            }}
            
            if (validMoves.length > 0) {{
                const randomMove = validMoves[Math.floor(Math.random() * validMoves.length)];
                makeMove(randomMove.row, randomMove.col);
            }}
        }}
        
        function updateScore() {{
            playerScore = 0;
            aiScore = 0;
            
            for (let i = 0; i < BOARD_SIZE; i++) {{
                for (let j = 0; j < BOARD_SIZE; j++) {{
                    if (board[i][j] === 1) playerScore++;
                    else if (board[i][j] === 2) aiScore++;
                }}
            }}
            
            document.getElementById('playerScore').textContent = playerScore;
            document.getElementById('aiScore').textContent = aiScore;
        }}
        
        function endGame() {{
            gameActive = false;
            let message = '游戏结束！\\n';
            message += '玩家: ' + playerScore + '\\n';
            message += 'AI: ' + aiScore + '\\n';
            
            if (playerScore > aiScore) {{
                message += '玩家获胜！';
            }} else if (aiScore > playerScore) {{
                message += 'AI获胜！';
            }} else {{
                message += '平局！';
            }}
            
            alert(message);
        }}
        
        function newGame() {{
            initGame();
        }}
        
        initGame();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_platform_game(self, game_id: int) -> str:
        """生成平台游戏"""
        title = f"{random.choice(self.game_names)}跳跃 {game_id}"
        
        body_content = """
        <canvas id="gameCanvas" width="800" height="400"></canvas>
        <div class="score">得分: <span id="score">0</span></div>
        <div class="score">生命: <span id="lives">3</span></div>
        <button class="btn" onclick="startGame()">开始游戏</button>
        <div style="margin-top: 10px; font-size: 14px;">
            使用方向键移动和跳跃
        </div>
        """
        
        style_content = """
        #gameCanvas {
            border: 3px solid #333;
            background: linear-gradient(to bottom, #87CEEB, #98FB98);
            margin: 20px 0;
        }
        """
        
        script_content = f"""
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        let player = {{
            x: 50,
            y: 300,
            width: 30,
            height: 30,
            vx: 0,
            vy: 0,
            onGround: false,
            color: '{random.choice(self.colors)}'
        }};
        
        let platforms = [
            {{x: 0, y: 350, width: 200, height: 50}},
            {{x: 300, y: 300, width: 150, height: 20}},
            {{x: 550, y: 250, width: 150, height: 20}},
            {{x: 200, y: 200, width: 100, height: 20}},
            {{x: 400, y: 150, width: 200, height: 20}},
            {{x: 700, y: 100, width: 100, height: 20}}
        ];
        
        let coins = [
            {{x: 350, y: 270, collected: false}},
            {{x: 600, y: 220, collected: false}},
            {{x: 230, y: 170, collected: false}},
            {{x: 500, y: 120, collected: false}},
            {{x: 750, y: 70, collected: false}}
        ];
        
        let enemies = [
            {{x: 320, y: 280, vx: 1, color: '#ff4444'}},
            {{x: 570, y: 230, vx: -1, color: '#ff4444'}}
        ];
        
        let score = 0;
        let lives = 3;
        let gameRunning = false;
        let keys = {{}};
        
        function gameLoop() {{
            if (!gameRunning) return;
            
            update();
            draw();
            requestAnimationFrame(gameLoop);
        }}
        
        function update() {{
            // Player movement
            if (keys['ArrowLeft']) {{
                player.vx = -5;
            }} else if (keys['ArrowRight']) {{
                player.vx = 5;
            }} else {{
                player.vx *= 0.8; // Friction
            }}
            
            if (keys['ArrowUp'] && player.onGround) {{
                player.vy = -15;
                player.onGround = false;
            }}
            
            // Gravity
            player.vy += 0.8;
            
            // Update position
            player.x += player.vx;
            player.y += player.vy;
            
            // Platform collision
            player.onGround = false;
            for (let platform of platforms) {{
                if (player.x < platform.x + platform.width &&
                    player.x + player.width > platform.x &&
                    player.y < platform.y + platform.height &&
                    player.y + player.height > platform.y) {{
                    
                    if (player.vy > 0) {{ // Falling
                        player.y = platform.y - player.height;
                        player.vy = 0;
                        player.onGround = true;
                    }}
                }}
            }}
            
            // Boundaries
            if (player.x < 0) player.x = 0;
            if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;
            
            // Fall off screen
            if (player.y > canvas.height) {{
                lives--;
                if (lives <= 0) {{
                    gameOver();
                }} else {{
                    resetPlayer();
                }}
            }}
            
            // Coin collection
            for (let coin of coins) {{
                if (!coin.collected &&
                    player.x < coin.x + 20 &&
                    player.x + player.width > coin.x &&
                    player.y < coin.y + 20 &&
                    player.y + player.height > coin.y) {{
                    
                    coin.collected = true;
                    score += 100;
                }}
            }}
            
            // Enemy movement and collision
            for (let enemy of enemies) {{
                enemy.x += enemy.vx;
                
                // Enemy platform collision
                let onPlatform = false;
                for (let platform of platforms) {{
                    if (enemy.x + 15 > platform.x && 
                        enemy.x + 15 < platform.x + platform.width &&
                        enemy.y + 15 >= platform.y) {{
                        onPlatform = true;
                        break;
                    }}
                }}
                
                if (!onPlatform) {{
                    enemy.vx *= -1; // Turn around at edge
                }}
                
                // Player-enemy collision
                if (player.x < enemy.x + 15 &&
                    player.x + player.width > enemy.x &&
                    player.y < enemy.y + 15 &&
                    player.y + player.height > enemy.y) {{
                    
                    lives--;
                    if (lives <= 0) {{
                        gameOver();
                    }} else {{
                        resetPlayer();
                    }}
                }}
            }}
            
            updateUI();
        }}
        
        function draw() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Draw platforms
            ctx.fillStyle = '#8B4513';
            for (let platform of platforms) {{
                ctx.fillRect(platform.x, platform.y, platform.width, platform.height);
            }}
            
            // Draw player
            ctx.fillStyle = player.color;
            ctx.fillRect(player.x, player.y, player.width, player.height);
            
            // Draw coins
            ctx.fillStyle = '#FFD700';
            for (let coin of coins) {{
                if (!coin.collected) {{
                    ctx.beginPath();
                    ctx.arc(coin.x + 10, coin.y + 10, 10, 0, Math.PI * 2);
                    ctx.fill();
                }}
            }}
            
            // Draw enemies
            for (let enemy of enemies) {{
                ctx.fillStyle = enemy.color;
                ctx.fillRect(enemy.x, enemy.y, 15, 15);
            }}
        }}
        
        function resetPlayer() {{
            player.x = 50;
            player.y = 300;
            player.vx = 0;
            player.vy = 0;
        }}
        
        function updateUI() {{
            document.getElementById('score').textContent = score;
            document.getElementById('lives').textContent = lives;
        }}
        
        function gameOver() {{
            gameRunning = false;
            alert('游戏结束！得分: ' + score);
        }}
        
        function startGame() {{
            // Reset game state
            score = 0;
            lives = 3;
            gameRunning = true;
            
            // Reset coins
            for (let coin of coins) {{
                coin.collected = false;
            }}
            
            resetPlayer();
            updateUI();
            gameLoop();
        }}
        
        // Keyboard event listeners
        document.addEventListener('keydown', function(e) {{
            keys[e.code] = true;
        }});
        
        document.addEventListener('keyup', function(e) {{
            keys[e.code] = false;
        }});
        
        updateUI();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_racing_game(self, game_id: int) -> str:
        """生成赛车游戏"""
        title = f"{random.choice(self.game_names)}赛车 {game_id}"
        
        body_content = """
        <canvas id="gameCanvas" width="400" height="600"></canvas>
        <div class="score">得分: <span id="score">0</span></div>
        <div class="score">速度: <span id="speed">0</span></div>
        <button class="btn" onclick="startGame()">开始游戏</button>
        <div style="margin-top: 10px; font-size: 14px;">
            使用左右方向键控制
        </div>
        """
        
        style_content = """
        #gameCanvas {
            border: 3px solid #333;
            background: #666;
            margin: 20px 0;
        }
        """
        
        script_content = f"""
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        let player = {{
            x: canvas.width / 2 - 25,
            y: canvas.height - 100,
            width: 50,
            height: 80,
            speed: 5,
            color: '{random.choice(self.colors)}'
        }};
        
        let obstacles = [];
        let roadLines = [];
        let score = 0;
        let speed = 0;
        let gameRunning = false;
        let keys = {{}};
        
        function initGame() {{
            obstacles = [];
            roadLines = [];
            score = 0;
            speed = 0;
            
            // Initialize road lines
            for (let i = 0; i < 10; i++) {{
                roadLines.push({{
                    y: i * 80 - 400
                }});
            }}
        }}
        
        function gameLoop() {{
            if (!gameRunning) return;
            
            update();
            draw();
            requestAnimationFrame(gameLoop);
        }}
        
        function update() {{
            speed = Math.min(speed + 0.01, 10);
            score += Math.floor(speed);
            
            // Player movement
            if (keys['ArrowLeft'] && player.x > 50) {{
                player.x -= player.speed;
            }}
            if (keys['ArrowRight'] && player.x < canvas.width - 100) {{
                player.x += player.speed;
            }}
            
            // Update road lines
            for (let line of roadLines) {{
                line.y += speed * 2;
                if (line.y > canvas.height) {{
                    line.y -= 800;
                }}
            }}
            
            // Spawn obstacles
            if (Math.random() < 0.02 + speed * 0.001) {{
                obstacles.push({{
                    x: 50 + Math.random() * (canvas.width - 150),
                    y: -50,
                    width: 50,
                    height: 80,
                    color: '#' + Math.floor(Math.random()*16777215).toString(16)
                }});
            }}
            
            // Update obstacles
            for (let i = obstacles.length - 1; i >= 0; i--) {{
                obstacles[i].y += speed * 2;
                
                // Remove off-screen obstacles
                if (obstacles[i].y > canvas.height) {{
                    obstacles.splice(i, 1);
                    continue;
                }}
                
                // Collision detection
                if (player.x < obstacles[i].x + obstacles[i].width &&
                    player.x + player.width > obstacles[i].x &&
                    player.y < obstacles[i].y + obstacles[i].height &&
                    player.y + player.height > obstacles[i].y) {{
                    
                    gameOver();
                    return;
                }}
            }}
            
            updateUI();
        }}
        
        function draw() {{
            // Clear canvas
            ctx.fillStyle = '#333';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Draw road
            ctx.fillStyle = '#555';
            ctx.fillRect(50, 0, canvas.width - 100, canvas.height);
            
            // Draw road lines
            ctx.fillStyle = '#fff';
            for (let line of roadLines) {{
                ctx.fillRect(canvas.width / 2 - 2, line.y, 4, 40);
            }}
            
            // Draw road edges
            ctx.fillStyle = '#ffff00';
            ctx.fillRect(48, 0, 4, canvas.height);
            ctx.fillRect(canvas.width - 52, 0, 4, canvas.height);
            
            // Draw player car
            ctx.fillStyle = player.color;
            ctx.fillRect(player.x, player.y, player.width, player.height);
            
            // Draw player car details
            ctx.fillStyle = '#000';
            ctx.fillRect(player.x + 10, player.y + 10, 30, 20);
            ctx.fillRect(player.x + 10, player.y + 50, 30, 20);
            
            // Draw obstacles
            for (let obstacle of obstacles) {{
                ctx.fillStyle = obstacle.color;
                ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
                
                // Draw obstacle details
                ctx.fillStyle = '#000';
                ctx.fillRect(obstacle.x + 10, obstacle.y + 10, 30, 20);
                ctx.fillRect(obstacle.x + 10, obstacle.y + 50, 30, 20);
            }}
        }}
        
        function updateUI() {{
            document.getElementById('score').textContent = Math.floor(score);
            document.getElementById('speed').textContent = Math.floor(speed);
        }}
        
        function gameOver() {{
            gameRunning = false;
            alert('游戏结束！得分: ' + Math.floor(score));
        }}
        
        function startGame() {{
            initGame();
            gameRunning = true;
            gameLoop();
        }}
        
        // Keyboard event listeners
        document.addEventListener('keydown', function(e) {{
            keys[e.code] = true;
        }});
        
        document.addEventListener('keyup', function(e) {{
            keys[e.code] = false;
        }});
        
        updateUI();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_shooting_game(self, game_id: int) -> str:
        """生成射击游戏"""
        title = f"{random.choice(self.game_names)}射击 {game_id}"
        
        body_content = """
        <canvas id="gameCanvas" width="600" height="400"></canvas>
        <div class="score">得分: <span id="score">0</span></div>
        <div class="score">生命: <span id="lives">3</span></div>
        <button class="btn" onclick="startGame()">开始游戏</button>
        <div style="margin-top: 10px; font-size: 14px;">
            使用方向键移动，空格键射击
        </div>
        """
        
        style_content = """
        #gameCanvas {
            border: 3px solid #333;
            background: #000;
            margin: 20px 0;
        }
        """
        
        script_content = f"""
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        let player = {{
            x: canvas.width / 2,
            y: canvas.height - 50,
            width: 40,
            height: 30,
            speed: 5,
            color: '{random.choice(self.colors)}'
        }};
        
        let bullets = [];
        let enemies = [];
        let powerups = [];
        let score = 0;
        let lives = 3;
        let gameRunning = false;
        let keys = {{}};
        let lastShot = 0;
        
        function gameLoop() {{
            if (!gameRunning) return;
            
            update();
            draw();
            requestAnimationFrame(gameLoop);
        }}
        
        function update() {{
            const now = Date.now();
            
            // Player movement
            if (keys['ArrowLeft'] && player.x > 0) {{
                player.x -= player.speed;
            }}
            if (keys['ArrowRight'] && player.x < canvas.width - player.width) {{
                player.x += player.speed;
            }}
            if (keys['ArrowUp'] && player.y > 0) {{
                player.y -= player.speed;
            }}
            if (keys['ArrowDown'] && player.y < canvas.height - player.height) {{
                player.y += player.speed;
            }}
            
            // Shooting
            if (keys['Space'] && now - lastShot > 200) {{
                bullets.push({{
                    x: player.x + player.width / 2,
                    y: player.y,
                    width: 4,
                    height: 10,
                    speed: 8,
                    color: '#ffff00'
                }});
                lastShot = now;
            }}
            
            // Update bullets
            for (let i = bullets.length - 1; i >= 0; i--) {{
                bullets[i].y -= bullets[i].speed;
                if (bullets[i].y < 0) {{
                    bullets.splice(i, 1);
                }}
            }}
            
            // Spawn enemies
            if (Math.random() < 0.02) {{
                enemies.push({{
                    x: Math.random() * (canvas.width - 30),
                    y: -30,
                    width: 30,
                    height: 30,
                    speed: 2 + Math.random() * 3,
                    color: '#ff4444',
                    health: 1
                }});
            }}
            
            // Update enemies
            for (let i = enemies.length - 1; i >= 0; i--) {{
                enemies[i].y += enemies[i].speed;
                
                if (enemies[i].y > canvas.height) {{
                    enemies.splice(i, 1);
                    continue;
                }}
                
                // Enemy-player collision
                if (player.x < enemies[i].x + enemies[i].width &&
                    player.x + player.width > enemies[i].x &&
                    player.y < enemies[i].y + enemies[i].height &&
                    player.y + player.height > enemies[i].y) {{
                    
                    enemies.splice(i, 1);
                    lives--;
                    if (lives <= 0) {{
                        gameOver();
                        return;
                    }}
                }}
            }}
            
            // Bullet-enemy collision
            for (let i = bullets.length - 1; i >= 0; i--) {{
                for (let j = enemies.length - 1; j >= 0; j--) {{
                    if (bullets[i].x < enemies[j].x + enemies[j].width &&
                        bullets[i].x + bullets[i].width > enemies[j].x &&
                        bullets[i].y < enemies[j].y + enemies[j].height &&
                        bullets[i].y + bullets[i].height > enemies[j].y) {{
                        
                        enemies[j].health--;
                        bullets.splice(i, 1);
                        
                        if (enemies[j].health <= 0) {{
                            score += 100;
                            enemies.splice(j, 1);
                            
                            // Random powerup
                            if (Math.random() < 0.1) {{
                                powerups.push({{
                                    x: enemies[j] ? enemies[j].x : Math.random() * canvas.width,
                                    y: enemies[j] ? enemies[j].y : Math.random() * canvas.height,
                                    width: 20,
                                    height: 20,
                                    type: 'health',
                                    color: '#00ff00'
                                }});
                            }}
                        }}
                        break;
                    }}
                }}
            }}
            
            // Update powerups
            for (let i = powerups.length - 1; i >= 0; i--) {{
                powerups[i].y += 2;
                
                if (powerups[i].y > canvas.height) {{
                    powerups.splice(i, 1);
                    continue;
                }}
                
                // Powerup-player collision
                if (player.x < powerups[i].x + powerups[i].width &&
                    player.x + player.width > powerups[i].x &&
                    player.y < powerups[i].y + powerups[i].height &&
                    player.y + player.height > powerups[i].y) {{
                    
                    if (powerups[i].type === 'health') {{
                        lives = Math.min(lives + 1, 5);
                    }}
                    powerups.splice(i, 1);
                }}
            }}
            
            updateUI();
        }}
        
        function draw() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Draw stars background
            ctx.fillStyle = '#fff';
            for (let i = 0; i < 50; i++) {{
                const x = Math.random() * canvas.width;
                const y = Math.random() * canvas.height;
                ctx.fillRect(x, y, 1, 1);
            }}
            
            // Draw player
            ctx.fillStyle = player.color;
            ctx.fillRect(player.x, player.y, player.width, player.height);
            
            // Draw player details
            ctx.fillStyle = '#fff';
            ctx.fillRect(player.x + 18, player.y - 5, 4, 10);
            
            // Draw bullets
            for (let bullet of bullets) {{
                ctx.fillStyle = bullet.color;
                ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
            }}
            
            // Draw enemies
            for (let enemy of enemies) {{
                ctx.fillStyle = enemy.color;
                ctx.fillRect(enemy.x, enemy.y, enemy.width, enemy.height);
            }}
            
            // Draw powerups
            for (let powerup of powerups) {{
                ctx.fillStyle = powerup.color;
                ctx.fillRect(powerup.x, powerup.y, powerup.width, powerup.height);
                
                // Draw + sign for health
                if (powerup.type === 'health') {{
                    ctx.fillStyle = '#fff';
                    ctx.fillRect(powerup.x + 8, powerup.y + 5, 4, 10);
                    ctx.fillRect(powerup.x + 5, powerup.y + 8, 10, 4);
                }}
            }}
        }}
        
        function updateUI() {{
            document.getElementById('score').textContent = score;
            document.getElementById('lives').textContent = lives;
        }}
        
        function gameOver() {{
            gameRunning = false;
            alert('游戏结束！得分: ' + score);
        }}
        
        function startGame() {{
            bullets = [];
            enemies = [];
            powerups = [];
            score = 0;
            lives = 3;
            gameRunning = true;
            player.x = canvas.width / 2;
            player.y = canvas.height - 50;
            updateUI();
            gameLoop();
        }}
        
        // Keyboard event listeners
        document.addEventListener('keydown', function(e) {{
            keys[e.code] = true;
            e.preventDefault();
        }});
        
        document.addEventListener('keyup', function(e) {{
            keys[e.code] = false;
            e.preventDefault();
        }});
        
        updateUI();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_rpg_game(self, game_id: int) -> str:
        """生成RPG游戏"""
        title = f"{random.choice(self.game_names)}冒险 {game_id}"
        
        body_content = """
        <div id="gameArea">
            <div id="map"></div>
            <div id="character">
                <div class="stat">生命: <span id="hp">100</span>/100</div>
                <div class="stat">等级: <span id="level">1</span></div>
                <div class="stat">经验: <span id="exp">0</span>/100</div>
                <div class="stat">金币: <span id="gold">0</span></div>
            </div>
            <div id="actions">
                <button class="btn" onclick="explore()">探索</button>
                <button class="btn" onclick="rest()">休息</button>
                <button class="btn" onclick="shop()">商店</button>
            </div>
            <div id="log"></div>
        </div>
        """
        
        style_content = """
        #gameArea {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        #map {
            width: 300px;
            height: 200px;
            border: 2px solid #333;
            background: linear-gradient(45deg, #8FBC8F, #228B22);
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            border-radius: 10px;
        }
        
        #character {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            max-width: 300px;
            margin: 0 auto;
        }
        
        .stat {
            background: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            font-weight: bold;
        }
        
        #actions {
            display: flex;
            gap: 10px;
            justify-content: center;
        }
        
        #log {
            height: 150px;
            background: #f9f9f9;
            border: 2px solid #ccc;
            border-radius: 10px;
            padding: 10px;
            overflow-y: auto;
            font-family: monospace;
        }
        """
        
        script_content = f"""
        let player = {{
            hp: 100,
            maxHp: 100,
            level: 1,
            exp: 0,
            expToNext: 100,
            gold: 0,
            items: []
        }};
        
        let currentLocation = '森林';
        
        const locations = [
            '森林', '山洞', '河边', '村庄', '废墟', '神庙'
        ];
        
        const monsters = [
            {{name: '史莱姆', hp: 20, damage: 5, exp: 15, gold: 5}},
            {{name: '哥布林', hp: 35, damage: 8, exp: 25, gold: 10}},
            {{name: '骷髅', hp: 50, damage: 12, exp: 40, gold: 15}},
            {{name: '兽人', hp: 80, damage: 18, exp: 60, gold: 25}},
            {{name: '巨龙', hp: 200, damage: 35, exp: 150, gold: 100}}
        ];
        
        function updateDisplay() {{
            document.getElementById('hp').textContent = player.hp;
            document.getElementById('level').textContent = player.level;
            document.getElementById('exp').textContent = player.exp;
            document.getElementById('gold').textContent = player.gold;
            document.getElementById('map').textContent = currentLocation;
        }}
        
        function addLog(message) {{
            const log = document.getElementById('log');
            const div = document.createElement('div');
            div.textContent = message;
            log.appendChild(div);
            log.scrollTop = log.scrollHeight;
        }}
        
        function explore() {{
            if (player.hp <= 0) {{
                addLog('你已经死亡，无法探索！');
                return;
            }}
            
            const event = Math.random();
            
            if (event < 0.6) {{
                // 遇到怪物
                const monster = monsters[Math.floor(Math.random() * Math.min(monsters.length, player.level + 1))];
                battle(monster);
            }} else if (event < 0.8) {{
                // 找到金币
                const gold = Math.floor(Math.random() * 20) + 5;
                player.gold += gold;
                addLog(`你找到了 ${{gold}} 金币！`);
            }} else if (event < 0.9) {{
                // 找到经验
                const exp = Math.floor(Math.random() * 15) + 5;
                gainExp(exp);
                addLog(`你获得了 ${{exp}} 经验值！`);
            }} else {{
                // 移动到新地点
                currentLocation = locations[Math.floor(Math.random() * locations.length)];
                addLog(`你来到了 ${{currentLocation}}`);
            }}
            
            updateDisplay();
        }}
        
        function battle(monster) {{
            addLog(`遭遇 ${{monster.name}}！`);
            
            let monsterHp = monster.hp;
            
            while (monsterHp > 0 && player.hp > 0) {{
                // 玩家攻击
                const playerDamage = Math.floor(Math.random() * (player.level * 10)) + 5;
                monsterHp -= playerDamage;
                addLog(`你对 ${{monster.name}} 造成 ${{playerDamage}} 伤害`);
                
                if (monsterHp <= 0) {{
                    addLog(`${{monster.name}} 被击败！`);
                    gainExp(monster.exp);
                    player.gold += monster.gold;
                    addLog(`获得 ${{monster.exp}} 经验和 ${{monster.gold}} 金币`);
                    break;
                }}
                
                // 怪物攻击
                const monsterDamage = Math.floor(Math.random() * monster.damage) + 1;
                player.hp -= monsterDamage;
                addLog(`${{monster.name}} 对你造成 ${{monsterDamage}} 伤害`);
                
                if (player.hp <= 0) {{
                    player.hp = 0;
                    addLog('你被击败了！');
                    break;
                }}
            }}
        }}
        
        function gainExp(exp) {{
            player.exp += exp;
            
            while (player.exp >= player.expToNext) {{
                player.exp -= player.expToNext;
                player.level++;
                player.maxHp += 20;
                player.hp = player.maxHp; // 升级回满血
                player.expToNext = player.level * 100;
                addLog(`恭喜升级！现在是 ${{player.level}} 级！`);
            }}
        }}
        
        function rest() {{
            if (player.hp >= player.maxHp) {{
                addLog('你的生命值已满！');
                return;
            }}
            
            const heal = Math.floor(player.maxHp * 0.3);
            player.hp = Math.min(player.hp + heal, player.maxHp);
            addLog(`你休息了一会，恢复了 ${{heal}} 生命值`);
            updateDisplay();
        }}
        
        function shop() {{
            const items = [
                {{name: '生命药水', price: 50, effect: () => {{
                    const heal = 50;
                    player.hp = Math.min(player.hp + heal, player.maxHp);
                    addLog(`使用生命药水，恢复 ${{heal}} 生命值`);
                }}}},
                {{name: '经验药水', price: 100, effect: () => {{
                    gainExp(50);
                    addLog('使用经验药水，获得 50 经验值');
                }}}},
                {{name: '力量药水', price: 200, effect: () => {{
                    player.maxHp += 10;
                    addLog('使用力量药水，最大生命值增加 10');
                }}}}
            ];
            
            const item = items[Math.floor(Math.random() * items.length)];
            
            if (player.gold >= item.price) {{
                if (confirm(`购买 ${{item.name}} (${{item.price}} 金币)？`)) {{
                    player.gold -= item.price;
                    item.effect();
                    addLog(`购买了 ${{item.name}}`);
                    updateDisplay();
                }}
            }} else {{
                addLog(`金币不足，无法购买 ${{item.name}}`);
            }}
        }}
        
        // 初始化
        addLog('欢迎来到冒险世界！');
        addLog('点击探索开始你的冒险吧！');
        updateDisplay();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_quiz_game(self, game_id: int) -> str:
        """生成问答游戏"""
        title = f"{random.choice(self.game_names)}问答 {game_id}"
        
        body_content = """
        <div id="gameArea">
            <div id="questionArea">
                <div id="questionNumber">问题 1/10</div>
                <div id="question">点击开始游戏</div>
            </div>
            <div id="answers"></div>
            <div class="score">得分: <span id="score">0</span></div>
            <div class="score">时间: <span id="timer">30</span>秒</div>
            <button class="btn" onclick="startQuiz()">开始问答</button>
        </div>
        """
        
        style_content = """
        #gameArea {
            max-width: 600px;
            margin: 0 auto;
        }
        
        #questionArea {
            background: #f0f0f0;
            padding: 30px;
            border-radius: 15px;
            margin: 20px 0;
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        
        #questionNumber {
            font-size: 16px;
            color: #666;
            margin-bottom: 15px;
        }
        
        #question {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            text-align: center;
        }
        
        #answers {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 20px 0;
        }
        
        .answer-btn {
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
            border: none;
            padding: 20px;
            font-size: 18px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .answer-btn:hover {
            transform: scale(1.05);
        }
        
        .answer-btn.correct {
            background: linear-gradient(45deg, #4CAF50, #45a049);
        }
        
        .answer-btn.incorrect {
            background: linear-gradient(45deg, #f44336, #da190b);
        }
        """
        
        script_content = f"""
        const questions = [
            {{
                question: "中国的首都是哪里？",
                answers: ["北京", "上海", "广州", "深圳"],
                correct: 0
            }},
            {{
                question: "1 + 1 等于多少？",
                answers: ["1", "2", "3", "4"],
                correct: 1
            }},
            {{
                question: "地球有几个月亮？",
                answers: ["0个", "1个", "2个", "3个"],
                correct: 1
            }},
            {{
                question: "一年有多少天？",
                answers: ["364天", "365天", "366天", "367天"],
                correct: 1
            }},
            {{
                question: "太阳从哪个方向升起？",
                answers: ["东方", "西方", "南方", "北方"],
                correct: 0
            }},
            {{
                question: "水的化学符号是什么？",
                answers: ["H2O", "CO2", "O2", "N2"],
                correct: 0
            }},
            {{
                question: "中国最长的河流是什么？",
                answers: ["黄河", "长江", "珠江", "淮河"],
                correct: 1
            }},
            {{
                question: "一个小时有多少分钟？",
                answers: ["50分钟", "60分钟", "70分钟", "80分钟"],
                correct: 1
            }},
            {{
                question: "彩虹有几种颜色？",
                answers: ["5种", "6种", "7种", "8种"],
                correct: 2
            }},
            {{
                question: "人体最大的器官是什么？",
                answers: ["心脏", "肝脏", "肺", "皮肤"],
                correct: 3
            }}
        ];
        
        let currentQuestionIndex = 0;
        let score = 0;
        let timeLeft = 30;
        let timer = null;
        let gameActive = false;
        
        function shuffleArray(array) {{
            for (let i = array.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }}
        }}
        
        function startQuiz() {{
            if (gameActive) return;
            
            currentQuestionIndex = 0;
            score = 0;
            timeLeft = 30;
            gameActive = true;
            
            // 随机排列问题
            shuffleArray(questions);
            
            updateDisplay();
            showQuestion();
            startTimer();
        }}
        
        function showQuestion() {{
            if (currentQuestionIndex >= questions.length) {{
                endQuiz();
                return;
            }}
            
            const question = questions[currentQuestionIndex];
            
            document.getElementById('questionNumber').textContent = 
                `问题 ${{currentQuestionIndex + 1}}/${{questions.length}}`;
            document.getElementById('question').textContent = question.question;
            
            const answersDiv = document.getElementById('answers');
            answersDiv.innerHTML = '';
            
            question.answers.forEach((answer, index) => {{
                const btn = document.createElement('button');
                btn.className = 'answer-btn';
                btn.textContent = answer;
                btn.onclick = () => selectAnswer(index);
                answersDiv.appendChild(btn);
            }});
        }}
        
        function selectAnswer(selectedIndex) {{
            if (!gameActive) return;
            
            const question = questions[currentQuestionIndex];
            const buttons = document.querySelectorAll('.answer-btn');
            
            buttons.forEach((btn, index) => {{
                btn.onclick = null;
                if (index === question.correct) {{
                    btn.classList.add('correct');
                }} else if (index === selectedIndex) {{
                    btn.classList.add('incorrect');
                }}
            }});
            
            if (selectedIndex === question.correct) {{
                score += 10;
            }}
            
            updateDisplay();
            
            setTimeout(() => {{
                currentQuestionIndex++;
                showQuestion();
            }}, 1500);
        }}
        
        function startTimer() {{
            timer = setInterval(() => {{
                timeLeft--;
                document.getElementById('timer').textContent = timeLeft;
                
                if (timeLeft <= 0) {{
                    endQuiz();
                }}
            }}, 1000);
        }}
        
        function stopTimer() {{
            if (timer) {{
                clearInterval(timer);
                timer = null;
            }}
        }}
        
        function endQuiz() {{
            gameActive = false;
            stopTimer();
            
            document.getElementById('question').textContent = 
                `游戏结束！最终得分: ${{score}}/${{questions.length * 10}}`;
            document.getElementById('answers').innerHTML = '';
            
            let message = '游戏结束！\\n';
            message += `得分: ${{score}}/${{questions.length * 10}}\\n`;
            message += `正确率: ${{Math.round(score / (questions.length * 10) * 100)}}%`;
            
            alert(message);
        }}
        
        function updateDisplay() {{
            document.getElementById('score').textContent = score;
        }}
        
        updateDisplay();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def generate_memory_game(self, game_id: int) -> str:
        """生成记忆游戏"""
        title = f"{random.choice(self.game_names)}记忆 {game_id}"
        
        body_content = """
        <div id="gameBoard"></div>
        <div class="score">配对: <span id="pairs">0</span>/8</div>
        <div class="score">翻牌: <span id="flips">0</span></div>
        <button class="btn" onclick="newGame()">新游戏</button>
        """
        
        style_content = """
        #gameBoard {
            display: grid;
            grid-template-columns: repeat(4, 80px);
            grid-template-rows: repeat(4, 80px);
            gap: 10px;
            margin: 20px auto;
            width: fit-content;
        }
        
        .memory-card {
            width: 80px;
            height: 80px;
            border: 3px solid #333;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            cursor: pointer;
            background: #ddd;
            transition: all 0.6s;
            transform-style: preserve-3d;
        }
        
        .memory-card.flipped {
            transform: rotateY(180deg);
        }
        
        .memory-card.matched {
            background: #4caf50;
            color: white;
        }
        
        .card-front, .card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 7px;
        }
        
        .card-front {
            background: #666;
            color: white;
            transform: rotateY(180deg);
        }
        
        .card-back {
            background: #ddd;
        }
        """
        
        script_content = f"""
        const symbols = ['🌟', '🎈', '🎯', '🎨', '🎵', '🎲', '🎪', '🎭'];
        let cards = [];
        let flippedCards = [];
        let matchedPairs = 0;
        let flipCount = 0;
        let gameActive = true;
        
        function createCards() {{
            const gameCards = [...symbols, ...symbols]; // 创建成对的符号
            
            // 随机排列
            for (let i = gameCards.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [gameCards[i], gameCards[j]] = [gameCards[j], gameCards[i]];
            }}
            
            return gameCards.map((symbol, index) => ({{
                id: index,
                symbol: symbol,
                flipped: false,
                matched: false
            }}));
        }}
        
        function newGame() {{
            cards = createCards();
            flippedCards = [];
            matchedPairs = 0;
            flipCount = 0;
            gameActive = true;
            updateDisplay();
        }}
        
        function updateDisplay() {{
            const gameBoard = document.getElementById('gameBoard');
            gameBoard.innerHTML = '';
            
            cards.forEach(card => {{
                const cardElement = document.createElement('div');
                cardElement.className = 'memory-card';
                
                if (card.flipped || card.matched) {{
                    cardElement.classList.add('flipped');
                }}
                
                if (card.matched) {{
                    cardElement.classList.add('matched');
                }}
                
                cardElement.innerHTML = `
                    <div class="card-back">?</div>
                    <div class="card-front">${{card.symbol}}</div>
                `;
                
                cardElement.onclick = () => flipCard(card.id);
                gameBoard.appendChild(cardElement);
            }});
            
            document.getElementById('pairs').textContent = matchedPairs;
            document.getElementById('flips').textContent = flipCount;
        }}
        
        function flipCard(cardId) {{
            if (!gameActive) return;
            
            const card = cards[cardId];
            
            // 不能翻已经翻开或匹配的卡
            if (card.flipped || card.matched) return;
            
            // 不能翻超过2张卡
            if (flippedCards.length >= 2) return;
            
            card.flipped = true;
            flippedCards.push(card);
            flipCount++;
            
            updateDisplay();
            
            if (flippedCards.length === 2) {{
                gameActive = false;
                setTimeout(checkMatch, 1000);
            }}
        }}
        
        function checkMatch() {{
            const [card1, card2] = flippedCards;
            
            if (card1.symbol === card2.symbol) {{
                // 匹配成功
                card1.matched = true;
                card2.matched = true;
                matchedPairs++;
                
                if (matchedPairs === symbols.length) {{
                    setTimeout(() => {{
                        alert(`恭喜完成！总共翻牌 ${{flipCount}} 次`);
                    }}, 500);
                }}
            }} else {{
                // 匹配失败，翻回去
                card1.flipped = false;
                card2.flipped = false;
            }}
            
            flippedCards = [];
            gameActive = true;
            updateDisplay();
        }}
        
        newGame();
        """
        
        return self.generate_base_html(title, body_content, style_content, script_content)

    def commit_changes(self, start_index: int, end_index: int):
        """提交更改到git"""
        try:
            result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Git add failed: {result.stderr}")
                return False
                
            commit_message = f"Generated games {start_index}-{end_index}"
            result = subprocess.run(['git', 'commit', '-m', commit_message], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Git commit failed: {result.stderr}")
                return False
                
            print(f"Successfully committed games {start_index}-{end_index}")
            return True
        except Exception as e:
            print(f"Error committing changes: {e}")
            return False

    def generate_games(self, total_games: int = 10000, batch_size: int = 10):
        """生成指定数量的游戏文件"""
        print(f"开始生成 {total_games} 个游戏文件...")
        
        for i in range(0, total_games, batch_size):
            batch_start = i + 1
            batch_end = min(i + batch_size, total_games)
            
            print(f"生成第 {batch_start}-{batch_end} 个游戏...")
            
            # 生成这批游戏
            for game_id in range(batch_start, batch_end + 1):
                template_func = random.choice(self.game_templates)
                game_html = template_func(game_id)
                
                file_path = os.path.join(self.games_dir, f"{game_id}.html")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(game_html)
            
            # 每10个文件提交一次
            if self.commit_changes(batch_start, batch_end):
                print(f"✅ 已完成并提交第 {batch_start}-{batch_end} 个游戏")
            else:
                print(f"❌ 提交第 {batch_start}-{batch_end} 个游戏时出错")
            
            # 显示进度
            progress = (batch_end / total_games) * 100
            print(f"进度: {progress:.1f}% ({batch_end}/{total_games})")
        
        print(f"🎉 所有 {total_games} 个游戏生成完成！")

# 主程序
if __name__ == "__main__":
    generator = GameGenerator()
    generator.generate_games(10000, 10)