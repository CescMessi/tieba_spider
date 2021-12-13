import json
from collections import Counter
from config import cfg

def parser(all_dict):
    name_list = []
    titles = ''
    # 写入标题文件
    with open(cfg.titles_file, 'w') as tf:
        for content in all_dict.values():
            title = content['title']
            tf.write(f'{title}\n')
            titles += f'{title}\n'
            name_list.append(content['name'])
    
    # 发帖数与回帖数排序
    name_dict = Counter(name_list)
    sorted_num_dict = sorted(name_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_content_dict = sorted(all_dict.values(), key=lambda x: int(x['replyNum']), reverse=True)

    with open(cfg.user_post_num_file, 'w') as uf:
        json.dump(sorted_num_dict, uf, ensure_ascii=False, indent=4)

    with open(cfg.sort_replay_file, 'w') as rf:
        json.dump(sorted_content_dict, rf, ensure_ascii=False, indent=4)

    return titles    