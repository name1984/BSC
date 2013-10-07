from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def run_bsc(request):
    t=get_template('index_plantilla.html')
    html= t.render(Context({'title':'BSC GPA','path_image_logo':'./images/logogpa.png'}))
    return HttpResponse(html)
