from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'question', 'answer',)


class QuestionForm(forms.ModelForm):
	
	class Meta:
		model=Post
		fields=('question',)        


class AnswerForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('answer',)
