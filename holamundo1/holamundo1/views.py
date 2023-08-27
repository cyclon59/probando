import datetime
from django.http import HttpResponse

def saludo(request):
    docum= "<h1>Hola Alumnos bienvenidos al DJANGO!¡¡¡¡¡</h1>"
    return HttpResponse(docum)
def nosvemos(request):
    return HttpResponse("Nos velmont")
def fechaactual(request):
    fecha_actual=datetime.datetime.now()
    docum= """
            <html>
                <body>
                    <h1>La fecha y la hora es %s</h1>
                </body>
            </html>"""%fecha_actual
    return HttpResponse(docum)
def calculaedad(request,edad,agno):
    #edadactual=18892
    periodo=agno-2023
    edadfutura=edad+periodo
    docum= """
            <html>
                <body>
                    <h1>En el año  %s tendras %s años</h1>
                </body>
            </html>"""%(agno,edadfutura)
    return HttpResponse(docum)
