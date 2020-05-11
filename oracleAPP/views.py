from django.shortcuts import render, redirect
import cx_Oracle
from django.db import models
# Create your views here.
def sel(request):

    return render(request,'main.html',{})

def first(request):
    return render(request,'first.html',{})

def firstProc(request):
    if request.method == 'GET':
        return redirect(request.GET['year']+'/'+request.GET['term']);

def firstExact(request,year, term):
    con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
    c = con.cursor();

    c.execute('SELECT * FROM task1 WHERE year = '+str(year)+' AND semester = '+str(term)+' ORDER BY numberOf DESC')

    obj = [];
    for i in c:
        obj.append(list(i));
    context = {'obj': obj,'year': year,'term': term}
    return render(request, 'firstExact.html', context)


def second(request):
    return render(request,'second.html',{})

def secondProc(request):
    if request.method == 'GET':
        return redirect(request.GET['year']+'/'+request.GET['term']+'/'+request.GET['ders_kod']);

def secondExact(request,year, term,ders_kod):
    con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
    c = con.cursor();

    c.execute('SELECT practice, COUNT(*) as numberOf FROM course_selections WHERE year = '+str(year)+' AND term = '+str(term)+' and ders_kod = \''+ders_kod+'\' AND practice IS NOT NULL GROUP BY practice ORDER BY numberOf DESC')

    obj = [];
    for i in c:
        obj.append(list(i));


    context = {'obj': obj,'year': year,'term': term,'ders_kod': ders_kod}
    return render(request, 'secondExact.html', context)

def third(request):
    return render(request,'third.html',{})

def thirdProc(request):
    if request.method == 'GET':
        return redirect(request.GET['year']+'/'+request.GET['term']+'/'+request.GET['stud_id']);

def thirdExact(request,year, term,stud_id):
    con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
    c = con.cursor();

    c.execute('SELECT stud_id, SUM(credits*getGr(qiymet_herf))/SUM(credits) FROM course_selections INNER JOIN course_sections ON course_sections.ders_kod = course_selections.ders_kod WHERE course_selections.year='+str(year) +' AND course_selections.term = '+str(term)+' AND stud_id =\''+stud_id+'\' GROUP BY stud_id')

    obj = [];
    for i in c:
        obj.append(list(i));

    c.execute('SELECT stud_id, gpa FROM task3 WHERE stud_id = \'' + stud_id+'\'')
    obj1 = [];
    for i in c:
        obj1.append(list(i));

    context = {'obj': obj,'obj1':obj1, 'year': year,'term': term,'stud_id': stud_id}
    return render(request, 'thirdExact.html', context)

def fifth(request):
    return render(request,'fifth.html',{})

def fifthProc(request):
    if request.method == 'GET':
        return redirect(request.GET['year']+'/'+request.GET['term']+'/'+request.GET['stud_id']);

def fifthExact(request,year, term,stud_id):
    con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
    c = con.cursor();

    c.execute('SELECT DISTINCT stud_id, course_selections.year, course_selections.term, course_selections.ders_kod, credits, qiymet_yuz FROM course_selections INNER JOIN course_sections ON course_selections.ders_kod = course_sections.ders_kod WHERE stud_id = \''+stud_id+'\' and course_selections.year = '+str(year)+' and course_selections.term = '+str(term)+' AND qiymet_yuz<50')

    obj = [];
    for i in c:
        obj.append(list(i)[4]);
    priceSem = sum(obj)*25000;

    c.execute('SELECT DISTINCT stud_id, course_selections.year, course_selections.term, course_selections.ders_kod, credits, qiymet_yuz FROM course_selections INNER JOIN course_sections ON course_selections.ders_kod = course_sections.ders_kod WHERE stud_id = \''+stud_id+'\' AND qiymet_yuz<50')
    obj1 = [];
    for i in c:
        obj1.append(list(i)[4]);
    priceTot = sum(obj1) * 25000;

    context = {'studId':stud_id,'priceSem': priceSem,'priceTot':priceTot}
    return render(request, 'fifthExact.html', context)


def sixth(request):
    return render(request,'sixth.html',{})

def sixthProc(request):
    if request.method == 'GET':
        return redirect(request.GET['year']+'/'+request.GET['term']+'/'+request.GET['emp_id']);

def sixthExact(request,year, term, emp_id):
    con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
    c = con.cursor();
    c.execute('SELECT DISTINCT * FROM task6 WHERE year = '+str(year)+' AND semester = '+str(term)+' AND emp_id = '+emp_id);

    obj = []

    for i in c:
        obj.append(list(i))

    print(obj)

    context = {'empId':emp_id,'obj': obj}
    return render(request, 'sixthExact.html', context)

def seventh(request):
    return render(request,'seventh.html',{})

def seventhProc(request):
    if request.method == 'GET':
        return redirect(request.GET['year']+'/'+request.GET['term']+'/'+request.GET['emp_id']);

def seventhExact(request,year, term, emp_id):
    con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
    c = con.cursor();
    c.execute('SELECT DISTINCT emp_id, course_sections.year, course_sections.term, course_sections.ders_kod, min_start_time FROM course_sections INNER JOIN course_schedule ON course_sections.ders_kod = course_schedule.ders_kod WHERE  emp_id = {} and course_sections.year = {} and course_sections.term = {}'.format(emp_id,year,term));
    print('SELECT DISTINCT emp_id, course_sections.year, course_sections.term, course_sections.ders_kod, min_start_time FROM course_sections INNER JOIN course_schedule ON course_sections.ders_kod = course_schedule.ders_kod WHERE  emp_id = {} and course_sections.year = {} and course_sections.term = {}'.format(emp_id,year,term))
    obj = []

    for i in c:
        obj.append(list(i))

    print(obj)

    context = {'empId':emp_id,'obj': obj,'year': year,'term':term}
    return render(request, 'seventhExact.html', context)

def eighth(request):
    return render(request,'eighth.html',{})

def eighthProc(request):
    if request.method == 'GET':
        return redirect(request.GET['year']+'/'+request.GET['term']+'/'+request.GET['stud_id']);

def eighthExact(request,year, term, stud_id):
    con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
    c = con.cursor();
    c.execute('SELECT DISTINCT stud_id, course_selections.year, course_selections.term, course_selections.ders_kod, min_start_time FROM course_selections INNER JOIN course_schedule ON course_selections.ders_kod = course_schedule.ders_kod WHERE stud_id = \'{}\' and course_selections.year = {} and course_selections.term = {}'.format(stud_id,year,term))

    obj = []

    for i in c:
        obj.append(list(i))


    context = {'studId':stud_id,'obj': obj,'year': year,'term':term}
    return render(request, 'eighthExact.html', context)

def nineth(request):
    return render(request,'nineth.html',{})

def ninethProc(request):
    if request.method == 'GET':
        return redirect(request.GET['year']+'/'+request.GET['term']+'/'+request.GET['stud_id']);

def ninethExact(request,year, term, stud_id):
    con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
    c = con.cursor();
    c.execute('SELECT DISTINCT stud_id, course_selections.year, course_selections.term,course_selections.ders_kod, credits, qiymet_yuz FROM course_selections INNER JOIN course_sections ON course_selections.ders_kod = course_sections.ders_kod WHERE stud_id = \'{}\' and course_selections.year = {} and course_selections.term = {}'.format(stud_id,year,term))

    obj = []

    for i in c:
        obj.append(list(i))


    context = {'studId':stud_id,'obj': obj,'year': year,'term':term}
    return render(request, 'ninethExact.html', context)



def thirteenth(request):
    con = cx_Oracle.connect('hr/hr@localhost:1521/orcl')
    c = con.cursor();
    c.execute('SELECT sum(credits)*25000 FROM course_selections INNER JOIN course_sections ON course_selections.ders_kod = course_sections.ders_kod AND course_selections.year = course_sections.year AND course_selections.term = course_sections.term AND course_selections.section = course_sections.section WHERE qiymet_herf LIKE \'F\'')

    obj = []

    for i in c:
        obj.append(list(i))


    context = {'obj': obj}
    return render(request, 'thirteenth.html', context)

def sorry(request):
    return render(request, 'sorry.html', {})