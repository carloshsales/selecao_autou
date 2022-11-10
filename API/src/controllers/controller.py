from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import mysql


class IndexController(MethodView):
    def get(self):       
        return render_template("public/index.html")
    
    def post(self):
        login = request.form['login']
        pass
    


class GetAllController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM users")
            data = cur.fetchall()
            
        return render_template("public/dashboard.html", data=data)


        
class RegisterController(MethodView):
    def get(self):      
        return render_template("public/admin/register.html")
    
    def post(self):
        regist = request.form['regist']
        email = request.form['email']
        name = request.form['name']
        last_name = request.form['last_name']
        departament = request.form['departament']
        role = request.form['role']
        image = request.form['image']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s), (regist, email, name, last_name, departament, role, image)")
            cur.connection.commit()
            return redirect('/')
