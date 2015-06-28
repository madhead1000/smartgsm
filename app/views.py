from flask import request, redirect, render_template, url_for,jsonify,session, current_app,g
from app import app, mysql
from app.models import Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum,Comments,Replies,News,Comments_news,Replies_news
from app import db
from flask.ext.paginate import Pagination
from app.forms import CommentForm,TipusForm
import datetime
from  sqlalchemy.sql.expression import func, select
import re
###
# Search.
###
@app.route('/related', methods=["POST", "GET"])
def relate():
  if request.method=='GET':
    brand = request.args.get('brand', "", type=str)
    phon = ""
    phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
              ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
    for phone in phones:
      if not phon:
        phon = db.session.query(phone).filter_by(Brand=brand).order_by(func.random()).all()
  return render_template('related.html',phone=phon, brand=brand)

@app.route('/latest_news', methods=["POST", "GET"])
def latest_news():
  if request.method=='GET':
    latest_news = db.session.query(News).all()
  return render_template('latest_news.html',latest_news=latest_news)

@app.route('/search', methods=["POST", "GET"])
def search():
  if request.method=='POST':
    search_text = request.form['search_text']
  else:
    search_text = ""
  phon = ""
  phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
            ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
  for phone in phones:
    if not phon:
      phon = db.session.query(phone).filter(phone.Name.like('%'+search_text+'%')).all()
  return render_template('search.html',phone=phon, search_text=search_text)

@app.route('/compare_search', methods=["POST", "GET"])
def comp_search():
  if request.method=='POST':
    search_text = request.form['compare_search_text']
  else:
    search_text = ""
  phon = []
  phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
            ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
  for phone in phones:
    if not phon:
      phon = db.session.query(phone).filter(phone.Name.like('%'+search_text+'%')).all()
  return render_template('compare_search.html',phone=phon,search_text=search_text)

@app.route('/compare_search1', methods=["POST", "GET"])
def comp_search1():
  if request.method=='POST':
    search_text = request.form['compare_search_text']
    id1 = request.form['id1']
  else:
    search_text = ""
  phon = []
  phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
            ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
  for phone in phones:
    if not phon:
      phon = db.session.query(phone).filter(phone.Name.like('%'+search_text+'%')).all()
  return render_template('compare_search1.html',phone=phon,search_text=search_text,id1=id1)

@app.route('/compare_search2', methods=["POST", "GET"])
def comp_search2():
  if request.method=='POST':
    search_text = request.form['compare_search_text']
    id = request.form['id']
  else:
    search_text = ""
  phon = []
  phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
            ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
  for phone in phones:
    if not phon:
      phon = db.session.query(phone).filter(phone.Name.like('%'+search_text+'%')).all()
  return render_template('compare_search2.html',phone=phon,search_text=search_text,id=id)

###
# Phone Specification by id.
###

@app.route('/specs/<id>', methods=["GET"])
def specs(id):
  phon = ""
  phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
            ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
  for phone in phones:
    if not phon:
      phon = db.session.query(phone).filter_by(phoneId=id).first()
      comments = Comments.query.filter_by(phoneId=id).all()
      count = Comments.query.filter_by(phoneId=id).count()
  return render_template('specs.html', phone=phon,comments=comments, id=id, count=count)

###
# Compare phones by id.
###
@app.route('/compare/<id>', methods=["GET", "POST"])
def compare(id):
  phon = ""
  phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
            ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
  for phone in phones:
    if not phon:
      phon = db.session.query(phone).filter_by(phoneId=id).first()
  phones = Apple.query.filter_by(phoneId = "").first()
  return render_template('compare.html', phone=phon, phones=phones,id=id)

@app.route('/compare/<id>/<id1>', methods=["GET", "POST"])
def compares(id,id1):
  phon = ""
  phons = ""
  phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
            ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
  for phone in phones:
    if not phon:
      phon = db.session.query(phone).filter_by(phoneId=id).first()
  for phone in phones:
    if not phons:
      phons = db.session.query(phone).filter_by(phoneId=id1).first()
  if phone:
    return render_template('compare.html', phone=phon, phones=phons,id=id,id1=id1)
  return render_template('404.html')

###
# list phones by brand.
###

@app.route('/phones/<brand>', methods=["GET"])
def mobiles(brand, page=1):
    cur = mysql.connect().cursor()
    cur.execute("select count(*) from %s" % (brand))
    total = cur.fetchone()[0]
    page, per_page, offset = get_page_items()
    sql = "select phoneId, Name, Picture, OS, Announced, Type, `Primary`, WLAN, GPS,Bluetooth from %s order by name limit {}, {}".format(offset, per_page) % (brand)
    cur.execute(sql)
    phones = cur.fetchall()
    pagination = get_pagination(page=page, per_page=per_page, total=total, record_name='phones', format_total=True, format_number=True)
    return render_template('phones.html', phones=phones,page=page, per_page=per_page, pagination=pagination,brand=brand)
    
###
# Phone Comments.
###
@app.route('/comments/<id>', methods=["GET"])
def comments(id, page=1):
  cur = mysql.connect().cursor()
  cur.execute("select count(*) from Comments where phoneId = %s" % (id))
  total = cur.fetchone()[0]
  page, per_page, offset = get_page_items()
  phon = ""
  phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
            ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
  for phone in phones:
    if not phon:
      phon = db.session.query(phone).filter_by(phoneId=id).first()
  sql = "select * from Comments where phoneId=%s order by id limit {}, {}".format(offset, per_page) % (id)
  cur.execute(sql)
  comments = cur.fetchall()
  count = Comments.query.filter_by(phoneId=id).count()
  pagination = get_pagination(page=page, per_page=per_page, total=total, record_name='comments', format_total=True, format_number=True)
  return render_template('comments.html',phone=phon,comments=comments, id=id, count=count,page=page, per_page=per_page, pagination=pagination)

@app.route('/comment/<id>', methods=["GET", "POST"])
def comment(id):
  form = CommentForm()
  phon = ""
  phones = [Samsung,Apple,Microsoft,Nokia,Sony,LG,HTC,Motorola,Huawei,Lenovo,Xiaomi,Acer,Asus,Oppo,Blackberry,Alcatel,
            ZTE,Toshiba,Gigabyte,Pantech,XOLO,Lava,Micromax,BLU,Spice,Verykool,Maxwest,Celkon,Gionee,Vivo,NIU,Yezz,Parla,Plum]
  for phone in phones:
    if not phon:
      phon = db.session.query(phone).filter_by(phoneId=id).first()
  if form.validate():
    comment = Comments(id,datetime.datetime.now(),form.body.data,form.author.data)
    db.session.add(comment)
    db.session.commit()
  return render_template('comment.html',phone=phon,form=form)

###
# News.
###
@app.route('/news')
def new(page=1):
  cur = mysql.connect().cursor()
  cur.execute("select count(*) from news")
  total = cur.fetchone()[0]
  page, per_page, offset = get_page_items()
  sql = "select * from news order by id limit {}, {}".format(offset, per_page)
  cur.execute(sql)
  news = cur.fetchall()
  pagination = get_pagination(page=page, per_page=per_page, total=total, record_name='news', format_total=True, format_number=True)
  for new in news:
    p = re.compile(r'<.*?>')
    return render_template('all_news.html',news=news,p=p,page=page, per_page=per_page, pagination=pagination)

def count_comments(id,count=0):
  comment = Comments_news.query.filter_by(newsid=id).all()
  for comment in comment:
    count = Comments_news.query.filter_by(newsid=id).count()+Replies_news.query.filter_by(ids=comment.id).count()
  return count
app.jinja_env.globals.update(count_comments=count_comments)

@app.route('/news/<id>')
def news(id):
  news = db.session.query(News).filter_by(newsid=id).first()
  comments = Comments_news.query.filter_by(newsid=id).all()
  p = re.compile(r'<.*?>')
  new = p.sub('', news.Content)
  new = re.sub("\s\s+" , " ", new)
  return render_template('news.html',news=news,new=new)

@app.route('/news/comment/<id>', methods=["GET", "POST"])
def news_comment(id):
  form = CommentForm()
  cur = mysql.connect().cursor()
  sql = "select newsid, Picture, Content, Name from news WHERE newsid=%s" %(id)
  cur.execute(sql)
  news = cur.fetchone()
  p = re.compile(r'<.*?>')
  new = p.sub('', news[2])
  if form.validate():
    comment = Comments_news(newsid=id,created_at=datetime.datetime.now(),body=form.body.data,author=form.author.data)
    db.session.add(comment)
    db.session.commit()
  return render_template('news_comment.html',news=news,new=new,form=form)

@app.route('/news/replies/<id>', methods=["GET", "POST"])
def news_replies(id):
  form = CommentForm()
  comments = Comments_news.query.filter_by(id=id).first()
  if form.validate():
    reply = Replies_news(datetime.datetime.now(),form.body.data,form.author.data,id)
    db.session.add(reply)
    db.session.commit()
  return render_template('news_comment.html',comment=comments,form=form)

@app.route('/news/comments/<id>')
def news_comments(id,page=1):
  cur = mysql.connect().cursor()
  cur.execute("select count(*) from Comments_news where newsid = %s" % (id))
  total = cur.fetchone()[0]
  page, per_page, offset = get_page_items()
  sql = "select * from Comments_news where newsid=%s order by id limit {}, {}".format(offset, per_page) % (id)
  cur.execute(sql)
  comments = cur.fetchall()
  news = News.query.filter_by(newsid=id).first()
  p = re.compile(r'<.*?>')
  new = p.sub('', news.Content)
  pagination = get_pagination(page=page, per_page=per_page, total=total, record_name='news_comments', format_total=True, format_number=True)
  count = 0
  comm = Comments_news.query.filter_by(newsid=id).all()
  if comm:
    for comment in comm:
      count = Comments_news.query.filter_by(newsid=id).count()+Replies_news.query.filter_by(ids=comment.id).count()
  return render_template('news_comments.html',news=news,new=new,comments=comments,count=count,page=page, per_page=per_page, pagination=pagination)

###
# micilanious.
###
@app.route('/advertise')
def advert():
  return render_template('advertising.html')

@app.route('/privacy')
def privacy():
  return render_template('privacy.html')

@app.route('/terms')
def terms():
  return render_template('terms.html')

@app.route('/faq')
def faq():
  return render_template('faq.html')

@app.route('/')
def home():
  news = News.query.all()
  phones=Toshiba.query.all()
  for new in news:
    p = re.compile(r'<.*?>')
  return render_template('home.html',news=news,new=new,p=p,phones=phones)


@app.route('/contact/')
def contact():
    """Render the website's about page."""
    return render_template('contact.html')

@app.route('/tipus/')
def tip():
    form = TipusForm()
    if form.validate():
      tip = Tip(form.name.data,form.email.data,form.subject.dataform.body.data)
      db.session.add(tip)
      db.session.commit()
    """Render the website's about page."""
    return render_template('tipus.html',form=form)
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def get_css_framework():
    return current_app.config.get('CSS_FRAMEWORK', 'bootstrap3')


def get_link_size():
    return current_app.config.get('LINK_SIZE', 'sm')


def show_single_page_or_not():
    return current_app.config.get('SHOW_SINGLE_PAGE', False)


def get_page_items():
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page')
    if not per_page:
        per_page = current_app.config.get('PER_PAGE', 1)
    else:
        per_page = int(per_page)

    offset = (page - 1) * per_page
    return page, per_page, offset


def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'records')
    return Pagination(css_framework=get_css_framework(),
                      link_size=get_link_size(),
                      show_single_page=show_single_page_or_not(),
                      **kwargs
                      )

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")