from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField('slug', max_length=256, unique=True, allow_unicode=True)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        
    def __str__(self):
        return self.slug