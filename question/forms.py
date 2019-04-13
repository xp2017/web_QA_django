from django import forms
from .models import Question, Comment, Article, ArticleComment
from simditor.fields import RichTextFormField

class QuestionPostForm(forms.ModelForm):
    #body = RichTextFormField()


    class Meta:
        model = Question
        fields = ('title', 'body',)


class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('answer',)


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('image_above', 'title', 'article', 'status',)



class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('comment',)


