from django.contrib import admin

from .models import Project, Team, Hours, ClosedDays
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

class ProjectAdmin(admin.ModelAdmin):
    # fields = ('title', 'start_date', 'dead_date')
    list_display = ('title', 'start_date')
    
class HoursAdmin(admin.ModelAdmin):
    list_display = ('completed', 'date', 'project')
    list_filter = ('project',)

class ClosedDaysAmin(admin.ModelAdmin):
	"""docstring for ClosedDaysAmin"""
	list_display = ('project', 'day')	



admin.site.register(Project, ProjectAdmin)
admin.site.register(Team)
admin.site.register(ClosedDays, ClosedDaysAmin)
admin.site.register(Hours, HoursAdmin)
