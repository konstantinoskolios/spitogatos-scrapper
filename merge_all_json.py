import json
import os

def json_to_dict(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

combined_data = {}

for file_path in os.listdir("samples"):
    data = json_to_dict(f"samples/{file_path}")
    combined_data.update(data)
        
with open("output_all_json.json","w",encoding="utf-8") as file:
    json.dump(combined_data,file,ensure_ascii=False, indent=4)