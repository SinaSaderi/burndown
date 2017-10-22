from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from datetime import date
import datetime
from random import randint
import math


from project.models import Project, ClosedDays, Team, Hours

class IndexPageTest(TestCase):

    def test_Index(self):
        pass


class ProjectTest(TestCase):
    def setUp(self):

        project = Project.objects.create(title='test', velocity=19, total_hours=500)

        for i in range(10):
            date = timezone.now() + datetime.timedelta(days=i)
            completed = randint(10,25)
            Hours.objects.create(completed=completed, date=date, project=project)

    def test_project(self):
        project = Project.objects.get(pk=1)

        totalDays = int(math.ceil(float(project.total_hours) / (project.velocity)))
        self.assertIs(totalDays, 27)

