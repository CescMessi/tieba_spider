import requests
import logging
import json
from time import sleep
from tqdm import tqdm
from bs4 import BeautifulSoup
from config import cfg

class TiebaDownloader:
    def __init__(self) -> None:
        base_url = f'https://tieba.baidu.com/f?kw={cfg.tieba_name}&ie=utf-8'
        self.url_list = [f'{base_url}&pn={str(i*50)}' for i in range(cfg.page_num+1)]

    def get_html_text(self, url):
        '''获取单个链接的html内容
        '''
        try:
            r = requests.get(
                url, 
                timeout=30, 
                headers=cfg.headers, 
                cookies=cfg.cookies
            )
            r.raise_for_status()
            r.encoding = 'utf-8'
            if '百度安全认证' in r.text:
                raise 
            return r.text
        except:
            logging.error(f'{url}请求失败！可能存在验证码！')
            return None

    def get_content(self, url):
        '''提取链接网页中的信息
        '''
        infomations = []
        html_text = self.get_html_text(url)
        if html_text is None:
            return None
        soup = BeautifulSoup(html_text, 'lxml')
        liTags = soup.find_all(
            'li', 
            attrs={'class':'j_thread_list clearfix thread_item_box'}
        )

        # 通过循环找到每个帖子的信息：
        for li in liTags:
            # 初始化一个字典来存储文章信息
            comment = {}
            try:
                # 开始筛选信息，并保存到字典中
                comment['title'] = li.find(
                    'a', attrs={'class': 'j_th_tit'}).text.strip()
                comment['link'] = "http://tieba.baidu.com/" + \
                    li.find('a', attrs={'class': 'j_th_tit'})['href']
                comment['name'] = li.find(
                    'span', attrs={'class': 'tb_icon_author'}).attrs['title'][6:]
                comment['time'] = li.find(
                    'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
                comment['replyNum'] = li.find(
                    'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
                infomations.append(comment)
            except:
                logging.error(f'网页{url}找不到信息')
                return None
        return infomations

    def write_jsons(self, all_dict):
        with open(cfg.all_result_file, 'w') as f:
            json.dump(all_dict, f, ensure_ascii=False, indent=4)

    def __call__(self):
        all_dict = {}
        for i, url in tqdm(enumerate(self.url_list), total=len(self.url_list)):
            content = self.get_content(url)
            if content is None:
                logging.error(f'第{i+1}页获取失败！')
                continue
            for post in content:
                all_dict[post['link'].split('/')[-1]] = post
            sleep(cfg.delay_time)
        self.write_jsons(all_dict)
        return all_dict


if __name__ == '__main__':
    down = TiebaDownloader()
    down()




    
    