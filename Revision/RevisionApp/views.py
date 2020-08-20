from django.shortcuts import render
from django.views import View


class Register(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        return render(request, 'auth/register.html')


class Login(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        return render(request, 'auth/login.html')
