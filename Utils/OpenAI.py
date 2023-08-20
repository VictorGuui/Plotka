import os
import requests
from dotenv import load_dotenv

load_dotenv()


class OpenAI:
    def __init__(self) -> None:
        self.key = os.getenv("API_KEY")

    def chat_request(self, system, message_history=[]):

        message_history.insert(0,{"role": "system", "content": system})
        response = requests.post(
            url="https://api.openai.com/v1/chat/completions",
            headers={"Authorization": "Bearer " + self.key},
            json={
                "model": "gpt-3.5-turbo",
                "messages": message_history,
            },     
        )
        data = None
        if response.status_code == 200:
            response_json = response.json()
            data = response_json["choices"][0]["message"]["content"]

        return data

    def completion(
        self, 
        prompt
    ):
        response = requests.post(
            url="https://api.openai.com/v1/completions",
            headers={"Authorization": "Bearer " + self.key},
                    json={
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0
        }
        )
        if response.status_code == 200:
            response_json = response.json()
            data = response_json["choices"][0]["text"]

        return data