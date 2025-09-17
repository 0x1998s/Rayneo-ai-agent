"""
Prompt管理API
"""
from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/")
async def list_prompts(current_user: User = Depends(get_current_user)):
    """获取Prompt列表"""
    return {"message": "Prompts list endpoint - 待实现"}


@router.post("/")
async def create_prompt(current_user: User = Depends(get_current_user)):
    """创建Prompt"""
    return {"message": "Create prompt endpoint - 待实现"}
