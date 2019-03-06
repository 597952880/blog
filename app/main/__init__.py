#main:处理与博客相关的业务逻辑(主业务)
#如:发表博客,查看博客,删除博客,修改博客,...
#将自己添加到蓝图中
from flask import Blueprint
main = Blueprint("main",__name__)
from .import views