from django.contrib import admin
from .models import Section, Bullet, Text, Project, ProgressBar, Bars

# Register your models here.
admin.site.register(Introduction)
admin.site.register(Section)
admin.site.register(Bullet)
admin.site.register(Text)
admin.site.register(Project)
admin.site.register(Bars)
admin.site.register(ProgressBar)
