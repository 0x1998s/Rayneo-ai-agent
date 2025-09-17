"""
日志配置和管理
"""
import sys
import os
from pathlib import Path
from loguru import logger as _logger
from app.core.config import settings

# 创建日志目录
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# 移除默认处理器
_logger.remove()

# 控制台输出配置
_logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    colorize=True
)

# 文件输出配置
_logger.add(
    settings.LOG_FILE,
    level=settings.LOG_LEVEL,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    rotation=settings.LOG_MAX_SIZE,
    retention=settings.LOG_BACKUP_COUNT,
    compression="zip",
    encoding="utf-8"
)

# 错误日志单独记录
_logger.add(
    "logs/error.log",
    level="ERROR",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    rotation="1 day",
    retention="30 days",
    compression="zip",
    encoding="utf-8"
)

# 导出logger实例
logger = _logger


def setup_logging():
    """设置日志配置"""
    logger.info(f"🔧 日志系统初始化完成")
    logger.info(f"📝 日志级别: {settings.LOG_LEVEL}")
    logger.info(f"📁 日志文件: {settings.LOG_FILE}")


# 在模块加载时初始化日志
setup_logging()
