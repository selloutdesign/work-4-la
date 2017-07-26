from django.contrib import admin

# Register your models here.

# app/admin.py

from import_export import widgets, fields, resources
from import_export.admin import ImportExportModelAdmin
from .models import Book, Category

class CatNameWidget(widgets.ManyToManyWidget):
    def get_queryset(self, value, row):
        return self.model.objects.filter(
            name__iexact=row['name']
            )

class BookResource(resources.ModelResource):
    categories_name = fields.Field(
        column_name="categories",
        attribute="categories",
        widget=widgets.ManyToManyWidget(Category, field='name'))

    class Meta:
        model = Book
        skip_unchanged = True
        report_skipped = True
        fields = ('id', 'name', 'author','published','price', 'categories_name')
        

class CategoryResource(resources.ModelResource):
    
    class Meta:
        model = Category
        
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CategoryResource

class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BookResource
    filter_horizontal = ('categories',)
    list_filter =['author']
    list_display = ('name', 'author_email')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)