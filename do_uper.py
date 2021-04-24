from sqlalchemy import Column, String, create_engine,ForeignKey,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


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
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    BASE.to_dict = to_dict


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
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    BASE.to_dict = to_dict


"""
团体领导：leader
    领导身份证号：lssn （p）
    领导姓名：lname
"""
class leader(BASE):
    __tablename__='LEADER'
    lssn = Column(String(18),primary_key=True)
    lname = Column(String(10))
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    BASE.to_dict = to_dict


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
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    BASE.to_dict = to_dict


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
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    BASE.to_dict = to_dict


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
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    BASE.to_dict = to_dict


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
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    BASE.to_dict = to_dict


"""
排行榜：rank
    排名：lno
    作品序号：wno （p） （f：works.wno）
"""
class rank(BASE):
    __tablename__='RANK'
    rno = Column(Integer)
    wno = Column(Integer,ForeignKey("WORKS.wno"),primary_key=True)
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    BASE.to_dict = to_dict



def table_insert(tablename,mlist):
    if tablename=='works':
        if len(mlist)!=3:
            print("表项格式错误！")
        else:
            new_works = works(wname = mlist[0],wno = mlist[1],cname = mlist[2])
            session.add(new_works)

    elif tablename=='collection':
        if len(mlist)!=2:
            print("表项格式错误！")
        else:
            new_collection = collection(cname = mlist[0],lssn = mlist[1])
            session.add(new_collection)

    elif tablename=='team':
        if len(mlist)!=2:
            print("表项格式错误！")
        else:
            new_team = team(tname = mlist[0],lssn = mlist[1])
            session.add(new_team)

    elif tablename=='leader':
        if len(mlist)!=2:
            print("表项格式错误！")
        else:
            new_leader = leader(lssn = mlist[0],lname = mlist[1])
            session.add(new_leader)
    
    elif tablename=='author':
        if len(mlist)!=3:
            print("表项格式错误！")
        else:
            new_author = author(aname = mlist[0],assn = mlist[1],lssn = mlist[2])
            session.add(new_author)

    elif tablename=='spons':
        if len(mlist)!=4:
            print("表项格式错误！")
        else:
            if(int(mlist[3])<0):
                mlist[3] = 0
            new_spons = spons(sno = mlist[0],sssn = mlist[1],wno = mlist[2],amount = mlist[3])
            session.add(new_spons)

    elif tablename=='comments':
        if len(mlist)!=4:
            print("表项格式错误！")
        else:
            new_comments = comments(cno = mlist[0],cssn = mlist[1],cnum = mlist[2],wno = mlist[3])
            session.add(new_comments)

    elif tablename=='rank':
        if len(mlist)!=2:
            print("表项格式错误！")
        else:
            new_rank = rank(rno = mlist[0],wno = mlist[1])
            session.add(new_rank)
    else:
        print("表名错误！")

def table_select(tablename):
    if tablename=='works':
        rows = session.query(works).all()
        for row in rows:
            print(row.to_dict())

    elif tablename=='collection':
        rows = session.query(collection).all()
        for row in rows:
            print(row.to_dict())

    elif tablename=='team':
        rows = session.query(team).all()
        for row in rows:
            print(row.to_dict())

    elif tablename=='leader':
        rows = session.query(leader).all()
        for row in rows:
            print(row.to_dict())
    
    elif tablename=='author':
        rows = session.query(author).all()
        for row in rows:
            print(row.to_dict())

    elif tablename=='spons':
        rows = session.query(spons).all()
        for row in rows:
            print(row.to_dict())

    elif tablename=='comments':
        rows = session.query(comments).all()
        for row in rows:
            print(row.to_dict())

    elif tablename=='rank':
        rows = session.query(rank).all()
        for row in rows:
            print(row.to_dict())
    else:
        print("表名错误！")

def table_delete(tablename,arrange,mlist):
    if tablename=='works':
        if arrange=='wname':
            for part in mlist:
                session.query(works).filter(works.wname==part).delete()
        elif arrange=='wno':
            for part in mlist:
                session.query(works).filter(works.wno==int(part)).delete()
        elif arrange=='cname':
            for part in mlist:
                session.query(works).filter(works.cname==part).delete()
        else:
            print("表"+tablename+"中没有项"+arrange)

    elif tablename=='collection':
        if arrange=='cname':
            for part in mlist:
                session.query(collection).filter(collection.cname==part).delete()
        elif arrange=='lssn':
            for part in mlist:
                session.query(collection).filter(collection.lssn==part).delete()
        else:
            print("表"+tablename+"中没有项"+arrange)

    elif tablename=='team':
        if arrange=='tname':
            for part in mlist:
                session.query(team).filter(team.tname==part).delete()
        elif arrange=='lssn':
            for part in mlist:
                session.query(team).filter(team.lssn==part).delete()
        else:
            print("表"+tablename+"中没有项"+arrange)

    elif tablename=='leader':
        if arrange=='lssn':
            for part in mlist:
                session.query(leader).filter(leader.lssn==part).delete()
        elif arrange=='lname':
            for part in mlist:
                session.query(leader).filter(leader.lname==part).delete()
        else:
            print("表"+tablename+"中没有项"+arrange)
    
    elif tablename=='author':
        if arrange=='aname':
            for part in mlist:
                session.query(author).filter(author.aname==part).delete()
        elif arrange=='assn':
            for part in mlist:
                session.query(author).filter(author.assn==part).delete()
        elif arrange=='lssn':
            for part in mlist:
                session.query(author).filter(author.lssn==part).delete()
        else:
            print("表"+tablename+"中没有项"+arrange)

    elif tablename=='spons':
        if arrange=='sno':
            for part in mlist:
                session.query(spons).filter(spons.sno==int(part)).delete()
        elif arrange=='sssn':
            for part in mlist:
                session.query(spons).filter(spons.sssn==part).delete()
        elif arrange=='wno':
            for part in mlist:
                session.query(spons).filter(spons.wno==int(part)).delete()
        elif arrange=='amount':
            for part in mlist:
                session.query(spons).filter(spons.amount==int(part)).delete()
        else:
            print("表"+tablename+"中没有项"+arrange)

    elif tablename=='comments':
        if arrange=='cno':
            for part in mlist:
                session.query(comments).filter(comments.cno==int(part)).delete()
        elif arrange=='cssn':
            for part in mlist:
                session.query(comments).filter(comments.cssn==part).delete()
        elif arrange=='cnum':
            for part in mlist:
                session.query(comments).filter(comments.cnum==int(part)).delete()
        elif arrange=='wno':
            for part in mlist:
                session.query(comments).filter(comments.wno==int(part)).delete()
        else:
            print("表"+tablename+"中没有项"+arrange)

    elif tablename=='rank':
        if arrange=='rno':
            for part in mlist:
                session.query(rank).filter(rank.rno==int(part)).delete()
        elif arrange=='wno':
            for part in mlist:
                session.query(rank).filter(rank.wno==int(part)).delete()
        else:
            print("表"+tablename+"中没有项"+arrange)
    else:
        print("表名错误！")


try:
    # 连接MySQL数据库，地址：localhost:3306,账号：root,密码：123,数据库：test
    MySQLEngine=create_engine('mysql://root:@localhost/uper?charset=utf8', encoding='utf-8')
    print('连接MySQL数据库成功')
except Exception:
    print('连接数据库失败表')
    exit(0)

DBSession = sessionmaker(bind=MySQLEngine)
session = DBSession()

message = ''

while message!='exit':
    message = input("Input Order: ")
    if message!='exit':
        if message.find("insert")!=-1:
            mlist = message.split()
            tablename = mlist[1]
            mlist = mlist[2:]
            table_insert(tablename,mlist)

        if message.find("select")!=-1:
            #通过作品名查询排名，使用连接查询
            if message.find("rankof")!=-1:
                mlist = message.split()
                wname = mlist[2]
                rows = session.query(rank).join(works).filter(works.wname==wname).all()
                for row in rows:
                    print(row.to_dict())
            elif message.find("allamount")!=-1:
            #查询作品的总赞助量
                #子查询，同时使用分组查询
                rows1 = session.query(spons.wno,func.sum(spons.amount).label('all_amount')).group_by(spons.wno).subquery()
                #父查询
                rows = session.query(works.wname,rows1.c.all_amount).filter(works.wno==rows1.c.wno).all()
                for a,b in rows:
                    print(a,b)
            else:
                mlist = message.split()
                tablename = message[7:]
                print(tablename+':')
                table_select(tablename)
            
        if message.find("delete")!=-1:
            mlist = message.split()
            tablename = mlist[1]
            arrange = mlist[2]
            mlist = mlist[3:]
            table_delete(tablename,arrange,mlist)

        if message.find("change")!=-1:
            mlist = message.split()
            tablename = mlist[1]
            arrange = mlist[2]
            primname = []
            primname.append(mlist[3])
            mlist = mlist[5:]
            table_delete(tablename,arrange,primname)
            table_insert(tablename,mlist)

        if message.find("commit")!=-1:
            try:
                session.commit()
            except Exception:
                print("存在非法操作！")
            session = DBSession()
