"""
用户模型
"""
from sqlalchemy import Column, String, Boolean, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.models.base import BaseModel


class User(BaseModel):
    """用户表"""
    __tablename__ = "users"
    
    user_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True, comment="用户UUID")
    username = Column(String(50), unique=True, index=True, nullable=False, comment="用户名")
    email = Column(String(100), unique=True, index=True, nullable=False, comment="邮箱")
    hashed_password = Column(String(255), nullable=False, comment="加密密码")
    full_name = Column(String(100), comment="全名")
    is_active = Column(Boolean, default=True, comment="是否激活")
    is_superuser = Column(Boolean, default=False, comment="是否超级用户")
    avatar_url = Column(String(500), comment="头像URL")
    bio = Column(Text, comment="个人简介")
    last_login_at = Column(DateTime, comment="最后登录时间")
    
    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
