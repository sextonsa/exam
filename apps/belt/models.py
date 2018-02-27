from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
import datetime
import time
email_val= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_val= re.compile(r'^[a-zA-Z]+$')
today = time.strftime('%b %d')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 1:
            errors["fname"] = "First name should not be left blank"
        if len(postData['lname']) < 1:
            errors["lname"] = "Last name should not be left blank"
        if len(postData['email']) < 1:
        	errors['email'] = 'Email should not be left blank'
        if not name_val.match(postData['fname']):
        	errors['invalid'] = 'Name cannot contain numbers!'
        if not email_val.match(postData['email']):
        	errors['nurrr'] = 'Must be a valid email address'
        if len(postData['pword']) < 1:
        	errors['pword'] = 'Password can not be left blank'
        if postData['pword'] != postData['cword']:
        	errors['nah'] = 'Passwords do not match'
        emailchk=User.objects.filter(email=postData['email'])
        if len(emailchk)!=0:
        	errors['mail'] = 'You already have an account, plz login'
        return errors
    def login_validator(self,postData):
    	pings = {}  	
        passchk= User.objects.filter(email=postData['email'])
        print passchk
        print passchk[0].password
        if not bcrypt.checkpw(postData['pword'].encode(), passchk[0].password.encode()):
        	pings['bad'] = 'Your password is wrong bruhhh'
        return pings
	
class User(models.Model):
	alias = models.CharField(max_length=225)
	first_name = models.CharField(max_length=225)
	last_name = models.CharField(max_length=225)
	email = models.CharField(max_length=225)
	password = models.CharField(max_length=225)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	friends=models.ManyToManyField('self', through='Friend',symmetrical=False, related_name='friends_with')
	objects =UserManager() 
class Friend(models.Model):
	name=models.CharField(max_length=225)
	from_user= models.ForeignKey(User, related_name='from_user')
	to_user=models.ForeignKey(User, related_name='to_user')