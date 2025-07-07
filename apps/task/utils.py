import requests

from apps.task.settings import HF_API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli" # change as per use!
HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def classify_task_priority(title, description):
    labels = ["Low", "Medium", "High", "Critical"]
    text = f"{title}. {description}"

    response = requests.post(API_URL, headers=HEADERS, json={
        "inputs": text,
        "parameters": {"candidate_labels": labels}
    })

    result = response.json()
    if isinstance(result, dict) and 'labels' in result:
        return result['labels'][0]
    
