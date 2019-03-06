#users:处理与用户相关的业务逻辑
#如:注册,登录,... ...
from flask import Blueprint
users = Blueprint("users",__name__)
from . import views