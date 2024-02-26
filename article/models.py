from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Article(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = RichTextField(verbose_name="Содержание")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    article_image = ProcessedImageField(upload_to='blog_photos',
                                             processors=[ResizeToFill(360,300)],
                                             format='JPEG',
                                             options={'quality':60})
    article_image_thumbnail = ImageSpecField(source = 'article_image',
                                        processors=[ResizeToFill(360, 300)],
                                        format='JPEG',
                                        options={'quality': 60})
    #image_2 = models.ImageField(blank=True, null=True)

    category = models.CharField(max_length=50, null=True, blank=True)
    main_article = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
