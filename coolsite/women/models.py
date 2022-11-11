from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class VDC(models.Model):
    name = models.CharField(max_length=50)
    vdc_uuid = models.UUIDField(unique=True)
    site = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=50)
    storage_uuid = models.UUIDField()
    type = models.CharField(max_length=50)
    volume = models.IntegerField()
    vdc_uuid = models.ForeignKey(
        VDC,
        on_delete=models.PROTECT,
        related_name='vdc'
    )

    def __str__(self):
        return self.name
