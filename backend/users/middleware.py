from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest, HttpResponse
from .forms import LograForm
import json

class JwtComparerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        uro = False
        upo = json.loads(request.body)
        try:
            print(upo['login'])
        except:
            uro = True
        if uro == True:
            cookie_value = request.COOKIES.get('my_cookie', 'undefined')
            print(cookie_value)
            if cookie_value != 'undefined':
                print("✅, Переадресация одобрена")
            else:
                return HttpResponse('REDIRTOLOGIN')
        else :
            print('✅, Запрос регистрации')


class IsValidMiddleware(MiddlewareMixin):
    def process_request(self, request):
            # upo = json.loads(request.body)
            print(json.loads(request.body))
            print(request.POST)
            uniform = LograForm(json.loads(request.body))
            if uniform.is_valid():
                print('✅, Данные введены правильно')
            else:
                print(str(uniform.errors))
                if "<li>Поле не должно содержать слово &#x27;login&#x27;.</li>" in str(uniform.errors):
                    return HttpResponse("LoginCommonWordError")
                if "><li>Поле не должно  содержать слово &#x27;password&#x27;.</li>" in str(uniform.errors):
                    return HttpResponse("PasswordCommonWordError")
                if  "<li>Поле не должно  содержать слово &#x27;adresl&#x27;. Это системное имя</li>" in str(uniform.errors):
                    return HttpResponse("AdreslCommonWordError")
                if  "<li>Логин не может быть длинее 30 символов</li>" in str(uniform.errors):
                    return HttpResponse("LoginTooLongError")
                if  "<li>Пароль не может быть длинее 30 символов</li>" in str(uniform.errors):
                    return HttpResponse("PasswordTooLongError")
                if  "<li>Пароль не может быть короче 10 символов</li>" in str(uniform.errors):
                    return HttpResponse("PasswordTooShortError")


