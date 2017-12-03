from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
	__tablename__='user'
	id = Column(String(20),primary_key=True)
	name = Column(String(20))

#create_engine初始化数据库连接，'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'   
engine = create_engine("mysql+mysqlconnector://root:111111@localhost:3306/test")
#创建DBSession类型，并bind上面的连接符
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='5',name='Bob')
new_user1 = User(id='2',name='Anna')
new_user2 = User(id='3',name='Jerry')
new_user3 = User(id='4',name='Mary')
session.add(new_user1)
session.add(new_user2)
session.add(new_user3)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id=='5').one()
print('type:',type(user))
print('id:',user.id)
print('name:',user.name)

session.close()