from django.db import models

from django_chinook.core.models import BaseModel


class Artist(BaseModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Album(BaseModel):
    title = models.CharField(max_length=160)
    artist = models.ForeignKey(Artist, models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Composer(BaseModel):
    composer = models.CharField(max_length=30)

    def __str__(self):
        return self.composer

    class Meta:
        ordering = ('composer',)


class MediaType(BaseModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Genre(BaseModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Track(BaseModel):
    title = models.CharField(max_length=200)
    composer = models.ManyToManyField(Composer)
    album = models.ForeignKey(Album, models.PROTECT)
    media_type = models.ForeignKey(MediaType, models.PROTECT)
    genre = models.ForeignKey(Genre, models.PROTECT)
    composer_name = models.CharField(max_length=220, default=None, blank=True, null=True)
    milliseconds = models.PositiveIntegerField(default=0)
    byte_s = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
