@echo off
chcp 65001 >nul

echo 🚀 启动 Rayneo AI Agent 应用...

REM 检查Docker是否安装
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker 未安装，请先安装 Docker Desktop
    pause
    exit /b 1
)

docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker Compose 未安装，请先安装 Docker Compose
    pause
    exit /b 1
)

REM 创建必要的目录
echo 📁 创建必要的目录...
if not exist "logs" mkdir logs
if not exist "uploads" mkdir uploads
if not exist "models" mkdir models
if not exist "static" mkdir static

REM 复制环境配置文件
if not exist ".env" (
    echo 📋 复制环境配置文件...
    copy ".env.example" ".env" >nul
    echo ⚠️  请编辑 .env 文件以配置您的环境变量
)

REM 启动服务
echo 🐳 启动 Docker 服务...
docker-compose up -d

REM 等待服务启动
echo ⏳ 等待服务启动...
timeout /t 10 /nobreak >nul

REM 检查服务状态
echo 🔍 检查服务状态...
docker-compose ps

echo.
echo ✅ Rayneo AI Agent 启动完成！
echo.
echo 📱 访问地址:
echo    前端应用: http://localhost:3000
echo    API文档:  http://localhost:8000/docs
echo    监控面板: http://localhost:3001 (Grafana)
echo.
echo 📝 日志查看:
echo    docker-compose logs -f backend
echo    docker-compose logs -f frontend
echo.
echo 🛑 停止服务:
echo    docker-compose down
echo.
pause
