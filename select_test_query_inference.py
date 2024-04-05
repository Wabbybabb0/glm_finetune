import json
import os
import subprocess

# 打开dev.json
dev_json_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider_test/dev.json'
file = open(dev_json_path, 'r', encoding='utf-8')
paper = []
for line in file.readlines():
    dic = json.loads(line)
    paper.append(dic)
# print(paper[1])




# 新建一个空的JSON文件:spider_dev_process.json
spider_dev_query_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider_test/only_test_query.json'
with open(spider_dev_query_path, 'w') as json_file:
    json_file.write('')

i=0
for single_data in paper:
    i+=1
    # question_content = single_data["question"]
    # cmd_command = "python inference_hf.py ./output/checkpoint-2000 --prompt" + " \"" + question_content + "\""
    # os.system(cmd)
    question_content = single_data["question"]
    cmd_command = "python inference_hf.py ./output/checkpoint-2000 --prompt" + " \"" + question_content + "\""
    query_content = subprocess.run(cmd_command, shell=True, capture_output=True, text=True)
    single_query = ""
    if query_content.stdout is None or query_content.stdout == "":
        single_query = "ERROR\n"
    else:
        single_query = query_content.stdout
    print('第', i,'个', single_query)
    with open(spider_dev_query_path, 'a') as f:
        f.write(single_query)


# import json
# import os
# import subprocess
#
# # 打开dev.json
# dev_json_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider/dev_test.json'
# file = open(dev_json_path, 'r', encoding='utf-8')
# paper = []
# for line in file.readlines():
#     dic = json.loads(line)
#     paper.append(dic)
# # print(paper[1])




# # 新建一个空的JSON文件:spider_dev_process.json
# spider_dev_query_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider_dev_process/only_query1.json'
# with open(spider_dev_query_path, 'w') as json_file:
#     json_file.write('')
#
# i=0
# for single_data in paper:
#     i+=1
#     # question_content = single_data["question"]
#     # cmd_command = "python inference_hf.py ./output/checkpoint-2000 --prompt" + " \"" + question_content + "\""
#     # os.system(cmd)
#     question_content = single_data["question"]
#     cmd_command = "python inference_hf.py ./output/checkpoint-2000 --prompt" + " \"" + question_content + "\""
#     query_content = subprocess.run(cmd_command, shell=True, capture_output=True, text=True)
#     single_query = ""
#     if query_content.stdout is None or query_content.stdout == "":
#         single_query = "ERROR\n"
#     else:
#         single_query = query_content.stdout
#     print('第', i,'个', single_query)
#     with open(spider_dev_query_path, 'a') as f:
#         f.write(single_query)


