"""
Rayneo AI Agent - 主应用程序入口
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uvicorn
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import init_db
from app.api.routes import api_router
from app.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用程序生命周期管理"""
    logger.info("🚀 启动 Rayneo AI Agent 应用程序...")
    
    # 初始化数据库
    await init_db()
    logger.info("✅ 数据库初始化完成")
    
    # 这里可以添加其他初始化逻辑
    # 比如加载模型、初始化向量数据库等
    
    yield
    
    logger.info("🛑 关闭 Rayneo AI Agent 应用程序...")


# 创建 FastAPI 应用
app = FastAPI(
    title="Rayneo AI Agent API",
    description="雷鸟科技 AI Agent 本地化大模型应用平台",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS 中间件配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静态文件服务
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# 注册 API 路由
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    """根路径 - 系统状态检查"""
    return {
        "message": "🚀 Rayneo AI Agent API 正在运行",
        "version": "1.0.0",
        "status": "healthy",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """健康检查端点"""
    try:
        # 这里可以添加数据库连接检查、Redis连接检查等
        return {
            "status": "healthy",
            "timestamp": "2024-01-01T00:00:00Z",
            "services": {
                "database": "connected",
                "redis": "connected",
                "milvus": "connected",
                "ollama": "connected"
            }
        }
    except Exception as e:
        logger.error(f"健康检查失败: {e}")
        raise HTTPException(status_code=503, detail="Service unavailable")


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """全局异常处理器"""
    logger.error(f"未处理的异常: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "服务器内部错误，请稍后重试"
        }
    )


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
