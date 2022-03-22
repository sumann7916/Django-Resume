from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class UserInfo(models.Model):
	skype = models.URLField(default='#')
	instagram = models.URLField(default='#', null=True)
	facebook = models.URLField(default='#', null=True)
	linkedin = models.URLField(default='#', null=True)
	twitter = models.URLField(default='#', null=True)
	city = models.CharField(max_length=20)
	country = models.TextField(max_length=20)
	Degree = models.TextField(max_length=20)
	email = models.EmailField()
	

class Category(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title



class Post(models.Model):
	thumbnail = models.ImageField()
	title = models.CharField(max_length=30)
	categories = models.OneToOneField(Category, on_delete=models.CASCADE, null=True)
	content = RichTextField(blank=True, null=True)