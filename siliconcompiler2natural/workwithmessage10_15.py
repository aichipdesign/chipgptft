import openai
import json
import os

with open("./user_message_10_15.json", 'r') as f:
    content = f.read()
    
msgs = json.loads(content) if len(content) > 0 else {}

# print(type(msgs))

message = []

for item in msgs["mapping"]:
    # print(msgs["mapping"][item])
    mes = msgs["mapping"][item]["message"]
    if mes:
        # print(mes)
        if not "author" in mes.keys():
            continue
        message.append({"role": mes["author"]["role"], "content": mes["content"]["parts"][0]})


for i in message:
    print(i)
    print("\n---------------------\n")
    
jsondata = {"zyh":message}

with open("./gpt_download_json_10_15.json","w") as f:
    json.dump(jsondata, f)
    
