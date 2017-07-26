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
    job_description_link = models.URLField(blank = True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank = True)
    qualifications = models.TextField(blank = True)
    responsibilities = HTMLField(blank = True)
    career_ladder = models.URLField(blank = True)
    exam_notes = models.TextField(blank = True)
    occupational_category = models.ForeignKey(OccupationalCategory, on_delete=models.CASCADE, blank = True, null = True)
    skills = models.ManyToManyField(Skill, blank = True)
    related_keywords = models.ManyToManyField(RelatedKeyword, blank = True)
    categories = models.ManyToManyField(Category, blank = True)
    salary_low = models.IntegerField()
    salary_high = models.IntegerField()
    exam_date = models.DateField()
    
    def __str__(self):
        return self.title