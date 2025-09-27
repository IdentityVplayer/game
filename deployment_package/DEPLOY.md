# 🚀 GitHub部署指南

## 快速部署到GitHub Pages

### 📋 准备工作
1. 确保已有GitHub账户
2. 下载或克隆本项目所有文件

### 🌟 方法一：GitHub网页界面（推荐新手）

#### 步骤1：创建仓库
1. 登录GitHub，点击右上角的 "+" → "New repository"
2. 仓库名建议设为：`game-collection` 或 `10000-games`
3. 设置为 **Public**（公开仓库才能使用免费的GitHub Pages）
4. 勾选 "Add a README file"
5. 点击 "Create repository"

#### 步骤2：上传文件
1. 在新建的仓库页面，点击 "uploading an existing file"
2. 将本项目的所有文件拖拽到上传区域，或点击选择文件
3. 确保上传以下文件：
   ```
   index.html
   README.md
   .gitignore
   deploy.sh
   games/snake.html
   games/tetris.html
   games/breakout.html
   games/2048.html
   games/flappy.html
   games/space_shooter.html
   games/puzzle.html
   games/memory.html
   games/racing.html
   games/platformer.html
   ```
4. 在页面底部填写提交信息：`🎮 第一批10款游戏上线`
5. 点击 "Commit changes"

#### 步骤3：启用GitHub Pages
1. 在仓库页面，点击 "Settings"（设置）标签
2. 在左侧菜单中找到 "Pages"
3. 在 "Source" 下拉菜单中选择 "Deploy from a branch"
4. 在 "Branch" 中选择 "main"
5. 在文件夹选择中保持 "/ (root)"
6. 点击 "Save"

#### 步骤4：等待部署
1. 页面会显示：`Your site is ready to be published at https://yourusername.github.io/repository-name`
2. 等待1-5分钟，GitHub会自动构建和部署
3. 点击链接即可访问你的游戏网站！

### 💻 方法二：命令行（适合开发者）

#### 前提条件
- 已安装Git
- 已配置GitHub账户

#### 步骤1：配置Git（如果未配置）
```bash
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱@example.com"
```

#### 步骤2：初始化并部署
```bash
# 进入项目目录
cd /path/to/game-collection

# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交文件
git commit -m "🎮 第一批10款游戏上线"

# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/yourusername/game-collection.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

#### 步骤3：启用Pages（同方法一的步骤3）

### 🎯 方法三：使用部署脚本

1. 给脚本执行权限：
```bash
chmod +x deploy.sh
```

2. 编辑脚本，修改仓库地址：
```bash
# 在deploy.sh中找到并修改这行
REPO_URL="https://github.com/yourusername/game-collection.git"
```

3. 运行脚本：
```bash
./deploy.sh
```

### ✅ 部署完成检查清单

- [ ] 网站可以正常访问
- [ ] 主页显示所有10个游戏
- [ ] 每个游戏都可以正常打开和运行
- [ ] 在手机上测试游戏是否正常运行
- [ ] 游戏分数可以正常保存

### 🌐 访问地址格式
```
https://yourusername.github.io/repository-name
```

例如：
- 用户名：gamedev123
- 仓库名：game-collection
- 访问地址：https://gamedev123.github.io/game-collection

### 🔧 常见问题解决

#### 问题1：404页面找不到
**原因**：Pages还未完成部署
**解决**：等待5-10分钟，或检查仓库是否为Public

#### 问题2：游戏页面空白
**原因**：文件路径错误
**解决**：确保games文件夹和所有HTML文件都已上传

#### 问题3：无法推送代码
**原因**：权限或网络问题
**解决**：
1. 检查仓库地址是否正确
2. 确认有仓库的写入权限
3. 尝试使用SSH而不是HTTPS

#### 问题4：Pages显示README而不是游戏
**原因**：未正确设置入口文件
**解决**：确保根目录有index.html文件

### 📱 自定义域名（可选）

如果你有自己的域名：

1. 在仓库根目录创建 `CNAME` 文件
2. 文件内容为你的域名，如：`games.yoursite.com`
3. 在域名服务商处添加CNAME记录指向：`yourusername.github.io`

### 🔄 更新游戏

添加新游戏时：
1. 在games文件夹中添加新的HTML文件
2. 在index.html中更新游戏列表
3. 提交并推送更改：
```bash
git add .
git commit -m "🎮 添加新游戏"
git push
```

### 📊 查看网站统计

可以集成以下服务查看访问统计：
- Google Analytics
- GitHub自带的Insights
- Cloudflare Analytics

---

🎉 **恭喜！你现在拥有了自己的在线游戏网站！**

分享地址给朋友们一起玩游戏吧！