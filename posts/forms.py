from django import forms
from haystack.forms import SearchForm


#submit a post form
class PostForm(forms.Form):
	title = forms.CharField(max_length=100)
	body = forms.CharField(widget=forms.Textarea)
	tags = forms.CharField(required=False)
	picture1title = forms.CharField(max_length=100, required=False)
	picture1 = forms.ImageField(required=False)
	picture2title = forms.CharField(max_length=100, required=False)
	picture2 = forms.ImageField(required=False)
	picture3title = forms.CharField(max_length=100, required=False)
	picture3 = forms.ImageField(required=False)

#submit a comment form
class ParentCommentForm(forms.Form):
	body = forms.CharField(widget=forms.Textarea)

class PostSearchForm(SearchForm):
	search_term = forms.CharField(max_length=30, required=True)

	def search(self):
		sqs = super(PostSearchForm, self).search()
		
		if not self.is_valid():
			return self.no_query_found()
