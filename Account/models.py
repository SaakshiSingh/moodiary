from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null = True,blank=True,on_delete = models.CASCADE)
	otp = models.CharField(max_length=6,null=True)
	is_email_verified = models.BooleanField(default=False,blank=True)
	is_phone_verified = models.BooleanField(default=False,blank=True)
	phone = PhoneNumberField(null=True)
	payment_id = models.CharField(max_length=100,null=True,blank=True)
	hasPremium = models.BooleanField(default=False,blank=True)


	def __str__(self):
		return self.user.username

class Diary(models.Model):
	title = models.CharField(max_length = 200)
	#content = models.TextField()
	content = RichTextField(blank=True,null=True)
	dateCreated = models.DateField(auto_now_add=True)
	dateModified = models.DateField(auto_now=True)
	writer = models.ForeignKey(Customer,on_delete = models.CASCADE,null=True)
	picture = models.ImageField(upload_to="images/",default = "default.png")
	mood = models.CharField(max_length=200,blank=True,null=True)

	def __str__(self):
		return str(self.title +" by "+ self.writer.user.username)
	def diary_user(self):
		return self.writer.user
	
	diary_user.short_description = "User of the diary"
	diary_user = property(diary_user)

class Mood(models.Model):
	mood_choices = (
		('happy','HAPPY'),
		('sad','SAD'),
		('anxious','ANXIOUS'),
		('calm','CALM'),
		('relaxed','RELAXED'),
		('angry','ANGRY'),
		('fearful','FEARFUL'),
		('depressed','DEPRESSED'),
		('lonely','LONELY'),
		('surprised','SURPRISED'),
		('annoyed','ANNOYED'),
		('nervous','NERVOUS'),
		('sick','SICK'),
		('sleepy','SLEEPY'),
		('excited','EXCITED'),
		('stressed','STRESSED'),
		('grumpy','GRUMPY'),
		('scared','SCARED'),
		('bored','BORED'),

		)
	
	type_of_mood = MultiSelectField(default = 'happy',choices = mood_choices)
	dateTime = models.DateField(auto_now_add = True,)
	writer = models.ForeignKey(Customer,on_delete = models.SET_NULL,null=True)

	def __str__(self):
		moods = self.type_of_mood
		result=""
		for mood in moods:
			result = result + mood +" "
		return str(result)

	def mood_user(self):
		return self.writer.user
	
	mood_user.short_description = "User of the mood"
	mood_user = property(mood_user)




