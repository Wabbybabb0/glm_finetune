import json

# 打开dev.json
dev_json_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider/dev.json'
file = open(dev_json_path, 'r', encoding='utf-8')
paper = []
for line in file.readlines():
    dic = json.loads(line)
    paper.append(dic)
print(type(paper[1]))


# 新建一个空的JSON文件:spider_dev_process.json
spider_dev_process_path = '/home/xby00008312/llm_cptt/glm_finetune/from_github/ChatGLM3/finetune_demo/data/spider_dev_process/only_question.json'
with open(spider_dev_process_path, 'w') as json_file:
    json_file.write('')

i=0
for single_data in paper:
    i+=1
    question_content = single_data["question"]
    print('第',i,'个',question_content)
    with open(spider_dev_process_path, 'a') as f:
        f.write(question_content + '\n')