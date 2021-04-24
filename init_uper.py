from sqlalchemy import Column, String, create_engine,ForeignKey,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


"""
作品：works
    作品名：wname
    作品号：wno（p）
    所属作品集：cname （f：collection.cname）
"""
class works(BASE):
    __tablename__ = 'WORKS'
    wname = Column(String(10))
    wno = Column(Integer, primary_key=True)
    cname = Column(ForeignKey("COLLECTION.cname"))
    __table_args__ = {
        "mysql_charset": "utf8"
    }


"""
作品集：collection
    作品集名称：cname （p）
    所属团体领导身份证号：lssn （f：leader.lssn）
"""
class collection(BASE):
    __tablename__='COLLECTION'
    cname = Column(String(10), primary_key=True)
    lssn = Column(String(18), ForeignKey("LEADER.lssn"))
    __table_args__ = {
        "mysql_charset": "utf8"
    }


"""
团体领导：leader
    领导身份证号：lssn （p）
    领导姓名：lname
"""
class leader(BASE):
    __tablename__='LEADER'
    lssn = Column(String(18),primary_key=True)
    lname = Column(String(10),unique=True)
    __table_args__ = {
        "mysql_charset": "utf8"
    }


"""
创作团体：group
    团体名：tname
    领导身份证号：lssn （p）（f：leader.lssn）
"""
class team(BASE):
    __tablename__='TEAM'
    tname = Column(String(10))
    lssn = Column(String(18),ForeignKey("LEADER.lssn"),primary_key=True)
    __table_args__ = {
        "mysql_charset": "utf8"
    }


"""
作者：author
    作者名：aname
    作者身份证号：assn （p）
    作者所属团体领导身份证号：lssn （f：leader.lssn） 
"""
class author(BASE):
    __tablename__='AUTHOR'
    aname = Column(String(10))
    assn = Column(String(18),primary_key=True)
    lssn = Column(String(18),ForeignKey("LEADER.lssn"))
    __table_args__ = {
        "mysql_charset": "utf8"
    }


"""
赞助：spons
    赞助序号：sno （p）
    赞助者身份证号：sssn
    赞助作品号：wno （f：works.wno）
    赞助金额：amount
"""
class spons(BASE):
    __tablename__='SPONS'
    sno = Column(Integer,primary_key=True)
    sssn = Column(String(18))
    wno = Column(Integer,ForeignKey("WORKS.wno"))
    amount = Column(Integer)
    __table_args__ = {
        "mysql_charset": "utf8"
    }


"""
评分：comments
    评分序号：cno （p）
    评论者身份证号：cssn
    评分：cnum
    评分作品号：wno （f：works.wno）
"""
class comments(BASE):
    __tablename__='COMMENTS'
    cno = Column(Integer,primary_key=True)
    cssn = Column(String(18))
    cnum = Column(Integer)
    wno = Column(ForeignKey("WORKS.wno"))
    __table_args__ = {
        "mysql_charset": "utf8"
    }


"""
排行榜：rank
    排名：rno
    作品序号：wno （p） （f：works.wno）
"""
class rank(BASE):
    __tablename__='RANK'
    rno = Column(Integer)
    wno = Column(Integer,ForeignKey("WORKS.wno"),primary_key=True)
    __table_args__ = {
        "mysql_charset": "utf8"
    }




"""
class Student(BASE):
    # 表的名字:STUDENT
    __tablename__ = 'STUDENT'
    # 学号
    sno = Column(String(10))
    # 姓名
    sname = Column(String(20), primary_key=True)
    # 创建表的参数
    __table_args__ = {
        "mysql_charset": "utf8"
    }

class Classroom(BASE):
    __tablename__ = 'CLASSROOM'
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(20),ForeignKey("STUDENT.sname"))
    __table_args__ = {
        "mysql_charset": "utf8"   
    }
"""

try:
    # 连接MySQL数据库，地址：localhost:3306,账号：root,密码：123,数据库：test
    MySQLEngine=create_engine('mysql://root:@localhost/uper?charset=utf8', encoding='utf-8')
    #print('连接MySQL数据库成功', MySQLEngine)
    BASE.metadata.create_all(MySQLEngine)
except Exception as e:
    print('连接数据库失败表', e)
