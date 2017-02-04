from os import path
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def wordCount(filename):
    '''
    简单计算词频的函数
    :param filename: 文件名
    :return: 词频
    '''
    wordCount = {}
    file = open(filename,'r')
    while True:
        line = file.readline()
        if line:
            wordlist = line.split(',[')
            if len(wordlist) == 1: continue
            wordlist = wordlist[1].split('],')[0].split(',')
            for word in wordlist:
                word = word.replace(' ', '').replace("'", '')
                if word in wordCount.keys():
                    wordCount[word] = wordCount[word]+1
                else:
                    wordCount[word] = 1
        else:
            break
    return [(k, wordCount[k]) for k in wordCount.keys()]


def generateCloud(filename,imagename,cloudname,fontname):
    '''
    生成标签云的函数
    '''
    coloring = imread(imagename)             # 读取背景图片
    wc = WordCloud(background_color="white", # 背景颜色max_words=2000,# 词云显示的最大词数
                   mask=coloring,            # 设置背景图片
                   stopwords=STOPWORDS,      # 停止词
                   font_path=fontname,       # 兼容中文字体
                   max_font_size=150)        # 字体最大值

    #计算好词频后使用generate_from_frequencies函数生成词云
    #txtFreq例子为[('词a', 100),('词b', 90),('词c', 80)]
    txtFreq = wordCount(filename)
    wc.generate_from_frequencies(txtFreq)
    # 生成图片
    plt.imshow(wc)
    plt.axis("off")
    # 绘制词云
    plt.figure()
    # 保存词云
    wc.to_file(cloudname)

if __name__ == '__main__':
    d = path.dirname(__file__)              # 获取当前文件路径
    fontname = path.join(d, 'msyh.ttf')     # 中文字体路径
    filename = path.join(d, '广州.txt')      # txt文件路径
    imagename = path.join(d, "circle.jpg")  # 背景图片路径
    cloudname = path.join(d, "cloud.png")   # 标签云路径
    generateCloud(filename, imagename, cloudname, fontname)

