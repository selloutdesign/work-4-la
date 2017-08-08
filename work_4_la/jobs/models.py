from django.db import models

from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class OccupationalCategory(models.Model):
    name = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
        
class RelatedKeyword(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    classspec_id = models.BigIntegerField()
    job_description_link = models.URLField(blank = True, null = True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank = True, null = True)
    qualifications = models.TextField(blank = True, null = True)
    responsibilities = HTMLField(blank = True, null = True)
    career_ladder = models.URLField(blank = True, null = True)
    exam_notes = models.TextField(blank = True, null = True)
    occupational_category = models.ForeignKey(OccupationalCategory, on_delete=models.CASCADE, blank = True, null = True)
    skills = models.ManyToManyField(Skill, blank = True)
    related_keywords = models.ManyToManyField(RelatedKeyword, blank = True)
    categories = models.ManyToManyField(Category, blank = True)
    salary_low = models.IntegerField(blank = True)
    salary_high = models.IntegerField(blank = True)
    exam_date = models.DateField(blank = True, null = True)
    
    def __str__(self):
        return self.title