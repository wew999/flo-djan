from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth import get_user_model

User = get_user_model()

class JwtComparerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path != '/login' and request.path != '/quit':
            cookie_value = request.COOKIES.get('my_cookie', 'undefined')
            print(cookie_value)
            if cookie_value != 'undefined':
                return redirect('thrash')
            else:
                return redirect('/login')
