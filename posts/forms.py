from django import forms
from haystack.forms import SearchForm
from django.core.exceptions import ValidationError

def validate_tags(tag_field_value):
	if tag_field_value:
		tag_list = tag_field_value.strip(';').lower().split(';')
		tag_list = [t.strip() for t in tag_list if len(t) > 0]
		for tag in tag_list:
			if len(tag) > 40:
				raise ValidationError('Each tag must be 40 characters or less')

class PostForm(forms.Form):
	title = forms.CharField(max_length=100)
	body = forms.CharField(widget=forms.Textarea)
	tags = forms.CharField(required=False, validators=[validate_tags])
	picture1title = forms.CharField(max_length=100, required=False)
	picture1 = forms.ImageField(required=False)
	picture2title = forms.CharField(max_length=100, required=False)
	picture2 = forms.ImageField(required=False)
	picture3title = forms.CharField(max_length=100, required=False)
	picture3 = forms.ImageField(required=False)
	human = forms.CharField(required=True)

class ParentCommentForm(forms.Form):
	body = forms.CharField(widget=forms.Textarea)

class PostSearchForm(SearchForm):
	search_term = forms.CharField(max_length=30, required=True)

	def search(self):
		sqs = super(PostSearchForm, self).search()

		if not self.is_valid():
			return self.no_query_found()
