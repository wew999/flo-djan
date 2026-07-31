from django.shortcuts import render
from users.models import logData, orderData
import json
import jwt
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import ast

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
    return render(request, "index.html")

@csrf_exempt
def postuser(request):
    print(request.body)
    copium = json.loads(request.body)
    isSpecial = True
    try:
        print(copium['special'])
    except:
        isSpecial = False
    if isSpecial == False:
        loginbl = copium['login']
        passwordbl = copium['password']

        ustInfo = logData.objects.all()
        for us in ustInfo :
            if loginbl == us.username:
                return HttpResponse("<h1>ассортимент</h1>")
        print(f"{loginbl} == {passwordbl} == !!!!!!!!!!!!!!!!!!!!!!")
        usInfo = logData.objects.create(username=loginbl, password=passwordbl)
        usInfo.save()
        token_object = {
            "username": f"{loginbl}",
            "password": f"{passwordbl}",
        }
        print(token_object)
        token = create_token(token_object)
        print(token)
        response = HttpResponse("Yo!")
        response.set_cookie('my_cookie', token, max_age=3600, httponly=True, samesite="None", path="/",  secure=True)
        return response
    else:
        return HttpResponse("JWT CHECKED!")

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

@csrf_exempt
def postorder(request):
    copium = json.loads(request.body)
    isSpecial = True
    try:
        print(copium['special'])
    except:
        isSpecial = False
    if isSpecial == True:
        cookie_value = request.COOKIES.get('my_cookie', 'undefined')
        print(cookie_value)
        decoded_token = jwt.decode(cookie_value, 'tenfeettwentytheflowerman', algorithms=['HS256'])
        print(decoded_token)
        log1n = decoded_token['username']
        ustInfo = orderData.objects.filter(user__username=log1n).values('user', 'order', 'identifier')
       # orderData.objects.all().delete()
        if not ustInfo.exists():
            return HttpResponse("Nothing")
        else:
            # subsonic= orderData.objects.all()
            #  for us in subsonic :
            #      if log1n == us.user__username:
            #          return HttpResponse(us)
            riksha = ''
            for orderu in ustInfo:
                print(orderu['user'], orderu['order'], orderu['identifier'])
                riksha = ast.literal_eval(orderu['order'])
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return HttpResponse(riksha)
    else:
     #   ress = copium['address']
        cookie_value = request.COOKIES.get('my_cookie', 'undefined')
        print(cookie_value)
        decoded_token = jwt.decode(cookie_value, 'tenfeettwentytheflowerman', algorithms=['HS256'])
        print(decoded_token)
        log1n = decoded_token['username']
        frontInfo = logData.objects.get(username=log1n)
        print(frontInfo)
        backInfor = orderData.objects.filter( user__username=log1n)
        iden = 0
        if backInfor.exists():
            iden = len(backInfor) + 1
        else:
            iden = 1
        backInfo = orderData(order=request.body, identifier=iden)
        backInfo.user = frontInfo
        backInfo.save()
        return HttpResponse("Сохранено типо")