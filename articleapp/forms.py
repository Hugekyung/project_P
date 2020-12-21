from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article # Article을 db에서 가져온다.
        fields = ['title', 'image', 'content']