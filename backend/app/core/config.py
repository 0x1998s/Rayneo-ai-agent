"""
应用程序配置管理
"""
from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """应用程序设置"""
    
    # 基础配置
    APP_NAME: str = "Rayneo AI Agent"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # 服务器配置
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # 数据库配置
    DATABASE_URL: str = Field(
        default="postgresql://rayneo_user:rayneo_pass@localhost:5432/rayneo_ai_agent",
        description="PostgreSQL 数据库连接URL"
    )
    
    # Redis 配置
    REDIS_URL: str = Field(
        default="redis://localhost:6379",
        description="Redis 连接URL"
    )
    
    # Milvus 向量数据库配置
    MILVUS_HOST: str = Field(default="localhost", description="Milvus 主机地址")
    MILVUS_PORT: int = Field(default=19530, description="Milvus 端口")
    MILVUS_USER: str = Field(default="", description="Milvus 用户名")
    MILVUS_PASSWORD: str = Field(default="", description="Milvus 密码")
    
    # Ollama 配置
    OLLAMA_BASE_URL: str = Field(
        default="http://localhost:11434",
        description="Ollama API 基础URL"
    )
    OLLAMA_DEFAULT_MODEL: str = Field(
        default="llama2:7b",
        description="默认使用的模型"
    )
    
    # JWT 配置
    SECRET_KEY: str = Field(
        default="rayneo-ai-agent-secret-key-change-in-production",
        description="JWT 密钥"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS 配置
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000"
    ]
    
    # 文件上传配置
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE: int = 100 * 1024 * 1024  # 100MB
    ALLOWED_FILE_TYPES: List[str] = [
        "pdf", "docx", "doc", "txt", "md",
        "xlsx", "xls", "csv",
        "png", "jpg", "jpeg", "gif", "bmp"
    ]
    
    # 模型配置
    MODEL_CACHE_DIR: str = "models"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    EMBEDDING_DIMENSION: int = 384
    
    # 任务队列配置
    CELERY_BROKER_URL: str = Field(
        default="redis://localhost:6379/0",
        description="Celery 消息代理URL"
    )
    CELERY_RESULT_BACKEND: str = Field(
        default="redis://localhost:6379/0",
        description="Celery 结果后端URL"
    )
    
    # 日志配置
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"
    LOG_MAX_SIZE: int = 10 * 1024 * 1024  # 10MB
    LOG_BACKUP_COUNT: int = 5
    
    # 监控配置
    ENABLE_METRICS: bool = True
    METRICS_PORT: int = 9090
    
    # 开发模式配置
    RELOAD: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# 创建全局配置实例
settings = Settings()


def get_database_url() -> str:
    """获取数据库连接URL"""
    return settings.DATABASE_URL


def get_redis_url() -> str:
    """获取Redis连接URL"""
    return settings.REDIS_URL


def get_milvus_config() -> dict:
    """获取Milvus配置"""
    return {
        "host": settings.MILVUS_HOST,
        "port": settings.MILVUS_PORT,
        "user": settings.MILVUS_USER,
        "password": settings.MILVUS_PASSWORD
    }


def get_ollama_config() -> dict:
    """获取Ollama配置"""
    return {
        "base_url": settings.OLLAMA_BASE_URL,
        "default_model": settings.OLLAMA_DEFAULT_MODEL
    }
