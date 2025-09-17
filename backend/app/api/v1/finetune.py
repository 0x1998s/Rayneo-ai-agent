"""
模型微调API
"""
from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/jobs")
async def list_finetune_jobs(current_user: User = Depends(get_current_user)):
    """获取微调任务列表"""
    return {"message": "Finetune jobs list endpoint - 待实现"}


@router.post("/jobs")
async def create_finetune_job(current_user: User = Depends(get_current_user)):
    """创建微调任务"""
    return {"message": "Create finetune job endpoint - 待实现"}
