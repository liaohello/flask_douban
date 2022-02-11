import jieba   #分词
from matplotlib import pyplot as plt    #绘图
from wordcloud import  WordCloud        #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import sqlite3                          #数据库

con = sqlite3.connect("movie1.db")
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
con.close()

#准备分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))
#准备图片
img = Image.open(r'.\static\assets\img\tree.jpg')
img_array = np.array(img) #img --> array
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')
# plt.show()
plt.savefig(r'.\static\assets\img\word.jpg', dpi= 500)