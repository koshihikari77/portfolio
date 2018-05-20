from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['title']

    def __str__(self):
        return self.title


class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    is_published = models.BooleanField(default=False, verbose_name="Is published?")
    published_at = models.DateTimeField(null=True, blank=True, editable=False, verbose_name="Published at")
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True,verbose_name="Category")
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='タグ')
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')