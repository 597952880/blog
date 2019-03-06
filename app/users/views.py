#处理与用户业务逻辑相关的视图和路由
from . import users
from ..import db
from ..models import *
from flask import render_template,request,session,redirect

@users.route('/login',methods=['GET','POST'])
def login_views():
  if request.method == 'GET':
    return render_template('login.html')
  else:
    #接收前端传递过来的用户名和密码
    loginname = request.form['username']
    upwd = request.form['password']
    #查询数据库,验证用户名和密码是否存在
    user=User.query.filter_by(loginname=loginname,upwd=upwd).first()
    #根据结果保存进session
    if user:
      #登录成功,保存数据进session,并且跳转至首页
      #将id 和 loginname 同时保存进session
      session['id'] = user.ID
      session['loginname'] = loginname
      return redirect('/')
    else:
      #登录失败,返回到登录页面
      return redirect('/login')







