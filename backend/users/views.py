from django.shortcuts import render
from users.models import logData, orderData, myProductionData
import json
from django.core import serializers
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
        isRepeated = False
        ustInfo = logData.objects.all()
        for us in ustInfo :
            if loginbl == us.username:
                if passwordbl == us.password:
                    usInfo = logData.objects.filter(username=loginbl).first()
                    loginbl = usInfo.username
                    passwordbl = usInfo.password
                    isRepeated = True
                else:
                    return HttpResponse("Пароль или логин не совпадают")


        print(f"{loginbl} == {passwordbl} == !!!!!!!!!!!!!!!!!!!!!!")
        usInfo = logData.objects.create(username=loginbl, password=passwordbl)
        if isRepeated == False:
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
        if copium['special'] != 'returnorder':
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
            cookie_value = request.COOKIES.get('my_cookie', 'undefined')
            print(cookie_value)
            decoded_token = jwt.decode(cookie_value, 'tenfeettwentytheflowerman', algorithms=['HS256'])
            print(decoded_token)
            log1n = decoded_token['username']
            backInfor = orderData.objects.filter( user__username=log1n).values('user', 'order', 'identifier')
            riksha = ''
            for orderu in backInfor:
                print(orderu['user'], orderu['order'], orderu['identifier'])
                if orderu['order'] != "b'{}'":
                    riksha = ast.literal_eval(orderu['order'])
                    print(orderu['order'])
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return HttpResponse(riksha)
    else:
     #   ress = copium['address']
        cookie_value = request.COOKIES.get('my_cookie', 'undefined')
        print(cookie_value)
        decoded_token = jwt.decode(cookie_value, 'tenfeettwentytheflowerman', algorithms=['HS256'])
        print(decoded_token)
        log1n = decoded_token['username']
        frontInfo = logData.objects.filter(username=log1n).first()
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
        backInfor = orderData.objects.filter( user__username=log1n).values('user', 'order', 'identifier')
        for orderu in backInfor:
            print(orderu['user'], orderu['order'], orderu['identifier'])
        return HttpResponse("Сохранено типо")


@csrf_exempt
def productbase(request):
    if request.method == "POST":
        cookie_value = request.COOKIES.get('my_cookie', 'undefined')
        print(cookie_value)
        decoded_token = jwt.decode(cookie_value, 'tenfeettwentytheflowerman', algorithms=['HS256'])
        print(decoded_token)
        log1n = decoded_token['username']
        passw0rd = decoded_token['password']
        if log1n == 'adminp' and passw0rd == 'admin311':
            return HttpResponse("ALLOWED")
        else:
            return  HttpResponse("NOT ALLOWED")


@csrf_exempt
def product(request):
    if request.method != "GET":
        isSpecial = True
        try:
            js_on = json.loads(request.body)
            hilo = js_on['special']
        except:
            isSpecial = False
        if isSpecial == False:
                print(request.body)
                js_on = json.loads(request.body)
                hdng = js_on['heading']
                src = js_on['info']
                prc = js_on['prc']
                newProd = myProductionData(heading=hdng, info=src, price=prc)
                newProd.save()
                return  HttpResponse("SAVED (ADMIN)")
        else:
            print(request.body)
            js_on = json.loads(request.body)
            print(js_on)
            print('6767676767676766767676767')
            heading1 = js_on['special']
            newProd = myProductionData.objects.filter(heading=heading1).first()
            print(newProd)
            return  HttpResponse(newProd.info)
    else:
        newProd =myProductionData.objects.all()
        if newProd.exists():
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            newProd = serializers.serialize('json', newProd)
            return  HttpResponse(newProd)
        else:
            return  HttpResponse("Nothing")

@csrf_exempt
def functionthatdeletsdatabase(request):
    myProductionData.objects.all().delete()
    orderData.objects.all().delete()
    logData.objects.all().delete()
    return  HttpResponse("УНИЧТОЖЕНО!")