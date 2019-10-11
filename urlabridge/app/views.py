from django.shortcuts import render
from django.http import HttpResponse
from .models import Domain, Path
from django.db import connection


def index(request):
    return HttpResponse("Hello, world. You're at the url-abridge index.")


def redirect(request, path):
    host_domain = Domain.objects.get(domain='bepure.co')
    redirect_path = Path.objects.get(redirect_from=path, domain=host_domain)
    return HttpResponse("Redirect from: {}, redirect to: {}".format(redirect_path.redirect_from, redirect_path.redirect_to))
