from django.shortcuts import render
from django.http import HttpResponse
from .models import Domain, Path
from django.shortcuts import redirect
from django.core import exceptions


def page_redirect(request, path):
    host = request.META['HTTP_HOST']
    try:
        host_domain = Domain.objects.get(domain=host)
    except exceptions.ObjectDoesNotExist:
        return HttpResponse('This domain has not been configured yet. Sign into the admin panel and set it up there.')
    try:
        redirect_path = Path.objects.get(redirect_from=path, domain=host_domain)
    except exceptions.ObjectDoesNotExist:
        return HttpResponse('This path has not been configured yet. Sign into the admin panel and set it up there.')
    return redirect(redirect_path.redirect_to)
