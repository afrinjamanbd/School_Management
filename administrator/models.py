from django.db import models

# Create your models here.

from datetime import date

# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     class Meta:
#         managed = False
#         db_table = 'MyBlog'


# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     email = models.EmailField()


# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField(default=date.today)
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField(default=0)
#     number_of_pingbacks = models.IntegerField(default=0)
#     rating = models.IntegerField(default=5)

#     def __str__(self):
#         return self.headline