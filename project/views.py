from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from datetime import date, timedelta
import datetime
import math


from .models import Project, Hours, ClosedDays

def index(request):
    """ List all projects with start date and dead line

    """
    template = loader.get_template("index.html")
    projects = Project.objects.order_by('-start_date')
    context = {
        'APPTITLE': 'BurnDown Chart',
        'projects': projects
    }
    return HttpResponse(template.render(context, request))


def project(request, project_id):
    """ Project detail and burn down chart

    """
    project = get_object_or_404(Project, pk=project_id)
    mainTotalHours = project.total_hours

    totalDays = int(math.ceil(float(project.total_hours) / (project.velocity)))
    closedDays = [d.day for d in ClosedDays.objects.filter(project_id = project_id)]

    # Add closed days and to project and calculate them for deadline.
    i = 0
    days = []
    while(len(days) != totalDays):
        nextDay = project.start_date + datetime.timedelta(days=i)
        if(nextDay not in closedDays):
            days.append(str(datetime.datetime.strptime(str(nextDay), '%Y-%m-%d').strftime('%d-%m')))
        i += 1
        
    dayPercentage = (1010 - (19 * len(days))) / (len(days) + 1.0)


    #:margin between hours (vertical)
    hourDown = project.total_hours
    aHours = []
    aHours.append(hourDown)
    for i in range(project.velocity):
        hourDown = int(hourDown - (project.total_hours / project.velocity))
        aHours.append(hourDown)

    # print aHours
    if aHours[-1] != 0:
        aHours.append(0)
    project.total_hours += 1

    hourPercentage = (450 / (25 + 0.55)) + 10
    totalHours = range(project.total_hours)[::-1]

    hours = Hours.objects.filter(project=project).order_by('date')
    # print len(hours)

    normalHours = project.total_hours / len(days)

    completed =[h.completed for h in hours]
    normalCompleted = 400 / totalDays
    tableCompleted = [(normalCompleted * h.completed / 20) for h in hours]
    completedHours = sum(completed)
    remainingHours = mainTotalHours - completedHours 
    totalPercentage = (remainingHours * 100) / mainTotalHours
    context = {
        'project': project,
        'days': days,
        'dayPercentage': dayPercentage,
        'totalHours': aHours,
        'hourPercentage': hourPercentage,
        'aComple': completed,
        'nHour': normalHours,
        'totalDaysCount': len(closedDays) + len(days) - 1,
        'closedDaysCount': len(closedDays),
        'remainingHours': remainingHours,
        'velocity': project.velocity,
        'totalPercentage': totalPercentage,
        'tableCompleted': tableCompleted,
    }
    return render(request, 'project.html', context)
