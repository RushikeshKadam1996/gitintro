import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='azkbatch')

# user details   
def addUser(t):
    db=getConnection()
    sql='insert into user values(%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

# Done show all posts
def selectAllblog():
    db=getConnection()
    sql='select * from blog'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

# done for user login
def selectUserByemail(email):
    db=getConnection()
    sql='select email,password from user where email=%s'
    cr=db.cursor()
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data



# Author details
# Done for Author registration
def addAut(a1):
    db=getConnection()
    sql='insert into author values(%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,a1)
    db.commit()
    db.close()

# Done for Author login
def selectAuthorByemail(emaila):
    db=getConnection()
    sql='select aemail,apassword from author where aemail=%s'
    cr=db.cursor()
    cr.execute(sql,emaila)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

# Blog details
# insert blog
def addBlog(a2):
    db=getConnection()
    sql='insert into blog values(%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,a2)
    db.commit()
    db.close()

# Done (Edit button)
def sel(e):
    db=getConnection()
    sql='select * from blog where Author_name=%s'
    cr=db.cursor()
    cr.execute(sql,e)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data[0]

# Done for (update details)
def updateBlog(t2):
    db=getConnection()
    sql='update blog set Author_name=%s,Blog_title=%s,Blog=%s where Author_name=%s'
    cr=db.cursor()
    cr.execute(sql,t2)
    db.commit()
    db.close()

# done for delete
def deleteBlog(id):
    db=getConnection()
    sql='delete from blog where Author_name=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

# Done
def selectAllblog():
    db=getConnection()
    sql='select * from blog'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist



















