#!/bin/bash

# 🚀 GitHub Pages 一键部署脚本
# 10000款游戏大全项目部署工具

echo "🎮 开始部署10000款游戏大全..."

# 检查是否在git仓库中
if [ ! -d ".git" ]; then
    echo "📝 初始化Git仓库..."
    git init
    echo "✅ Git仓库初始化完成"
fi

# 添加所有文件
echo "📁 添加文件到Git..."
git add .

# 检查是否有改动
if git diff --staged --quiet; then
    echo "ℹ️  没有文件改动，跳过提交"
else
    # 提交改动
    echo "💾 提交改动..."
    git commit -m "🎮 游戏项目更新 - $(date '+%Y-%m-%d %H:%M:%S')"
    echo "✅ 文件提交完成"
fi

# 检查是否有远程仓库
if ! git remote get-url origin > /dev/null 2>&1; then
    echo ""
    echo "⚠️  未找到远程仓库地址"
    echo "请手动添加远程仓库："
    echo "git remote add origin https://github.com/yourusername/game-collection.git"
    echo ""
    echo "或者编辑此脚本，修改下面的仓库地址："
    echo "REPO_URL=\"https://github.com/yourusername/game-collection.git\""
    echo ""
    
    # 可以在这里设置默认仓库地址
    # REPO_URL="https://github.com/yourusername/game-collection.git"
    # echo "🔗 添加远程仓库..."
    # git remote add origin $REPO_URL
    # echo "✅ 远程仓库添加完成"
    
    exit 1
fi

# 设置主分支
echo "🌿 设置主分支..."
git branch -M main

# 推送到GitHub
echo "🚀 推送到GitHub..."
if git push -u origin main; then
    echo "✅ 推送成功！"
    echo ""
    echo "🎉 部署完成！"
    echo ""
    echo "📋 接下来的步骤："
    echo "1. 访问你的GitHub仓库"
    echo "2. 进入 Settings → Pages"
    echo "3. 选择 'Deploy from a branch'"
    echo "4. 选择 'main' 分支和 '/ (root)' 文件夹"
    echo "5. 点击保存，等待部署完成"
    echo ""
    echo "🌐 部署完成后，你的游戏网站将在以下地址可用："
    echo "https://yourusername.github.io/game-collection"
    echo ""
    echo "🎮 现在就可以分享你的10000款游戏网站了！"
else
    echo "❌ 推送失败"
    echo "请检查："
    echo "1. 网络连接是否正常"
    echo "2. GitHub仓库是否存在"
    echo "3. 是否有推送权限"
    echo ""
    echo "💡 如果是第一次推送，请确保："
    echo "1. 已创建GitHub仓库"
    echo "2. 已配置Git用户名和邮箱："
    echo "   git config --global user.name 'Your Name'"
    echo "   git config --global user.email 'your.email@example.com'"
    exit 1
fi