from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse

class HomeView(View):
  template_name = 'mytestsite/home.html'
  def get(self, request, *args, **kwargs):
    return render(request, self.template_name, {})

class DashboardView(View):
  template_name = 'mytestsite/dashboard.html'
  def get(self, request, *args, **kwargs):
    return render(request, self.template_name, {})

class SignInView(View):
  template_name = 'mytestsite/sign-in.html'
  def get(self, request, *args, **kwargs):
    return render(request, self.template_name, {})

class MyView(View):
  template_name = 'startbootstrap-sb-admin-gh-pages/index.html'
  def get(self, request, *args, **kwargs):
    return render(request, self.template_name, {})