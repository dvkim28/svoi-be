from django.contrib.auth import get_user_model
from django.db import models

from advr.utils import from_txt_to_slug


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_txt_to_slug(str(self.title))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        verbose_name = "category"
        verbose_name_plural = "categories"


class SubCategory(models.Model):
    title = models.CharField(
        max_length=100,
    )
    slug = models.SlugField()
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} in {self.category}"


class Ad(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    sub_category = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    show_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} in {self.sub_category}"
