from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
import MySQLdb
from MySQLdb.cursors import DictCursor



def play_2(request):
    print("练习2！");
    conn = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        db = "t_user",
        charset = "utf8"
    )
    cursor = conn.cursor(DictCursor);
    cursor.execute("select name,password from user");
    infos = cursor.fetchall();
    for info in infos:
        print(info);
        temp = loader.get_template("practice2.html");
        content = temp.render(info,request);
    cursor.close();
    conn.close();
    return HttpResponse(content);