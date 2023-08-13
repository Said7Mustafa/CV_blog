from django.contrib import admin

# Register your models here.
from .models import CV, Experience, Education, Skill, Language, Certification, Project, Hobby

admin.site.register(CV)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Certification)
admin.site.register(Project)
admin.site.register(Hobby)
