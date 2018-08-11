from django.db import models

class Users1(models.Model):
	id = models.IntegerField(primary_key=True)
	age = models.IntegerField(max_length=10)
	class Meta:
		db_table = 'users'
		app_label = "myproject" 

'''class DetailsUsers(models.Model):
	id = models.IntegerField(primary_key=True)
	age = models.IntegerField(max_length=10)
	class Meta:
		db_table = 'number'
		app_label = "myproject"  '''
		
class Details(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=10)
	address = models.CharField(max_length=10)
	number = models.CharField(max_length=10)
	class Meta:
		db_table = 'details'
		app_label = "myproject" 
		
