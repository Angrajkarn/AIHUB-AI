from app.services.openai_service import ask_openai

def summarize_responses(responses: dict) -> str:
    prompt = "Merge these responses into a clear summary:\n\n"
    for k, v in responses.items():
        prompt += f"{k}: {v}\n"
    prompt += "\nFinal Summary:"
    return ask_openai(prompt)