#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: guanguan

from datetime import datetime
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())



if __name__ == '__main__':
    manager.run()
