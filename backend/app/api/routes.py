"""
API 路由聚合器
"""
from fastapi import APIRouter
from app.api.v1 import (
    auth,
    models,
    documents,
    workflows,
    prompts,
    finetune,
    chat,
    admin
)

# 创建主路由器
api_router = APIRouter()

# 注册各模块路由
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["认证"]
)

api_router.include_router(
    models.router,
    prefix="/models",
    tags=["模型管理"]
)

api_router.include_router(
    documents.router,
    prefix="/documents",
    tags=["文档管理"]
)

api_router.include_router(
    workflows.router,
    prefix="/workflows",
    tags=["工作流"]
)

api_router.include_router(
    prompts.router,
    prefix="/prompts",
    tags=["Prompt管理"]
)

api_router.include_router(
    finetune.router,
    prefix="/finetune",
    tags=["模型微调"]
)

api_router.include_router(
    chat.router,
    prefix="/chat",
    tags=["对话接口"]
)

api_router.include_router(
    admin.router,
    prefix="/admin",
    tags=["系统管理"]
)
