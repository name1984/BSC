# -*- encoding: utf-8 -*-

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from time import strftime
from bscard.models import mision

def runBsc(request):
    t=get_template('base.html')
    date= {'month':strftime("%b"),'year':strftime("%Y")}
    html= t.render(Context({'maintitle':'BSC GPA', 'title':'Resultados','subtitle':'Perspectiva Financiera','month':date["month"], 'year':date["year"],'currentpage':'status'}))
    return HttpResponse(html)

def addKpi(request):
    t=get_template('base.html')
    date= {'month':strftime("%b"),'year':strftime("%Y")}
    html= t.render(Context({'maintitle':'BSC GPA', 'title':'Ingreso Indicadores','subtitle':'Perspectiva Financiera','month':date["month"], 'year':date["year"], 'currentpage':'add'}))
    return HttpResponse(html)

def addMision(request):
    t=get_template('ingreso_mision.html')
    date= {'month':strftime("%b"),'year':strftime("%Y")}
    html= t.render(Context({'maintitle':'BSC GPA', 'title':'Configuración','subtitle':'Misión Empresarial','month':date["month"], 'year':date["year"], 'currentpage':'conf'}))
    return HttpResponse(html)

def addPerspective(request):
    t=get_template('ingreso_perspectivas.html')
    date= {'month':strftime("%b"),'year':strftime("%Y")}
    html= t.render(Context({'maintitle':'BSC GPA', 'title':'Configuración','subtitle':'Perspectivas','month':date["month"], 'year':date["year"], 'currentpage':'conf'}))
    
    return HttpResponse(html)
