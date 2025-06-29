from fastapi import APIRouter, Request
from app.services.summary_engine import summarize_responses

router = APIRouter()

@router.post("/summary")
async def summary_handler(request: Request):
    body = await request.json()
    responses = body["responses"]
    final_summary = summarize_responses(responses)
    return {"summary": final_summary}