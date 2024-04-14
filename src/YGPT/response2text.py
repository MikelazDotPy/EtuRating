import requests
import json
import time

DIR_ID = "b1gvnbq0m68gbd058car"
API_KEY = "AQVN3224iXMMytMpj63Hz_joD9rl7glh9zURbpLQ"
TOKEN_LIM = 10000


def get_gpt_text(prompt: str, message: str):
    messages_json = [
                        {"role": "system", "text": f"{prompt}"},
                        {"role": "user", "text": message}
                    ]
    resp = {
        "modelUri": f"gpt://{DIR_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0,
            "maxTokens": f"{TOKEN_LIM}"
        },
        "messages": messages_json
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}"
    }

    time.sleep(1)
    #return requests.post(url, headers=headers, json=resp)
    text = requests.post(url, headers=headers, json=resp).text
    return json.loads(text)["result"]["alternatives"][0]["message"]["text"].replace("\n", " ")

def multi_gpt_text(prompt: str, messages: list[str]):
    return [get_gpt_text(prompt, mess) for mess in messages]
