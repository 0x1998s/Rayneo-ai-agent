"""
工作流管理API
"""
from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/")
async def list_workflows(current_user: User = Depends(get_current_user)):
    """获取工作流列表"""
    return {"message": "Workflows list endpoint - 待实现"}


@router.post("/")
async def create_workflow(current_user: User = Depends(get_current_user)):
    """创建工作流"""
    return {"message": "Create workflow endpoint - 待实现"}
