import logging
from wordcloud import WordCloud, STOPWORDS
from config import cfg

def generate_wordcloud(text):
    '''
    输入文本生成词云
    '''
    font_path=cfg.font
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white",# 设置背景颜色
        max_words=cfg.max_words, # 词云显示的最大词数      
        stopwords=stopwords, # 设置停用词
        font_path=font_path, # 兼容中文字体，不然中文会显示乱码
        width=cfg.width,
        height=cfg.height      
    )

    # 生成词云 
    wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file(cfg.image_name)

    # # 显示图像
    # plt.imshow(wc, interpolation='bilinear')
    # # interpolation='bilinear' 表示插值方法为双线性插值
    # plt.axis("off")# 关掉图像的坐标
    # plt.show()
