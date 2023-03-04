import openai
import requests
import json

# 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
# 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
url = 'https://api.openai.com/v1/chat/completions';
header={"Authorization":"Bearer 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"}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}
res = requests.post(url= url,headers=header,json=data)

print(res.text)
resMess = json.decoder(res.text)
print(resMess.ch)
