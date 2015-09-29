import json
import datetime
import markdown
import urllib
from functools import wraps
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from .forms import *

#markdown-ify text
def md(s):
	return markdown.markdown(s).lstrip('<p>').rstrip('</p>')

#map function that returns a list, not an iterator
def jmap(f, l):
	return list(map(f, l))

#filters out flagged posts
def exclude_flagged(l):
	return list(filter(lambda e: e.flagged == False, l))

#Preview for list view
class PostPreview():
	def __init__(self, post):
		self.post_id = post.pk
		self.title = post.title
		self.post_time = post.created
		self.flagged = post.flagged
		#first 75 words for preview
		self.preview_text = md(' '.join(post.body.split(' ')[:75]) + '...')
		self.tags = exclude_flagged(post.tag_set.all())


def cast_post_to_preview(post):
	return PostPreview(post)

#image thumbnails in posts have a fixed height of 150px
def shrink_divisor(img):
	return(img.height/150.0)

class PicturePreview():
	def __init__(self, picture):
		self.picture_id = picture.pk
		self.title = picture.title
		self.post = picture.post
		self.flagged = picture.flagged
		self.image = picture.image
		self.url = picture.image.url
		self.height = int(self.image.height/shrink_divisor(self.image))
		self.width = int(self.image.width/shrink_divisor(self.image))

def cast_picture_to_preview(picture):
	return PicturePreview(picture)

def index(request):
	#get posts, order by newest first
	last_posts = jmap(cast_post_to_preview, Post.objects.order_by('-created'))
	#exclude posts that have been flagged by admins
	last_posts = exclude_flagged(last_posts)
	#5 posts per preview
	paginator = Paginator(last_posts, 5)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	header_text = 'Latest Posts'
	context = {'posts': posts, 'header': header_text}
	return render(request, 'posts/list_view.html', context)

def post_view(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	#marked = user_marked_post(request.user, post_id)
	#mark_count = post.mark_set.all().count()
	pictures = exclude_flagged(jmap(cast_picture_to_preview, post.picture_set.all()))
	if len(pictures) == 0:
		pictures = None
	tags = post.tag_set.all()
	if len(tags) == 0:
		tags = None
	comments = post.parentcomment_set.order_by('-created')
	if len(comments) == 0:
		comments = None
	comment_form = ParentCommentForm()
	context = {'post': post, 'body': md(post.body), 'pictures': pictures, 'tags': tags, 'comments': comments, 'comment_form': comment_form}
	return render(request, 'posts/post_view.html', context)

def tag_view(request, tag_name):
	tag = get_object_or_404(Tag, name=urllib.unquote(tag_name))
	posts = jmap(cast_post_to_preview, tag.posts.all())

	paginator = Paginator(posts, 5)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	header_text = 'Posts Tagged with "{0}"'.format(urllib.unquote(tag_name))
	context = { 'tag': tag, 'posts': posts, 'header': header_text}

	return render(request, 'posts/list_view.html', context)

#post new entry
def post_form(request):
	if request.method == 'POST':
		#user = User.objects.get(username=request.user)
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			human = request.POST['human']

			#anti-spam
			if human and human.lower() == 'blue':
				pass
			else:
				return HttpResponseRedirect('/posts/')

			title = request.POST['title']
			body = request.POST['body']
			raw_tags = request.POST.get('tags', False)
			picture_1_title = request.POST.get('picture1title', False)
			picture_2_title = request.POST.get('picture2title', False)
			picture_3_title = request.POST.get('picture3title', False)


			picture_1 = None
			try:
				picture_1 = request.FILES['picture1']
			except:
				pass

			picture_2 = None
			try:
				picture_2 = request.FILES['picture2']
			except:
				pass

			picture_3 = None
			try:
				picture_3 = request.FILES.get['picture3']
			except:
				pass

			new_post = Post(title=title, body=body)
			new_post.save()

			if picture_1:
				i = Picture(image=picture_1, title=picture_1_title, post=new_post)
				i.save()

			if picture_2:
				i = Picture(image=picture_2, title=picture_2_title, post=new_post)
				i.save()

			if picture_3:
				i = Picture(image=picture_3, title=picture_3_title, post=new_post)
				i.save()



			#clean tags up
			tag_list = raw_tags.strip(';').lower().split(';')
			tag_list = [t.strip() for t in tag_list if len(t) > 0]


			for tag in tag_list:
				tag = tag.strip()
				t = None
				#make new tag if it doesn't exist yet
				if Tag.objects.filter(name=tag).count() == 0:
					t = Tag(name=tag)
					t.save()
				#use existing tag
				else:
					t = Tag.objects.get(name=tag)

				t.posts.add(new_post)
			return HttpResponseRedirect('/posts/' + str(new_post.pk))
		else:
			context = {}
			context['body_text'] = request.POST['body']
			context['title_text'] = request.POST['title']
			context['tags_text'] = request.POST['tags']
			context['picture1text'] = request.POST.get('picture1title', False)
			context['picture2text'] = request.POST.get('picture2title', False)
			context['picture3text'] = request.POST.get('picture3title', False)
			context['form'] = form

			return render(request, 'posts/add_post.html', context)
	elif request.method == 'GET':
		form = PostForm()
		return render(request, 'posts/add_post.html', {'form': form})

def formatting_help(request):
	return render(request, 'posts/formatting_help.html')


def add_parent_comment(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if request.method == 'POST':
		form = ParentCommentForm(request.POST)
		if form.is_valid():
			body = form.cleaned_data['body']
			comment = ParentComment(post=post, body=body)
			comment.save()
			#we'll redirect if the user isn't authenticated, we pass authentication status it as a field
			response = json.dumps({"body": comment.body, "time": comment.created.strftime("%m/%d/%Y %H:%M")})
			return HttpResponse(response, content_type="application/json")
		else:
			form = ParentCommentForm()
			return HttpResponseRedirect('/posts/' + str(post_id))
	else:
		print("A GET? Some hacking is going on...")
		return HttpResponseRedirect('/posts/' + str(post_id))

def add_child_comment(request, parent_id):
	pass

def resource_not_found(request):
    response = render(request, 'posts/404.html')
    response.status_code = 404
    return response

def server_error(request):
    response = render(request, 'posts/500.html')
    response.status_code = 500
    return response
