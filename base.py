from flask import *
from DBM import *

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("welcome.html")

@app.route("/welcome")
def wel():
    return render_template("welcome.html")

# User details
# Done
@app.route("/register")
def register():
    return render_template("register.html")


# Done
@app.route("/insert",methods=['post'])                  
def ins():
    name=request.form["name"]
    city=request.form["city"]
    email=request.form["email"]
    password=request.form["password"]
    t=(name,city,email,password)
    addUser(t)
    return redirect("/")

# Done
@app.route("/login")
def login():
    return render_template("login.html")

# Done
@app.route("/log",methods=["post"])
def log():
    email1=request.form["email1"]
    password1=request.form["password1"]
    t=(email1,password1)
    t1=selectUserByemail(email1)
    if t in t1:
        return redirect("/details")
    else:
        return redirect("/login")

# done
@app.route("/details")
def details():
    d=selectAllblog()
    return render_template("details.html",elist=d)
     


# Author details
# Registration Done
@app.route("/registera")
def regist():
    return render_template("registera.html")

# Insert Author details
@app.route("/inserta",methods=['post'])
def inser():
    Aname=request.form["aname"]
    Acity=request.form["acity"]
    Aemail=request.form["aemail"]
    Apassword=request.form["apassword"]
    a1=(Aname,Acity,Aemail,Apassword)
    addAut(a1)
    return redirect("/")

# Author login form
@app.route("/logina")
def logina():
    return render_template("logina.html")

# Author login 
@app.route("/loga",methods=["post"])
def loga():
    email2=request.form["email2"]
    password2=request.form["password2"]
    t=(email2,password2)
    t1=selectAuthorByemail(email2)
    if t in t1:
        return redirect("/authorinterface")
    else:
        return redirect("/logina")

@app.route("/authorinterface")
def authorinterface():
    return render_template("authorinterface.html")

@app.route("/addpost")
def addpost():
    return render_template("addpost.html")



# Insert Blog details
@app.route("/addpost",methods=['post'])
def inserBlog():
    Auname=request.form["Author_name"]
    BlogTitle=request.form["Blog_title"]
    Blogs=request.form["Blog"]
    a2=(Auname,BlogTitle,Blogs)
    addBlog(a2)
    return redirect("/addpost")

# Done for edit
@app.route("/edit")
def e():
    Name_edit=request.args.get("Author_name")
    info=sel(Name_edit)
    return render_template("edit.html",elist=info)

# Done for update
@app.route("/update",methods=["post"])
def up():
    Auname=request.form["Author_name"]
    BlogTitle=request.form["Blog_title"]
    Blog=request.form["Blog"]
    t2=(Auname,BlogTitle,Blog)
    updateBlog(t2)
    return redirect("/viewpost")

# done for delete
@app.route("/delete")
def delete():
    em=request.args.get("Author_name")
    deleteBlog(em)
    return redirect("/viewpost")

# done
@app.route("/viewpost")
def Audetails():
    d=selectAllblog()
    return render_template("viewpost.html",elist=d)

# @app.route("/viewpost")
# def viewpost():
#     d=selectAllblog ()
#     return render_template("viewpost.html",elist=d)

# secondchanges
    

if __name__=="__main__":
    app.run(debug=True)
   
