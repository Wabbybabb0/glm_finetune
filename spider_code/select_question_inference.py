import json
import os

# 打开dev.json
dev_json_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider/dev.json'
file = open(dev_json_path, 'r', encoding='utf-8')
paper = []
for line in file.readlines():
    dic = json.loads(line)
    paper.append(dic)
# print(paper[1])




# 新建一个空的JSON文件:spider_dev_process.json
# spider_dev_query_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider_dev_process/only_query.json'
# with open(spider_dev_query_path, 'w') as json_file:
#     json_file.write('')

# i=0
# for single_data in paper:
#     i+=1
#     question_content = single_data["question"]
#     cmd_command = "python inference_hf.py ./output/checkpoint-2000 --prompt" + " \"" + question_content + "\""
#     print(cmd_command)
#     os.system(cmd)
    # with open(spider_dev_query_path, 'a') as f:
    #     f.write(question_content + '\n')

question_content = paper[1]["question"]
cmd_command = "python inference_hf.py ./output/checkpoint-2000 --prompt" + " \"" + question_content + "\""
print(cmd_command)
os.system(cmd_command)

