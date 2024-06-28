from django.db import models
from django.contrib.auth.models import User
from typing import Any
from django.utils.text import slugify
from django.urls import reverse
import PIL
from PIL import Image

# genre
class Genre(models.Model):
    genre_title = models.CharField(max_length=255)

    def __str__(self):
        return self.genre_title

#cusomer profile
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# books inventory
class Books(models.Model):
    title = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    thumbnail = models.ImageField(upload_to='media', null=True)
    summary = models.TextField(null=True)
    price = models.PositiveIntegerField(null=True)
    stripe_price_id = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=13, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    availability = models.BooleanField(default=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Books"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def _optimize_image(self):
        img_path = self.thumbnail.path
        with Image.open(img_path) as img:
            # Resize the image
            max_size = (800, 800)
            img.thumbnail(max_size, Image.LANCZOS)

            # Save the image with optimization
            img.save(img_path, optimize=True, quality=75)

    def get_absolute_url(self):
        return reverse("elib:book_detail", kwargs={"slug": self.slug})

# buy record
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.book.title}'

    def get_total_price(self):
        return self.quantity * self.book.price

    def increase_quantity(self, amount=1):
        self.quantity += amount
        self.save()

    def decrease_quantity(self, amount=1):
        self.quantity = max(1, self.quantity - amount)
        self.save()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(CartItem)

    def __str__(self):
        return f'Cart with {self.items.count()} items'

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
