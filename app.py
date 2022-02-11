from flask import Flask,render_template
import sqlite3
app = Flask(__name__)
#路由解析
#模板渲染
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()

    return render_template('movie.html',movies = datalist)

@app.route('/rating')
def rating():
    scorelist = []
    numberlist = []
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        scorelist.append(item[0])
        numberlist.append(item[1])
    cur.close()
    con.close()

    return render_template('rating.html',scorelist = scorelist, numberlist = numberlist)

@app.route('/wordcloud')
def wordcloud():
    return render_template('wordcloud.html')

@app.route('/team')
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run()
