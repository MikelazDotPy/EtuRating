import requests
import json

HRU = """НЕ ИСПОЛЬЗОВАТЬ ДАННЫЕ ИЗ ПРИМЕРА
Пример:
Ввод:
Курс «Webтехнологии» охватывает широкий спектр технологий и подходов, использующихся при разработке Интернетсайтов и webприложений. Рассматриваются основы построения webприложений с использованием HTML,
CSS. Студенты последовательно изучают основы протокола HTTP, настройку webсервера, основы JavaScript, TypeScript и PHP, построение статических
HTMLстраниц и оформления с использованием CSS, LESS и SASS, разработку
сервера приложений с использованием Node.JS. Построение серверной части
на основе Express и Nest, разработка клиентских приложений с использованием
Angular, React и Vue. Выполнение модульного тестирования webприложений,
сборка приложений с использованием GULP и Webpack, обеспечение безопасности webприложений.
Вывод:
web-разработка,frontend,backend,html,css,javascript,typescript,php,node-js,express,nestjs,angular,react,vue,gulp,webpack"""

PROMT = """На вход подаётся аннотация дисциплины
На выход надо дать навыки, которые получит студент, изучивший эту дисциплину. В каждом пункте ответа должно содержатся 
ТОЛЬКО название технологии. ЧЕТКИЙ ФОРМАТ ВЫВОДА: каждый пункт через запятую без пробелов, НИКАКИХ НОВЫХ СТРОК, НИКАКИХ СЛОВ ПО ТИПУ "Ответ" "Вывод" и так далее
"""

DIR_ID = ""
API_KEY = ""
TOKEN_LIM = 5000


def get_gpt_text(prompt: str, messages: list[str]):
    messages_json = [{"role": "system", "text": f"{prompt}"}] + [{"role": "user", "text": el} for el in messages]

    resp = {
        "modelUri": f"gpt://{DIR_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": f"{TOKEN_LIM}"
        },
        "messages": messages_json
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}"
    }

    return requests.post(url, headers=headers, json=resp)


summ = """Рассматриваются основные этапы развития вычислительной техники и
её компонентов, как устроена работа современной вычислительной системы. В
курсе изучаются разновидности архитектур вычислительных систем. Рассматриваются форматы представления данных на компьютере. В курсе представлены основные сведения для изучения базовых концепций языка программирования Python: стандартные типы данных, функции и методы их обработки. Изучается интегрированная среда разработки PyCharm для языка Python. Изучается
Машина Тьюринга: формальное определение, машина Тьюринга как стандартная вычислительная модель. Рассматриваются примеры решений задач с помощью машины Тьюринга на языке Python"""
jss = get_gpt_text(PROMT, [summ])
print(jss.text)
jsss = jss.text
print(json.loads(jsss)["result"]["alternatives"][0]["message"]["text"])
