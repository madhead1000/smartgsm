from flask import Flask
from flaskext.mysql import MySQL
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
import os

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Mobiles'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Mobiles'
app.config['SECRET_KEY'] = 'madthing'
db = SQLAlchemy(app)


from app import views, models

if __name__ == '__main__':
    app.run()
