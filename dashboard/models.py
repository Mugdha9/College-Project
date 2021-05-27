from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#OPTIONS = (
    #('0','Not at All'),
    #('1','Several Days'),
    #('2','More than half the days'),
    #('3','Nearly every day')
#)
class phq9test(models.Model):
    SELECT_OPTIONS = [
        (0,'Not at All'),
        (1,'Several Days'),
        (2,'More than half the days'),
        (3,'Nearly every day'),
        ]

    ans1 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans2 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans3 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans4 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans5 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans6 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans7 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans8 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans9 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    total_score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length = 10,default='A')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user1 = models.CharField(max_length = 100, primary_key = True,default = 'mugdha');

    def __str__(self):
        return self.user.username

class generalized_anxiety(models.Model):
    SELECT_OPTIONS = [
        (0,'Never'),
        (1,'A few times'),
        (2,'Sometimes'),
        (3,'Often'),
        (4,'Constantly'),
        ]

    ans1 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans2 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans3 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans4 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans5 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans6 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans7 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans8 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    total_score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    percentage = models.FloatField(max_length = 10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user1 = models.CharField(max_length = 100, primary_key = True,default = 'mugdha');


    def __str__(self):
        return self.user.username

class panicdisorder(models.Model):
    SELECT_OPTIONS = [
        (0,'Not at All'),
        (1,'Mild'),
        (2,'Moderate'),
        (3,'Severe'),
        ]

    ans1 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans2 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans3 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans4 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans5 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans6 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans7 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans8 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    total_score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    percentage = models.FloatField(max_length = 10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user1 = models.CharField(max_length = 100, primary_key = True,default = 'mugdha');


    def __str__(self):
        return self.user.username

class post_traumaticstress(models.Model):
    SELECT_OPTIONS = [
        (0,'No'),
        (1,'Yes'),
        ]

    ans1 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans2 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans3 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans4 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans5 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans6 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans7 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans8 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    total_score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    percentage = models.FloatField(max_length = 10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user1 = models.CharField(max_length = 100, primary_key = True,default = 'mugdha');


    def __str__(self):
        return self.user.username

class major_depressive(models.Model):
    SELECT_OPTIONS = [
        (0,'Not at All'),
        (1,'Mild'),
        (2,'Moderate'),
        (3,'Severe'),
        ]

    ans1 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans2 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans3 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans4 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans5 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans6 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans7 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans8 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    total_score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    percentage = models.FloatField(max_length = 10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user1 = models.CharField(max_length = 100, primary_key = True,default = 'mugdha');


    def __str__(self):
        return self.user.username

class manic_episodes(models.Model):
    SELECT_OPTIONS = [
        (0,'Not at All'),
        (1,'Mild'),
        (2,'Moderate'),
        (3,'Severe'),
        ]

    ans1 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans2 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans3 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans4 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans5 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans6 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans7 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    ans8 = models.IntegerField(choices=SELECT_OPTIONS,default=0)
    total_score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    percentage = models.FloatField(max_length = 10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user1 = models.CharField(max_length = 100, primary_key = True,default = 'mugdha');


    def __str__(self):
        return self.user.username
