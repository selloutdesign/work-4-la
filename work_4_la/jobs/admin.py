from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import widgets, fields, resources
from .models import Job, Category, RelatedKeyword, Skill, OccupationalCategory


# Register your models here.

class JobResource(resources.ModelResource):
    categories = fields.Field(
        column_name='categories',
        attribute='categories',
        widget=widgets.ManyToManyWidget(Category, field='name'))
    skills = fields.Field(
        column_name='skills',
        attribute='skills',
        widget=widgets.ManyToManyWidget(Skill, field='name'))
    related_keywords = fields.Field(
        column_name='related_keywords',
        attribute='related_keywords',
        widget=widgets.ManyToManyWidget(RelatedKeyword, field='name'))
    occupational_category = fields.Field(
        column_name='occupational_category',
        attribute='occupational_category',
        widget=widgets.ForeignKeyWidget(OccupationalCategory, field='name')
        )
    
    class Meta:
        model = Job
        skip_unchanged = True
        report_skipped = True

class CategoryResource(resources.ModelResource):
    
    class Meta:
        model = Category

class RelatedKeywordResource(resources.ModelResource):
    
    class Meta:
        model = RelatedKeyword
        
class SkillResource(resources.ModelResource):
    
    class Meta:
        model = Skill
        
class OccupationalCategoryResource(resources.ModelResource):
    
    class Meta:
        model = OccupationalCategory
        
        
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CategoryResource

class RelatedKeywordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RelatedKeywordResource

class SkillAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SkillResource

class OccupationalCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = OccupationalCategoryResource

class JobAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = JobResource
    list_filter = ['categories']
    list_display = ('title','job_description_link', 'salary_low')
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(RelatedKeyword, RelatedKeywordAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(OccupationalCategory, OccupationalCategoryAdmin)
admin.site.register(Job, JobAdmin)