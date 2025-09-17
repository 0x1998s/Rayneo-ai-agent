"""
模型管理API
"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
import httpx
from pydantic import BaseModel

from app.core.config import settings
from app.utils.logger import logger
from app.api.v1.auth import get_current_user
from app.models.user import User

router = APIRouter()


class ModelInfo(BaseModel):
    """模型信息"""
    name: str
    size: Optional[str] = None
    digest: Optional[str] = None
    modified_at: Optional[str] = None
    details: Optional[dict] = None


class ModelResponse(BaseModel):
    """模型响应"""
    models: List[ModelInfo]


class ChatRequest(BaseModel):
    """聊天请求"""
    model: str
    messages: List[dict]
    stream: bool = False
    temperature: float = 0.7
    max_tokens: int = 1000


@router.get("/", response_model=ModelResponse)
async def list_models(current_user: User = Depends(get_current_user)):
    """获取可用模型列表"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.OLLAMA_BASE_URL}/api/tags")
            if response.status_code == 200:
                data = response.json()
                models = []
                for model in data.get("models", []):
                    models.append(ModelInfo(
                        name=model["name"],
                        size=model.get("size"),
                        digest=model.get("digest"),
                        modified_at=model.get("modified_at"),
                        details=model.get("details")
                    ))
                logger.info(f"获取到 {len(models)} 个可用模型")
                return ModelResponse(models=models)
            else:
                raise HTTPException(status_code=500, detail="Failed to fetch models from Ollama")
    except httpx.RequestError as e:
        logger.error(f"连接 Ollama 服务失败: {e}")
        raise HTTPException(status_code=503, detail="Ollama service unavailable")


@router.post("/pull")
async def pull_model(
    model_name: str,
    current_user: User = Depends(get_current_user)
):
    """拉取新模型"""
    try:
        async with httpx.AsyncClient(timeout=300.0) as client:
            response = await client.post(
                f"{settings.OLLAMA_BASE_URL}/api/pull",
                json={"name": model_name}
            )
            if response.status_code == 200:
                logger.info(f"用户 {current_user.username} 开始拉取模型: {model_name}")
                return {"message": f"Model {model_name} pull started", "status": "started"}
            else:
                raise HTTPException(status_code=400, detail="Failed to pull model")
    except httpx.RequestError as e:
        logger.error(f"拉取模型失败: {e}")
        raise HTTPException(status_code=503, detail="Ollama service unavailable")


@router.delete("/{model_name}")
async def delete_model(
    model_name: str,
    current_user: User = Depends(get_current_user)
):
    """删除模型"""
    # 只有超级用户可以删除模型
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Only superusers can delete models")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{settings.OLLAMA_BASE_URL}/api/delete",
                json={"name": model_name}
            )
            if response.status_code == 200:
                logger.info(f"超级用户 {current_user.username} 删除模型: {model_name}")
                return {"message": f"Model {model_name} deleted successfully"}
            else:
                raise HTTPException(status_code=400, detail="Failed to delete model")
    except httpx.RequestError as e:
        logger.error(f"删除模型失败: {e}")
        raise HTTPException(status_code=503, detail="Ollama service unavailable")


@router.post("/chat")
async def chat_with_model(
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):
    """与模型对话"""
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{settings.OLLAMA_BASE_URL}/api/chat",
                json={
                    "model": request.model,
                    "messages": request.messages,
                    "stream": request.stream,
                    "options": {
                        "temperature": request.temperature,
                        "num_predict": request.max_tokens
                    }
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                logger.info(f"用户 {current_user.username} 与模型 {request.model} 对话")
                return {
                    "model": request.model,
                    "message": result.get("message", {}),
                    "done": result.get("done", True),
                    "total_duration": result.get("total_duration"),
                    "load_duration": result.get("load_duration"),
                    "prompt_eval_count": result.get("prompt_eval_count"),
                    "eval_count": result.get("eval_count")
                }
            else:
                raise HTTPException(status_code=400, detail="Failed to chat with model")
    except httpx.RequestError as e:
        logger.error(f"模型对话失败: {e}")
        raise HTTPException(status_code=503, detail="Ollama service unavailable")


@router.get("/status")
async def get_ollama_status(current_user: User = Depends(get_current_user)):
    """获取 Ollama 服务状态"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{settings.OLLAMA_BASE_URL}/api/version")
            if response.status_code == 200:
                return {
                    "status": "healthy",
                    "version": response.json(),
                    "base_url": settings.OLLAMA_BASE_URL
                }
            else:
                return {
                    "status": "unhealthy",
                    "message": "Ollama service is not responding properly"
                }
    except httpx.RequestError:
        return {
            "status": "unavailable",
            "message": "Cannot connect to Ollama service"
        }
