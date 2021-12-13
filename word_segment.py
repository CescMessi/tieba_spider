from collections import Counter
from os import path
import jieba
from config import cfg



class WordSegmentor:
    def __init__(self, text) -> None:
        self.text = text
        jieba.load_userdict(cfg.user_dict) # 导入用户自定义词典

    def isEmoji(self, content):
        if not content:
            return False
        if u"\U0001F600" <= content and content <= u"\U0001F64F":
            return True
        elif u"\U0001F300" <= content and content <= u"\U0001F5FF":
            return True
        elif u"\U0001F680" <= content and content <= u"\U0001F6FF":
            return True
        elif u"\U0001F1E0" <= content and content <= u"\U0001F1FF":
            return True
        else:
            return False

    def word_segment(self):
        '''
        通过jieba进行分词并通过空格分隔,返回分词后的结果
        '''
        single_word_list = cfg.reserved_single_words
        # 计算每个词出现的频率，并存入txt文件
        jieba_word=jieba.cut(self.text,cut_all=False, HMM=True) # cut_all是分词模式，True是全模式，False是精准模式，默认False
        data=[]
        for word in jieba_word:
            if len(word) <= 1 and not self.isEmoji(word[0]) and (word not in single_word_list) :
                continue
            data.append(word)
        dataDict=Counter(data)
        sorted_data_dict = sorted(dataDict.items(), key=lambda x: x[1], reverse=True)
        with open(cfg.word_frequency_file,'w') as fw:
            import json
            json.dump(sorted_data_dict, fw, ensure_ascii=False, indent=4)


        # 返回分词后的结果
        seg_list_text =' '.join(data)
        return seg_list_text
