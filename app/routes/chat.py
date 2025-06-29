from fastapi import APIRouter, Request
from app.services.openai_service import ask_openai
from app.services.gemini_service import ask_gemini
# from app.services.claude_service import ask_claude
from concurrent.futures import ThreadPoolExecutor

router = APIRouter()

@router.post("/chat")
async def chat_handler(request: Request):
    body = await request.json()
    prompt = body["prompt"]
    selected_ais = body["ais"]

    results = {}
    with ThreadPoolExecutor() as executor:
        if "chatgpt" in selected_ais:
            results["chatgpt"] = executor.submit(ask_openai, prompt)
        if "gemini" in selected_ais:
            results["gemini"] = executor.submit(ask_gemini, prompt)
        # if "claude" in selected_ais:
        #     results["claude"] = executor.submit(ask_claude, prompt)

    output = {k: v.result() for k, v in results.items()}
    return {"responses": output}