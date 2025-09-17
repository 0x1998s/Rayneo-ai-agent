"""
对话接口API
"""
from fastapi import APIRouter, Depends
from app.api.v1.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/")
async def chat(current_user: User = Depends(get_current_user)):
    """对话接口"""
    return {"message": "Chat endpoint - 待实现"}


@router.get("/history")
async def chat_history(current_user: User = Depends(get_current_user)):
    """对话历史"""
    return {"message": "Chat history endpoint - 待实现"}
