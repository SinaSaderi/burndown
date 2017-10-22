from __future__ import unicode_literals

from django.db import models
from django_jalali.db import models as jmodels
from datetime import date
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField('Start date', null=True, blank=True, default=date.today)
    velocity = models.IntegerField(default=1)
    total_hours = models.IntegerField('Total hours', null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return "%s" % self.title

class ClosedDays(models.Model):
    day = models.DateField('Closed day', null=True, blank=True, default=date.today)
    project = models.ForeignKey(Project, null=True, blank=True)

    def __str__(self):
        return "%s" % str(self.day)
    
    class Meta:
        verbose_name = 'Closed day'
        verbose_name_plural = 'Closed days'


class Hours(models.Model):
    completed = models.IntegerField('Completed hours', null=True, blank=True)
    date = models.DateField('Date', null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    project = models.ForeignKey(Project, default=1, null=True, blank=True)

    def __str__(self):
        return str(self.completed)

    class Meta:
        verbose_name = 'Completed hour'
        verbose_name_plural = 'Completed hours'
