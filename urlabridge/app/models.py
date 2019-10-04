from django.db import models


class Domain(models.Model):
    domain = models.CharField(max_length=200)


class Path(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    redirect_from = models.CharField(max_length=5000)
    redirect_to = models.CharField(max_length=1000)
