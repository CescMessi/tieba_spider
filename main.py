import logging
from tieba_downloader import TiebaDownloader
from tieba_parser import parser
from word_segment import WordSegmentor
from draw_wordcloud import generate_wordcloud


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log', level=logging.DEBUG, format=LOG_FORMAT)

if __name__ == '__main__':
    downloader = TiebaDownloader()
    print('下载网页中……')
    all_dict = downloader()
    titles = parser(all_dict)
    segmentor = WordSegmentor(titles)
    seg_list_text = segmentor.word_segment()
    generate_wordcloud(seg_list_text)
    print('词云图片已生成')