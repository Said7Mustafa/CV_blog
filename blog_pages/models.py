from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_enrolled = models.BooleanField(default=False)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=100)

class Language(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=100)

class Certification(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)

class Hobby(models.Model):
    name = models.CharField(max_length=100)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    experiences = models.ManyToManyField(Experience)
    education = models.ManyToManyField(Education)
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)
    certifications = models.ManyToManyField(Certification)
    projects = models.ManyToManyField(Project)
    hobbies = models.ManyToManyField(Hobby)
