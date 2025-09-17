"""
数据库连接和会话管理
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
from typing import Generator
import redis
from contextlib import asynccontextmanager

from app.core.config import settings
from app.utils.logger import logger

# SQLAlchemy 配置
engine = create_engine(
    settings.DATABASE_URL,
    poolclass=StaticPool,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {},
    echo=settings.DEBUG
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 数据库模型基类
Base = declarative_base()
metadata = MetaData()

# Redis 连接
redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)


def get_db() -> Generator[Session, None, None]:
    """获取数据库会话"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_redis() -> redis.Redis:
    """获取Redis客户端"""
    return redis_client


async def init_db() -> None:
    """初始化数据库"""
    try:
        # 创建所有表
        Base.metadata.create_all(bind=engine)
        logger.info("✅ 数据库表创建成功")
        
        # 测试数据库连接
        with SessionLocal() as db:
            db.execute("SELECT 1")
            logger.info("✅ 数据库连接测试成功")
            
        # 测试Redis连接
        redis_client.ping()
        logger.info("✅ Redis连接测试成功")
        
    except Exception as e:
        logger.error(f"❌ 数据库初始化失败: {e}")
        raise


@asynccontextmanager
async def get_db_context():
    """数据库上下文管理器"""
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        logger.error(f"数据库操作失败: {e}")
        raise
    finally:
        db.close()


class DatabaseManager:
    """数据库管理器"""
    
    def __init__(self):
        self.engine = engine
        self.SessionLocal = SessionLocal
        self.redis_client = redis_client
    
    def create_tables(self):
        """创建所有表"""
        Base.metadata.create_all(bind=self.engine)
    
    def drop_tables(self):
        """删除所有表"""
        Base.metadata.drop_all(bind=self.engine)
    
    def get_session(self) -> Session:
        """获取数据库会话"""
        return self.SessionLocal()
    
    def test_connection(self) -> bool:
        """测试数据库连接"""
        try:
            with self.SessionLocal() as db:
                db.execute("SELECT 1")
            return True
        except Exception as e:
            logger.error(f"数据库连接测试失败: {e}")
            return False
    
    def test_redis_connection(self) -> bool:
        """测试Redis连接"""
        try:
            self.redis_client.ping()
            return True
        except Exception as e:
            logger.error(f"Redis连接测试失败: {e}")
            return False


# 创建数据库管理器实例
db_manager = DatabaseManager()
