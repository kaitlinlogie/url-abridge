from django.db import models


class Domain(models.Model):
    domain = models.CharField(max_length=200)

    def __str__(self):
        return self.domain


class Path(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    redirect_from = models.CharField(max_length=5000)
    redirect_to = models.CharField(max_length=1000)

    class Meta:
        unique_together = ('domain', 'redirect_from')

    def __str__(self):
        return '{}/{} -> {}'.format(self.domain, self.redirect_from, self.redirect_to)
