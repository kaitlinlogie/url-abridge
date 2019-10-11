from django.shortcuts import render
from django.http import HttpResponse
from .models import Domain, Path
from django.shortcuts import redirect


def page_redirect(request, path):
    host_domain = Domain.objects.get(domain='bepure.co')
    redirect_path = Path.objects.get(redirect_from=path, domain=host_domain)
    return redirect(redirect_path.redirect_to)
