from django.db import models


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to="images/create/")

    def __str__(self):
        return self.title


class Post_list(models.Model):
    hashtags = models.ManyToManyField(
        Hashtag,
        related_name="Hashtag",
    )
    post = models.ForeignKey(Post, related_name="Post", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    picter = models.ImageField(upload_to="images/")
    video = models.FileField(upload_to="videos/")

    def __str__(self):
        return f"{self.title}"


class Module(models.Model):
    post_list = models.ForeignKey(
        Post_list, related_name="module", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.title}"
