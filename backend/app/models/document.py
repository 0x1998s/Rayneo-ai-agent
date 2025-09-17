"""
文档和知识库模型
"""
from sqlalchemy import Column, String, Text, Integer, Float, JSON, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import enum

from app.models.base import BaseModel


class DocumentType(str, enum.Enum):
    """文档类型枚举"""
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    MD = "md"
    XLSX = "xlsx"
    CSV = "csv"
    IMAGE = "image"
    OTHER = "other"


class ProcessingStatus(str, enum.Enum):
    """处理状态枚举"""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class Document(BaseModel):
    """文档表"""
    __tablename__ = "documents"
    
    doc_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True, comment="文档UUID")
    filename = Column(String(255), nullable=False, comment="文件名")
    original_filename = Column(String(255), nullable=False, comment="原始文件名")
    file_path = Column(String(500), nullable=False, comment="文件路径")
    file_size = Column(Integer, comment="文件大小(字节)")
    file_type = Column(Enum(DocumentType), nullable=False, comment="文件类型")
    mime_type = Column(String(100), comment="MIME类型")
    
    # 内容信息
    title = Column(String(500), comment="文档标题")
    content = Column(Text, comment="文档内容")
    summary = Column(Text, comment="文档摘要")
    keywords = Column(JSON, comment="关键词列表")
    language = Column(String(10), default="zh", comment="语言")
    
    # 处理状态
    processing_status = Column(Enum(ProcessingStatus), default=ProcessingStatus.PENDING, comment="处理状态")
    processing_error = Column(Text, comment="处理错误信息")
    
    # 向量化信息
    embedding_model = Column(String(100), comment="嵌入模型")
    chunk_count = Column(Integer, default=0, comment="分块数量")
    
    # 用户关联
    user_id = Column(Integer, ForeignKey("users.id"), comment="上传用户ID")
    
    # 关系
    user = relationship("User", back_populates="documents")
    chunks = relationship("DocumentChunk", back_populates="document", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Document(filename={self.filename}, type={self.file_type})>"


class DocumentChunk(BaseModel):
    """文档分块表"""
    __tablename__ = "document_chunks"
    
    chunk_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True, comment="分块UUID")
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False, comment="文档ID")
    
    # 分块内容
    content = Column(Text, nullable=False, comment="分块内容")
    chunk_index = Column(Integer, nullable=False, comment="分块索引")
    start_pos = Column(Integer, comment="开始位置")
    end_pos = Column(Integer, comment="结束位置")
    
    # 向量信息
    embedding_vector = Column(JSON, comment="嵌入向量")
    vector_id = Column(String(100), comment="向量数据库ID")
    
    # 元数据
    metadata = Column(JSON, comment="元数据")
    
    # 关系
    document = relationship("Document", back_populates="chunks")
    
    def __repr__(self):
        return f"<DocumentChunk(document_id={self.document_id}, index={self.chunk_index})>"


class KnowledgeBase(BaseModel):
    """知识库表"""
    __tablename__ = "knowledge_bases"
    
    kb_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True, comment="知识库UUID")
    name = Column(String(100), nullable=False, comment="知识库名称")
    description = Column(Text, comment="描述")
    
    # 配置信息
    embedding_model = Column(String(100), nullable=False, comment="嵌入模型")
    chunk_size = Column(Integer, default=512, comment="分块大小")
    chunk_overlap = Column(Integer, default=50, comment="分块重叠")
    
    # 统计信息
    document_count = Column(Integer, default=0, comment="文档数量")
    chunk_count = Column(Integer, default=0, comment="分块数量")
    
    # 用户关联
    user_id = Column(Integer, ForeignKey("users.id"), comment="创建用户ID")
    
    # 关系
    user = relationship("User")
    
    def __repr__(self):
        return f"<KnowledgeBase(name={self.name})>"
