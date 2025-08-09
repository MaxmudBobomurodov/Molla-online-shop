from django.db import models
from pages.models import BaseModel


class BlogCategory(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class BlogAuthor(BaseModel):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class BlogTags(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class BlogModel(BaseModel):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE,related_name='blogs')
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    long_description = models.TextField()

    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE,related_name='blog_category')
    tags = models.ManyToManyField(BlogTags)

    comment = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'