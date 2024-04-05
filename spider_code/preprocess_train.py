import json
import os
import numpy as np

# 原始数据集
original_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider_original/train_spider.json'
with open(original_path,'r') as f:
    data = json.load(f)

# 只有question和query的数据集
train_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider/train.json'
with open(train_path, 'w') as f:
    f.write('')

# 选取query和question
i=0
for single_query in data :
    i=i+1
    question_dict = {key: value for key, value in single_query.items() if key == 'question'}
    query_dict = {key: value for key, value in single_query.items() if key == 'query'}
    print('第',i,'个')
    print(question_dict)
    print(query_dict)
    json_question = json.dumps(question_dict, indent=4)
    json_query = json.dumps(query_dict, indent=4)
    json_question_no_n = json_question.replace('\n', '')
    json_query_no_n = json_query.replace('\n','')

    with open(train_path, 'a') as f:
        f.write(json_question_no_n)
        f.write(json_query_no_n + '\n')

#替换{}和一些空格
with open(train_path, 'r') as input_file:
    json_data = input_file.readlines()
json_data = [line.replace('}{    ', ', ') for line in json_data]
json_data = [line.replace('    ', '') for line in json_data]
json_data = ''.join(json_data)
with open(train_path, 'w') as output_file:
    output_file.write(json_data)
