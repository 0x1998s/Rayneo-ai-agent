#!/bin/bash

# Rayneo AI Agent 启动脚本

echo "🚀 启动 Rayneo AI Agent 应用..."

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose 未安装，请先安装 Docker Compose"
    exit 1
fi

# 创建必要的目录
echo "📁 创建必要的目录..."
mkdir -p logs uploads models static

# 复制环境配置文件
if [ ! -f .env ]; then
    echo "📋 复制环境配置文件..."
    cp .env.example .env
    echo "⚠️  请编辑 .env 文件以配置您的环境变量"
fi

# 启动服务
echo "🐳 启动 Docker 服务..."
docker-compose up -d

# 等待服务启动
echo "⏳ 等待服务启动..."
sleep 10

# 检查服务状态
echo "🔍 检查服务状态..."
docker-compose ps

echo ""
echo "✅ Rayneo AI Agent 启动完成！"
echo ""
echo "📱 访问地址:"
echo "   前端应用: http://localhost:3000"
echo "   API文档:  http://localhost:8000/docs"
echo "   监控面板: http://localhost:3001 (Grafana)"
echo ""
echo "📝 日志查看:"
echo "   docker-compose logs -f backend"
echo "   docker-compose logs -f frontend"
echo ""
echo "🛑 停止服务:"
echo "   docker-compose down"
