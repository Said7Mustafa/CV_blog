
from blog_pages.models import Experience, Education, Skill, Language, Certification, Project, Hobby, Resume


# Delete all instances of your models
Experience.objects.all().delete()
Education.objects.all().delete()
Skill.objects.all().delete()
Language.objects.all().delete()
Certification.objects.all().delete()
Project.objects.all().delete()
Hobby.objects.all().delete()
Resume.objects.all().delete()

print('Data cleaned successfully')
