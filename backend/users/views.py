from django.shortcuts import render
from users.models import logData
import json
import jwt

secret_key = 'tenfeettwentytheflowerman'

def create_token(payload):
    return jwt.encode(payload, secret_key, algorithm='HS256')


from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Главная</h1>")
# Create your views here.
def about(request):

    return HttpResponse("<h1>Про нас</h1>")

def asssortiment(request):
    return HttpResponse("<h1>ассортимент</h1>")

def thrash(request):
        return render(request, "index.html")

def login(request):
    return render(request, "login.vue")

def postuser(request):
    json.loads(request)
    print(request)
    """
    ustInfo = logData.objects.all()
    for us in ustInfo :
        if loginbl == us.username:
            return HttpResponse("<h1>ассортимент</h1>")
    print(f"{loginbl} == {passwordbl} == {adressbl} !!!!!!!!!!!!!!!!!!!!!!")
    usInfo = logData.objects.create(username=loginbl, password=passwordbl, address=adressbl)
    usInfo.save()
    token_object = {
        "username": f"{loginbl}",
        "password": f"{passwordbl}",
        "address": f"{adressbl}"
    }
    print(token_object)
    token = create_token(token_object)
    print(token)
    response = HttpResponse("Yo!")
    response.set_cookie('my_cookie', token, max_age=3600, httponly=True)
    return response
    return HttpResponse(f"<h1>{token}</h1>")
    """

def quit(request):
    return render(request, "quit.html")

def userpost(request):
    loginbl = request.POST.get("loginar", "Undefined")
    passwordbl = request.POST.get("password", "Undefined")
    ustInfo = logData.objects.all()
    for us in ustInfo :
        if loginbl != us.username or passwordbl != us.password:
            return HttpResponse(f"<h1>Регистрируйся вонючка</h1>")
    token_object = {
        "username": f"{loginbl}",
        "password": f"{passwordbl}",
    }
    print(token_object)
    token = create_token(token_object)
    print(token)
    return HttpResponse(f"<h1>{token}</h1>")


def loluser(request):
    usInfo = logData.objects.all()
    bruhArr = []
    for us in usInfo :
        animeArr = [us.username, us.password, us.address]
        bruhArr.append(animeArr)
    print(usInfo)
    print(f"{usInfo} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return HttpResponse(f"<p> {bruhArr} =======> Данные бд </p>")