# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.services.llm_service import LLMService

# router = APIRouter()
# llm_service = LLMService()

# class ChatRequest(BaseModel):
#     message: str
    
# router = APIRouter(tags=["Chat"])
# @router.post("/chat")
# async def chat(request: ChatRequest):
#     try:
#         response = llm_service.chat(request.message)
#         return {"model_response": response}
#     except Exception as e:
#         return {"error": str(e)}


from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    response = llm_service.process_message(request.message)
    return {"response": response}