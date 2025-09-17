"""
数据库基础模型
"""
from sqlalchemy import Column, Integer, DateTime, String, Text, Boolean
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """基础模型类"""
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now(), nullable=False, comment="创建时间")
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False, comment="更新时间")
    is_deleted = Column(Boolean, default=False, nullable=False, comment="是否删除")
    
    def to_dict(self):
        """转换为字典"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
