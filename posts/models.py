from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

#post/article on the site
class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=100, blank=True, default='')
	body = models.TextField()
	flagged = models.BooleanField(default=False)

	def __unicode__(self):
		return(self.title + '|' + str(self.created))

	class Meta:
	     ordering = ('created',)

#tags for posts
class Tag(models.Model):
	name = models.CharField(max_length=40, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	posts = models.ManyToManyField(Post)
	flagged = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ('created',)

#comment on article, called parent for possibility of child
class ParentComment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	post = models.ForeignKey(Post)
	body = models.TextField()
	flagged = models.BooleanField(default=False)

	def __unicode__(self):
		return('Parent Comment|' + self.post.title + '|' + '|' + str(self.created))

	class Meta:
		ordering = ('created',)

#Not implemented yet, waiting for others' comment, no pun intended
class ChildComment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	parent = models.ForeignKey(ParentComment)
	body = models.TextField()
	flagged = models.BooleanField(default=False)

	def __unicode__(self):
		return('Child Comment|' + self.parent.post.title + '|' + str(self.created))

	class Meta:
		ordering = ('created',)

#Like a 'star' on Twitter or an 'upvote' on Quora
class Mark(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post)

	def __unicode__(self):
		return(self.post.title + '|' + str(self.created))

	class Meta:
		ordering= ('created',)

#image associated with a post
class Picture(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True)
	post = models.ForeignKey(Post)
	flagged = models.BooleanField(default=False)
	image = models.ImageField(upload_to="posts/pictures/", blank=True)

	def __unicode__(self):
		return(self.title + '|' + self.post.title + '|' + str(self.created))

	class Meta:
		ordering = ('created',)
