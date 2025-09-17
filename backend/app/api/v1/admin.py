"""
系统管理API
"""
from fastapi import APIRouter, Depends, HTTPException
from app.api.v1.auth import get_current_user
from app.models.user import User

router = APIRouter()


def require_superuser(current_user: User = Depends(get_current_user)):
    """要求超级用户权限"""
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Superuser required")
    return current_user


@router.get("/stats")
async def get_system_stats(current_user: User = Depends(require_superuser)):
    """获取系统统计"""
    return {"message": "System stats endpoint - 待实现"}


@router.get("/users")
async def list_users(current_user: User = Depends(require_superuser)):
    """获取用户列表"""
    return {"message": "Users list endpoint - 待实现"}
