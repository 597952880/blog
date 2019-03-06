#启动和管理项目的相关操作代码
from app import create_app,db
#通过Manager()管理项目,并增加数据迁移指令
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
#导入所有的实体类方便使用db指令做迁移
# from app import models
from app.models import *

#调用create_app得到app实例
app = create_app()
#创建Manager实例用于托管app
manager = Manager(app)
#创建Migrate对象用于关联要管理的app和db
migarate = Migrate(app,db)
#再通过Manager对象增加db迁移指令
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
  #使用Manager实例来启动程序
  manager.run()
  # app.run()







