from .models import Job, Category, OccupationalCategory, Skill
import django_filters


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab


class JobFilter(django_filters.FilterSet):
    # category__name = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    occupational_category = django_filters.ModelChoiceFilter(queryset=OccupationalCategory.objects.all())
    skills = django_filters.ModelMultipleChoiceFilter(queryset=Skill.objects.all())
    class Meta:
        model = Job
        fields = [ 'title', 'description', 'occupational_category', 'skills']