from django.http.response import HttpResponse
import datetime



def index(request):
    now = datetime.datetime.now()
    return HttpResponse("<body bgcolor='#996633'><font color=white>Welcome Dave,<br /><br />Server time : " + str(now))
