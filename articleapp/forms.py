from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto; text-align: left'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False) # project를 설정하지 않아도 되도록

    class Meta:
        model = Article # Article을 db에서 가져온다.
        fields = ['title', 'image', 'project', 'content'] # project: 게시물을 어떤 project에 넣을 것인지 선택할 수 있도록