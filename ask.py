import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:8b"

def ask(question: str) -> dict:
    
    payload = {
        "model": MODEL,
        "stream": False,
        "think": False,
        "options": {
            "num_predict": 1000,
            "temperature": 0.7,
            "top_p": 0.9
        },
        "messages": [
            {"role": "system", "content": "คุณเป็นผู้ช่วยที่มีความรู้และสามารถตอบคำถามได้อย่างชัดเจน ตอบภาษาไทยเท่านั้น"},
            {"role": "user", "content": question}
        ]

    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    response.raise_for_status()
    return response.json()
    
    
if __name__ == "__main__":
    question = input("ถามคำถามของคุณ: ")
    data =ask(question)
    content = data["message"]["content"]
    tokens = data["eval_count"]
    seconds = data["eval_duration"] / 1e9
    print("คำตอบ:", content)
    print("จำนวนโทเค็นที่ใช้:", tokens)
    print("เวลาที่ใช้ในการประมวลผล (วินาที):", round(seconds, 2), "วินาที")
    print("ความเร็ว:", round(tokens / seconds, 1), "tokens/s")