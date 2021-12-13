class Config:
    # 用于爬取数据
    delay_time = 5  # 两次请求的间隔时间
    tieba_name = '华南农业大学'  # 贴吧名
    page_num = 2  # 爬取贴吧的页数，最大200
    all_result_file = 'output/all.json'  # 保存帖子名、作者、时间、回复数的json文件位置
    user_post_num_file = 'output/user.json'  # 按发帖数对用户排序的json文件位置
    sort_replay_file = 'output/replay.json'  # 按回复数对帖子排序的json文件位置
    titles_file = 'output/title.txt'  # 下载得到的全部标题文件，一行一个

    cookies = None

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    # 用于分词
    user_dict = 'userdict/userdict.txt'  # 用户词典
    reserved_single_words = ['赢', '输']  # 不被忽略的单字
    word_frequency_file = 'output/word_frequency.json'  # 词频保存文件

    # 用于绘制词云图
    image_name = 'output/scau.png'
    font = 'font/msyh.ttf'  # 字体文件
    max_words = 5000  # 生成的词数上限
    width = 4000  # 图片宽度
    height = 2000  # 图片高度


cfg = Config()