# SiliconCompiler Script To Natural Language

author: Yunhao Zhou

## How to generate data for finetuning LLM used to generate siliconcompiler package python script

### 1. Process message downloaded from Openai

The message of the context of in-context learning is <a href="./user_message_10_15.json">user_message_10_15.json</a>. You should run  <a href="./workwithmessage10_15.py">workwithmessage10_15.py</a> to process it.

The processed data will be saved as <a href="./user_message_10_15.json">user_message_10_15.json</a>.

### 2. Use <a href="./user_message_10_15.json">user_message_10_15.json</a> as context to generate data for LLM training

Please run <a href="./LLM_data_generation.py">LLM_data_generation.py</a> to generate data. Results will be saved in <a href="./LLM_data">/siliconcompiler2natural/LLM_data</a>
