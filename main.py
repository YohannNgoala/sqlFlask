import form as form
import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= Display

@app.route('/display/admin')
def display_admin():
    title = "Admin"
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from admin")
    data = cursor.fetchall()
    print(data)
    return render_template("list.html", data=data, title=title)

@app.route('/display/course')
def display_course():
    title = "Course"
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from course")
    data = cursor.fetchall()
    return render_template("list.html", data=data, title=title)

@app.route('/display/grade')
def display_grade():
    title = "Grade"
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from grade")
    data = cursor.fetchall()
    return render_template("list.html", data=data, title=title)

@app.route('/display/role')
def display_role():
    title = "Role"
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from role")
    data = cursor.fetchall()
    return render_template("list.html", data=data, title=title)

@app.route('/display/role_right')
def display_role_right():
    title = "RoleRight"
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from role_right")
    data = cursor.fetchall()
    return render_template("list.html", data=data, title=title)

@app.route('/display/student')
def display_student():
    title = "Student"
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from student")
    data = cursor.fetchall()
    return render_template("list.html", data=data, title=title)

@app.route('/display/student_course')
def display_student_course():
    title = "StudentCourse"
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from student_course")
    data = cursor.fetchall()
    return render_template("list.html", data=data, title=title)

@app.route('/display/speciality')
def display_speciality():
    title = "Speciality"
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from speciality")
    data = cursor.fetchall()
    return render_template("list.html", data=data, title=title)

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= CREATE
@app.route('/create/admin', methods=['GET', 'POST'])
def redirection_create_admin():
    return render_template("/Create/create_admin.html")

@app.route('/create/admin/success',methods=['GET', 'POST'])
def create_admin():
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    mail = request.form['mail']
    phone = request.form['phone']
    dob = request.form['dob']
    speciality_id = request.form['specialityId']
    role_id = request.form['roleId']
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("insert into admin (first_name,last_name,mail,phone,dob,speciality_id,role_id) "
                   "values (%s, %s, %s, %s, %s, %s, %s);",
                   (first_name, last_name, mail, phone, dob, speciality_id, role_id))
    mydb.commit()
    return render_template("success.html")

@app.route('/create/course', methods=['GET', 'POST'])
def redirection_create_course():
    return render_template("Create/create_course.html")

@app.route('/create/course/success',methods=['GET', 'POST'])
def create_course():
    name = request.form['name']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    admin_id = request.form['admin_id']
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("insert into course (name,start_time,end_time,admin_id) "
                   "values (%s, %s, %s, %s);",
                   (name, start_time, end_time, admin_id))
    mydb.commit()
    return render_template("success.html")

@app.route('/create/grade', methods=['GET', 'POST'])
def redirection_create_grade():
    return render_template("Create/create_grade.html")

@app.route('/create/grade/success',methods=['GET', 'POST'])
def create_grade():
    student_id = request.form['student_id']
    speciality_id = request.form['speciality_id']
    mark = request.form['mark']
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("insert into grade (student_id, speciality_id, mark) values (%s,%s,%s);",
                   (student_id, speciality_id, mark))
    mydb.commit()
    return render_template("success.html")
@app.route('/create/role', methods=['GET', 'POST'])
def redirection_create_role():
    return render_template("Create/create_role.html")

@app.route('/create/role/success',methods=['GET', 'POST'])
def create_role():
    libelle = request.form['libelle']
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("insert into role (libelle) "
                   "values ('%s');"
                   % libelle)
    mydb.commit()
    return render_template("success.html")

@app.route('/create/role_right', methods=['GET', 'POST'])
def redirection_create_role_right():
    return render_template("Create/create_role_right.html")

@app.route('/create/role_right/success',methods=['GET', 'POST'])
def create_role_right():
    libelle = request.form['libelle']
    role_id = request.form['role_id']
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("insert into role_right (libelle,role_id) "
                   "values ('%s', %s);",
                   (libelle, role_id))
    mydb.commit()
    return render_template("success.html")


@app.route('/create/speciality', methods=['GET', 'POST'])
def redirection_create_speciality():
    return render_template("Create/create_speciality.html")

@app.route('/create/speciality/success',methods=['GET', 'POST'])
def create_speciality():
    libelle = request.form['libelle']

    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("insert into speciality (libelle) "
                   "values ('%s');"
                   % libelle)
    mydb.commit()
    return render_template("success.html")

@app.route('/create/student', methods=['GET', 'POST'])
def redirection_create_student():
    return render_template("Create/create_student.html")

@app.route('/create/student/success',methods=['GET', 'POST'])
def create_student():
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    mail = request.form['mail']
    phone = request.form['phone']
    dob = request.form['dob']
    gpa = request.form['gpa']
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("insert into student (first_name,last_name,mail,phone,dob,gpa) "
                   "values (%s, %s, %s, %s, %s, %s);",
                   (first_name, last_name, mail, phone, dob, gpa))
    mydb.commit()
    return render_template("success.html")

@app.route('/create/student_course', methods=['GET', 'POST'])
def redirection_create_student_course():
    return render_template("Create/create_student_course.html")

@app.route('/create/student_course/success',methods=['GET', 'POST'])
def create_student_course():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("insert into student_course (student_id,course_id) "
                   "values (%s, %s);",
                   (student_id, course_id))
    mydb.commit()
    return render_template("success.html")


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= UPDATE
@app.route('/fupdate/<title>/<id>')
def redirect_update(title, id):
    if title == 'Admin':
        return (redirect_update_admin(id))
    else:
        return "UP¨NON"

@app.route('/update/admin/<id>', methods=['GET'])
def redirect_update_admin(id):
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from admin where admin_id = %s;" % id)
    data = cursor.fetchall()
    return render_template("update_admin.html", data=data, id=id)

@app.route('/update/success/<id>',methods=['GET', 'POST'])
def update_admin(id):
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    mail = request.form['mail']
    phone = request.form['phone']
    dob = request.form['dob']
    speciality_id = request.form['specialityId']
    role_id = request.form['roleId']
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("update admin set "
                   "first_name = '%s',"
                   "last_name = '%s',"
                   "mail = '%s',"
                   "phone = '%s',"
                   "dob = '%s',"
                   "speciality_id = %s,"
                   "role_id = %s "
                   "where admin_id = %s;" %
                   (first_name, last_name, mail, phone, dob, speciality_id, role_id, id))
    mydb.commit()
    return render_template("success.html")

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= REMOVE

@app.route('/fremove/<title>/<id>')
def redirect_remove(title, id):
    if title == 'Admin':
        return redirect_remove_admin(id)
    if title == 'Course':
        return redirect_remove_course(id)
    if title == 'Grade':
        return redirect_remove_grade(id)
    if title == 'Role':
        return redirect_remove_role(id)
    if title == 'RoleRight':
        return redirect_remove_role_right(id)
    if title == 'Speciality':
        return redirect_remove_speciality(id)
    if title == 'Student':
        return redirect_remove_student(id)
    if title == 'StudentCourse':
        return redirect_remove_student_course(id)
    else:
        return "REMOVE NOPE"

@app.route('/remove/admin/<id>', methods=['GET'])
def redirect_remove_admin(id):
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from admin where admin_id = %s;" % id)
    data = cursor.fetchall()
    return render_template("Remove/remove_admin.html", data=data, id=id)



@app.route('/remove/admin/success/<id>',methods=['GET', 'POST'])
def remove_admin(id):
        mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
        cursor = mydb.cursor()
        cursor.execute("select course_id from course where admin_id = %s" %  id)
        courseList = cursor.fetchall()
        for c in courseList:
            cursor.execute("delete from student_course where course_id = %s;" % c[0])
        cursor.execute("delete from course where admin_id = %s;" % id)
        cursor.execute("delete from admin where admin_id = %s;" % id)
        mydb.commit()
        return render_template("success.html")


@app.route('/remove/course/<id>', methods=['GET'])
def redirect_remove_course(id):
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from course where course_id = %s;" % id)
    data = cursor.fetchall()
    return render_template("Remove/remove_course.html", data=data, id=id)



@app.route('/remove/course/success/<id>',methods=['GET', 'POST'])
def remove_course(id):
        mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
        cursor = mydb.cursor()
        cursor.execute("delete from student_course where course_id = %s;" % id)
        cursor.execute("delete from course where course_id = %s;" % id)
        mydb.commit()
        return render_template("success.html")


@app.route('/remove/grade/<id>', methods=['GET'])
def redirect_remove_grade(id):
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from grade where grade_id = %s;" % id)
    data = cursor.fetchall()
    return render_template("Remove/remove_grade.html", data=data, id=id)



@app.route('/remove/grade/success/<id>',methods=['GET', 'POST'])
def remove_grade(id):
        mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
        cursor = mydb.cursor()
        cursor.execute("delete from grade where grade_id = %s;" % id)
        mydb.commit()
        return render_template("success.html")


@app.route('/remove/role/<id>', methods=['GET'])
def redirect_remove_role(id):
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from role where role_id = %s;" % id)
    data = cursor.fetchall()
    return render_template("Remove/remove_role.html", data=data, id=id)



@app.route('/remove/role/success/<id>',methods=['GET', 'POST'])
def remove_role(id):
        mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
        cursor = mydb.cursor()
        cursor.execute("select * from admin where role_id = %s" % id)
        adminList = cursor.fetchall()
        for c in adminList:
            cursor.execute("select course_id from course where admin_id = %s" % c[0])
            courseList = cursor.fetchall()
            for cl in courseList:
                cursor.execute("delete from student_course where course_id = %s;" % cl[0])
            cursor.execute("delete from course where admin_id = %s" % c[0])
        cursor.execute("delete from admin where role_id = %s" %id)
        cursor.execute("delete from role_right where role_id = %s" %id)
        cursor.execute("delete from role where role_id = %s;" %id)
        mydb.commit()
        return render_template("success.html")



@app.route('/remove/role_right/<id>', methods=['GET'])
def redirect_remove_role_right(id):
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from role_right where right_id = %s;" % id)
    data = cursor.fetchall()
    return render_template("Remove/remove_role_right.html", data=data, id=id)



@app.route('/remove/role_right/success/<id>',methods=['GET', 'POST'])
def remove_role_right(id):
        mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
        cursor = mydb.cursor()
        cursor.execute("delete from role_right where right_id = %s;" % id)
        mydb.commit()
        return render_template("success.html")


@app.route('/remove/speciality/<id>', methods=['GET'])
def redirect_remove_speciality(id):
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from speciality where speciality_id = %s;" % id)
    data = cursor.fetchall()
    return render_template("Remove/remove_speciality.html", data=data, id=id)



@app.route('/remove/speciality/success/<id>',methods=['GET', 'POST'])
def remove_speciality(id):
        mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
        cursor = mydb.cursor()
        cursor.execute("select * from admin where speciality_id = %s" % id)
        adminList = cursor.fetchall()
        for c in adminList:
            cursor.execute("select course_id from course where admin_id = %s" % c[0])
            courseList = cursor.fetchall()
            for cl in courseList:
                cursor.execute("delete from student_course where course_id = %s;" % cl[0])
            cursor.execute("delete from course where admin_id = %s" % c[0])
        cursor.execute("delete from admin where speciality_id = %s" %id)
        cursor.execute("delete from grade where speciality_id = %s" %id)
        cursor.execute("delete from speciality where speciality_id = %s;" %id)
        mydb.commit()
        return render_template("success.html")

@app.route('/remove/student/<id>', methods=['GET'])
def redirect_remove_student(id):
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from student where student_id = %s;" % id)
    data = cursor.fetchall()
    return render_template("Remove/remove_student.html", data=data, id=id)



@app.route('/remove/student/success/<id>',methods=['GET', 'POST'])
def remove_student(id):
        mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
        cursor = mydb.cursor()
        cursor.execute("delete from grade where student_id = %s" % id)
        cursor.execute("delete from student_course where student_id = %s" % id)
        cursor.execute("delete from student where student_id = %s;" % id)
        mydb.commit()
        return render_template("success.html")

@app.route('/remove/student_course/<id>', methods=['GET'])
def redirect_remove_student_course(id):
    mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
    cursor = mydb.cursor()
    cursor.execute("select * from student_course where student_course_id = %s;" % id)
    data = cursor.fetchall()
    return render_template("Remove/remove_student_course.html", data=data, id=id)



@app.route('/remove/student_course/success/<id>',methods=['GET', 'POST'])
def remove_student_course(id):
        mydb = mysql.connector.connect(user='root', host='127.0.0.1', port='3306', database='flaskprojectdb')
        cursor = mydb.cursor()
        cursor.execute("delete from student_course where student_course_id = %s;" % id)
        mydb.commit()
        return render_template("success.html")

@app.route("/")
def show_index():
   return render_template("index.html")