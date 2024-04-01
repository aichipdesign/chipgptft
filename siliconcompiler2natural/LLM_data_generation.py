from openai import OpenAI
import json
import os


client = OpenAI(api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  # api of chatgpt 

class ChatGPT:
    def __init__(self, user):
        self.user = user
        self.messages = [{"role": "system", "content": ""}]
        # self.filename="./gpt_download_json.json"
        self.filename="./gpt_download_json_10_15.json"  # the context of former chatting for generating siliconcompiler script(for in context learning)

    def ask_gpt(self):
        
        rsp = client.chat.completions.create(
          model="gpt-3.5-turbo-16k",
          messages=self.messages
        )
        return rsp.get("choices")[0]["message"]["content"]

    def writeTojson(self):
        try:
            
            if not os.path.exists(self.filename):
                with open(self.filename, "w") as f:
                    pass
           
            with open(self.filename, 'r') as f:
                content = f.read()
                msgs = json.loads(content) if len(content) > 0 else {}
            
            msgs.update({self.user : self.messages})
            
            with open(self.filename, 'w') as f:
                json.dump(msgs, f)
        except Exception as e:
            print(f"error: {e}")      
            
    def loadjson(self):
        try:
            
            if not os.path.exists(self.filename):
                with open(self.filename, "w") as f:
                    pass
            
            with open(self.filename, 'r') as f:
                content = f.read()
                msgs = json.loads(content) if len(content) > 0 else {}

            
            print(list(msgs.values())[0])
            self.messages = list(msgs.values())[0]
            
        except Exception as e:
            print(f"error: {e}")      
            
      
      

def main():
    user = "zyh"
    chat = ChatGPT(user)
    chat.loadjson()  # load the message derived by in context learning
    
    # inquiry
    q = "generate randomly like before"
           
    chat.messages.append({"role": "user", "content": q})
    
    for ii in range(30):
        LLM_data = []
        for i in range(2,50):
            
            answer = chat.ask_gpt()
            print(f"【ChatGPT】{answer}")
            print("------------------------------")
            LLM_data.append(answer)

        filename = "./LLM_data/LLM_data_1500case"+str(ii)+".json"  # output the result
        with open(filename,'w') as file:
            json.dump(LLM_data,file)
    
    
if __name__ == '__main__':
    main()
