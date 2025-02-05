import os
import json
from tqdm import tqdm

# 合并json文件
def merge_json_files(input_folder, output_file):
    merged_data = []

    # 获取文件夹中的所有 JSON 文件路径
    json_files = [f for f in os.listdir(input_folder) if f.endswith('.jsonl')]

    for file in tqdm(json_files):

        file_path = os.path.join(input_folder, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for conv in data:
                merged_data.append(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":

    input_folder = "/root/Project_FunGPT/Developing/Data/Dui_LLM/sample"  # 存放 JSON 文件的文件夹路径
    output_file = "/root/Project_FunGPT/Developing/Data/Dui_LLM/feasible_data/ft_data.jsonl"  # 合并后的 JSON 文件路径
    merge_json_files(input_folder, output_file)