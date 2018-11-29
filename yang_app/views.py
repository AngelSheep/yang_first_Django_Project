import MySQLdb
from MySQLdb.cursors import DictCursor
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def comeon_yy(request):
    print("这是我的第一个Django项目，哈哈~~~");
    idd = request.GET.get("id");
    print(type(idd),idd)
    conn = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        db = "python-mysql-db",
        charset = "utf8"
    )
    cursor = conn.cursor(DictCursor);
    cursor.execute("select id,title,note from t_dept");
    infos = cursor.fetchall();
    conn.commit();
    for info in infos:
        print("部门id:",info.get("id"));
        print("部门名称:",info.get("title"));
        print("部门描述:",info.get("note"));
        temp = loader.get_template("hello_yang.html");
        content = temp.render(info,request);
    return HttpResponse(content);

# 测试1
def test1(request):
    print("我是app下的test1")
    return HttpResponse("我是yang_app下的test1")

def test2(request):
    print("我是app下的test2")
    return HttpResponse("我是app下的test2")

def testyy(request):
    pass