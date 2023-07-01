from django.db import models
from django.conf import settings
import re
import os
from datetime import date


class Experience(models.Model):
    exp_year =models.CharField( max_length=153)
    exp_tittle = models.CharField(max_length=50)
    exp_about = models.CharField(max_length=130)
    def __str__(self):
        return self.exp_tittle
    
    
class Education(models.Model):
    edu_year = models.CharField( max_length=50)
    edu_tittle = models.CharField( max_length=250)
    edu_about = models.CharField( max_length=250)
    def __str__(self):
        return self.edu_tittle
    
class Opinion(models.Model):
    opinion_name = models.CharField( max_length=50)
    opinion_text = models.CharField( max_length=150)
    opinion_img = models.FilePathField(path=os.path.join(settings.BASE_DIR, "My_portf/static/uploads"), default="")
    @property
    def image_path(self):
        return re.sub('.*img/','',self.opinion_img)

    def __str__(self):
        return self.opinion_name
    
class Portfolio(models.Model):
    
    portfolio_name = models.CharField( max_length=50)
    portfolio_link = models.CharField( max_length=250)
    portfolio_img = models.FilePathField(path=os.path.join(settings.BASE_DIR, "My_portf/static/uploads"), default="")
    @property
    def image_path(self):
        return re.sub('.*img/','',self.portfolio_img)
    
    
    
    def __str__(self):
        return self.portfolio_name
class Blog(models.Model):
    
    blog_name = models.CharField( max_length=50)
    blog_text = models.CharField( max_length=250)
    blog_link = models.CharField( max_length=250)
    blog_img = models.FilePathField(path=os.path.join(settings.BASE_DIR, "My_portf/static/uploads"), default="")
    @property
    def image_path(self):
        return re.sub('.*img/','',self.blog_img)
    def __str__(self):
        return self.blog_name
    
    
class Contact(models.Model):
    mail_name=models.CharField( max_length=50)
    mail_message=models.CharField( max_length=250)
    mail_address=models.EmailField( max_length=254)
    def __str__(self):
        return self.mail_name