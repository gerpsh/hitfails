from django.test import TestCase
from django.test import Client
from ..views import *
from ..models import *
import json
import os.path

class GetTests(TestCase):
    def setUp(self):
        Post.objects.create(title="test", body="test")
        Tag.objects.create(name="lol")

    def test_pk(self):
        p = Post.objects.create(title="test", body="test")
        self.assertEqual(p.pk, 4)

    def test_index(self):
        c = Client()
        response = c.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_tag(self):
        c = Client()
        response = c.get('/posts/tag/lol/')
        self.assertEqual(response.status_code, 200)

    def test_add_post(self):
        c = Client()
        response = c.get('/posts/add-post/')
        self.assertEqual(response.status_code, 200)

class PostSubmitTest(TestCase):
    def test_post_successful(self):
        c = Client()
        response = c.post('/posts/add-post/', {'title': 'test title', 'body': 'test body', 'tags': 'lol;fail;win'})
        self.assertEqual(response.status_code, 200)

    def test_bad_char(self):
        c = Client()
        blns = json.loads(open(os.path.dirname(__file__) + '/../fixtures/blns.json').read())
        for s in blns:
            response = c.post('/posts/add-post/', {'title': 'test title', 'body': 'test body', 'tags': s})
            self.assertEqual(response.status_code, 200)
            response = c.get('/posts/')
            self.assertEqual(response.status_code, 200)

            response = c.post('/posts/add-post/', {'title': 'test title', 'body': s, 'tags': 'lol;fail;win'})
            self.assertEqual(response.status_code, 200)
            response = c.get('/posts/')
            self.assertEqual(response.status_code, 200)

            response = c.post('/posts/add-post/', {'title': s, 'body': 'test body', 'tags': 'lol;fail;win'})
            self.assertEqual(response.status_code, 200)
            response = c.get('/posts/')
            self.assertEqual(response.status_code, 200)
