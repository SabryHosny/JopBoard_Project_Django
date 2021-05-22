from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


def image_upload(instance, filename):
    name, extention = filename.split(".")
    return f"jobs\{instance.pk}.{extention}"

# Create your models here.


class Jop(models.Model):
    # The first element in each tuple is the actual value to be set on the model,
    # and the second element is the human-readable name.
    # Make a select box with these choices instead of the standard text field.
    owner = models.ForeignKey(
        User, related_name='job_owner', on_delete=models.CASCADE)
    JOP_TYPE = [
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
    ]

    title = models.CharField(max_length=100)
    jop_type = models.CharField(
        max_length=15, choices=JOP_TYPE, default="Full Time")
    # location
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Jop, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    Name = models.CharField(max_length=25)

    def __str__(self):
        return self.Name


class Jop_Applier(models.Model):
    jop = models.ForeignKey(
        "Jop", related_name="Apply_Jop", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
