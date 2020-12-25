from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article # Article을 db에서 가져온다.
        fields = ['title', 'image', 'project', 'content'] # project: 게시물을 어떤 project에 넣을 것인지 선택할 수 있도록